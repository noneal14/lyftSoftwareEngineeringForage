import unittest
from tires.carrigan_tires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_does_need_service_one(self):
        self.assertTrue(CarriganTires([0.1,0.1,0.1,0.9]).needs_service())
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        
    def test_does_not_need_service_one(self):
        self.assertFalse(CarriganTires([0.1,0.1,0.1,0.5]).needs_service())
        
if __name__ == '__main__':
    unittest.main()
        