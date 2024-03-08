from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_blackjack(self, input_mock, randint_mock):
        '''
        The user receives a blackjack and the dealer receives cards with a hand less
        than 21
        '''
        output = run_test([12, 5, 6], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)



    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_greater_value(self, input_mock, randint_mock):
        '''
        The user and dealer both receive cards with a hand less than 21 but the user has
        a higher hand value.
        '''
        output = run_test([12, 5, 5], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)




    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_dealer_bust(self, input_mock, randint_mock):
        '''
        The user receives cards with a hand value less than 21 and the dealer
        receives a hand value greater than 21
        So the user wins beacuse the dealer busts
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [13, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew a 10\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_user_wins_blackjack_dealer_bust(self, input_mock, randint_mock):
        '''
        The user receives cards with a hand equal to 21 and the dealer
        receives cards greater than 21
        The user wins beacuse the dealer busts and the user gets a blackjack
        '''
        output = run_test([12, 5, 6], ['y', 'n'], [13, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a King\n" \
                   "Drew a 5\n" \
                   "Dealer has 15.\n" \
                   "Drew a 10\n" \
                   "Final hand: 25.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)





    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_blackjack(self, input_mock, randint_mock):
        '''
        The dealer receives card with a hand equal to 21 and the user receives
        cards with a hand less than 21.
        The dealer wins because he gets a blackjack
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [6, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 5\n" \
                   "Dealer has 11.\n" \
                   "Drew a 10\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)



    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_greater_value(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.
        '''
        output = run_test([3, 5, 7], ['y', 'n'], [4, 5, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 7\n" \
                   "You have 15. Hit (y/n)? n\n" \
                   "Final hand: 15.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 4\n" \
                   "Drew a 5\n" \
                   "Dealer has 9.\n" \
                   "Drew a 9\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)



    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_blackjack_user_busts(self, input_mock, randint_mock):
        '''
        The dealer receives cards that end up with a hand equal to 21 and the user receives 
        cards that end up with a hand greater than 21. 
        The dealer wins because he gets a blackjack and the user busts
        '''
        output = run_test([9, 5, 10], ['y', 'n'], [6, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 5\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 5\n" \
                   "Dealer has 11.\n" \
                   "Drew a 10\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)



    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_both_bust(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand greater than 21.
        The dealer wins because the user busts
        '''
        output = run_test([9, 5, 10], ['y', 'n'], [7, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 5\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 7\n" \
                   "Drew a 5\n" \
                   "Dealer has 12.\n" \
                   "Drew a 10\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_dealer_wins_user_busts(self, input_mock, randint_mock):
        '''
        The user receives cards with a hand greater than 21 and the dealer
        receives card with a hand value less than 21.
        The dealer wins because the user busts

        '''
        output = run_test([9, 5, 10], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 5\n" \
                   "You have 14. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)




    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push_both_blackjack(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand equal to 21.
        Nobody wins
        '''
        output = run_test([12, 5, 6], ['y', 'n'], [6, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a Queen\n" \
                   "Drew a 5\n" \
                   "You have 15. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 5\n" \
                   "Dealer has 11.\n" \
                   "Drew a 10\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)




    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_push_same_value(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21 but equal.
        Nobody wins
        '''
        output = run_test([6, 5, 6], ['y', 'n'], [2, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 6\n" \
                   "Drew a 5\n" \
                   "You have 11. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 5\n" \
                   "Dealer has 7.\n" \
                   "Drew a 10\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)





    


    


    


    

    

    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
