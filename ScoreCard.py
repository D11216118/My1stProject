#分數計算功能設計
class ScoreCard:
    def __init__(self):
        self.scores = {}

    def add_score(self, player_name, score):
        if player_name in self.scores:
            self.scores[player_name] += score
        else:
            self.scores[player_name] = score

    def get_score(self, player_name):
        return self.scores.get(player_name, 0)

    def get_all_scores(self):
        return self.scores
if __name__ == "__main__":
    score_card = ScoreCard()
    score_card.add_score("Alice", 10)
    score_card.add_score("Bob", 15)
    score_card.add_score("Alice", 5)
    
    print("Alice的分數:", score_card.get_score("Alice"))
    print("Bob的分數:", score_card.get_score("Bob"))
    print("所有分數:", score_card.get_all_scores())
# Example usage
# score_card = ScoreCard()
# score_card.add_score("Alice", 10)
# score_card.add_score("Bob", 15)
# score_card.add_score("Alice", 5)
# print("Alice's score:", score_card.get_score("Alice"))
# print("Bob's score:", score_card.get_score("Bob"))
# print("All scores:", score_card.get_all_scores())

    