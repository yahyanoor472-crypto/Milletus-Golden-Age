__version__ = "0.1"

health_uses = 10
levels = [1]

# Level System

class Levels:
    def __init__(self):
        self.level = 1

    def choose_level(self):
        try:
            player_choose_level = int(input("Choose a Level: "))
        except ValueError:
            print("Choose a correct level sonsong tv!")
            return

        if player_choose_level in levels:
            self.level = player_choose_level
        else:
            print("That level dosen't exist!!!")

    def level_1(self, beavers:list, player):
        global health_uses

        for beaver in beavers:
            while True:
                enter = input("Enter d (Increase health) or a (Attack Beaver) \nenter: ")

                if enter.strip().lower() == "d":
                    if health_uses > 0:
                        player.hp += 2
                        health_uses -= 1

                        if player.hp > player.max_hp:
                            player.hp = player.max_hp
                    else:
                        print("You do not have more health increase uses left muhehehe...")
                        continue

                elif enter.strip().lower() == "a":
                    beaver.hp -= player.dammage

                    if beaver.hp < 0:
                        beaver.hp = 0

                else:
                    print("Invalid input how dare ja!")
                    continue

                if beaver.hp <= 0:
                    bars = round((beaver.hp / beaver.max_hp) * 10)
                    beaver.beaver_health_bar = "=" * bars

                    bars = round((player.hp / player.max_hp) * 10)
                    player.player_health_bar = "=" * bars

                    print(f"Player Health : {player.player_health_bar}")
                    print(f"Beaver Health : {beaver.beaver_health_bar}")

                    print("You have successfully killed the beaver congrats")
                    break

                print("Beaver's turn")

                if beaver.steps < 6:
                    beaver.steps += 1
                    print("Beaver came 1 step closer!")

                if beaver.steps == 6:
                    player.hp -= beaver.dammage
                    beaver.steps += 1
                    print("Beaver Attacked you!")

                if player.hp < 0:
                    player.hp = 0

                bars = round((player.hp / player.max_hp) * 10)
                player.player_health_bar = "=" * bars

                bars = round((beaver.hp / beaver.max_hp) * 10)
                beaver.beaver_health_bar = "=" * bars

                print(f"Player Health : {player.player_health_bar}")
                print(f"Beaver Health : {beaver.beaver_health_bar}")

                if player.hp <= 0:
                    print("You died!")
                    break

# Beaver System

class Beaver:
    def __init__(self, hp, dammage, steps):
        self.max_hp = hp
        self.bar_value = 10
        self.beaver_health_bar = "=" * self.bar_value
        self.hp = hp
        self.dammage = dammage
        self.steps = steps

b1 = Beaver(75, 10, 0)

# Player System

class Player:
    def __init__(self, hp, dammage):
        self.max_hp = hp
        self.bar_value = 10
        self.player_health_bar = "=" * self.bar_value
        self.hp = hp
        self.dammage = dammage

player = Player(50, 5)

set_level = Levels()

set_level.choose_level()

set_level.level_1([b1], player)