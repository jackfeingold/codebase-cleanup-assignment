# codebase-cleanup-template

To get started with the ["Codebase Cleanup" Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/codebase-cleanup/README.md).

## Setup

Create virtual environment:

```sh
conda create -n codebase-env python=3.8
```

```sh
conda activate codebase-env
```

Install packages:

```sh
pip install -r requirements.txt
```


## Configuration

Obtain a premium AlphaVantage API Key [here](https://www.alphavantage.co/).

Sign up for a [SendGrid Account](https://sendgrid.com/), verify single sender, then obtain a Sendgrid API Key. 


Set environment variables using a ".env" file approach:

```sh
ALPHAVANTAGE_API_KEY="..."

SENDER_ADDRESS="example@gmail.com"
SENDGRID_API_KEY="SG...."
```


## Usage

Run the game:

```sh
python app/game.py
```
The game is designed to simulate a game of rock, paper, scissors between the user and the computer.  When the game is activated as described above, the user will be asked to choose between rock, paper, and scissors.  When the user's input is recorded, the computer will then choose a choice from the same list at random.

Once both of the choices are recorded, the program will then compare the choices in a function called winnerDetermination() and determine a winner.  The parameters for the function are the computer's choice, denoted as "computer", and the user's choice, denoted as "user".  In the code, the function is defined as winnerDetermination(computer, user).  There is an if statement that looks at the possible conditions where the user wins and ties, assigning a True or False value to a variable called win.  Before this, however, the function compares the two parameters.  If they are the same, the program will write that there is a tie.  If the conditions that satisfy a user victory are present, win = True and the program will print a congratulatory message.  If the conditions are not true and there is not a tie, win = False and the program will alert the user that they have lost the game.

