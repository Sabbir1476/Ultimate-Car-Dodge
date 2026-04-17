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

## ⚙️ Installation & Requirements

Ensure that you have Python 3.x installed. Then, install the required libraries:

```bash
pip install pygame PyOpenGL
```

### Running the game
```bash
python game.py
```
