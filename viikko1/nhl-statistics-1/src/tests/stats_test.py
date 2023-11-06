import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStats(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search(self):
        player = self.stats.search("Semenko")
        self.assertAlmostEqual(str(player), "Semenko EDM 4 + 12 = 16")

    def test_search_tuntematon(self):
        player = self.stats.search("Koira")
        self.assertAlmostEqual(player, None)
    
    def test_team(self):
        team_players = self.stats.team("EDM")
        list_players = []
        for player in team_players:
            list_players.append(str(player))
        self.assertAlmostEqual(list_players, ['Semenko EDM 4 + 12 = 16', 'Kurri EDM 37 + 53 = 90', 'Gretzky EDM 35 + 89 = 124'])
    
    def test_top(self):
        top_players = self.stats.top(0)
        self.assertAlmostEqual(str(top_players[0]), 'Gretzky EDM 35 + 89 = 124')
