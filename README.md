# AI Magnetic Cave Game

### Authors
- Sami Moqbel: moqbelsami@gmail.com
- Lama Abdelmohsen: lamaabothaher15@gmail.com

## Description
This is a Python implementation of a board game where two players take turns placing pieces on an 8x8 board. The game supports two modes: Player vs Player and Player vs Bot. The objective is to connect a certain number of pieces in a row either horizontally, vertically, or diagonally.

## Features
- Player vs Player mode
- Player vs Bot mode with the option for the bot to start first
- Board display
- Move validation
- Detection of connected pieces
- Evaluation function for the bot
- Minimax algorithm for the bot

## Instructions
1. Choose a game mode from the menu:
    - 1) Player vs Player
    - 2) Player vs Bot (Player starts first)
    - 3) Player vs Bot (Bot starts first)
    - 4) Exit
2. Players will be prompted to enter their moves in the format "numberletter" (e.g., "1a", "2b").
3. The game will display the board after each move.
4. The game ends when a player connects the required number of pieces in a row or when the board is full.

## How to Run

1. **Install Required Libraries:**

   Make sure you have the required libraries installed. You can install them using `pip`:

   ```bash
   pip install pandas
   
Download the Script:

Ensure you have the Python script ai_magnetic_cave_game.py.

Create the Bash Script:

Create a bash script named run_game.sh with the following content:

bash
"
#!/bin/bash

# Check if the required Python script exists
if [[ ! -f "ai_magnetic_cave_game.py" ]]; then
    echo "The ai_magnetic_cave_game.py script is missing."
    exit 1
fi
"

# Run the Python script
python ai_magnetic_cave_game.py

Make the script executable:
"
bash
chmod +x run_game.sh
"

Run the Game:

Execute the bash script to start the game:

bash
./run_game.sh

