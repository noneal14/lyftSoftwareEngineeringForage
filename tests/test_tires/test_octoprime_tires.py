import unittest
from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_does_need_service_one(self):
        self.assertTrue(OctoprimeTires([1.0, 1.0, 1.0, 0.1]).needs_service())
        
    def test_does_not_need_service_one(self):
        self.assertFalse(OctoprimeTires([0.1,0,1,0.1,0.4]).needs_service())
        
if __name__ == '__main__':
    unittest.main()
        