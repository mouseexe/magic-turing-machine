import sys
import fileinput

# Represents a single space on the tape
class Space:
  def __init__(self, symbol, left, right):
    self.symbol = symbol
    self.left = left
    self.right = right

# Represents the tape of the machine
class Tape:
  def __init__(self):
    self.head = None
    self.left = None

# Saves the binary state of the machine
class State:
  def __init__(self, auto):
    self.state = True
    self.auto = auto

# Colors for easier reading
class bcolors:
  WARNING = '\033[93m'
  ENDC = '\033[0m'

# Run the program
def main():
  automatic = 'y' == input('Automatic mode? (y/n): ')
  state = State(automatic) # Initialize state
  tape = Tape() # Initialize tape
  space = None # Set a null space for the start of the list
  if len(sys.argv) == 1:
    tapeString = input('Enter a tape (non-valid characters will be replaced by blank spaces): ') # Grab tape from the user
    for char in tapeString: # Process user tape
      if char.lower() not in 'abcdefghijklmnoprs':
        char = 's'
      if char.isupper(): # Check for head
        newSpace = Space(char.lower(), space, None)
        if space:
          space.right = newSpace
        space = newSpace
        tape.head = space
      else: # Otherwise add as normal space
        newSpace = Space(char, space, None)
        if space:
          space.right = newSpace
        space = newSpace

      if tape.left == None: # Set far left of tape if not already set
        tape.left = space
  else:
    for line in fileinput.input():
      for char in line:
        if char.lower() not in 'abcdefghijklmnoprs':
          char = 's'
        if char.isupper(): # Check for head
          newSpace = Space(char.lower(), space, None)
          if space:
            space.right = newSpace
          space = newSpace
          tape.head = space
        else: # Otherwise add as normal space
          newSpace = Space(char, space, None)
          if space:
            space.right = newSpace
          space = newSpace

        if tape.left == None: # Set far left of tape if not already set
          tape.left = space

  if tape.head: # Check that tape has a head
    while readHead(state, tape): # Loop until halt
      print(printTape(tape)) # Display machine progress
      if not state.auto:
        input() # Allow user to manually increment
    with open("output.txt", "w") as text_file:
          print(printOutput(tape), file=text_file)
  else:
    print('Head required.')

def readHead(state, tape):
  # Ensure there are no empty spaces on the edges of the tape
  if tape.head.left == None:
    tape.head.left = Space('s', None, tape.head)
    tape.left = tape.head.left
  if tape.head.right == None:
    tape.head.right = Space('s', tape.head, None)

  if state.state: # State Alpha
    if tape.head.symbol == 'a':
      tape.head.symbol = 'r'
      tape.head = tape.head.left
    elif tape.head.symbol == 'b':
      tape.head.symbol = 'c'
      tape.head = tape.head.right
    elif tape.head.symbol == 'c':
      tape.head.symbol = 'd'
      tape.head = tape.head.left
    elif tape.head.symbol == 'd':
      tape.head.symbol = 'a'
      tape.head = tape.head.right
    elif tape.head.symbol == 'e':
      tape.head.symbol = 'f'
      tape.head = tape.head.right
    elif tape.head.symbol == 'f':
      tape.head.symbol = 'e'
      tape.head = tape.head.left
    elif tape.head.symbol == 'g':
      tape.head.symbol = 'h'
      tape.head = tape.head.right
    elif tape.head.symbol == 'h':
      tape.head.symbol = 'i'
      tape.head = tape.head.left
    elif tape.head.symbol == 'i':
      tape.head.symbol = 'e'
      tape.head = tape.head.right
    elif tape.head.symbol == 'j': # Transition state
      tape.head.symbol = 'k'
      tape.head = tape.head.left
      state.state = False
    elif tape.head.symbol == 'k': # Transition state
      tape.head.symbol = 'i'
      tape.head = tape.head.left
      state.state = False
    elif tape.head.symbol == 'l': # Transition state
      tape.head.symbol = 'b'
      tape.head = tape.head.left
      state.state = False
    elif tape.head.symbol == 'm':
      tape.head.symbol = 'p'
      tape.head = tape.head.left
    elif tape.head.symbol == 'n':
      tape.head.symbol = 'm'
      tape.head = tape.head.right
    elif tape.head.symbol == 'o': # Halt state
      return False
    elif tape.head.symbol == 'p': # Transition state
      tape.head.symbol = 'o'
      tape.head = tape.head.right
      state.state = False
    elif tape.head.symbol == 'r':
      tape.head.symbol = 's'
      tape.head = tape.head.right
    elif tape.head.symbol == 's':
      tape.head.symbol = 'r'
      tape.head = tape.head.left
  else: # State Bravo
    if tape.head.symbol == 'a':
      tape.head.symbol = 's'
      tape.head = tape.head.right
    elif tape.head.symbol == 'b':
      tape.head.symbol = 's'
      tape.head = tape.head.right
    elif tape.head.symbol == 'c':
      tape.head.symbol = 'a'
      tape.head = tape.head.left
    elif tape.head.symbol == 'd':
      tape.head.symbol = 'c'
      tape.head = tape.head.right
    elif tape.head.symbol == 'e': # Transition state
      tape.head.symbol = 'j'
      tape.head = tape.head.right
      state.state = True
    elif tape.head.symbol == 'f':
      tape.head.symbol = 'g'
      tape.head = tape.head.left
    elif tape.head.symbol == 'g':
      tape.head.symbol = 'f'
      tape.head = tape.head.right
    elif tape.head.symbol == 'h':
      tape.head.symbol = 'g'
      tape.head = tape.head.left
    elif tape.head.symbol == 'i':
      tape.head.symbol = 'h'
      tape.head = tape.head.right
    elif tape.head.symbol == 'j': # Transition state
      tape.head.symbol = 'e'
      tape.head = tape.head.right
      state.state = True
    elif tape.head.symbol == 'k':
      tape.head.symbol = 'h'
      tape.head = tape.head.right
    elif tape.head.symbol == 'l':
      tape.head.symbol = 'm'
      tape.head = tape.head.right
    elif tape.head.symbol == 'm':
      tape.head.symbol = 'n'
      tape.head = tape.head.left
    elif tape.head.symbol == 'n':
      tape.head.symbol = 'm'
      tape.head = tape.head.right
    elif tape.head.symbol == 'o': # Transition state
      tape.head.symbol = 'r'
      tape.head = tape.head.left
      state.state = True
    elif tape.head.symbol == 'p':
      tape.head.symbol = 'r'
      tape.head = tape.head.right
    elif tape.head.symbol == 'r':
      tape.head.symbol = 'l'
      tape.head = tape.head.left
    elif tape.head.symbol == 's':
      tape.head.symbol = 'b'
      tape.head = tape.head.left
  return True

def printTape(tape):
  curr = tape.left
  printString = ''
  while curr:
    if curr is tape.head:
      printString += bcolors.WARNING + curr.symbol.upper() + bcolors.ENDC
    else:
      printString += curr.symbol
    curr = curr.right
  return printString

def printOutput(tape):
  curr = tape.left
  printString = ''
  while curr:
    if curr is tape.head:
      printString += curr.symbol.upper()
    else:
      printString += curr.symbol
    curr = curr.right
  return printString

main()
