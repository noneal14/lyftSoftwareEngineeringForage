import unittest
from engine.sternman_engine import SternmanEngine

class SternmanEngineTests(unittest.TestCase):
    def test_does_need_service_one(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())
        
    def test_does_not_need_service_one(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())
    
if __name__ == '__main__':
    unittest.main()
