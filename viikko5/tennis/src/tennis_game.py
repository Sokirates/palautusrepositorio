class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.points = {"0": "Love", 1: "Fifteen", "2": "Thirty", "3": "Forty"}

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.m_score1 == self.m_score2:
            score = self.tie()

        elif self.m_score1 > 3 or self.m_score2 > 3:
            difference_point = self.m_score1 - self.m_score2
            score = self.advantage(difference_point) + "" + self.better_points_player()

        else:
            score = self.other()
            return score
        
    def advantage_or_winning(self, difference_point):
        if -2< difference_point < 2:
            return "Advantage"
        else:
            return "win for"
    
    def better_points_player(self):
        if self.m_score1 < self.m_score2:
            return self.m_score2
        else:
            self.m_score1

    def other(self):
        return self.points[str(self.m_score1)] + "-" + self.points[str(self.m_score2)]
    
    def tie(self):
        if self.m_score1 > 3:
            return "Deuce"
        else:
            return self.points[str(self.m_score1)] + "-All"


