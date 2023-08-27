import unittest
from battery.spindler_battery import SpindlerBattery
from datetime import date

class SpindlerBatteryTests(unittest.TestCase):
    def test_does_need_service_one(self):
        start = date.fromisoformat("2023-08-26")
        fromDate = date.fromisoformat("1956-08-26")
        nubb = SpindlerBattery(start, fromDate)
        self.assertTrue(nubb.needs_service())

    def test_does_need_service_two(self):
        start = date.fromisoformat("2023-08-26")
        fromDate = date.fromisoformat("2020-08-25")
        nubb = SpindlerBattery(start, fromDate)
        self.assertTrue(nubb.needs_service())
        
    def test_does_not_need_service_one(self):
        start = date.fromisoformat("2023-08-26")
        fromDate = date.fromisoformat("2022-08-26")
        nubb = SpindlerBattery(start, fromDate)
        self.assertFalse(nubb.needs_service())
        
if __name__ == '__main__':
    unittest.main()
