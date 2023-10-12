import sys
import unittest
sys.path.append('../')
from datetime import date
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestBattery(unittest.TestCase):
    def test_nubbin(self):
        new_battery = NubbinBattery(date(2020, 1, 1),date(2012, 1, 1))
        self.assertTrue(new_battery.needs_service())
        new_battery = NubbinBattery(date(2020, 1, 1), date(2029, 1, 1))
        self.assertFalse(new_battery.needs_service())
    def test_spindler(self):
        new_battery = SpindlerBattery(date(2020, 1, 1), date(2017, 1, 1))
        self.assertTrue(new_battery.needs_service())
        new_battery = SpindlerBattery(date(2020, 1, 1), date(2019, 1, 1))
        self.assertFalse(new_battery.needs_service())

if __name__ == '__main__':
    unittest.main()