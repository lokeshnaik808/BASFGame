# BASFGame

The main.py file contains the code for the game. All the functions/classes and pieces of code are documented with docstrings or comments to explains the logic they contain.

The game's setting is that, that there are 3 entities in game, namely, Hero (which Player Controls), Orc and a Dragon. Hero is on one side and the Orc and Dragon (monsters) are on one side. Orc and Dragon attack the Hero and Hero fights these two monsters.

The entities have Health points and Damage Points (amount of health damage it does to its enemy in a single attack) of:
1. Hero: 40 Health Points and 2 Damage Points
2. Orc: 7 Health Points and 1 Damage Points
3. Dragon: 20 Health Points and 3 Damage Points

Every 1500ms, the orc attacks the hero for 1 Damage.
Every 2000ms, the dragon attacks the hero for 3 damage.
(irrespective of whether Player gives any input or not)

Each time the player types "attack orc" or "attack dragon" in console, the hero attacks the corresponding monster for 2 damage. Player can give these instructions in console at any point of time in game (the game does not pause to take user's input)

If the orc's or dragon's health points are reduced to zero, it is dead and can neither attack nor be attacked.

If both monsters die, the player wins the game.
If the hero's health points are reduced to zero, the player loses the game.


After every action by any entity, i.e. if Any Monster attacks Hero or Hero attacks any Monster, the corresponding consequence is printed out on console displayed what action has occured (e.g. 'Orc has attacked Player') and 'attacked entity's Health after attack is 123'.

At the end of the game, stats such as Health Points of the winning side are displayed.

**A Sample log of an earlier played game is present in repository for reference**

## Technical Aspects

The code is entirely written in python and mostly uses python's inbuilt libraries. It only uses one external library i.e 'schedule'.

To Run the game, follow the steps below:
1. Clone the Library Locally
2. Create a VENV for this repo in your local environment
3. run `pip install -r requirements.txt` within the scope of VEVN
4. Simply execute the `main.py` file and Enjoy the game!
