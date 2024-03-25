import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_card_balance_at_beginning_correc(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
        
    def test_loading_money_increases_the_balance_correctly(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_balance_will_decrease_correctly_if_there_is_enough_money(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_balance_will_not_change_if_there_is_not_enough_money(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_method_returns_True_if_the_money_was_enough(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_method_returns_False_if_the_money_was_not_enough(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)

    def test_saldo_euroina_works(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)
