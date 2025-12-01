#! /usr/bin/env python3.14

# --- Advent of Code ---
# ------- Day 01 -------

# --- Imports ---
from rich import print
from pathlib import Path



# --- Functions ---
def processInstruction(
        instruction: str, 
        currentPosition: int) -> int:
    '''
    precessInstruction takes an instruction string allong with the
    current position as an integer. It then returns the new 
    position as an integer.
    '''

    # Using a high value integer for a finite field
    value: int = 10_000 + currentPosition

    # Process instruction. Used if blocks given the two instructions.
    if instruction[0] == 'R':
        value += int(instruction[1:-1])
    elif instruction[0] == 'L':
        value -= int(instruction[1:-1])

    # Using modulo to enforce the finite field
    position: int = value % 100

    return position

def processMethod0x434C49434B(
        instruction: str,
        currentPosition: int) -> dict:
    '''
    processMethod0x434C49434B takes an instruction string along with
    the current position as an integer. It then returns a dictionary
    containing the new position as an integer and the number of times
    the dial showed a zero value.
    '''

    # Using a high value integer for a finite field
    value: int = 10_000 + currentPosition

    # Keep track of zeros
    zeros: int = 0
    
    # Keep track of rotations
    rotations: int = int(instruction[1:-1])

    # Process instruction. Used if blocks given the two instructions.
    if instruction[0] == 'R':
        for _ in range(rotations):
            value += 1

            # Check for zero value
            if value % 100 == 0:
                zeros +=1

    elif instruction[0] == 'L':
        for _ in range(rotations):
            value -= 1

            # Check for zero value
            if value % 100 == 0:
                zeros +=1

    # Using modulo to enforce the finite field
    position: int = value % 100

    return {
            "position":position,
            "zeros":zeros
            }



# --- Main ---
def main():

    # --- Puzzle 1 ---

    # Set starting position
    position: int = 50
    password: int = 0

    # Read instructions from file
    filepath: Path = Path('./puzzle1.input')
    with filepath.open() as file:
        
        # Process instructions one by one
        for line in file:
            position = processInstruction(line, position)

            # Check if position is zero
            if position == 0:
                password += 1

    # Report the password
    print("--- Puzzle #1 ---")
    print(f'The password is "{password}"')

    # --- Puzzle 2 ---

    # Set starting position
    position: int = 50
    password: int = 0

    # Read instructions from file
    with filepath.open() as file:
        
        # Process instructions one by one
        for line in file:
            data = processMethod0x434C49434B(line, position)
            position = data["position"]
            password += data["zeros"]


    # Report the password
    print("--- Puzzle #2 ---")
    print(f'The password is "{password}"')
    


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exitting script now!")
        exit()
