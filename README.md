# 🚗 Ultimate Car Dodge

A fast-paced 2D arcade dodging game built with **Python**, **PyGame**, and **PyOpenGL**.

Dodge incoming traffic, chain combos, and survive as long as possible in a visually dynamic, procedurally rendered environment. The game combines smooth movement physics, skill-based scoring, and real-time difficulty scaling to deliver an engaging arcade experience.

---

## 🌟 Features

### 🎨 Procedural Graphics

* Fully rendered using **PyOpenGL primitives**
* No static textures — everything is dynamically generated
* Vehicles and environments scale cleanly with proper orientation

### ⚡ Smooth Movement System

* Lane transitions use interpolation:

  ```
  position += (target - position) * 0.2
  ```
* Eliminates abrupt movement and creates fluid gameplay

### 🔥 Combo & Scoring System

* Chain dodges to unlock multipliers:

  * **3 dodges → 2X score**
  * **5 dodges → 3X score**
* **Close Call Bonus (+15):** Rewarded for narrowly avoiding traffic

### 💎 Power-ups & Entities

* 🔴 **Red Cars:** Deadly obstacles → collision = Game Over
* 🟢 **Green Collectibles:** +20 score boost
* 🔵 **Blue Shields:** Temporary invincibility with visual forcefield

### 🎮 Dynamic Gameplay Features

* Real-time difficulty scaling:

  * EASY → MEDIUM → HARD
* Lane-based tracking system
* Pre-emptive warning system (`!`) for incoming traffic
* Screen shake and visual effects on collisions

### 🧠 Game States

* Main Menu (`Press Enter to Start`)
* Active Gameplay
* Game Over (with instant restart option)

---

## 🎮 Controls

| Key               | Action                  |
| ----------------- | ----------------------- |
| **Enter**         | Start Game              |
| **← Left Arrow**  | Move Left               |
| **→ Right Arrow** | Move Right              |
| **R**             | Restart after Game Over |

---

## 🎯 Objective

Survive as long as possible by dodging incoming vehicles while maximizing your score through:

* Combo chains
* Close calls
* Strategic movement

---

## ⚙️ Installation

Make sure you have **Python 3.x** installed.

Install dependencies:

```bash
pip install pygame PyOpenGL
```

---

## ▶️ Run the Game

```bash
python game.py
```

---

## 🚀 Future Improvements (Optional Ideas)

* Sound effects & background music
* High score saving system
* Mobile or web version
* Additional power-ups and enemy types

---

## 📌 Project Highlights

* Procedural rendering (no sprites)
* Physics-inspired smooth movement
* Skill-based scoring system
* Clean game state management

---

## 📄 License

This project is open-source. Feel free to use, modify, and distribute.

---

## 👨‍💻 Author

Developed by **Sabbir**

---

⭐ If you like this project, consider giving it a star on GitHub!
