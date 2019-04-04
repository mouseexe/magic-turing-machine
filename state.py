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
  def __init__(self, mode):
    self.state = True
    self.mode = mode

# Colors for easier reading
class bcolors:
  ALPHA = '\033[93m'
  BRAVO = '\033[94m'
  ENDC = '\033[0m'

# Run the program
def main():
  config = input('Mode? (silent, small, auto, other): ')
  if config == 'silent':
    state = State(3)
  elif config == 'small':
    state = State(2)
  elif config == 'auto':
    state = State(1)
  else:
    state = State(0)
  tape = Tape() # Initialize tape
  space = None # Set a null space for the start of the list
  heads = []
  if len(sys.argv) == 1:
    tapeString = input('Enter a tape (non-valid characters will be replaced by blank spaces): ')
    for char in tapeString: # Process user tape
      if char.lower() not in 'abcdefghijklmnoprs':
        continue
      if char.isupper(): # Check for head
        newSpace = Space(char.lower(), space, None)
        if space:
          space.right = newSpace
        space = newSpace
        heads.append(space)
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
          continue
        if char.isupper(): # Check for head
          newSpace = Space(char.lower(), space, None)
          if space:
            space.right = newSpace
          space = newSpace
          heads.append(space)
        else: # Otherwise add as normal space
          newSpace = Space(char, space, None)
          if space:
            space.right = newSpace
          space = newSpace

        if tape.left == None: # Set far left of tape if not already set
          tape.left = space

  tape.head = heads[int(len(heads)/2)]

  if tape.head: # Check that tape has a head
    while readHead(state, tape): # Loop until halt
      if state.mode == 2:
        print('{}'.format(printTape(tape, state)), end='\r')
      if state.mode == 1:
        print(printTape(tape, state))
      if state.mode == 0:
        input(printTape(tape, state))
    print(printTape(tape, state))
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

def printTape(tape, state):
  curr = tape.left
  printString = ''
  while curr:
    if curr is tape.head:
      if state.state:
        printString += bcolors.ALPHA + curr.symbol.upper() + bcolors.ENDC
      else:
        printString += bcolors.BRAVO + curr.symbol.upper() + bcolors.ENDC
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
