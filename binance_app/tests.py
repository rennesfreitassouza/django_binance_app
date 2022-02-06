from django.test import TestCase
from selenium import webdriver
from binance_app.src.database import convert_to_datetime, hash_data
from binance_app.models import TradingPair, TradingPairHash
from django.db.utils import IntegrityError


# Create your tests here.
class FunctionalTestCase(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_index_page_1(self):
        self.browser.get("http://127.0.0.1:8000/")
        self.assertIn('New HTTP GET request', self.browser.page_source)

    def test_index_page_3(self):
        self.browser.get("http://127.0.0.1:8000/")
        text = self.browser.find_element_by_id("id_for_test")
        text.click()
        self.assertIn(
            'http://127.0.0.1:8000/',
            self.browser.current_url)

    def tearDown(self):
        self.browser.quit()


class UnitTestCase(TestCase):

    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 't_b_app/home.html')

    def save_trading_pair(self):
        tp_row = TradingPair(trading_pair_symbol='test',
                             symbol_avg_price=0,
                             api_dt=convert_to_datetime(1644083042327),
                             error='')
        tp_row.save()
        return tp_row

    def test_trading_pair_model(self):
        tp = self.save_trading_pair()
        pulled_tp = TradingPair.objects.get(trading_pair_symbol=tp.trading_pair_symbol,
                                            symbol_avg_price=tp.symbol_avg_price,
                                            api_dt=tp.api_dt,
                                            error=tp.error)
        self.assertEqual(tp, pulled_tp)

    def save_trading_pair_hash(self):
        tp_row = self.save_trading_pair()
        tp_hash = TradingPairHash(
            trading_pair=tp_row, hash=hash_data(str(tp_row)))
        tp_hash.save()
        return tp_hash

    def test_trading_pair_hash(self):
        tp_hash0 = self.save_trading_pair_hash()
        tp_hash1 = self.save_trading_pair_hash()
        self.assertNotEqual(first=tp_hash0,
                            second=tp_hash1,
                            msg=f"tp_hash0.hash: {tp_hash0.hash}\
                                tp_hash1.hash: {tp_hash1.hash}")

    def test_trading_pair_hash_collision(self):
        def save_trading_pair_hash_collision():
            tp_row = self.save_trading_pair()
            tp_hash = TradingPairHash(
                trading_pair=tp_row,
                hash='MWRkNGMzYmQyMzdiNDMzN2NlYmVjYjgwOTM2YTdlZTg=')
            tp_hash.save()
        save_trading_pair_hash_collision()
        self.assertRaises(IntegrityError,
                          save_trading_pair_hash_collision)
