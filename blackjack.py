# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from blackjack_helper import *

# Write all of your part 3 code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.

# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
# Use randint to generate random cards. 
user_starting_hand = draw_starting_hand("your")

while user_starting_hand < 21:
    user_choice = input("You have " + str(user_starting_hand) +". Hit (y/n)? ")
    if user_choice == "y":
        user_starting_hand = user_starting_hand + draw_card()
    elif user_choice == "n":
        break
    else:
        print("Sorry I didn't get that.")
print_end_turn_status(user_starting_hand)
#If user inputs yes
#elif user_choice == "y":
    
dealer_starting_hand = draw_starting_hand("DEALER")
while dealer_starting_hand < 17:
    print("Dealer has "+ str(dealer_starting_hand))
    dealer_starting_hand = dealer_starting_hand + draw_card()
print_end_turn_status(dealer_starting_hand)

print_end_game_status(user_starting_hand, dealer_starting_hand)
  
  
  




