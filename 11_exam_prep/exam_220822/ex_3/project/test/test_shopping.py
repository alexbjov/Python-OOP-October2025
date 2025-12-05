from unittest import TestCase, main

from project.shopping_cart import ShoppingCart


class TestShoppingCar(TestCase):
    def setUp(self):
        self.cart = ShoppingCart("Bstore", 10_000.0)
    
    def test_init(self):
        self.assertEqual("Bstore", self.cart.shop_name)
        self.assertEqual(10_000.0, self.cart.budget)
        self.assertEqual({}, self.cart.products)
    
    def test_shop_name_starting_with_small_letter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.shop_name = "myshop"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))
        self.assertEqual("Bstore", self.cart.shop_name)
    
    def test_shop_name_not_is_alfa_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.shop_name = "My1sh#op"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))
        self.assertEqual("Bstore", self.cart.shop_name)
    
    def test_add_to_cart_price_equal_to_100_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.add_to_cart("A", 100)
        self.assertEqual("Product A cost too much!", str(ex.exception))
        self.assertEqual({}, self.cart.products)
    
    def test_add_to_cart_price_more_than_100_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.cart.add_to_cart("A", 101)
        self.assertEqual("Product A cost too much!", str(ex.exception))
        self.assertEqual({}, self.cart.products)
    
    def test_add_to_cart_valid_price_success(self):
        self.assertEqual({}, self.cart.products)
        result = self.cart.add_to_cart("A", 50)
        self.assertEqual("A product was successfully added to the cart!", result)
        self.assertEqual({"A": 50}, self.cart.products)
    
    def test_remove_from_cart_existing_product(self):
        self.cart.products = {"A": 20, "B": 30}
        result = self.cart.remove_from_cart("A")
        self.assertEqual("Product A was successfully removed from the cart!", result)
        self.assertEqual({"B": 30}, self.cart.products)
    
    def test_remove_from_cart_non_existing_product(self):
        self.cart.products = {"A": 20, "B": 30}
        with self.assertRaises(ValueError) as ex:
            self.cart.remove_from_cart("C")
        self.assertEqual("No product with name C in the cart!", str(ex.exception))
        self.assertEqual({"A": 20, "B": 30}, self.cart.products)
    
    def test_add_two_carts(self):
        self.cart.products = {"A": 20, "B": 30}
        
        cart_2 = ShoppingCart("Smallshop", 20_000.0)
        cart_2.products = {"C": 40, "D": 50}
        
        new_cart = self.cart + cart_2
        self.assertIsInstance(new_cart, ShoppingCart)
        self.assertIsNotNone(new_cart)
        self.assertEqual("BstoreSmallshop", new_cart.shop_name)
        self.assertEqual(30_000.0, new_cart.budget)
        self.assertEqual({"A": 20, "B": 30, "C": 40, "D": 50}, new_cart.products)
    
    def test_buy_product_success(self):
        self.cart.products = {"A": 20, "B": 30}
        result = self.cart.buy_products()
        self.assertEqual("Products were successfully bought! Total cost: 50.00lv.", result)
        self.assertEqual({"A": 20, "B": 30}, self.cart.products)
    
    def test_buy_product_raises(self):
        self.cart.products = {"A": 20, "B": 30}
        self.cart.budget = 40
        with self.assertRaises(ValueError) as ex:
            self.cart.buy_products()
        
        self.assertEqual("Not enough money to buy the products! Over budget with 10.00lv!", str(ex.exception))
        self.assertEqual({"A": 20, "B": 30}, self.cart.products)


if __name__ == '__main__':
    main()
