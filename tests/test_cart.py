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
    def test_discount_calculation(self):
        cart = Cart()
        # Thêm đĩa vào giỏ để tổng tiền đúng bằng 100$
        dvd1 = DigitalVideoDisc("DVD 1", "Category", "Director", 120, 50.0)
        dvd2 = DigitalVideoDisc("DVD 2", "Category", "Director", 120, 50.0)
        cart.add_dvd(dvd1)
        cart.add_dvd(dvd2)

        # Kiểm tra 1: Tổng 100$ giảm 20% phải còn 80$
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)

        # Kiểm tra 2: Phần trăm > 100 phải ném ra lỗi ValueError
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)