class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

    def show_player(self):
        print(self.name, "- Score:", self.score)


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_scores(self):
        print("Natijalar:")
        for p in self.players:
            p.show_player()

    def highest_score(self):
        max_score = 0
        best_player = None

        for p in self.players:
            if p.score > max_score:
                max_score = p.score
                best_player = p

        if best_player:
            print("Eng yuqori ball:", best_player.name,
                  "-", best_player.score)


def main():
    p1 = Player("Ali")
    p2 = Player("Vali")

    game = Game()

    game.add_player(p1)
    game.add_player(p2)

    p1.add_score(50)
    p2.add_score(70)

    game.show_scores()

    game.highest_score()


main()
