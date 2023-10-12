import sys
import unittest
sys.path.append('../')
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
class TestEngine(unittest.TestCase):
    def test_capulet(self):
        new_engine = CapuletEngine(100000, 10000)
        self.assertTrue(new_engine.needs_service())
        new_engine = CapuletEngine(20000,10000)
        self.assertFalse(new_engine.needs_service())
    def test_sternman(self):
        new_engine = SternmanEngine(True)
        self.assertTrue(new_engine.needs_service())
        new_engine = SternmanEngine(False)
        self.assertFalse(new_engine.needs_service())
    def test_willoughby_engine(self):
        new_engine = WilloughbyEngine(100000, 10000)
        self.assertTrue(new_engine.needs_service())
        new_engine = WilloughbyEngine(20000,10000)
        self.assertFalse(new_engine.needs_service())
if __name__ == '__main__':
    unittest.main()
