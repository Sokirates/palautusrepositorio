import unittest
from statistics_service import StatisticsService


class TestStats(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService()

    def test_search(self):
        self.stats("Mikko Rantanen")
        self.assertAlmostEqual(self.stats.search, "Mikko")


