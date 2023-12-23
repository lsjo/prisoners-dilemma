import random

class Player:
  def __init__(self, score, profile, choice, turns, copies):  
    self.score = score
    self.profile = profile
    self.choice = choice
    self.turns = turns
    self.copies = copies

p1a = Player(0, "always cooperate","" ,[], 1)
p1b = Player(0, "always cooperate","" ,[], 1)
p1c = Player(0, "always cooperate","" ,[], 1)
p2a = Player(0, "always defect","" ,[], 1)
p2b = Player(0, "always defect","" ,[], 1)
p3a = Player(0, "tit for tat","" ,[], 1)
p3b = Player(0, "tit for tat","" ,[], 1)
p4a = Player(0, "random","" ,[], 1)
p4b = Player(0, "random","" ,[], 1)
p5a = Player(0, "sussy bot", "", [], 1)
p5b = Player(0, "sussy bot", "", [], 1)
p6a = Player(0, "user", "", [], 1)
p6b = Player(0, "user", "", [], 1)

players_list = [p1a, p1b, p2a, p2b, p3a, p3b, p4a, p4b, p5a, p5b]
game_list = [p1a, p1b, p1c, p2a, p3a]

pro = ["always cooperate", "always defect", "tit for tat", "random", "user", "sussy  bot"]
choices = ["cooperate", "defect"]

def game(A, B, rounds):
  for turn in range(rounds):
    if A.profile == pro[0]:
      A.choice = "cooperate"
    elif A.profile == pro[1]:
      A.choice = "defect"
    elif A.profile == pro[2]:
      if turn == 0:
        A.choice = "cooperate"
      else:
        A.choice = B.turns[turn-1]
    elif A.profile == pro[3]:
      A.choice = random.choice(choices)
    elif A.profile == pro[4]:
      A.choice = input("Player 1 choice: ")
    elif A.profile == pro[5]:
      if turn == 0:
        A.choice = "defect"
      else:
        A.choice = B.turns[turn-1]

    if B.profile == pro[0]:
      B.choice = "cooperate"
    elif B.profile == pro[1]:
      B.choice = "defect"
    elif B.profile == pro[2]:
      if turn == 0:
        B.choice = "cooperate"
      else:
        B.choice = A.turns[turn-1]
    elif B.profile == pro[3]:
      B.choice = random.choice(choices)
    elif B.profile == pro[4]:
      B.choice = input("Player 2 choice: ")
    elif B.profile == pro[5]:
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
        B.score = B.score + 4
        # print("Player 1 chose to cooperate while Player 2 chose to defect.")
    elif A.choice == "defect":
      if B.choice == "cooperate":
        A.score = A.score + 4
        # print("Player 1 chose to defect while Player 2 chose to cooperate")
      elif B.choice == "defect":
        A.score = A.score + 1
        B.score = B.score + 1
        # print("Both players chose to defect")
    # print("Player one score:", A.score)
    # print("Player two score:", B.score)     

  #print()
  #print("---------------------")
  #print( A.profile, "total score:", A.score)
  #print(B.profile, "total score:", B.score)
  if A.score > B.score:
    # print("Player One Wins!")
    lol = "lol"
  elif B.score > A.score:
    # print("Player Two Wins!")
    lol = "lol"    
  else:
    lol = "lol"
    # print("Draw.")
  # print("---------------------")

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
    

tournament_1 = [p1a, p1b, p1c, p2a, p3a]

for n in tournament_1:
  print(n.profile, n.score)
print()
print()

def environment(generations, replicated, eliminated, players, rounds_per_game, rounds_per_tournament):
    for n in range(generations):
        tournament(players, rounds_per_game, rounds_per_tournament)
        evolution(players, replicated, eliminated)
        print()
        for x in tournament_1:
            print(x.profile, x.score)
        string = "Generation " + str((n)+1) + " completed."
        print(string)
        print("------------------------")
        input()


environment(7, 1, 1, tournament_1, 10, 1)
