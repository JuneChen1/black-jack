import random

def cardPoint(x):
  if x%13 == 0: #A
    return 11
  elif x%13 > 9: #JQK
    return 10
  else:
    return x%13+1 #2~10

def deal(cardList, pointList):
  temp = deckList.pop()
  cardList.append(temp)
  pointList.append(cardPoint(temp))

def printCard(c):
  for i in c:
    if i//13 == 0:
      print(chr(9824), end="") #黑桃
    elif i//13 == 1:
      print(chr(9829), end="") #紅心
    elif i//13 == 2:
      print(chr(9830), end="") #方塊
    elif i//13 == 3:
      print(chr(9827), end="") #梅花
    
    if i%13 == 0:
      print("A", end=" ")
    elif i %13 == 10:
      print("J", end=" ")
    elif i %13 == 11:
      print("Q", end=" ")
    elif i %13 == 12:
      print("K", end=" ")
    else:
      print(str(i%13+1), end=" ")
  print()

def printMessage():
  print("玩家的牌：", end="")
  printCard(playerCard)
  print("玩家的牌面點數：", sum(playerPoint), sep="")
  print("莊家的牌：", end="")
  printCard(bankerCard)
  print("莊家的牌面點數：", sum(bankerPoint), sep="")
  
deckList = list(range(0, 52))
random.shuffle(deckList)

playerCard = []
playerPoint = []
bankerCard = []
bankerPoint = []

for i in range(2):
  deal(playerCard, playerPoint)

deal(bankerCard, bankerPoint)
printMessage()