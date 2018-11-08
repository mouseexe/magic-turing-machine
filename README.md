# magic-turing-machine
Magic: the Gathering is Turing complete.

## What does that mean? 
A system is Turing complete if you can replicate any Turing machine inside of it. In this example, we use a (2,3) universal Turing machine, or a "2 state, 3 color" Turing machine that can itself replicate any other Turing machine.

## What is a Turing machine?
A Turing machine is a state machine that reads input and writes output to a two direction, infinitely long tape, or strip of paper. We read one symbol at a time off this tape, at the head, or middle of the machine. The head will read the symbol below it and replace it with a new symbol, then move the tape either left or right. We dictate this behavior with a pre-defined set of rules. For our (2,3) universal Turing machine, our rules are as follows:

| | Alpha | Beta |
| :---: | :---: | :---: |
| (A) | P(B), R, Beta | P(C), L, Alpha |
| (B) | P(C), L, Alpha | P(C), R, Beta |
| (C) | P(B), L, Alpha | P(A), R, Alpha |

Let's dissect what this means. The top row shows our states, in this case we have Alpha and Beta. These represent the '2' in (2,3). On the left column, we have (A), (B), and (C), our "colors." These represent the '3' in (2,3). When the head receives a new symbol, it checks this table to know what to do. If we were in Alpha and read (A), we see: "P(B), R, Beta"

This means that we print (B) overtop of the existing symbol, writing over it. Then we move the head to the right. Finally, we change states from Alpha to Beta. We always follow one of these 6 rules, depending on what state we're in and color we receive.

## What does this accomplish?
Turing machines can be used to solve a variety of problems. The one we build today won't really solve any problem in particular, and is more a proof of concept that we can build a universal Turing machine inside of Magic. If you're interested in the types of problems Turing machines can solve, I highly recommend searching online to see what they can achieve.

## How do we know that a (2,3) Turing machine is actually universal?
http://www.wolframscience.com/prizes/tm23/TM23Proof.pdf
Here's a 44 page proof written in 2007 by Alex Smith. He uses notation with the states being A/B, and the colors being 0,1,2, but the machine follows the same rules. This is a little in depth, so don't be worried if you don't really understand what's going on.
