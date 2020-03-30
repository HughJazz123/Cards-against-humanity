import random


black_cards = open("black_cards.txt").read().split("\n")

white_cards = open("white_cards.txt").read().split("\n")


def space():
    print("\n"*40)
space()
print("White cards:",len(white_cards))
print("Black cards:",len(black_cards))
p=int(input("Number of players (4-7): "))

p_=['p1','p2','p3','p4','p5','p6','p7']
 
score_keeper=[]
players=[]
namelist=[]

space()
for i in range(p):
    players.append(p_[i])
    score_keeper.append(p_[i])

    score_keeper[i]=0

    print("Enter name (Player",i+1,"):")
    name=input()
    
    namelist.append(name)
    print()

    players[i]=[]
    a=i
    for c in range(10):
        card=random.choice(white_cards)
        players[a].append(card)
        white_cards.remove(card)
a=0#card czar
s=""
space()



while s!="q":
    g=0#to take turns between players
    
    white_cards_players=[]#i have no idea what this is
    players_white_cards=[]#i have no idea what this is either
    non_card_czars=[]#tf is the difference
    
    black_card=random.choice(black_cards)
    black_cards.remove(black_card)
    while g<p:
        if a!=g:
            print(namelist[g],"'s turn:")
            non_card_czars.append(namelist[g])
            input()
            print("Black card:",black_card)
            print()
            for i in range(10):
                print(str(i+1)+". "+players[g][i])

            choice=int(input())
            choice=choice-1
            players_white_cards.append(players[g][choice])
            white_cards_players.append(players[g][choice])
            players[g].pop(choice)
        g+=1
        space()
    
    print("Black card:",black_card)
    print("Card Czar:",namelist[a])
    input()
    white_cards_in_order=[]
    c1=1
    for i in range(p-1):
        c=random.randint(0,len(players_white_cards)-1)
        print("Card "+str(c1)+": "+str(players_white_cards[c]))
        
        white_cards_in_order.append(players_white_cards[c])
        players_white_cards.pop(c)
        c1+=1

    card_czar_choice=int(input("Card (Enter the number of your choice): "))
    winner_card = white_cards_in_order[card_czar_choice-1]
    winner=white_cards_players.index(winner_card)
    
    print(non_card_czars[winner],"wins!")

    w=namelist.index(non_card_czars[winner])
    score_keeper[w]+=1
    
    s=input("Press Enter to continue (or 'q' to exit)\n")
    space()
    b=0
    for i in range(p):
        if b!=g and b<p:
            r=random.choice(white_cards)
            players[i].append(r)
            white_cards.remove(r)
    a+=1
    if a==p:
        a=0
for i in range(p):
    print(str(namelist[i])+": "+str(score_keeper[i])+" point(s)")
