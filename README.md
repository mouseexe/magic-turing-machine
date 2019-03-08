# Magic: The Gathering is Turing complete

Just want to see the deck? Here's [decklist with no explanation](https://tappedout.net/mtg-decks/spirit-of-turing/).

## TODO: What is a Turing machine?

## TODO: How do we set up the machine?

## How does the machine run?
Since a Turing machine needs a tape and a head to read it, we need to represent this in our game.
This is the large set of creature tokens we set up.
We have 18 unique symbols, represented by the letters A through S (excluding Q), which we have in game as creature types.
We have one type for each symbol, then we assign either Yeti or Zombie to each token as well, designating if it is on the left or right side of the tape.
For ease of management, we will also set up a single creature type for each symbol per side, so that we can create tokens that behave as both.
We end up with creature tokens such as a Creature - Ape Ally Yeti, or Creature - Ape Archer Zombie. 

Our head "reads" by watching for creature token deaths.
Whenever a creature token dies, this is effectively being at the center of the tape, being read by the head.
Our Rotlung Reanimators serve as our transition function.
At any given time, we have 18 Rotlung Reanimators phased in, watching for creature tokens to die.
There's two Rotlung Reanimators for each symbol, with one being phased in and the other phased out.
Whenever a creature dies, the phased in Rotlung Reanimator matching its creature type will see the death, and create a new token based on the transition function.
When a new creature token (or any creature, but we'll address that later) enters the battlefield, a few things happen.

First, our opponent's Noxious Ghouls matching Yeti or Zombie will go on the stack.
There are two of them, so there are 2 -1/-1's hitting whichever side of the tape wasn't just appended.

Second, our next opponent's Aether Flash goes onto the stack, ready to deal 2 damage to the newest member of the tape.

Third, our Valor in Akros and Gruul Ragebeast will go onto the stack.
Since they trigger at the same time, you choose which order they go onto the stack.
Because this machine runs free of human interaction, it is designed to not matter which order you apply them.
For this example, let's say that the Valor in Akros goes on first, then the Gruul Ragebeast second.

The Gruul Ragebeast trigger happens first.
The new token has to target an opponent's creature, and the only one without Shroud is a weakened Dread Slaver.
The two creatures fight, Dread Slaver dealing a grand total of 1 damage to our token.
The amount of damage our token deals to Dread Slaver doesn't matter, as it is Indestrucible thanks to That Which Was Taken.

Then Valor in Akros triggers.
Everything on the field gets +1/+1, moving each creature on the appended side of the tape one farther away from death.

Now Aether Flash goes off.
This deals just enough damage to the new creature token to bring it 1 point of damage away from death.

Now the Noxious Ghouls activate.
Everything on the opposite side of the tape gets -2/-2, which is a net of -1/-1 after the Valor in Akros.
This moves everything 1 point of damage closer to death, which kills the weakest.

At this point the cycle continues.
A Rotlung Reanimator triggers based on what symbol just died, and everything repeats.

If we ever run out of tape, that means nothing dies after a cycle finishes.
This means that the next item on the stack will come off, which is a carefully positioned extra Rotlung Reanimator trigger.
This Rotlung Reanimator watches for Weirds to die, and then creates a Weird when one does.
We've given this Rotlung Reanimator to the player on our left, while the rest are controlled by the player across from us.
This will ensure that the Weird trigger will go on the stack first, and never come off unless all other triggers are finished.
We have a Dralnu's Crusade to modify Weirds to be Weird Sands, which represent our blank symbol.
A Weird Sand is weakened enough by a Engineered Plague that it will die to the Aether Flash, causing a Sand to die.
This will then send the entire death cycle back in motion.

## How do we change states?
Changing states is done by abusing a mechanic known as phasing.
We have enchanted most of our Rotlung Reanimators with Cloaks of Invsibility, so that half of them are phased out at any given time.
We can change the state by swapping the phased in and out Rotlung Reanimators.
We swap them by duplicating a Time and Tide permanently on the stack with a Dualcaster Mage.

To trigger the Dualcaster Mage entering, all we need to do is kill it.
When it first entered, it fought the Dread Slaver, just like all the creature tokens.

When it dies, it will return to play, and be forced to target and cast Time and Tide.
To kill it, we create a unique creature token whenever we want to change states, a Trilobite.
A hacked and color-shifted Dragon Tempest triggers on Trilobites entering, which are forced to target Dualcaster Mage as the only thing without shroud or protection from blue.
Felhide Petrifier gives our Trilobites Deathtouch, which kills the Dualcaster instantly.

It then returns, which casts Time and Tide and swaps the states.
The Trilobite will die to the Aether Flash, and a separate set of Rotlung Reanimators will process the particular Trilobite to get the correct new creature onto the tape.

A Noxious Ghoul for both Trilobites and Humans will work to cancel out the stat boost from Valor of Akros as the non-tape pieces enter play.
To ensure that the Dualcaste Mage doesn't die to tape movement, as we can't make it a Yeti or Zombie to ensure it doesn't move the tape itself, we have to equalize the -1/-1's it takes from other Noxious Ghouls.

We use a color-shifted Death's Presence to give +1/+1 counters to Dualcaster Mage, which is the only creature without protection from blue.
This ensures that every time a creature dies, it boosts the toughness of Dualcaster Mage more than the next creature entering will subtract from it.
