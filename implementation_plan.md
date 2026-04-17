# 2D Car Dodge Game (PyOpenGL)

We will build a simple, infinite 2D car dodging game using PyOpenGL for graphics and PyGame for window administration and input handling.

## Proposed Architecture

Since the user requested using **PyOpenGL 2D**, we will create a classic top-down, multiple-lane driving scenario.
Window initialization, keyboard events, and the game loop will be handled by **PyGame** working in OpenGL mode. Rendering will strictly rely on **PyOpenGL** coordinate transformations and primitives.

### Entities and Mechanics
*   **Window**: 800x600 pixels.
*   **Perspective**: 2D Orthographic (using `glOrtho`).
*   **Lanes**: 3 fixed lanes.
*   **Player Car**: Spawns at the bottom. Moves between lanes using `Left` and `Right` arrow keys. (Color: Green/Blue)
*   **Enemy Cars**: Spawn randomly at the top and move downwards. Speed increases gradually based on the score or time survived. (Color: Red)
*   **Collision Detection**: AABB (Axis-Aligned Bounding Box) intersection check between the player and any enemy.
*   **Score**: Increases over time or for every car successfully dodged. Difficulty will multiply the score and car speeds.

### File Structure

We will create a single Python script `game.py` containing the logic and rendering, keeping it simple to install and run. 

#### [NEW] game.py
This file will contain:
1.  **Imports & Config**: `OpenGL.GL`, `pygame`, game constants (colors, window dimensions).
2.  **State Management**: Player position, list of active enemies, current speed, score, and `game_over` flag.
3.  **Entity Rendering Logic**: Helper functions to draw colored rectangles (for cars and road lines).
4.  **Game Loop**:
    *   **Event Handling**: Keypresses (Left/Right to move, R to restart if Game Over).
    *   **Update**: Move enemies down, spawn new ones periodically, increase speed/difficulty variables, clean up off-screen enemies, check collisions.
    *   **Render**: Clear buffers, render road/lanes, render player, render enemies.

## User Review Required

> [!IMPORTANT]
> The game requires `pygame` and `PyOpenGL` to be installed. Make sure you have these installed via `pip install pygame PyOpenGL` or checking your environment setup.

## Open Questions

None at this moment! 

## Verification Plan

### Automated Tests
*   We'll run `python -m py_compile game.py` to check for syntax errors before executing.

### Manual Verification
*   We will attempt to run `python game.py` (if you are ok with us running the command locally or if you prefer to run it). We will verify that a window opens, cars spawn, and movement/collisions function as expected.
