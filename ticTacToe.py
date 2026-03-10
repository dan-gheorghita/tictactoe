```python
# Initialize the game board with empty spaces
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# Function to print the current state of the game board
def printBoard(board):
    # Print the top row of the board
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')  # Print the horizontal line separating rows
    # Print the middle row of the board
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')  # Print the horizontal line separating rows
    # Print the bottom row of the board
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# Initialize the current player's turn to 'X'
turn = 'X'

# Loop through nine turns (three rows by three columns)
for i in range(9):
    # Print the current state of the board
    printBoard(theBoard)
    # Ask the current player for their next move
    print('Turn for ' + turn + '. Move on which space?')
    # Get the player's input for their move (space number)
    move = input()
    # Update the board with the player's move (replace space with 'X' or 'O')
    theBoard[move] = turn
    # Switch the current player's turn to the next player ('X' to 'O' or vice versa)
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
# Print the final state of the board
printBoard(theBoard)
```