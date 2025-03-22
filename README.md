# Python Snake Game

A classic Snake Game implementation using Python's Turtle graphics library.

## Description

This is a simple Snake Game where players control a snake that moves around the screen. The goal is to eat the red food dots to grow longer while avoiding collisions with the walls and the snake's own body.

## Features

- Snake movement using arrow keys
- Food spawns at random locations
- Score tracking system
- High score persistence using file storage
- Game over detection for wall and self-collision
- Visual feedback with different colors (green snake, red food, white text)

## Controls

- Up Arrow: Move snake up
- Down Arrow: Move snake down
- Left Arrow: Move snake left
- Right Arrow: Move snake right

## Files Structure

- `main.py`: Main game loop and initialization
- `snake.py`: Snake class controlling movement and growth
- `food.py`: Food class for spawning collectibles
- `scoreboard.py`: Score tracking and display
- `data.txt`: Stores the high score

## Requirements

- Python 3.x
- Turtle graphics library (built-in with Python)

## How to Run

```bash
python main.py
```