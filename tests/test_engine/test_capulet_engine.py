import unittest
from engine.capulet_engine import CapuletEngine

class CapuletEngineTests(unittest.TestCase):
    def test_does_need_service_one(self):
        mileage_now = 40000
        mileage_then = 500
        engine = CapuletEngine(mileage_now, mileage_then)
        self.assertTrue(engine.needs_service())
        
    def test_does_not_need_service_one(self):
        mileage_now = 40000
        mileage_then = 10000
        engine = CapuletEngine(mileage_now, mileage_then)
        self.assertFalse(engine.needs_service())

    def test_does_not_need_service_two(self):
        mileage_now = 30000
        mileage_then = 30000
        engine = CapuletEngine(mileage_now, mileage_then)
        self.assertFalse(engine.needs_service())
        
if __name__ == '__main__':
    unittest.main()
        