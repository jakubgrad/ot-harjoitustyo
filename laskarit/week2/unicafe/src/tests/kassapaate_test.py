import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_amount_of_money_in_the_created_cash_terminal_and_the_number_of_lunches_sold_are_correct(self):

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def if_the(self):

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_if_the_payment_is_sufficient_the_amount_of_money_in_the_cash_register_increases_by_the_price_of_the_lunch_and_the_amount_of_change_is_correct_for_cheap_lunch(self):
        change = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(change, 60)

    def test_if_the_payment_is_sufficient_the_amount_of_money_in_the_cash_register_increases_by_the_price_of_the_lunch_and_the_amount_of_change_is_correct_for_expensive_lunch(self):
        change = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(change, 100)

    def test_if_the_payment_is_sufficient_the_number_of_lunches_sold_increases_cheap_lunch(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_if_the_payment_is_sufficient_the_number_of_lunches_sold_increases_expensive_lunch(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_for_cash_if_the_payment_is_not_sufficient_the_amount_of_money_in_the_cash_register_will_not_change_all_money_will_be_returned_as_change_and_the_number_of_lunches_sold_will_not_change_for_cheap_lunch(self):
        change = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(change, 100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_for_cash_if_the_payment_is_not_sufficient_the_amount_of_money_in_the_cash_register_will_not_change_all_money_will_be_returned_as_change_and_the_number_of_lunches_sold_will_not_change_for_expensive_lunch(self):
        change = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(change, 100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_if_there_is_enough_money_on_the_card_the_amount_is_debited_from_the_card_and_True_is_returned_for_cheap_lunch(self):
        value = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        
        self.assertEqual(value,True)

    def test_if_there_is_enough_money_on_the_card_the_amount_is_debited_from_the_card_and_True_is_returned_for_expensive_lunch(self):
        value = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        
        self.assertEqual(value,True)

    def test_if_there_is_enough_money_on_the_card_the_number_of_lunches_sold_increases(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassapaate.edulliset, 1)
       
    def test_if_there_is_not_enough_money_on_the_card_the_amount_of_money_on_the_card_does_not_change_the_number_of_lunches_sold_remains_unchanged_and_False_is_returned_for_cheap_lunch(self):
        maksukortti = Maksukortti(50)
        value = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        
        self.assertEqual(maksukortti.saldo, 50)
        self.assertEqual(value, False)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_if_there_is_not_enough_money_on_the_card_the_amount_of_money_on_the_card_does_not_change_the_number_of_lunches_sold_remains_unchanged_and_False_is_returned_for_expensive_lunch(self):
        maksukortti = Maksukortti(50)
        value = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        
        self.assertEqual(maksukortti.saldo, 50)
        self.assertEqual(value, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_the_amount_of_money_in_the_cash_register_does_not_change_when_buying_with_a_card(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_when_loading_money_to_the_card_the_card_balance_changes_and_the_amount_of_money_in_the_cash_register_increases_by_the_loaded_amount(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_money_in_the_register_in_euros_is_okay(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_cannot_load_a_card_with_a_negative_sum(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 1000)
