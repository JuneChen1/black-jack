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
  print("*************************")

playerWin = 0
bankerWin = 0

while True:
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

  while True:
    if len(playerCard) == 2 and sum(playerPoint) == 21:
      print("Black Jack！")

    ans = input("玩家要加牌嗎(Y/N)？")
    if ans == "N" or ans == "n":
      break

    if ans != "Y" and ans != "y":
      continue

    deal(playerCard, playerPoint)
    if sum(playerPoint) > 21:
      if 11 in playerPoint:
        playerPoint[playerPoint.index(11)] = 1
        printMessage()
      else:
        printMessage()
        print("玩家爆牌，莊家獲勝")
        bankerWin += 1
        break
    else:
      printMessage()

  if sum(playerPoint) < 22:
    #莊家小於17點時，持續加牌
    while sum(bankerPoint) < 17:
      print("----莊家加牌----")
      deal(bankerCard, bankerPoint)

      if sum(bankerPoint) > 21:
        if 11 in bankerPoint:
          bankerPoint[bankerPoint.index(11)] = 1
      
      printMessage()

    if sum(bankerPoint) > 21:
      print("莊家爆牌，玩家獲勝")
      playerWin += 1   
    elif sum(playerPoint) > sum(bankerPoint):
      print("玩家勝利")
      playerWin += 1  
    elif sum(playerPoint) < sum(bankerPoint):
      print("莊家勝利")
      bankerWin += 1
    elif sum(playerPoint) == sum(bankerPoint):
      print("平局")
  
  print("玩家勝利{}次，莊家勝利{}次".format(playerWin, bankerWin))

  end = input("再來一場(Y/N)?")
  if end == "n" or end == "N":
    break
  print()