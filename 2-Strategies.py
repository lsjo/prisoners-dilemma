import random

p1_turns = []
p2_turns = []
p1_score = 0
p2_score = 0

pro = ["always cooperate", "always defect", "tit for tat", "random", "user"]
choices = ["cooperate", "defect"]
rounds = int(input("How many rounds would you like to play? "))
p1_profile = input("Player one profile: ")
p2_profile = input("Player two profile: ")

for turn in range(rounds):
  print()
  if p1_profile == pro[0]:
    p1_choice = "cooperate"
  elif p1_profile == pro[1]:
    p1_choice = "defect"
  elif p1_profile == pro[2]:
    if turn == 0:
      p1_choice = "cooperate"
    else:
      p1_choice = p2_turns[turn-1]
  elif p1_profile == pro[3]:
    p1_choice = random.choice(choices)
  elif p1_profile == pro[4]:
    p1_choice = input("Player 1 choice: ")

  if p2_profile == pro[0]:
    p2_choice = "cooperate"
  elif p2_profile == pro[1]:
    p2_choice = "defect"
  elif p2_profile == pro[2]:
    if turn == 0:
      p2_choice = "cooperate"
    else:
      p2_choice = p1_turns[turn-1]
  elif p2_profile == pro[3]:
    p2_choice = random.choice(choices)
  elif p2_profile == pro[4]:
    p2_choice = input("Player 2 choice: ")

  p1_turns.append(p1_choice)
  p2_turns.append(p2_choice)

  if p1_choice == "cooperate":
    if p2_choice == "cooperate":
      p1_score = p1_score + 3
      p2_score = p2_score + 3
      print("Both players chose to cooperate.")
    elif p2_choice == "defect":
      p2_score = p2_score + 5
      print("Player 1 chose to cooperate while Player 2 chose to defect.")
  elif p1_choice == "defect":
    if p2_choice == "cooperate":
      p1_score = p1_score + 5
      print("Player 1 chose to defect while Player 2 chose to cooperate")
    elif p2_choice == "defect":
      p1_score = p1_score + 1
      p2_score = p2_score + 1
      print("Both players chose to defect")
  print("Player one score:", p1_score)
  print("Player two score:", p2_score)     

  print()
  print("---------------------")
  print("Player one total score:", p1_score)
  print("Player two total score:", p2_score)
  if p1_score > p2_score:
    print("Player One Wins!")
  elif p2_score > p1_score:
    print("Player Two Wins!")
  else:
    print("Draw.")
  print("---------------------")

