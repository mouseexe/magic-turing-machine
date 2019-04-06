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
2. Cast [Paradox Engine](https://scryfall.com/card/aer/169/paradox-engine) and [Isochron Scepter](https://scryfall.com/card/ema/223/isochron-scepter), imprinting a draw cantrip (we'll use [Brainstorm](https://scryfall.com/card/c18/82/brainstorm)).
3. Using [Isochron Scepter](https://scryfall.com/card/ema/223/isochron-scepter) to cast [Brainstorm](https://scryfall.com/card/c18/82/brainstorm), we can untap our non-land mana sources and and the [Isochron Scepter](https://scryfall.com/card/ema/223/isochron-scepter) to make infinite mana and draw as many cards as we need.
4. Cast [Soul Foundry](https://scryfall.com/card/mrd/246/soul-foundry), imprinting [Clever Impersonator](https://scryfall.com/card/ktk/34/clever-impersonator).
5. Activate [Soul Foundry](https://scryfall.com/card/mrd/246/soul-foundry) two times to make two copies of [Isochron Scepter](https://scryfall.com/card/ema/223/isochron-scepter), imprinting [Noxious Revival](https://scryfall.com/card/nph/118/noxious-revival) and [Artificial Evolution](https://scryfall.com/card/ons/67/artificial-evolution).
6. Cast [Alchor's Tomb](https://scryfall.com/card/me4/178/alchors-tomb), [Dralnu's Crusade](https://scryfall.com/card/pls/104/dralnus-crusade), [Dragon Tempest](https://scryfall.com/card/ima/125/dragon-tempest), [Death's Presence](https://scryfall.com/card/rtr/121/deaths-presence), [Ivory Mask](https://scryfall.com/card/9ed/23/ivory-mask), [That Which Was Taken](https://scryfall.com/card/bok/162/that-which-was-taken), [Unnatural Selection](https://scryfall.com/card/apc/32/unnatural-selection), [Valor in Akros](https://scryfall.com/card/a25/38/valor-in-akros), [Leyline of Anticipation](https://scryfall.com/card/m11/61/leyline-of-anticipation), [Aether Flash](https://scryfall.com/card/7ed/172/aether-flash), and [Engineered Plague](https://scryfall.com/card/7ed/133/engineered-plague) (naming Weird as the creature type).
7. Activate [Soul Foundry](https://scryfall.com/card/mrd/246/soul-foundry) X times to create X copies of [Dralnu's Crusade](https://scryfall.com/card/pls/104/dralnus-crusade).
8. Activate the [Artificial Evolution](https://scryfall.com/card/ons/67/artificial-evolution) [Isochron Scepter](https://scryfall.com/card/ema/223/isochron-scepter) to assign proper rules text to each [Dralnu's Crusade](https://scryfall.com/card/pls/104/dralnus-crusade) (represented by images to be added later).
9. Activate the [Artificial Evolution](https://scryfall.com/card/ons/67/artificial-evolution) [Isochron Scepter](https://scryfall.com/card/ema/223/isochron-scepter) to assign proper rules text to [Dragon Tempest](https://scryfall.com/card/ima/125/dragon-tempest).
10. Activate [Alchor's Tomb](https://scryfall.com/card/me4/178/alchors-tomb) to color [Dragon Tempest](https://scryfall.com/card/ima/125/dragon-tempest) and [Death's Presence](https://scryfall.com/card/rtr/121/deaths-presence) to blue.
11. Cast [Vengeful Dead](https://scryfall.com/card/scg/80/vengeful-dead), [Dread Slaver](https://scryfall.com/card/avr/98/dread-slaver), [Crippling Blight](https://scryfall.com/card/m15/92/crippling-blight), [Gruul Ragebeast](https://scryfall.com/card/gtc/170/gruul-ragebeast), [Crystalline Sliver](https://scryfall.com/card/tpr/207/crystalline-sliver), [Ward Sliver](https://scryfall.com/card/lgn/25/ward-sliver), [Rotlung Reanimator](https://scryfall.com/card/ons/164/rotlung-reanimator), [Noxious Ghoul](https://scryfall.com/card/hop/35/noxious-ghoul), [Felhide Petrifier](https://scryfall.com/card/jou/70/felhide-petrifier), and [Drana's Chosen](https://scryfall.com/card/ogw/84/dranas-chosen).
12. Activate [Soul Foundry](https://scryfall.com/card/mrd/246/soul-foundry) to create enough copies of [Drana's Chosen](https://scryfall.com/card/ogw/84/dranas-chosen), [Rotlung Reanimator](https://scryfall.com/card/ons/164/rotlung-reanimator), [Ward Sliver](https://scryfall.com/card/lgn/25/ward-sliver), and [Noxious Ghoul](https://scryfall.com/card/hop/35/noxious-ghoul).
13. Duplicate and [Donate](https://scryfall.com/card/uds/31/donate) all needed permanents to each player, recurring [Donate](https://scryfall.com/card/uds/31/donate) with the [Noxious Revival](https://scryfall.com/card/nph/118/noxious-revival) [Isochron Scepter](https://scryfall.com/card/ema/223/isochron-scepter) (exact donate list tba).
14. Cast [Mindslaver](https://scryfall.com/card/som/176/mindslaver) and activate it on an opponent with [Arcane Lighthouse](https://scryfall.com/card/cm2/233/arcane-lighthouse), then pass the turn.
15. Activate [Arcane Lighthouse](https://scryfall.com/card/cm2/233/arcane-lighthouse) to remove shroud from [Crystalline Sliver](https://scryfall.com/card/tpr/207/crystalline-sliver).
16. Activate the [Artificial Evolution](https://scryfall.com/card/ons/67/artificial-evolution) [Isochron Scepter](https://scryfall.com/card/ema/223/isochron-scepter) to change the rules text of [Crystalline Sliver](https://scryfall.com/card/tpr/207/crystalline-sliver).
17. Pass the turn back to yourself.
18. Create a token with one of the [Drana's Chosen](https://scryfall.com/card/ogw/84/dranas-chosen).
19. Activate the [Artificial Evolution](https://scryfall.com/card/ons/67/artificial-evolution) [Isochron Scepter](https://scryfall.com/card/ema/223/isochron-scepter) to change the rules text of the [Rotlung Reanimators](https://scryfall.com/card/ons/164/rotlung-reanimator), [Drana's Chosen](https://scryfall.com/card/ogw/84/dranas-chosen), [Ward Slivers](https://scryfall.com/card/lgn/25/ward-sliver), [Felhide Petrifier](https://scryfall.com/card/jou/70/felhide-petrifier), [Dread Slaver](https://scryfall.com/card/avr/98/dread-slaver), [Vengeful Dead](https://scryfall.com/card/scg/80/vengeful-dead), and all but two of the [Noxious Ghouls](https://scryfall.com/card/hop/35/noxious-ghoul).
20. Enchant the previously created token with a [Cloak of Invisibility](https://scryfall.com/card/mir/58/cloak-of-invisibility).
21. Activate [Soul Foundry](https://scryfall.com/card/mrd/246/soul-foundry) to enchant half of the [Rotlung Reanimators](https://scryfall.com/card/ons/164/rotlung-reanimator) with [Cloak of Invisibility](https://scryfall.com/card/mir/58/cloak-of-invisibility).
22. Sacrifice the token to [Ashnod's Altar](https://scryfall.com/card/ema/218/ashnods-altar) and return it to your hand with the [Noxious Revival](https://scryfall.com/card/nph/118/noxious-revival) [Isochron Scepter](https://scryfall.com/card/ema/223/isochron-scepter).
23. Cast [Time and Tide](https://scryfall.com/card/vis/46/time-and-tide) to phase out half of the [Rotlung Reanimators](https://scryfall.com/card/ons/164/rotlung-reanimator).
24. Cast [Cloak of Invisibility](https://scryfall.com/card/mir/58/cloak-of-invisibility) on a [Rotlung Reanimator](https://scryfall.com/card/ons/164/rotlung-reanimator), then activate [Soul Foundry](https://scryfall.com/card/mrd/246/soul-foundry) to enchant the rest.
25. Activate [Soul Foundry](https://scryfall.com/card/mrd/246/soul-foundry) to create a copy of [Isochron Scepter](https://scryfall.com/card/ema/223/isochron-scepter), imprinting [Ebony Charm](https://scryfall.com/card/mir/120/ebony-charm).
26. Bring all of your opponents to 1 life by activating the [Ebony Charm](https://scryfall.com/card/mir/120/ebony-charm) [Isochron Scepter](https://scryfall.com/card/ema/223/isochron-scepter).
27. Create a Weird token with [Drana's Chosen](https://scryfall.com/card/ogw/84/dranas-chosen).
28. Pass the turn, stopping on upkeep.
29. Cast [Gather Specimens](https://scryfall.com/card/ala/45/gather-specimens).
30. Activate the needed [Drana's Chosen](https://scryfall.com/card/ogw/84/dranas-chosen) to establish the initial tape.
31. Cast [Dualcaster Mage](https://scryfall.com/card/cm2/94/dualcaster-mage).
32. Activate the [Artificial Evolution](https://scryfall.com/card/ons/67/artificial-evolution) [Isochron Scepter](https://scryfall.com/card/ema/223/isochron-scepter) to assign proper rules text to the last two [Noxious Ghouls](https://scryfall.com/card/hop/35/noxious-ghoul).
33. Cast [Time and Tide](https://scryfall.com/card/vis/46/time-and-tide), hold priority.
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
Our [Rotlung Reanimators](https://scryfall.com/card/ons/164/rotlung-reanimator) serve as our transition function.
At any given time, we have 18 [Rotlung Reanimators](https://scryfall.com/card/ons/164/rotlung-reanimator) phased in, watching for creature tokens to die.
There's two [Rotlung Reanimators](https://scryfall.com/card/ons/164/rotlung-reanimator) for each symbol, with one being phased in and the other phased out.
Whenever a creature dies, the phased in [Rotlung Reanimator](https://scryfall.com/card/ons/164/rotlung-reanimator) matching its creature type will see the death, and create a new token based on the transition function.
When a new creature token (or any creature, but we'll address that later) enters the battlefield, a few things happen.

First, our opponent's [Noxious Ghouls](https://scryfall.com/card/hop/35/noxious-ghoul) matching Yeti or Zombie will go on the stack.
There are two of them, so there are 2 -1/-1's hitting whichever side of the tape wasn't just appended.

Second, our next opponent's [Aether Flash](https://scryfall.com/card/7ed/172/aether-flash) goes onto the stack, ready to deal 2 damage to the newest member of the tape.

Third, our [Valor in Akros](https://scryfall.com/card/a25/38/valor-in-akros) and [Gruul Ragebeast](https://scryfall.com/card/gtc/170/gruul-ragebeast) will go onto the stack.
Since they trigger at the same time, you choose which order they go onto the stack.
Because this machine runs free of human interaction, it is designed to not matter which order you apply them.
For this example, let's say that the [Valor in Akros](https://scryfall.com/card/a25/38/valor-in-akros) goes on first, then the [Gruul Ragebeast](https://scryfall.com/card/gtc/170/gruul-ragebeast) second.

The [Gruul Ragebeast](https://scryfall.com/card/gtc/170/gruul-ragebeast) trigger happens first.
The new token has to target an opponent's creature, and the only one without shroud is a weakened [Dread Slaver](https://scryfall.com/card/avr/98/dread-slaver).
The two creatures fight, [Dread Slaver](https://scryfall.com/card/avr/98/dread-slaver) dealing a grand total of 1 damage to our token.
The amount of damage our token deals to [Dread Slaver](https://scryfall.com/card/avr/98/dread-slaver) doesn't matter, as it is indestrucible thanks to [That Which Was Taken](https://scryfall.com/card/bok/162/that-which-was-taken).

Then [Valor in Akros](https://scryfall.com/card/a25/38/valor-in-akros) triggers.
Everything on the field gets +1/+1, moving each creature on the appended side of the tape one farther away from death.

Now [Aether Flash](https://scryfall.com/card/7ed/172/aether-flash) goes off.
This deals just enough damage to the new creature token to bring it 1 point of damage away from death.

Now the [Noxious Ghouls](https://scryfall.com/card/hop/35/noxious-ghoul) activate.
Everything on the opposite side of the tape gets -2/-2, which is a net of -1/-1 after the [Valor in Akros](https://scryfall.com/card/a25/38/valor-in-akros).
This moves everything 1 point of damage closer to death, which kills the weakest.

At this point the cycle continues.
A [Rotlung Reanimator](https://scryfall.com/card/ons/164/rotlung-reanimator) triggers based on what symbol just died, and everything repeats.

If we ever run out of tape, that means nothing dies after a cycle finishes.
This means that the next item on the stack will come off, which is a carefully positioned extra [Rotlung Reanimator](https://scryfall.com/card/ons/164/rotlung-reanimator) trigger.
This [Rotlung Reanimator](https://scryfall.com/card/ons/164/rotlung-reanimator) watches for Weirds to die, and then creates a Weird when one does.
We've given this [Rotlung Reanimator](https://scryfall.com/card/ons/164/rotlung-reanimator) to the player on our left, while the rest are controlled by the player across from us.
This will ensure that the Weird trigger will go on the stack first, and never come off unless all other triggers are finished.
We have a [Dralnu's Crusade](https://scryfall.com/card/pls/104/dralnus-crusade) to modify Weirds to be Weird Sands, which represent our blank symbol.
A Weird Sand is weakened enough by a [Engineered Plague](https://scryfall.com/card/7ed/133/engineered-plague) that it will die to the [Aether Flash](https://scryfall.com/card/7ed/172/aether-flash), causing a Sand to die.
This will then send the entire death cycle back in motion.

## How do we change states?
Changing states is done by abusing a mechanic known as phasing.
We have enchanted most of our [Rotlung Reanimators](https://scryfall.com/card/ons/164/rotlung-reanimator) with [Cloaks of Invisibility](https://scryfall.com/card/mir/58/cloak-of-invisibility), so that half of them are phased out at any given time.
We can change the state by swapping the phased in and out [Rotlung Reanimators](https://scryfall.com/card/ons/164/rotlung-reanimator).
We swap them by duplicating a [Time and Tide](https://scryfall.com/card/vis/46/time-and-tide) permanently on the stack with a [Dualcaster Mage](https://scryfall.com/card/cm2/94/dualcaster-mage).

To trigger the [Dualcaster Mage](https://scryfall.com/card/cm2/94/dualcaster-mage) entering, all we need to do is kill it.
When it first entered, it fought the [Dread Slaver](https://scryfall.com/card/avr/98/dread-slaver), just like all the creature tokens.

When it dies, it will return to play, and be forced to target and cast [Time and Tide](https://scryfall.com/card/vis/46/time-and-tide).
To kill it, we create a unique creature token whenever we want to change states, a Trilobite.
A modifieded and color-shifted [Dragon Tempest](https://scryfall.com/card/ima/125/dragon-tempest) triggers on Trilobites entering, which are forced to target [Dualcaster Mage](https://scryfall.com/card/cm2/94/dualcaster-mage) as the only thing without shroud or protection from blue.
[Felhide Petrifier](https://scryfall.com/card/jou/70/felhide-petrifier) gives our Trilobites deathtouch, which kills the Dualcaster instantly.

It then returns, which casts [Time and Tide](https://scryfall.com/card/vis/46/time-and-tide) and swaps the states.
The Trilobite will die to the [Aether Flash](https://scryfall.com/card/7ed/172/aether-flash), and a separate set of [Rotlung Reanimators](https://scryfall.com/card/ons/164/rotlung-reanimator) will process the particular Trilobite to get the correct new creature onto the tape.

A [Noxious Ghoul](https://scryfall.com/card/hop/35/noxious-ghoul) for both Trilobites and Humans will work to cancel out the stat boost from [Valor in Akros](https://scryfall.com/card/a25/38/valor-in-akros) as the non-tape pieces enter play.
To ensure that the [Dualcaster Mage](https://scryfall.com/card/cm2/94/dualcaster-mage) doesn't die to tape movement, as we can't make it a Yeti or Zombie to ensure it doesn't move the tape itself, we have to equalize the -1/-1's it takes from other [Noxious Ghouls](https://scryfall.com/card/hop/35/noxious-ghoul).

We use a color-shifted [Death's Presence](https://scryfall.com/card/rtr/121/deaths-presence) to give +1/+1 counters to [Dualcaster Mage](https://scryfall.com/card/cm2/94/dualcaster-mage), which is the only creature without protection from blue.
This ensures that every time a creature dies, it boosts the toughness of [Dualcaster Mage](https://scryfall.com/card/cm2/94/dualcaster-mage) more than the next creature entering will subtract from it.

## Credits
Special thanks to Alex Churchill for the basis of this work.

Additional thanks to reddit users /u/Rufus\_Reddit, /u/StellaAthena, /u/ais523, and everyone else on the reddit thread I posted in November 2018 for their assistance.

Thank you and I'm very sorry to every one of my friends who have had to listen to me talk about this for the last year.
