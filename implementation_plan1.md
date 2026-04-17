# Greatly Enhanced 2D Car Dodge Game Plan

This plan details a massive overhaul to your 2D Car Dodging game, implementing all the advanced mechanics, polish, and UI requested to ensure it feels like a fully-featured, high-quality project.

## Proposed Changes

We will refactor `game.py` to support these new features.

### 1. Game State Management
*   **[MODIFY]** `game.py`
    *   Introduce explicit states: `MAIN_MENU`, `PLAYING`, `GAME_OVER`.
    *   Add a Main Menu with a title and instructions ("Press ENTER to start", "Survive as long as possible").

### 2. Smooth Mechanics & Transitions
*   **[MODIFY]** `game.py`
    *   **Smooth Lane Changes**: Instead of instant jumping, track a `target_x` and smoothly interpolate the player's `x` position using `x += (target_x - x) * 0.2`.
    *   **Camera Shake**: Add an `x` and `y` matrix offset when a collision occurs, shaking back and forth for 30 frames.

### 3. Entity Enhancements
*   **[MODIFY]** `game.py`
    *   Return to **High-Quality Procedural Drawing**: Since imported textures were not satisfactory, I will craft very detailed car shapes using raw PyOpenGL polygons. They will strictly face correctly (Player up, Enemies down).
    *   **Entity Types**:
        *   **Red Car**: Danger (Instant Death).
        *   **Green Car** (or Coin): Collectible (+20 Score).
        *   **Blue Shield** (Power-up): Grants temporary invincibility, turning the player's car glowing blue.
    *   **Variations**: Some enemy cars will be wider or slightly faster depending on difficulty.

### 4. Advanced Visual Cues
*   **[MODIFY]** `game.py`
    *   **Lane Highlighting**: Draw a translucent bright rectangle specifically over the lane the player currently occupies.
    *   **Spawning Alerts**: A flashing warning indicator `(!)` at the very top of the lane 30-60 frames before a car physically appears.
    *   **Red Flash on Crash**: Fill the screen with a rapidly fading red rectangle when you lose.

### 5. Advanced Scoring System
*   **[MODIFY]** `game.py`
    *   **Combo System**: Track consecutive successful dodges. Multiplier resets if a car passes but you didn't dodge it safely (or collected a negative trait).
    *   **Close Call Bonus**: Distance calculation between player and enemy upon passing. Extra points `+5` awarded!
    *   **Leveling System**: Calculate levels based on score points (`Easy`, `Medium`, `Hard`, `Extreme`).

## User Review Required

> [!IMPORTANT]
> The image textures mapped previously will be entirely stripped in favor of high-quality geometry drawn via PyOpenGL to ensure they face appropriately and look completely crisp at any resolution. 

## Open Questions

- Do you have a preference for the visual appearance of the Shield power-up? (i.e. A floating crystal? A colored orb? Just a shield icon?) I will default to a glowing cyan Orb if none is selected.

## Verification Plan

### Automated Tests
*   Verify Python compilation.

### Manual Verification
*   Verify rendering state transitions (Menu -> Game -> Game Over).
*   Verify smooth lane moving.
*   Verify collisions explicitly (Red collision kills, Green collectible gives score, Shield prevents Red collision).
