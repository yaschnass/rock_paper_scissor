# Rock, Paper, Scissors Game

## Overview

This Python program implements a Rock, Paper, Scissors game where a human player competes against various computer players with different strategies. The game supports multiple types of computer opponents and handles scoring and game rounds automatically.

## Features

- **Human Player**: Interact with the game via standard input.
- **Computer Players**: Includes:
  - `RandomPlayer`: Chooses moves randomly.
  - `AllRockPlayer`: Always plays "rock".
  - `ReflectPlayer`: Repeats the opponent's previous move.
  - `CyclePlayer`: Cycles through moves in the order "rock", "paper", "scissors".
- **Game Mechanics**: Play multiple rounds, score tracking, and game result announcements.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yaschnass/rock_paper_scissor.git
    ```
2. Navigate into the project directory:
    ```bash
    cd rock_paper_scissor
    ```
3. Ensure you have Python 3 installed. The code is compatible with Python 3.x.

## Usage

1. Run the game:
    ```bash
    python3 rock_paper_scissors.py
    ```
2. Follow the prompts to choose between Rock, Paper, or Scissors.
3. The game will display the result of each round and your score.
4. After three rounds, the game will display the final results and ask if you want to play again.

## Game Flow

1. **Initialization**: The game initializes with a human player and a `CyclePlayer` opponent.
2. **Rounds**: The game plays three rounds, where each round consists of:
   - Each player choosing a move.
   - Determining the winner based on the moves.
   - Updating and displaying scores.
3. **End of Game**: After three rounds, the game announces the final results and asks if you want to play again.

## Classes

- **`Player`**: Base class for players with methods `move()` and `learn()`.
- **`AllRockPlayer`**: Always plays "rock".
- **`RandomPlayer`**: Chooses moves randomly.
- **`HumanPlayer`**: Prompts the user for their move.
- **`ReflectPlayer`**: Repeats the opponent's last move.
- **`CyclePlayer`**: Cycles through "rock", "paper", and "scissors".
- **`Game`**: Manages game logic, rounds, and scoring.

## Example

To play a game with a human player and a `CyclePlayer` opponent, the `Game` class is initialized as follows:

```python
game = Game(HumanPlayer(), CyclePlayer())
game.play_game()
```

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a description of your changes.

## Contact

For any questions or feedback, please contact [yaschnass](https://github.com/yaschnass) on GitHub.

