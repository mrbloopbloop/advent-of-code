# Advent of Code, 2025 - Day 1

To view the complete puzzle, go [here](https://adventofcode.com/2025/day/1)

## Puzzle 1

The first puzzle has us figuring out a password. There is a dial numbered zero to ninetynine and instructions on how to spin the dial. The dial starts at the fifty position. Our password is defined as the number of times the dial is at the 0 position after completing a step in the instructions.

### Thoughts

Some things that make this puzzle easier:
- Using a dial is similar to fineite fields in math, so using the modulo operator could be useful
- The instructions are in a file that is well formatted. Each instruction sits on its own line. This will be easier to parse.

#### Finite Fields

In math there is a useful concept called finite fields. We already use them intuitivly. A good example of a finite field is a clock. If we only look at the minute hand, it is always going to be somewhere between zero minutes and fiftynine minutes. One more minute after fifty nine and we wrap around to zero. This is very much like our dial in the puzzle. We will use that to our advantage.

#### Well Behaved Input

In this puzzle our input is very well behaved. There are no errors or corruptions. We can lean on that. In the real world we would need to validate all the data before acting on it. It would be smart to write the code in such a way to allow for this validation to be added in the future.

### Solution

The code I wrote uses a `processInstruction` function. This function takes an instruction string and the current possition as an integer and then returns the new position as an integer. In the `main` function I set the initial position and a password variable. I then opened the puzzle input and iterated over each line and used the `processInstruction` function on each line. Before ending each itteration, I would check if the possition was zero. If so, I incremented the password variable. Once the for loop was complete, I print the password.

## Puzzle 2

Puzzle 2 reveals there is a new protocol to use! 
Our new protocol will be almost identical to the previous one save for how we count our zeros. This new protocol includes any time our dial hits a zero *during* an instruction as well as after.

### Thoughts

So with this we have to modify our `processInstruction` function. I suppose there could be a new version of the function that implements the zero check and returns the number of zeros instead of the new position.

However, that wouldn't work because we lose track of the current possition. Perhaps use a dictionary or dataclass? That would work nicely. I will try using a dictionary.

### Solution

I modified the previous `processInstruction` function. Instead of returning the position as an integer, it returned a dictionary with the position and number of times the dial showed a zero. With this I iterated over the file again this time keeping track of position and number of zeros.

Apart from typos, this worked with no issues!
