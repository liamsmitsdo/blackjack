# Command Line Blackjack
#### Video Demo:  <url here>
---
### **Description:**

A command line interface version of the popular casino game 'Blackjack'. The game plays similarly to the real life alternative from the comfort of your own PC. To start simply run the *'main.py'* file and read the prompts.

### **- Gameplay:**
Once the game starts the player is told the rules of the game and is asked what bet they are willing to make. The player starts with $100 dollars in chips and any bets placed will be taken from this pool, conversely, any winnings will be added to this pool. Once tahe player places a bet, the dealer deals out the cards, two face up to the player and one face up with one face down to the dealer. The player is the prompted as to whether they would like to *hit* or *stand*, by entering 'h' or 's' respectively. If the player *hits* they receive another card face up, if they *stand*, the dealer reveals and hits until 17. At that point the game is decided and the better hand wins. Lastly, the player has the option to keep playing with their current pool of bets, by entering 'y' or 'n'.

### **- File breakdown:**
---
#### helpers.py: 

This file has all the relevant classes needed for the game to function. They were seperated for ease of use and to declutter the main file. 

There are 3 global constants used in helpers: 
|Constant|Description|
|---|---|
|Suit|Tuple with the four suits that come in a standard deck.|
|Rank|Tuple with the names of all the cards that form part of each suit|
|Value|Dictionary where the keys are the same card names from rank, and the values to each name represent that cards numeric value. This is used when calculating the value of the hands.|

There are 4 Classes that are in helpers, their description is as follows:

- Card