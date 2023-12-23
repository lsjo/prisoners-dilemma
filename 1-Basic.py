"""
This goes by player one's choice being the first - if they choose to cooperate,
it goes to the first set of nested lists and then if player two chooses to cooperate
it goes to the first scenario in each nested lists.
"""

p1_score = 0
p2_score = 0
p1_choice = ""
p2_choice = ""

rounds = str(input("How many rounds do you want to play? "))
rounds = int(rounds)

for n in range(rounds):
  print()
  p1_choice = input("Player one choice: ")
  p2_choice = input("Player two choice: ")

  # Outcomes thingy
  if p1_choice == "cooperate":
    if p2_choice == "cooperate":
      p1_score = p1_score + 3
      p2_score = p2_score + 3
    elif p2_choice == "defect":
      p2_score = p2_score + 5
  elif p1_choice == "defect":
    if p2_choice == "cooperate":
      p1_score = p1_score + 5
    elif p2_choice == "defect":
      p1_score = p1_score + 1
      p2_score = p2_score + 1
  print("Player one score:", p1_score)
  print("Player two score:", p2_score)
  print()

# Results
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
