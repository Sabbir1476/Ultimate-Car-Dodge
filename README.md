# Ultimate Car Dodge

A high-speed 2D arcade dodging game built using **Python**, **PyOpenGL**, and **PyGame**. 

This game features dynamic difficulty scaling, a built-in combo scoring system, smooth mathematical movement transitions, and fully procedural geometric rendering for high-performance visual effects!

## 🌟 Features

- **Procedural Graphics:** Ships, roads, and shields are rendered entirely through scalable PyOpenGL primitives, providing crisp graphics and orientation handling without reliance on static flat images. 
- **Combo System & Close Calls:** Chain your dodges for `2X` and `3X` multipliers. Expert dodging rewards you with hidden `+15` Close Call bonuses.
- **Powerups & Collectibles:** 
  - 🟢 **Green Collectibles:** Absorb to immediately boost your score `+20`.
  - 🔴 **Red Sports Cars:** Pure danger. Causes a crash, shaking the screen and applying a red screen flash.
  - 🔵 **Blue Crystals:** Temporary Invincibility Shields! Glowing forcefield effortlessly smashes through traffic.
- **Dynamic UX/UI:** Real-time level shifting (EASY, MEDIUM, HARD), Lane-highlight tracking, and animated Pre-Emptive Traffic Warnings to test your reflexes.

## 🎮 How to Play

### Controls
*   **[Enter]** - Start the Game from the Main Menu
*   **[←] Left Arrow** - Slide one lane to the left.
*   **[→] Right Arrow** - Slide one lane to the right.
*   **[R]** - Instantly restart upon a Game Over.

### Objective
Survive as long as possible by weaving through incoming traffic!
Advanced Procedural Geometry:
Dropped raw image textures in favor of highly-detailed scalable PyOpenGL polygons. This guarantees your player vehicle appropriately faces UP, highlighting its glowing headlights, while traffic faces DOWN, exposing red taillights.
Multiple Game States: 
We built a true MAIN_MENU ("Press Enter to Start") and standard GAME_OVER cycle.
Smooth Lane Traversal:
Mathematical interpolation has removed choppy teleporting; cars now glide dynamically left and right depending on their distance to target (position += (target - position) * 0.2).
Dynamic Entities:
🔴 Red Cars: Standard obstacle. Hits trigger a Game Over + massive screen shaking + a red screen flash.
🟢 Green Cars: Collectibles! Hitting these absorbs them to immediately boost your score +20.
🔵 Blue Shields: Rotating crystal tokens. Provide temporary Invincibility! When active, your vehicle gets a glowing forcefield, and hitting a red car effortlessly smashes them out of the way!
Scoring & Leveling Masterclass
Close Call System:
Added a calculation check determining if the player swerved out of danger precisely beside a passing vehicle. Dodging properly near traffic grants an unseen +15 Close Call Bonus.
Combo System:
Evading 3 cars consecutively boosts score gain to 2X. Evading 5 elevates you to 3X. Missing or getting hit resets the multiplier.
Visual Thresholds: 
Integrated an automated Level UI ranking you through "EASY," "MEDIUM," and "HARD" based on numerical checkpoints.
Pre-Emptive Traffic Warnings: 
Before a car physically drops into the screen, a red (!) flashes vividly at the apex of its corresponding lane so players can quickly react.

## ⚙️ Installation & Requirements

Ensure that you have Python 3.x installed. Then, install the required libraries:

```bash
pip install pygame PyOpenGL
```

### Running the game
```bash
python game.py
```
