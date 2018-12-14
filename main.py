#rps
import random
p1w = 0
p2w = 0
tie = 0
playagain = True
def plamt():
  pn = input("Number of Players?")
  if pn.isdigit():
    if int(pn)>2 or int(pn)<1:
      print("1-2, please.")
      return plamt()
    else:
      return int(pn)
  else:
    print("Try a number this time.")
    return plamt()
playeramount = plamt()
def convert(ipt):
  if ipt == 1:
    return "Rock"
  elif ipt == 2:
    return "Paper"
  else:
    return "Scissors"
print("""Rock
Paper
Scissors""")
def shell(pmt):
  global p1w
  global p2w
  global tie
  global playagain
  p1 = minishell("player1",pmt)
  if pmt == 2:
    p2 = minishell("player2",pmt)
  else:
    p2 = random.randint(1,3)
  if p1 == 1:
    if p2 == 2:
      win = False
    elif p2 == 3:
      win = True
    else:
      win = ""
  elif p1 == 2:
    if p2 == 2:
      win = ""
    elif p2 == 3:
      win = False
    else:
      win = True
  else:
    if p2 == 2:
      win = True
    elif p2 == 3:
      win = ""
    else:
      win = False
  p1 = convert(p1)
  p2 = convert(p2)
  print("Player 1 uses " + p1)
  print("Player 2 uses " + p2)
  if win == True:
    print("Player 1 Wins!")
    p1w += 1
  elif win == False:
    print("Player 2 Wins!")
    p2w += 1
  else:
    print("Tie!")
    tie += 1
  n = input("Play again? Y/N")
  n = n.lower()
  if n == "n":
    playagain = False
def minishell(player,pmt):
  print("1.rock\n2.paper\n3.scissors")
  p = input(player + ":")
  if p == "1" or p == "2" or p == "3":
    if pmt == 2:
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    return int(p)
  else:
    print("1,2 or 3 please.")
    return minishell(player,pmt)
while playagain:
  shell(playeramount)
  print("Player 1 has won "+ str(p1w)+ " time(s).")
  print("Player 2 has won "+ str(p2w)+ " time(s).")
  print("You have tied "+ str(tie)+ " time(s).")
print("Thanks for playing!")
