from helpers import Deck, Hand, Chips


def main():
    
    playing = True

    while True:
        # Print an opening statement
        print('\nWelcome to BlackJack! Get as close to 21 as you can without going over!\n\nDealer hits until she reaches 17. Aces count as 1 or 11.\n')
        
        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()
        
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
                
        # Set up the Player's chips
        player_chips = Chips()  # remember the default value is 100    
        
        # Prompt the Player for their bet
        take_bet(player_chips)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        while playing:  # recall this variable from our hit_or_stand function
            
            # Prompt for Player to Hit or Stand
            # hit_or_stand(deck,player_hand) 
            while True:
                x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
            
                if x[0].lower() == 'h':
                    hit(deck, player_hand)

                elif x[0].lower() == 's':
                    print("Player stands. Dealer is playing.")
                    playing = False

                else:
                    print("Sorry, please try again.")
                    continue
                break
            
            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)
            
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break        

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
        if player_hand.value <= 21:
            
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
        
            # Show all cards
            show_all(player_hand, dealer_hand)
            
            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push()
    
        # Inform Player of their chips total 
        print("\nPlayer's winnings stand at", player_chips.total)
        
        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
        
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break  


def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("BUST Player")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player WINS")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Player WINS! Dealer BUSTS")
    chips.win_bet()
    

def dealer_wins(player, dealer, chips):
    print("Dealer WINS!")
    chips.lose_bet()
    

def push():
    print("Dealer and Player tie! PUSH")


if __name__ == '__main__':
    main()
