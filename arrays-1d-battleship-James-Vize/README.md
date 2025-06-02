# Lab: Array Battleship

In the classic game "Battleship" players attempt to guess the the position of a ship on a cartesian coordinate plane.

In this lab we will create a simplified version of the game:

- There will be one dimension (an array instead of a grid)
- There will be one ship the occupies a single position on the array
- One player will place the ship, and the other will guess until the ship is found

The gameplay will proceed as follows:

- Player one is prompted to enter a board size.
- Player one is prompted to enter the ship's position. The position text will be hidden so that the other player can't see it.
- Player two is prompted to guess the ship's coordinate.
- After the board is initialized (player one's part) and after each guess, the board is displayed with the coordinates the player 
has guessed so far.
  - X indicates a hit
  - O indicates a miss
  - . indicates that the position has not been guessed
- A message is displayed telling player two if the ship was hit.
- The game continues until the player guesses the ship's coordinate correctly, at which point the program exits.

Proper programming practices must be followed:

- Display informative prompts and messages.
- Validate that player 2 has entered an integer for his/her guess.
- Validate that player 2's guess is in range of the board size.

*Example Output:*

```
Welcome to Battleship!
Player 1, Enter the board size: 4
Player 1, Enter the ship coordinate: 
 . | . | . | . |
 1 | 2 | 3 | 4 |
Player 2, Enter a guessed coordinate: 1
 O | . | . | . |
 1 | 2 | 3 | 4 |
Miss!
Player 2, Enter a guessed coordinate: 2
 O | X | . | . |
 1 | 2 | 3 | 4 |
Hit! You sank the ship!
```
