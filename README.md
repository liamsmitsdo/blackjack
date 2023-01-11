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

- Card - 
Initialises with a suit and a rank property, that will store that cards specific suit and rank. This was created to simplify the deck creation and so that each card could be it's own object.

- Deck - 
Initialises with an empty list to hold all the cards and then creates all 52 cards in order. The deck has two methods to help with gameplay. The shuffle method utilises 'shuffle' from the random module, and simulates the actual shuffling of the deck. The deal method will return the first item in the list, simulating the top card being picked.

- Hand - 
Each player will have a 'hand' which is an object that can keep track of cards the players' receive, as well as the value of their hand. The 'add_card' method takes in a card object and appends it to the hand objects list. It also calculates the value of that card (using the constant variable discussed above) and updates the total value. There is a method to hand the 'ace' interaction. It will give the ace a value of 11 by default, and check whether the hands total value exceeds 21, at which point it will change the value of the ace to 1.

- Chips - 
This object is created to keep track of the players total chips and handle all the interactions associated with that. The default chips are set to 100 and there are methods to update the total value, whether the player wins or loses a bet.

---
#### main.py:

This file has the main game loop and logic to perform the running of the game and is the file you should run in order to play the game.

