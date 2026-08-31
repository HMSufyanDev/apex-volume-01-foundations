# Rock, Paper, Scissors

A command-line Rock, Paper, Scissors game built with Python.

The player plays against the computer, and the game keeps running until the player chooses to quit.

I built this project to practice loops, conditions, user input, dictionaries, random values, and score tracking.

## How to Play

Run the program and enter:

```text
R → Rock
P → Paper
S → Scissor
Q → Quit
```

The computer randomly chooses its move.

The program then tells you who won the round and updates the scoreboard.

## Example

```text
=== Welcome to Rock, Paper, Scissors! ===

Scoreboard -> You: 0 | Computer: 0 | Draws: 0
Enter choice (R for Rock, P for Paper, S for Scissor, or Q to Quit): r

You chose: Rock | Computer chose: Scissor
You Win this round!

Scoreboard -> You: 1 | Computer: 0 | Draws: 0
```

When the player quits, the program displays the final result.

## Features

* Player vs computer
* Random computer choices
* Score tracking
* Draw tracking
* Input validation
* Continuous game loop
* Quit option
* Final scoreboard
* Overall winner

## Concepts Practiced

* Variables
* Dictionaries
* `while` loops
* `if / elif / else`
* `break`
* `continue`
* `input()`
* `lower()`
* `random.choice()`
* Comparison operators
* Boolean logic
* f-strings

## Program Flow

The main game follows this structure:

```text
Start
 ↓
Show scoreboard
 ↓
Get player's choice
 ↓
Is it Q?
 ├── Yes → Quit
 └── No
      ↓
Is the choice valid?
 ├── No → Show error → Continue
 └── Yes
      ↓
Generate computer choice
      ↓
Compare choices
      ↓
Update score
      ↓
Start next round
```

## Why I Built It

This was a good project for understanding how multiple concepts work together.

The biggest thing I practiced was keeping a program running continuously with a `while` loop while using `break` and `continue` to control what happens inside the loop.

## How to Run

Run the Python file from the terminal:

```bash
python rock_paper.py
```

Then follow the instructions shown in the terminal.
