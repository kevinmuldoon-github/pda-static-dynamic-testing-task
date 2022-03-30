import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        # set up some cards for testing

        self.card_1 = Card ('Hearts' , 7)
        self.card_2 = Card ('Clubs' , 2)
        self.card_3 = Card ('Spades' , 10)
        self.card_4 = Card ('Hearts' , 8)
        self.card_5 = Card ('Diamonds' , 5)
        self.card_6 = Card ('Spades' , 1) # Ace
        self.game = CardGame()
        self.cards = [self.card_1,self.card_2,self.card_3,self.card_4,self.card_5,self.card_6]

    def test_cards_have_suits (self):
        self.assertEqual("Hearts", self.card_1.suit)
        self.assertEqual("Spades", self.card_3.suit)
        self.assertEqual("Diamonds", self.card_5.suit)

    def test_cards_have_values(self):
        self.assertEqual(7, self.card_1.value)
        self.assertEqual(2, self.card_2.value)
        self.assertEqual(8, self.card_4.value)

    def test_check_for_ace(self):
        is_it_an_ace_1 = self.game.check_for_ace(self.card_1)
        self.assertEqual(False, is_it_an_ace_1)
        is_it_an_ace_2 = self.game.check_for_ace(self.card_2)
        self.assertEqual(False, is_it_an_ace_2)
        is_it_an_ace_3 = self.game.check_for_ace(self.card_6)
        self.assertEqual(True, is_it_an_ace_3)
    
    def test_highest_card(self):
        which_card_1 = self.game.highest_card(self.card_1, self.card_3)
        self.assertEqual(self.card_3, which_card_1)
        which_card_2 = self.game.highest_card(self.card_2, self.card_4)
        self.assertEqual(self.card_4, which_card_2)
        which_card_3 = self.game.highest_card(self.card_5, self.card_6) # Let's say Ace is low for this test!
        self.assertEqual(self.card_5, which_card_3)

    def test_cards_total(self):
        total = self.game.cards_total(self.cards)
        self.assertEqual("You have a total of 33", total)




