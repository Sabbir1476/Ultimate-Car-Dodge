import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import sys
import math

# --- Constants ----
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
LANE_POSITIONS = [200, 400, 600]
CAR_WIDTH = 55
CAR_HEIGHT = 100

STATE_MENU = 0
STATE_PLAY = 1
STATE_OVER = 2

TYPE_ENEMY = 0
TYPE_BONUS = 1
TYPE_SHIELD = 2

class Entity:
    def __init__(self, lane, y, type_id):
        self.lane = lane
        self.x = LANE_POSITIONS[lane]
        self.y = y
        self.type_id = type_id
        self.width = CAR_WIDTH
        self.height = CAR_HEIGHT
        
        if self.type_id == TYPE_ENEMY:
            self.color = (0.9, 0.1, 0.1) # Red Danger
            # Slightly varying size/speed for enemies? Keep it simple for now
        elif self.type_id == TYPE_BONUS:
            self.color = (0.1, 0.9, 0.1) # Green Bonus
            self.width = 40
            self.height = 70
        elif self.type_id == TYPE_SHIELD:
            self.color = (0.3, 0.5, 1.0) # Blue Shield Crystal
            self.width = 30
            self.height = 30
            
        self.passed = False

    def draw_car(self, facing_up=False, is_player=False, has_shield=False):
        glPushMatrix()
        glTranslatef(self.x, self.y, 0.0)
        
        half_w = self.width / 2.0
        half_h = self.height / 2.0
        
        # Shield glow
        if is_player and has_shield:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glColor4f(0.2, 0.7, 1.0, 0.5)
            # Draw a larger circle/octagon as shield
            glBegin(GL_POLYGON)
            for i in range(16):
                angle = i * (math.pi * 2 / 16)
                glVertex2f(math.cos(angle) * 60, math.sin(angle) * 70)
            glEnd()
            glDisable(GL_BLEND)
            
        if self.type_id == TYPE_SHIELD and not is_player: # Drop item
            glRotatef(pygame.time.get_ticks() * 0.2, 0, 0, 1)
            glColor3f(*self.color)
            glBegin(GL_POLYGON)
            for i in range(8):
                angle = i * (math.pi * 2 / 8)
                glVertex2f(math.cos(angle) * 20, math.sin(angle) * 20)
            glEnd()
            glPopMatrix()
            return

        if self.type_id == TYPE_BONUS and not is_player: # Bonus item is a distinct car shape
             glColor3f(*self.color)
             
        # Draw base Shadow
        glColor4f(0, 0, 0, 0.4)
        glBegin(GL_QUADS)
        glVertex2f(-half_w-5, -half_h-5)
        glVertex2f(half_w+5, -half_h-5)
        glVertex2f(half_w+5, half_h+5)
        glVertex2f(-half_w-5, half_h+5)
        glEnd()

        # Wheels (Black)
        glColor3f(0.05, 0.05, 0.05)
        wheel_w, wheel_h = 10, 24
        for wx, wy in [(-half_w, -half_h+15), (half_w-wheel_w, -half_h+15), 
                       (-half_w, half_h-15-wheel_h), (half_w-wheel_w, half_h-15-wheel_h)]:
            glBegin(GL_QUADS)
            glVertex2f(wx, wy); glVertex2f(wx + wheel_w, wy)
            glVertex2f(wx + wheel_w, wy + wheel_h); glVertex2f(wx, wy + wheel_h)
            glEnd()
            
        # Car Body
        if is_player:
            glColor3f(0.0, 0.6, 1.0) # Player is cool blue
        else:
            glColor3f(*self.color)
            
        glBegin(GL_QUADS)
        body_w_offset = 6
        glVertex2f(-half_w + body_w_offset, -half_h)
        glVertex2f(half_w - body_w_offset, -half_h)
        glVertex2f(half_w - body_w_offset, half_h)
        glVertex2f(-half_w + body_w_offset, half_h)
        glEnd()
        
        # Windshields
        glColor3f(0.1, 0.1, 0.2)
        wind_w_offset = 10
        glBegin(GL_QUADS)
        # Back window
        glVertex2f(-half_w + wind_w_offset, -half_h + 15)
        glVertex2f(half_w - wind_w_offset, -half_h + 15)
        glVertex2f(half_w - wind_w_offset, -half_h + 35)
        glVertex2f(-half_w + wind_w_offset, -half_h + 35)
        # Front window
        glVertex2f(-half_w + wind_w_offset, half_h - 35)
        glVertex2f(half_w - wind_w_offset, half_h - 35)
        glVertex2f(half_w - wind_w_offset, half_h - 15)
        glVertex2f(-half_w + wind_w_offset, half_h - 15)
        glEnd()
        
        # Lights
        if facing_up:
            headlight_y = half_h - 10
            tailight_y = -half_h
        else:
            headlight_y = -half_h
            tailight_y = half_h - 10
            
        front_h = 10
        # Headlights (Yellow/White)
        glColor3f(1.0, 1.0, 0.5)
        for hx in [-half_w + body_w_offset + 5, half_w - body_w_offset - 15]:
            glBegin(GL_QUADS)
            glVertex2f(hx, headlight_y); glVertex2f(hx + 10, headlight_y)
            glVertex2f(hx + 10, headlight_y + front_h); glVertex2f(hx, headlight_y + front_h)
            glEnd()
            
        # Taillights (Red)
        glColor3f(1.0, 0.0, 0.0)
        for hx in [-half_w + body_w_offset + 5, half_w - body_w_offset - 15]:
            glBegin(GL_QUADS)
            glVertex2f(hx, tailight_y); glVertex2f(hx + 10, tailight_y)
            glVertex2f(hx + 10, tailight_y + front_h); glVertex2f(hx, tailight_y + front_h)
            glEnd()
            
        # Draw Headlight beams if Player!
        if is_player:
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glColor4f(1.0, 1.0, 0.6, 0.2)
            for hx in [-half_w + body_w_offset + 5, half_w - body_w_offset - 15]:
                glBegin(GL_POLYGON)
                glVertex2f(hx + 5, half_h)
                glVertex2f(hx + 50, half_h + 150)
                glVertex2f(hx - 40, half_h + 150)
                glEnd()
            glDisable(GL_BLEND)
            
        glPopMatrix()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), DOUBLEBUF | OPENGL)
        pygame.display.set_caption("Ultimate Car Dodge")
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        self.font_main = pygame.font.SysFont('segoeui', 32, bold=True)
        self.font_title = pygame.font.SysFont('segoeui', 72, bold=True)
        self.font_small = pygame.font.SysFont('segoeui', 20, bold=True)
        self.clock = pygame.time.Clock()
        
        self.state = STATE_MENU
        self.reset_game()

    def reset_game(self):
        self.lane_idx = 1
        self.player_x = LANE_POSITIONS[self.lane_idx]
        self.player_target_x = self.player_x
        self.player_y = 120
        self.shield_timer = 0
        
        self.enemies = []
        self.warnings = [] # dicts: frame_count, lane, type
        
        self.score = 0
        self.dodged_consecutive = 0
        self.combo_multiplier = 1
        self.base_speed = 6.0
        self.spawn_timer = 0
        self.shake_timer = 0

    def drawText(self, text, x, y, font, color=(255,255,255), center_x=False, center_y=False):
        text_surface = font.render(str(text), True, color)
        text_data = pygame.image.tostring(text_surface, "RGBA", True)
        width, height = text_surface.get_size()
        if center_x: x = x - width / 2.0
        if center_y: y = y - height / 2.0
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glRasterPos2d(x, y)
        glDrawPixels(width, height, GL_RGBA, GL_UNSIGNED_BYTE, text_data)
        glDisable(GL_BLEND)

    def drawLanes(self):
        # Grass Background
        glClearColor(0.1, 0.45, 0.15, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # Asphalt
        glColor3f(0.2, 0.2, 0.22)
        glBegin(GL_QUADS)
        glVertex2f(100, 0); glVertex2f(700, 0)
        glVertex2f(700, WINDOW_HEIGHT); glVertex2f(100, WINDOW_HEIGHT)
        glEnd()
        
        # Edge lines
        glColor3f(0.9, 0.9, 0.9)
        glLineWidth(8.0)
        glBegin(GL_LINES)
        for x_edge in [100, 700]:
            glVertex2f(x_edge, 0); glVertex2f(x_edge, WINDOW_HEIGHT)
        glEnd()

        # Lane Divider (Yellow Dash)
        glColor3f(0.95, 0.8, 0.0)
        glLineWidth(6.0)
        speed = max(10, int(self.base_speed + (self.score * 0.02)))
        offset = (int(pygame.time.get_ticks() / (100 / speed)) % 80)
        
        for x in [300, 500]:
            glBegin(GL_LINES)
            for y in range(0 - offset, WINDOW_HEIGHT + 80, 80):
                glVertex2f(x, y); glVertex2f(x, max(0, y - 40))
            glEnd()
            
        # Draw Lane Highlight for exactly where the player targets
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(1.0, 1.0, 1.0, 0.05)
        hw = 90
        tx = self.player_target_x
        glBegin(GL_QUADS)
        glVertex2f(tx - hw, 0); glVertex2f(tx + hw, 0)
        glVertex2f(tx + hw, WINDOW_HEIGHT); glVertex2f(tx - hw, WINDOW_HEIGHT)
        glEnd()
        glDisable(GL_BLEND)

    def check_collision(self, ex, ey, ew, eh):
        pw, ph = CAR_WIDTH - 10, CAR_HEIGHT - 10 # slightly forgiving hitbox
        return (abs(self.player_x - ex) < (pw + ew) / 2) and \
               (abs(self.player_y - ey) < (ph + eh) / 2)

    def drawWarning(self, x, y, size):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        # Flashing triangle
        flash = (pygame.time.get_ticks() % 200) > 100
        if flash:
            glColor4f(1.0, 0.0, 0.0, 0.8)
            glBegin(GL_TRIANGLES)
            glVertex2f(x, y - size)
            glVertex2f(x - size, y)
            glVertex2f(x + size, y)
            glEnd()
        glDisable(GL_BLEND)

    def update_play(self):
        # Smooth interpolation for player movement
        self.player_x += (self.player_target_x - self.player_x) * 0.2
        
        if self.shield_timer > 0:
            self.shield_timer -= 1
            
        if self.shake_timer > 0:
            self.shake_timer -= 1

        # Difficulty scale
        current_speed = self.base_speed + (self.score * 0.01)
        # Cap logic spawn rate so it doesn't get instantly impossible
        spawn_rate = max(15, 50 - int(self.score / 50))
        
        # Spawn logic with warnings
        self.spawn_timer += 1
        if self.spawn_timer >= spawn_rate:
            lane = random.choice([0, 1, 2])
            # Determine type
            r = random.random()
            type_val = TYPE_ENEMY
            if r > 0.90: type_val = TYPE_SHIELD
            elif r > 0.75: type_val = TYPE_BONUS
            
            self.warnings.append({'lane': lane, 'frames': 40, 'type': type_val})
            self.spawn_timer = 0
            
        # Process warnings
        for w in self.warnings[:]:
            w['frames'] -= 1
            if w['frames'] <= 0:
                self.enemies.append(Entity(w['lane'], WINDOW_HEIGHT + CAR_HEIGHT, w['type']))
                self.warnings.remove(w)

        # Update Enemies & Checks
        to_remove = []
        for i, entity in enumerate(self.enemies):
            entity.y -= current_speed if entity.type_id == TYPE_ENEMY else (current_speed * 0.8)
            
            # Hitbox check
            if self.check_collision(entity.x, entity.y, entity.width, entity.height):
                if entity.type_id == TYPE_ENEMY:
                    if self.shield_timer > 0:
                        # Destroy enemy, keep shield, shake a little
                        self.shake_timer = 10
                        to_remove.append(i)
                        self.combo_multiplier = 1
                    else:
                        self.state = STATE_OVER
                        self.shake_timer = 20
                elif entity.type_id == TYPE_BONUS:
                    self.score += 20 * self.combo_multiplier
                    to_remove.append(i)
                elif entity.type_id == TYPE_SHIELD:
                    self.shield_timer = 300 # 5 seconds of shielding
                    to_remove.append(i)
            else:
                # Passed the player completely?
                if entity.y < self.player_y - CAR_HEIGHT and not entity.passed:
                    entity.passed = True
                    if entity.type_id == TYPE_ENEMY:
                        self.dodged_consecutive += 1
                        # Combo logic
                        if self.dodged_consecutive >= 5: self.combo_multiplier = 3
                        elif self.dodged_consecutive >= 3: self.combo_multiplier = 2
                        
                        self.score += 5 * self.combo_multiplier
                        
                        # Close call logic! Check distance during pass
                        dist = abs(self.player_x - entity.x)
                        # if they aren't fully settled into a lane, or they jumped recently
                        if dist > 60 and dist < 150: 
                            self.score += 15 # Close call!
            
            if entity.y < -CAR_HEIGHT and i not in to_remove:
                to_remove.append(i)
                
        for i in reversed(to_remove):
            self.enemies.pop(i)

    def draw_ui(self):
        # Top bar HUD
        level_txt = "EASY"
        c = (150, 255, 150)
        if self.score > 300: 
            level_txt = "HARD"
            c = (255, 100, 100)
        elif self.score > 100: 
            level_txt = "MEDIUM"
            c = (255, 255, 100)
            
        self.drawText(f"SCORE: {self.score}", 20, WINDOW_HEIGHT - 40, self.font_main)
        self.drawText(f"LEVEL: {level_txt}", WINDOW_WIDTH - 200, WINDOW_HEIGHT - 40, self.font_main, color=c)
        
        if self.combo_multiplier > 1:
            self.drawText(f"COMBO x{self.combo_multiplier}!", 20, WINDOW_HEIGHT - 80, self.font_main, color=(255, 200, 50))
            
        if self.shield_timer > 0:
            self.drawText(f"SHIELD ACTIVE", 20, WINDOW_HEIGHT - 120, self.font_small, color=(100, 200, 255))
            
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if self.state == STATE_MENU:
                        if event.key == pygame.K_RETURN:
                            self.state = STATE_PLAY
                    elif self.state == STATE_OVER:
                        if event.key == pygame.K_r:
                            self.reset_game()
                            self.state = STATE_PLAY
                    elif self.state == STATE_PLAY:
                        if event.key == pygame.K_LEFT:
                            self.lane_idx = max(0, self.lane_idx - 1)
                            self.player_target_x = LANE_POSITIONS[self.lane_idx]
                        if event.key == pygame.K_RIGHT:
                            self.lane_idx = min(2, self.lane_idx + 1)
                            self.player_target_x = LANE_POSITIONS[self.lane_idx]

            # Logic
            if self.state == STATE_PLAY:
                self.update_play()
                
            # Rendering Setup (Screenshake)
            glPushMatrix()
            if self.shake_timer > 0:
                sx = random.randint(-15, 15)
                sy = random.randint(-15, 15)
                glTranslatef(sx, sy, 0)
                
            self.drawLanes()

            if self.state in [STATE_PLAY, STATE_OVER]:
                for w in self.warnings:
                    self.drawWarning(LANE_POSITIONS[w['lane']], WINDOW_HEIGHT - 30, 20)
                    
                for e in self.enemies:
                    e.draw_car(facing_up=False)
                    
                # Player
                player_dummy = Entity(0, 0, TYPE_ENEMY)   
                player_dummy.x = self.player_x
                player_dummy.y = self.player_y
                player_dummy.draw_car(facing_up=True, is_player=True, has_shield=(self.shield_timer>0))
                
                self.draw_ui()

            # Global Fashes / UI Overlays
            if self.state == STATE_OVER:
                # Red Death flash fading into standard black overlay
                glEnable(GL_BLEND)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                red_intensity = min(1.0, self.shake_timer / 20.0)
                glColor4f(red_intensity, 0.0, 0.0, 0.75)
                glBegin(GL_QUADS)
                glVertex2f(0, 0); glVertex2f(WINDOW_WIDTH, 0)
                glVertex2f(WINDOW_WIDTH, WINDOW_HEIGHT); glVertex2f(0, WINDOW_HEIGHT)
                glEnd()
                glDisable(GL_BLEND)
                
                self.drawText("CRASHED!", WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 60, self.font_title, color=(255, 80, 80), center_x=True, center_y=True)
                self.drawText(f"FINAL SCORE: {self.score}", WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 10, self.font_main, center_x=True, center_y=True)
                self.drawText("Press 'R' to Restart", WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 70, self.font_main, color=(200, 200, 200), center_x=True, center_y=True)
                
            elif self.state == STATE_MENU:
                # Dark overlay for menu
                glEnable(GL_BLEND)
                glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
                glColor4f(0.0, 0.0, 0.0, 0.6)
                glBegin(GL_QUADS)
                glVertex2f(0, 0); glVertex2f(WINDOW_WIDTH, 0)
                glVertex2f(WINDOW_WIDTH, WINDOW_HEIGHT); glVertex2f(0, WINDOW_HEIGHT)
                glEnd()
                glDisable(GL_BLEND)
                
                self.drawText("ULTIMATE CAR DODGE", WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 80, self.font_title, color=(100, 200, 255), center_x=True, center_y=True)
                self.drawText("Survive as long as possible and dodge traffic!", WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + 20, self.font_main, center_x=True, center_y=True)
                
                # Instructions
                self.drawText("Left / Right Arrows to Move", WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 40, self.font_small, color=(200, 255, 200), center_x=True, center_y=True)
                self.drawText("Green: +Points  |  Blue: Shield  |  Red: Crash", WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 70, self.font_small, color=(255, 200, 100), center_x=True, center_y=True)

                # Flash Start
                if pygame.time.get_ticks() % 1000 > 500:
                    self.drawText("PRESS ENTER TO START", WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 140, self.font_main, color=(255, 255, 255), center_x=True, center_y=True)

            glPopMatrix() # Always pop the screenshake
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
