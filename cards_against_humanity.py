import random

black_cards = open("black_cards.txt").read().split("\n")
white_cards = open("white_cards.txt").read().split("\n")

def space():
    print("\n"*40)
space()
print("White cards:",len(white_cards))
print("Black cards:",len(black_cards))
p=int(input("Number of players (4+): "))

while p<4:
    print("minimum 4 players only.\n")
    p=int(input("Number of players (4+): "))
print()
score_keeper=[]
players=[]
player_n_cards=[]
player_cards=[]
for i in range(p):
    name=input("Player "+str(i+1)+": ")
    players.append(name)
    score_keeper.append(0)
    for i in range(10):
        random_card=random.choice(white_cards)
        player_n_cards.append(random_card)
        white_cards.remove(random_card)
    player_cards.append(player_n_cards)
    player_n_cards=[]

card_czar_number=0
while True:
    selected_cards=[]
    non_card_czars=players[:]
    non_card_czars.pop(card_czar_number)
    
    black_card=random.choice(black_cards)
    black_cards.remove(black_card)
    for i in range(p):
        if i!=card_czar_number:
            space()
            input((players[i])+"'s turn (Press enter to continue)\n")
            print("Black card: "+black_card+"\n")
            
            for x in range(10):
                print("Card "+str(x+1)+": "+player_cards[i][x])
            #selection process
            selection=int(input("\nSelect the number of the card you wish to pick: "))
            selection-=1
            selected_cards.append(player_cards[i][selection])
            player_cards[i].pop(selection)

            #adding another card
            adding_white_card=random.choice(white_cards)
            player_cards[i].append(adding_white_card)
            white_cards.remove(adding_white_card)
    space()
    input("Card Czar: "+players[card_czar_number]+"\n")
    shuffled_cards=selected_cards[:]
    random.shuffle(shuffled_cards)
    print("Black card: "+black_card+"\n")
    for i in range(len(shuffled_cards)):
        print("Card "+str(i+1)+": "+shuffled_cards[i])
    ##card czar selecting
    card_czar_selection=int(input("\nYour selection:\nCard: "))
    card_czar_selection-=1
    
    #card czar selected
    winner_card_number=selected_cards.index(shuffled_cards[card_czar_selection])
    winner_of_round=non_card_czars[winner_card_number]
    
    score_keeper[players.index(winner_of_round)]+=1

    if card_czar_number!=(len(players)-1):
        card_czar_number+=1
    else:
        card_czar_number=0
    print(winner_of_round+" wins!\n")
    quit_game=input("Enter 'q' to if you wish to quit, or else, press Enter: ")
    
    if quit_game=="q":
        space()
        print("Final scores:")
        for i in range(p):
            print(players[i]+": "+str(score_keeper[i])+" points")
        break
