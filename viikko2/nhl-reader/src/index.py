import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)



class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json() 
        players = [Player(player_dict) for player_dict in response]
        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()

        nationality_players = []
        for player in players:
            if player.nationality == nationality:
                nationality_players.append(player)
        nationality_players = sorted(nationality_players, key=lambda x: x.goals + x.assists, reverse=True)
        return nationality_players

if __name__ == "__main__":
    main()