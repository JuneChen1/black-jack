import random
import math

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
  # A A
  if pointList == [11, 11]:
    pointList[1] = 1

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

def winLose(winner, playerWin, bankerWin, chips):  
  if winner == "player":
    chips += wager     
    playerWin += 1
  elif winner == "banker":
    chips -= wager
    bankerWin += 1
  return playerWin, bankerWin, chips

playerWin = 0
bankerWin = 0
chips = input("請設定初始籌碼：")

while chips.isdigit() == False:
  print(("請輸入正整數"))
  chips = input("請設定初始籌碼：")
chips = int(chips)

while True:
  wager = input("請下注：")
  if wager.isdigit() == False:
    print("請輸入正整數")
    continue
  else:
    wager = int(wager)

  deckList = list(range(0, 52))
  random.shuffle(deckList)

  playerCard = []
  playerPoint = []
  bankerCard = []
  bankerPoint = []

  for i in range(2):
    deal(playerCard, playerPoint)
  # 測試用
  # playerCard = [0, 11]
  # playerPoint = [11, 10]
  
  deal(bankerCard, bankerPoint)
  printMessage()

  playerBJ = False
  bankerBJ = False
  if len(playerCard) == 2 and sum(playerPoint) == 21:
      print("Black Jack！")
      playerBJ = True
  
  print("請選擇步驟：加注輸入1/投降輸入2/跳過輸入3")
  ans = input()
  surrender = False

  if ans == "1":
    addWager = input("請加注：")

    while addWager.isdigit() == False:
      print("請輸入正整數")
      addWager = input("請加注：")
    wager += int(addWager)
    
    print("目前下注：", wager, sep="")
  elif ans == "2":
    print("已投降，收回一半籌碼")
    wager = math.ceil(wager/2)
    playerWin, bankerWin, chips = winLose("banker", playerWin, bankerWin, chips)
    surrender = True
  elif ans != "3":
    print("請重新輸入")
  print("*************************")

  while surrender == False:
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
        playerWin, bankerWin, chips = winLose("banker", playerWin, bankerWin, chips)
        break
    else:
      printMessage()

  if surrender == False and sum(playerPoint) < 22:
    #莊家小於17點時，持續加牌
    while sum(bankerPoint) < 17:
      print("----莊家加牌----")
      deal(bankerCard, bankerPoint)
      # 測試用
      # bankerCard = [0, 11]
      # bankerPoint = [11, 10]

      if sum(bankerPoint) > 21:
        if 11 in bankerPoint:
          bankerPoint[bankerPoint.index(11)] = 1
      
      printMessage()
      
    if len(bankerCard) == 2 and sum(bankerPoint) == 21:
      bankerBJ = True

    if bankerBJ == True and playerBJ == False:
      print("莊家Black Jack，莊家勝利")
      playerWin, bankerWin, chips = winLose("banker", playerWin, bankerWin, chips)
    elif bankerBJ == False and playerBJ == True:
      print("玩家Black Jack，玩家勝利")
      wager = math.floor(wager*1.5)
      playerWin, bankerWin, chips = winLose("player", playerWin, bankerWin, chips)
    elif bankerBJ == True and playerBJ == True:
      print("雙方Black Jack，平局")

    elif sum(bankerPoint) > 21:
      print("莊家爆牌，玩家獲勝")
      playerWin, bankerWin, chips = winLose("player", playerWin, bankerWin, chips)
    elif sum(playerPoint) > sum(bankerPoint):
      print("玩家點數大於莊家，玩家勝利")
      playerWin, bankerWin, chips = winLose("player", playerWin, bankerWin, chips)
    elif sum(playerPoint) < sum(bankerPoint):
      print("莊家點數大於玩家，莊家勝利")
      playerWin, bankerWin, chips = winLose("banker", playerWin, bankerWin, chips)
    elif sum(playerPoint) == sum(bankerPoint):
      print("雙方點數相同，平局")
    
  print("玩家勝利{}次，莊家勝利{}次".format(playerWin, bankerWin))
  print("持有籌碼：", chips, sep="")
  
  end = input("再來一場(Y/N)?")
  if end == "n" or end == "N":
    break
  while end != "y" and end != "Y":
    end = input("再來一場(Y/N)?")
  
  print("*************************")