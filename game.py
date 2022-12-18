import random

print('''         welcome to Betting zone.
Pick a player who you think can win...PLAYER1/PLAYER2
If you pick right one you win $100 or you loose $100.
          $$$Try your luck$$$
          ''')
choose = input().upper()
toss1 = random.randint(1, 6)
toss2 = random.randint(1, 6)
p1 = 0
p2 = 0
print("Player 1 choose: ", toss1)
print("Player 2 choose: ", toss2)
even_odd = toss1 + toss2
if even_odd % 2 == 0:
    print("addition of player1 and player2 choice is even so:")
    print("player 1 win the toss")
    print("Player 1 choose to bat first")
    print("***********************")
    l = 1
    m = 2
    while l != m:
        l = random.randint(1, 6)
        m = random.randint(1, 6)
        print("player 1 choose: ", l)
        print("player 2 choose: ", m)
        if l == m:
            break
        p1 = p1 + l
        print("Player 1 live score", p1)
        print("***********************")
    print("Player 1 OUT!!!")
    print("player 1 total score is:", p1)
    o = 1
    p = 2
    print("***********************")
    print("now its time for player 2 batting")
    while o != p:
        o = random.randint(1, 6)
        p = random.randint(1, 6)
        print("player 1 choose: ", o)
        print("player 2 choose: ", p)
        if o == p:
            break
        p2 = p2 + p
        print("Player 2 live score", p2)
        if p2 > p1:
            print("Player 2 chased player 1")
            break
        print("***********************")
    print("player 2 total score is:", p2)
    if p1 > p2:
        print("player 1 won by", p1 - p2, "runs")
    elif p1 == p2:
        print("match tied")
    else:
        print("player 2 won by", p2 - p1, "runs")


else:
    print("addition of player1 and player2 choice is odd so:")
    print("player 2 win the toss")
    print("Player 2 is bat first")
    print("***********************")
    l = 1
    m = 2
    while l != m:
        l = random.randint(1, 6)
        m = random.randint(1, 6)
        print("player 1 choose: ", l)
        print("player 2 choose: ", m)
        if l == m:
            break
        p2 = p2 + m
        print("Player 2 live score", p2)
        print("***********************")
    print("Player 2 OUT!!!")
    print("player 2 total score is:", p2)
    o = 1
    p = 2
    print("***********************")
    print("now its time for player 1 batting")
    while o != p:
        o = random.randint(1, 6)
        p = random.randint(1, 6)
        print("player 1 choose: ", o)
        print("player 2 choose: ", p)
        if o == p:
            break
        p1 = p1 + o
        print("Player 1 score", p1)
        if p1 > p2:
            print("Player 1 chased player 2")
            break
        print("***********************")
    print("player 1 total score is:", p1)
    if p1 > p2:
        print("player 1 won by", p1 - p2, "runs")
    elif p1 == p2:
        print("match tied")
    else:
        print("player 2 won by", p2 - p1, "runs")
if choose == "PLAYER1":
    if p1 > p2:
        print("you win $100")
    else:
        print("you loose $100")
elif choose == "PLAYER2":
    if p2 > p1:
        print("you win $100")
    else:
        print("you loose $100")
else:
    print("invalid choice")
