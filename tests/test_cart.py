import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        # Thêm 20 đĩa đầu tiên (Kỳ vọng: True)
        for i in range(20):
            dvd = DigitalVideoDisc(f"Title {i}", "Category", "Director", 120, 10.5)
            self.assertTrue(cart.add_dvd(dvd))
        
        # Thêm đĩa thứ 21 (Kỳ vọng: Trả về False vì giỏ đã đầy)
        dvd_21 = DigitalVideoDisc("21st DVD", "Category", "Director", 120, 10.5)
        self.assertFalse(cart.add_dvd(dvd_21))