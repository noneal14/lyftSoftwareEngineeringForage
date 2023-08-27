import unittest
from engine.willoughby_engine import WilloughbyEngine

class WilloughbyEngineTests(unittest.TestCase):
    def test_does_need_service_one(self):
        mileage_now = 70000
        mileage_then = 500
        engine = WilloughbyEngine(mileage_now, mileage_then)
        self.assertTrue(engine.needs_service())
        
    def test_does_not_need_service_one(self):
        mileage_now = 70000
        mileage_then = 10000
        engine = WilloughbyEngine(mileage_now, mileage_then)
        self.assertFalse(engine.needs_service())

    def test_does_not_need_service_two(self):
        mileage_now = 30000
        mileage_then = 30000
        engine = WilloughbyEngine(mileage_now, mileage_then)
        self.assertFalse(engine.needs_service())
        
if __name__ == '__main__':
    unittest.main()
