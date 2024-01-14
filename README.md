# Minesweeper Game

This is a simple Minesweeper game implemented in Python using the Kivy framework. The game allows players to explore a grid and identify hidden bombs by left-clicking on squares. The objective is to uncover all the non-bomb squares to win the game.

## Table of Contents
- Installation
- How to Play
- Screens
  - Main Screen
  - Game Screen
  - Settings Screen
  - Don't Push Screen
- MinesweeperGame Class
- MinesweeperApp Class
- MyApp Class

  ## Installation

To run the Minesweeper game, you need to have Python and Kivy installed on your system. Additionally, make sure to have the required audio files ('Toothless-Dancing-Meme-NEW-VARIATIONS.mp3', 'New_Nuke_Effect.mp3', 'Congratulations-BBC-Sound-Effect-into-Cheer-Into-Applause-Inclusion.mp3') available at the specified file paths.

![image](https://github.com/Kukkaikung/test/assets/152356019/a502c477-5600-4a64-9230-c9715da29358)

## How to Play
1. Enter your name in the provided input field on the Main Screen.
2. Click the "Confirm" button to set your name.
3. Use the "Start" button to begin a new Minesweeper game.
4. Explore the grid by left-clicking on squares.
5. If you uncover a bomb, the game will end with a "Game Over" message.
6. Uncover all non-bomb squares to win the game and receive a "Congratulations" message.
7. Navigate to the "Settings" screen to adjust audio settings.
8. Click the "Exit" button to close the application.

## Screens

### Main Screen
- Input your name and confirm to set it.
- Start a new Minesweeper game.
- Access the settings screen.
- Go to the tutorial screen.
- Engage in a special interaction with the "Don't Push" button.

### Game Screen
- Learn how to play Minesweeper.
- Navigate back to the main screen.
- Exit the application.

### Don't Push Screen
- Return to the main screen.
- Open a YouTube video as a warning.

## MinesweeperGame Class
- Implements the Minesweeper game logic.
- Handles bomb placement, button interactions, and game outcome.
- Utilizes sound effects for bomb explosions and game-winning moments.
- Displays popups for game results.

## MinesweeperApp Class
- Sets up and runs the Minesweeper game itself.

## MyApp Class
- Manages the overall application structure.
- Utilizes the Kivy ScreenManager for screen transitions.
- Integrates the Main Screen, Game Screen, Settings Screen, and Don't Push Screen.


Note: Ensure that you have the required audio files for a complete gaming experience. Adjust the file paths accordingly.

Feel free to explore, enjoy the Minesweeper game, and have fun!
