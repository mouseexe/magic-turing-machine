# magic-turing-machine
This project would not have been possible if not for the work done by Alex Churchill on https://www.toothycat.net/~hologram/Turing/About.html

I've expanded on his work and simplified the machine, and I believe this iteration is the best one that currently exists. I will try to keep this updated as new cards are printed and new possibilites emerge.

That being said, let's get to the reason you're here:

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

# How do we build this out of Magic cards?
Same way you eat an elephant: One bite at a time.

Before we jump in though, I want to address a problem that keeps this from being an entirely perfect Turing machine. The goal of any Turing machine to operate independently of human choice. We can eliminate most choice by not having may triggers, but we do have two player choices required. Chancellor of the Spires has a may trigger, which we will define here to always accept. Necroskitter also has a may trigger, which we will treat the same way. In short, treat these may triggers as regular triggers and the machine will function entirely.

## Engine Setup

As a general disclaimer, this entire machine should be buildable in an [Elder Dragon Highlander](https://mtg.gamepedia.com/Commander_(format)) deck, which means only one of each non-basic land. Any time you see a card that's a copy of another existing card, that's actually a Clever Impersonator copying the original.

To achieve this, we have a Soul Foundry with a Clever Impersonator imprinted. This will allow us to make as many token copies of the Impersonator as we need.

Many cards have had their text altered, which I've displayed in the images below. This was accomplished with Artificial Evolution, which we've imprinted onto an Isochron Scepter to cast as many times as we need. We also have a Brainstorm on another Isochron Scepter so that we can draw and manipulate the top of our deck as needed.

On the right, we have a Sol Ring and Chromatic Lantern, along with a Paradox Engine. This, along with any spell on an Isochron Scepter, generates us infinite mana and infinite castings. We can now loop Artificial Evolution and Brainstorm indefinitely.

The final piece of initial setup is Unnatural Selection. In this Turing machine, we represent our colors with creature types, so it's important to ensure that our machine pieces don't get caught in the tape, so to speak. We use Wizard as a machine designation, so anything with that creature type won't get killed as our machine runs.
![Engine Setup](https://github.com/mouseexe/magic-turing-machine/blob/master/Engine%20Setup.png)

## Creature Type Mapping

This is where it starts to get complicated. We have three colors: (A), (B), and (C). These are represented with the creature types Ape, Bat, and Cat. We also need to distinguish between the left and right sides of the tape, so we'll say that everything on the left is also a Leech, and everything on the right is also a Rat. To make a token that is both an Ape and a Leech, or an Ape and a Rat, we need a creature type that can represent both of these types at once. Here are the types we use, and what they represent. Ignore the Transition column for now, that will be important later.

| Left | Color | Right | Transition |
| :---: | :---: | :---: | :---: |
| Ally | Ape | Archer | Azra |
| Blinkmoth | Bat | Bringer | Beeble |
| Camel | Cat | Carrier | Citizen |

With these types defined, we can start setting up rules. For example, an Ally will always be an Ape, and an Ally will always be a Leech. An Archer will also always be an Ape, but will instead be a Rat, rather than a Leech. So every Ally token is a Token Creature - Ally Ape Leech, and so on. We use Dralnu's Crusade to define these type maps. The first Dralnu's Crusade is its own card, but the rest are just Clever Impersonators.

![Creature Type Mapping 1](https://github.com/mouseexe/magic-turing-machine/blob/master/Creature%20Type%20Mapping%201.png)
![Creature Type Mapping 2](https://github.com/mouseexe/magic-turing-machine/blob/master/Creature%20Type%20Mapping%202.png)

## Tape Creation and Management

Before we can start running our machine, we need to create an input tape. We manage the tape with Aether Flash, Virulent Plague, Valor in Akros, and a set of hacked Noxious Ghouls. Since the tokens we create are going to be 2/2s by default, and each will be pumped with two different Dralnu's Crusades, we're looking at a 4/4 token every time we make a new one. A Virulet Plague brings this down to a 2/2. Aether Flash deals 2 damage to every new creature, just enough to kill it. Valor in Akros triggers at the same time, and we stack the triggers so our new token gets +1/+1 before immediately dying. Then, we trigger one of the two sets of Noxious Ghouls. A Leech will give another -2/-2 to every non-Leech, while leaving Leeches the same. This nets every Leech +1 toughness, and every Rat -1 toughness (since Rats also benefit from Valor in Akros). This way, we ensure that every time a new token is made, a different token dies.

We also have a Noxious Ghoul for Trilobites and Sphinxes. This is because we will frequently have Trilobite tokens and a Sphinx creature entering the battlefield, so we want to give -1/-1 to all other creatures to cancel out the +1/+1 from Valor in Akros.

![Tape Management](https://github.com/mouseexe/magic-turing-machine/blob/master/Tape%20Management.png)

You'll notice that two Noxious Ghouls are highlighted in a red box. This is because we want to wait to create these Ghouls until our initial tape is created. With only one of each Ghoul, creating a new token nets that side +1 toughness, and +0 to the opposite side. This allows us to populate both sides of the tape without actually moving anything. Once our tape is created entirely, we can add the second two Ghouls to make it move as normal.

To create the initial tape, we use Drana's Chosen to add our choice of color on whichever side we want. Since they're all Wizards, you can tap another Chosen for Cohort (they've been hacked to read Wizard instead of Ally). To untap, simply repeat the Isochron Scepter loop from earlier.

![Tape Creation](https://github.com/mouseexe/magic-turing-machine/blob/master/Tape%20Creation.png)

## Head Logic

Now that we have our tape set up, we need to create our head! We use Xathrid Necromancers (many of which are, you guessed it, Clever Impersonators) to check for tokens dying. Whenever a token dies, our head reads it to determine the next symbol to write. Don't worry about the Necromancers to the right of the table just yet, those are for changing states down the road. You'll also notice a Cloak of Invisibility. Each Necromancer in the table in enchanted with a Cloak, but again, we'll discuss why in a bit.

The table depicted here is the same as the one I listed above in the initial description.

![Head Logic](https://github.com/mouseexe/magic-turing-machine/blob/master/Head%20Logic.png)

## Transitioning States

You'll notice that some of our head logic creates tokens that immediately die and create a different token. Azras always die and create Allies, Beebles always die and create Blinkmoths, and Citizens always die and create Carriers. That's because Azra, Beeble, and Citizen tokens only exist to prompt a state change. The page I linked above had an ingenius way of triggering a state change, which uses a mechanic called Phasing. Remember the Cloak of Invisibility I told you to not worry about earlier? Now we worry about it. Our Alpha and Beta states are all both enchanted with Cloaks of Invisibility (most of which were Clever Impersonators), and half of them have been phased out with our own Time and Tide before we started off the machine. We use Time and Tide again to swap the phased in and out Necromancers, but this time we don't want to cast it ourselves. Whenever a Trilobite enters the battlefield, our hacked Dragon Tempest will trigger. The new Trilobite will have to choose a target to deal damage to, and thanks to a pair of Ivory Masks (one for us, one donated to our opponent [It was brought to my attention that Ivory Mask cannot be donated using Bazaar Trader, so my next version replaces this with a True Believer]) and hacked Crystalline Slivers, the only legal target is Chancellor of the Spires, as everything else on the field has Shroud. Azras, Beebles, and Citizens are all Trilobites thanks to a hacked Dralnu's Crusade. Since our Trilobites are black and we have a Corrosive Mentor giving Wither, the damage triggered off Dragon Tempest is in the form of -1/-1 counters. Our Venom Sliver helps out as well, giving Trilobites Deathtouch so they can kill Chancellor with only one damage. When in the Chancellor dies, since it has -1/-1 counters on it, it will return to the battlefield under our opponent's control, due to the Necroskitter we donated with Bazaar Trader. To get this Chancellor back under our control again, we just have to ensure that we cast a Gather Specimens earlier in the turn, so all creatures come under our control. When the Chancellor returns to us, it targets the only instant in a graveyard, a Time and Tide belonging to our opponent. 

There's one piece missing. If we go a large number of moves without a transition, we'll have a lot of -1/-1s coming at our Sphinx, since it is neither a Leech nor a Rat. In order to prevent this, we need to establish early a pair of Door of Destinies (naming Sphinx) and an Inexorable Tide. When we set up our original tape, we have to cast a spell to untap Drana's Chosen. Every time we do, we proliferate the Doors of Destinies so our Sphinx has +2/+2 for every token on the tape. This will prevent it from dying to the Noxious Ghouls that move the tape. 

(Disclaimer: I made a mistake in labelling a Crystalline Sliver as giving Wizards Shroud, when it really should be two separate Slivers giving Rats and Leeches Shroud. I'll try to update the image in the near future.)

![Transitioning State](https://github.com/mouseexe/magic-turing-machine/blob/master/Transition%20Change.png)

## Opponent Control

How do we get our opponent to have a Time and Tide in their graveyard? Doesn't that require a very specific and rare card to be in our opponent's deck already? Fortunately, we can get around this. By using a Mindslaver to control our opponents turn, a Shared Fate to allow them to cast cards from our deck, and careful topdeck manipulation with our Isochroned Brainstorm, we can cast a Cunning Wish acting as our opponent. From there, we just gift our friend across the table a copy of their very own Time and Tide, which we promptly place into their graveyard. We can from here use our Relic of Progenitus to clean up all the pesky graveyards so that only Time and Tide remains for our Chancellor to target. Grand Abolisher, in the meantime, is just hanging out with us, stopping our opponent from messing with our beautiful Turing machine while it operates.

![Opponent Control](https://github.com/mouseexe/magic-turing-machine/blob/master/Opponent%20Control.png)

# Is this possible to actually do in game?
Yeah. Or well, I hope so. I made an EDH deck [here](http://tappedout.net/mtg-decks/spirit-of-turing/?cb=1541628479) that I believe can actually pull this off in real game of Magic. One day I hope to demonstrate that two strings are equal to each other with a Turing machine made of Magic cards, but I doubt any of my friends will let me get that far in a game!

# Wrapping up
Thank you for reading! I've spent a lot of time trying to improve Churchill's design, and I'm pretty happy with where this has ended up. If I missed something, made a mistake, or even if something just isn't entirely clear from my explanation, please shoot me an email at kevin.s.schwenk@gmail.com and I'll get it fixed.
