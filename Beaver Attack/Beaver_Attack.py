class Beaver:
    def __init__(self , hp , dammage , steps):
        self.hp = hp
        self.dammage = dammage
        self.steps = steps
b1 = Beaver(10 , 3 , 0)
class Player:
    def __init__(self , hp , dammage):
        self.hp = hp
        self.dammage = dammage
player = Player(50 , 5) 
while True: 
    enter = input("Enter d or a \nenter: ")
    if enter == "D" or enter == "d":
        player.hp += 2
    elif enter == "A" or enter == "a":
        b1.hp -= player.dammage
        if b1.hp <= 0:
            print("You have successfully killed the beaver congrats")
            break
    else:
        print("Invalid input how dare ja!")
    print("Beaver's turn")
    er = input("enter: ")
    if b1.steps < 6:
        b1.steps += 1
    if b1.steps == 6:
        player.hp -= b1.dammage
    if player.hp <= 0:
        print("You died!")