import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Hearts", 2)
        self.card2 = Card("Spades", 1)
        self.card3 = Card("Spades", 4)
        self.card_list = [self.card1, self.card2, self.card3]
        self.card_game_1 = CardGame()

    def test_check_for_ace(self):        
        self.assertEqual(True, self.card_game_1.check_for_ace(self.card2) )

    def test_highest_card(self):
        self.assertEqual(self.card3, self.card_game_1.highest_card(self.card1, self.card3))
    
    def test_cards_total(self):
        self.assertEqual("You have a total of 7", self.card_game_1.cards_total(self.card_list))