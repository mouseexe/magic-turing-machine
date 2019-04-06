# Magic: The Gathering is Turing complete

Just want to see the deck? Here's [decklist with no explanation](https://tappedout.net/mtg-decks/spirit-of-turing/).

## What is a Turing machine?
A [Turing machine](https://en.wikipedia.org/wiki/Turing_machine) is a simple computer, a state machine with a two-way infinite tape from which it reads input and writes output.

A [universal Turing machine](https://en.wikipedia.org/wiki/Universal_Turing_machine) (UTM) is a Turing machine that is capable of simulating any other Turing machine.

We are representing the UTM created by Yurii Rogozhin in his [1996 paper](https://www.sciencedirect.com/science/article/pii/S0304397596000771)

## How do we set up the machine?
In order to establish the machine, we need a few core cards.
There can be a couple ways to get to that stage, but we'll focus on just one path for now.
1. Have 9 mana sources available, at least 3 mana's worth being non-land.
2. Cast ![Paradox Engine](https://img.scryfall.com/cards/large/front/f/d/fd8ccd81-9e11-47fa-8e16-064c52c24506.jpg?1543700975) and Isochron Scepter, imprinting a draw cantrip (we'll use Brainstorm).
3. Using Isochron Scepter to cast Brainstorm, we can untap our non-land mana sources and and the Isochron Scepter to make infinite mana and draw as many cards as we need.
4. Cast Soul Foundry, imprinting Clever Impersonator.
5. Activate Soul Foundry two times to make two copies of Isochron Scepter, imprinting Noxious Revival and Artificial Evolution.
6. Cast Alchor's Tomb, Dralnu's Crusade, Dragon Tempest, Death's Presence, Ivory Mask, That Which Was Taken, Unnatural Selection, Valor in Akros, Crippling Blight, Leyline of Anticipation, and Engineered Plague (naming Weird as the creature type).
7. Activate Soul Foundry X times to create X copies of Dralnu's Crusade.
8. Activate the Artificial Evolution Isochron Scepter to assign proper rules text to each Dralnu's Crusade (represented by images to be added later).
9. Activate the Articicial Evolution Isochron Scepter to assign proper rules text to Dragon Tempest.
10. Activate Alchor's Tomb to color Dragon Tempest and Death's Presence to blue.
11. Cast Vengeful Dead, Dread Slaver, Gruul Ragebeast, Crystalline Sliver, Ward Sliver, Rotlung Reanimator, Noxious Ghoul, Felhide Petrifier, and Drana's Chosen.
12. Activate Soul Foundry to create enough copies of Drana's Chosen, Rotlung Reanimator, Ward Sliver, and Noxious Ghoul.
13. Duplicate and Donate all needed permanents to each player, recurring Donate with the Noxious Revival Isochron Scepter (exact donate list tba).
14. Cast Mindslaver and activate it on an opponent with Arcane Lighthouse, then pass the turn.
15. Activate Arcane Lighthouse to remove shroud from Crystalline Sliver.
16. Activate the Artifical Evolution Isochron Scepter to change the rules text of Crystalline Sliver.
17. Pass the turn back to yourself.
18. Create a token with one of the Drana's Chosen.
19. Activate the Artifical Evolution Isochron Scepter to change the rules text of the Rotlung Reanimators, Drana's Chosen, Ward Slivers, Felhide Petrifier, Dread Slaver, Vengeful Dead, and all but two of the Noxious Ghouls.
20. Enchant the previously created token with a Cloak of Invisibility.
21. Activate Soul Foundry to enchant half of the Rotlung Reanimators with Cloak of Invisiblity.
22. Sacrifice the token to Ashnod's Altar and return it to your hand with the Noxious Revival Isochron Scepter.
23. Cast Time and Tide to phase out half of the Rotlung Reanimators.
24. Cast Cloak of Invisibility on a Rotlung Reanimator, then activate Soul Foundry to enchant the rest.
25. Activate Soul Foundry to create a copy of Isochron Scepter, imprinting Ebony Charm.
26. Bring all of your opponents to 1 life by activating the Ebony Charm Isochron Scepter.
27. Create a Weird token with Drana's Chosen.
28. Pass the turn, stopping on upkeep.
29. Cast Gather Specimens.
30. Activate the needed Drana's Chosen to establish the initial tape.
31. Cast Dualcaster Mage.
32. Activate the Artifical Evolution Isochron Scepter to assign proper rules text to the last two Noxious Ghouls.
33. Cast Time and Tide, hold priority.
34. Sacrifice a Weird, hold priority.
35. Sacrifice one of the two middle tokens.
36. The machine will now run autonomously until a halt state is reached.

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

## Credits
Special thanks to Alex Churchill for the basis of this work.

Additional thanks to reddit users /u/Rufus\_Reddit, /u/StellaAthena, /u/ais523, and everyone else on the reddit thread I posted in November 2018 for their assistance.

Thank you and I'm very sorry to every one of my friends who have had to listen to me talk about this for the last year.
