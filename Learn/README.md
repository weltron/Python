# ROCK-PAPER-SCISSORS 

#### Video Demo: https://youtu.be/5EIlGe2Y13M)
    
### **Description** 
 A simple command-line game of Rock-Paper-Scissors, played against the computer.

## Getting Started
These instructions will help users to navigate to the game directory and test the game. 

### Prerequisites

Python 3.10

### Installing

1. Clone the repository:
```
git clone https://github.com/code50/13233377.git
```
2. Navigate to project directory:
``` 
cd project
```
3. Run game:
```
python project.py
```
4. Run test_project using pytest:
```
pytest test_project.py
```

### Game Play

The game has three moves namely:
- rock
- paper
- scissors

The game prompts the user to select between the three moves continously until 10 rounds have been compeleted or when the user types in  `quit` to end the game. 

The user is required to select only those moves and any invalid entry reprompts userto select from the available options.

The `project.py` file contains a `main` function and 5 other functions that facilitate the game play. 

The `beats` function takes two parameters that returns the game logic of what each move does. 

The `player` function prompts the user for input and verifies that the input entered is valid 

The `random_player` function randomly generates moves from a list of valid moves

The `round` function simulates each round of play by invoking the `beats` function to compare the moves made by  `player` and `random_player` then returns a tuple of two values representing the scores earned by each move

The `game` function takes two parameters and loops the `round` functions 10 times while keeping track of the scores earned on each round of play. After the last round, this function computes the scores of each player and declares the winner or draw based on the points earned by the players. 

The `main` function contains a number of variables that are passed into the `game` variable as parameters


### Testing

We use pytest to run a number of tests to ensure that our game is running as expected. 

We started by importing a number of modules that are used in the testing.

We tested the `beats` function using `test_beats` which took two moves and assertained that the resulting boolean value was as we expected.

We tested the `test_player` function to test the `player` function. We installed mock using `pip install pytest-mock` to help us run mock inputs that are shown in under the ` @pytest.mark.parametrize` module just before the function to assertain the values entered in inputs are valid values and invalid nes are rejected.

We then used the `random` module in the `test_random_player` function to confirm that the valid choices are in the list of choices applcable to the game. 

### Running Test

The following code is run to test the `test_project.py` file
```
pytest test_project.py
```
Green dots appear to confirm that the test was successful.

### Built With

- Python 3

### Authors

- Weltron Bitange

### Acknowledgments
- Inspiration was taken from the classic Rock-Paper-Scissors game. 





