from blackjack_helper import *
from test_helper import *
import unittest

class TestBlackjackHelper(unittest.TestCase):
  """
  Class for testing blackjack helper functions.
  """

  def test_print_card_name_example(self):
    """
    Example of a test to compare printed statements with expected

    This does not count as one of your tests
    """
    self.assertEqual(get_print(print_card_name, 2), "Drew a 2\n")
    

  def test_mock_randint_example(self):
    """
    Example of a test to compare output for a function that calls randint

    This does not count as one of your tests
    """
    self.assertEqual(mock_random([3], draw_card), 3)
    self.assertEqual(mock_random([3, 5], draw_starting_hand, "DEALER"), 8)

  


  # MAKE SURE ALL YOUR FUNCTION NAMES BEGIN WITH test_
  # WRITE YOUR TESTS BELOW.



  def test_print_card_name(self):
    self.assertEqual(get_print(print_card_name, 8), "Drew an 8\n")
    self.assertEqual(get_print(print_card_name, 15), "BAD CARD\n")
    self.assertEqual(get_print(print_card_name, 11), "Drew a Jack\n")
    self.assertEqual(get_print(print_card_name, 1), "Drew an Ace\n")
    self.assertEqual(get_print(print_card_name, 0), "BAD CARD\n")


  
  def test_draw_card(self):
    self.assertEqual(mock_random([11], draw_card), 10)
    self.assertEqual(mock_random([12], draw_card), 10)
    self.assertEqual(mock_random([13], draw_card), 10)
    self.assertEqual(mock_random([1], draw_card), 11)
    self.assertEqual(mock_random([6], draw_card), 6)
    self.assertEqual(mock_random([2], draw_card), 2)



  def test_print_header(self):
    self.assertEqual(get_print(print_header, "DEALER"), "-----------\nDEALER\n-----------\n")
    self.assertEqual(get_print(print_header, "USER"), "-----------\nUSER\n-----------\n")
    self.assertEqual(get_print(print_header, "NIMI"), "-----------\nNIMI\n-----------\n")
    self.assertEqual(get_print(print_header, "Player"), "-----------\nPlayer\n-----------\n")


  def test_draw_starting_hand(self):
     self.assertEqual(mock_random([1, 11], draw_starting_hand, "USER"), 21)
     self.assertEqual(mock_random([9, 6], draw_starting_hand, "DEALER"), 15)
     self.assertEqual(mock_random([12, 13], draw_starting_hand, "USER"), 20)
     self.assertEqual(mock_random([9, 0], draw_starting_hand, "DEALER"), 9)


  def test_print_end_turn_status(self):
    self.assertEqual(get_print(print_end_turn_status,21),"Final hand: 21.\nBLACKJACK!\n")
    self.assertEqual(get_print(print_end_turn_status,28),"Final hand: 28.\nBUST.\n")
    self.assertEqual(get_print(print_end_turn_status,17),"Final hand: 17.\n")
    self.assertEqual(get_print(print_end_turn_status,7),"Final hand: 7.\n")


  def test_print_end_game_status(self):
    output_1 = "-----------\nGAME RESULT\n-----------\nYou win!\n"
    output_2 = "-----------\nGAME RESULT\n-----------\nDealer wins!\n"
    output_3 = "-----------\nGAME RESULT\n-----------\nPush.\n"

    self.assertEqual(get_print(print_end_game_status, 17, 21),output_2)
    self.assertEqual(get_print(print_end_game_status, 21, 17),output_1)
    self.assertEqual(get_print(print_end_game_status, 18, 28),output_1)
    self.assertEqual(get_print(print_end_game_status, 28, 18),output_2)
    self.assertEqual(get_print(print_end_game_status, 28, 26),output_2)
    self.assertEqual(get_print(print_end_game_status, 18, 16),output_1)
    self.assertEqual(get_print(print_end_game_status, 16, 18),output_2)
    self.assertEqual(get_print(print_end_game_status, 18, 18),output_3)
    self.assertEqual(get_print(print_end_game_status, 21, 21),output_3)



  


    

    
     
     






  




if __name__ == '__main__':
    unittest.main()
