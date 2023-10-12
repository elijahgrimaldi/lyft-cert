import sys
import unittest
sys.path.append('../')
from tires.carrigan_tire import CarriganTire
from tires.octoprime_tire import OctoPrime


class TestTires(unittest.TestCase):
    def test_carrigan(self):
        new_tires = CarriganTire([0.1,0.5,0.3,0.6])
        self.assertFalse(new_tires.needs_service())
        new_tires = CarriganTire([0.1,0.9,1.2,0.3])
        self.assertTrue(new_tires.needs_service())
    def test_octoprime(self):
        new_tires = OctoPrime([0.1,0.2,0.3,0.6])
        self.assertFalse(new_tires.needs_service())
        new_tires = OctoPrime([0.8,0.9,1.2,0.6])
        self.assertTrue(new_tires.needs_service())
if __name__ == '__main__':
    unittest.main()

