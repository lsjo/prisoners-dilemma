import random

class Player:
  def __init__(self, score, profile, choice, turns, copies):  
    self.score = score
    self.profile = profile
    self.choice = choice
    self.turns = turns
    self.copies = copies

profiles = ["always cooperate", "always defect", "tit for tat", "random", "user", "sussy  bot"]
choices = ["cooperate", "defect"]

def game(A, B, rounds):
  for turn in range(rounds):
    if A.profile == profiles[0]:
      A.choice = "cooperate"
    elif A.profile == profiles[1]:
      A.choice = "defect"
    elif A.profile == profiles[2]:
      if turn == 0:
        A.choice = "cooperate"
      else:
        A.choice = B.turns[turn-1]
    elif A.profile == profiles[3]:
      A.choice = random.choice(choices)
    elif A.profile == profiles[4]:
      A.choice = input("Player 1 choice: ")
    elif A.profile == profiles[5]:
      if turn == 0:
        A.choice = "defect"
      else:
        A.choice = B.turns[turn-1]

    if B.profile == profiles[0]:
      B.choice = "cooperate"
    elif B.profile == profiles[1]:
      B.choice = "defect"
    elif B.profile == profiles[2]:
      if turn == 0:
        B.choice = "cooperate"
      else:
        B.choice = A.turns[turn-1]
    elif B.profile == profiles[3]:
      B.choice = random.choice(choices)
    elif B.profile == profiles[4]:
      B.choice = input("Player 2 choice: ")
    elif B.profile == profiles[5]:
      if turn == 0:
        B.choice = "cooperate"
      else:
        B.choice = A.turns[turn-1]

    A.turns.append(A.choice)
    B.turns.append(B.choice)

    if A.choice == "cooperate":
      if B.choice == "cooperate":
        A.score = A.score + 3
        B.score = B.score + 3
        # print("Both players chose to cooperate.")
      elif B.choice == "defect":
        B.score = B.score + 5
        # print("Player 1 chose to cooperate while Player 2 chose to defect.")
    elif A.choice == "defect":
      if B.choice == "cooperate":
        A.score = A.score + 5
        # print("Player 1 chose to defect while Player 2 chose to cooperate")
      elif B.choice == "defect":
        A.score = A.score + 1
        B.score = B.score + 1
        # print("Both players chose to defect")
    # print("Player one score:", A.score)
    # print("Player two score:", B.score)     

# p1 - always cooperate
# p2 - always defect
# p3 - tit for tat
# p4 - random

def get_score(Player):
  return Player.score

def tournament(players, rounds_per_game, rounds_per_tournament):
  for i in range(len(players)):
    x = i + 1
    while x < len(players):
      game(players[i], players[x], rounds_per_game)
      x = x + 1
  players.sort(key=get_score, reverse=True)

def evolution(players, eliminated, replicated):
    for q in players:
        print(q.profile, q.score)
    for n in range(eliminated):
        players.pop()
    for c in range(replicated):
        new_profile = players[c].profile
        players.append(Player(0, new_profile, "" ,[], 1)) 
    for y in range(len(players)):
        players[y].score = 0

set_players = {"always cooperate": 10, "always defect": 3, "tit for tat": 3}
tournament_list = []

for n in set_players:
  player_profile = n
  for x in range(tournamenta[n]):
    tournament_list.append(Player(0, player_profile, "", [], 1))

for n in tournament_list:
  print(n.profile, n.score)

def environment(generations, replicated, eliminated, tournament_list, rounds_per_game, rounds_per_tournament):
    for n in range(generations):
        tournament(players, rounds_per_game, rounds_per_tournament)
        evolution(players, replicated, eliminated)
        print()
        for x in players:
            print(x.profile, x.score)
        string = "Generation " + str((n)+1) + " completed."
        print(string)
        print("------------------------")
        input()

environment(20, 2, 2, tournament_list, 10, 1)
