
def enter():
    enter = input("Press \"Enter\" to continue")
def intro():
    intro = "Hey! There you are playing \"Rizz Simulator\""
    print(intro)
    enter()
    fun_m = "Here you will have so much fun!"
    print(fun_m)
    enter()
intro()
name = input("Please enter your name: ")
player = name
import random
print(f"Hello! {player}")
enter()


# Functions of Menu
def menu():
    pass
def back():
    while True:
        back = input("Type back to go back to the menu: ")
        if back == "back" or back == "Back":
            menu()
            break
def rules():
    rules = '''1. You are given two options: (right/left)
2. When you choose one the other's rizz decreases
3. Each choice increases 15 rizz and decreases the other by 3 - 5
4. You're goal is to match both faces rizz
5. Rizz can never go below 0 (negatives)
6. Invalid answers will break the game!
7. Menu is highly sensitive even a small mistake of spelling in menu , would break the game'''
    print(rules)
    back()
def play():
    # Variables
    global Right_Face_Rizz , Left_Face_Rizz
    Right_Face_Rizz = 0
    Left_Face_Rizz = 0

    # Functions
    def add_rizz_to_right():
        global Right_Face_Rizz, Left_Face_Rizz

        Right_Face_Rizz += 15

        if Left_Face_Rizz > 0:
            Left_Face_Rizz -= random.randint(3, 5)


    def add_rizz_to_left():
        global Right_Face_Rizz, Left_Face_Rizz

        Left_Face_Rizz += 15

        if Right_Face_Rizz > 0:
            Right_Face_Rizz -= random.randint(3, 5)


    # Logic
    while True:

        face = input("Which Face do You Want to Rizz (right or left): ")

        if face == "right":
            add_rizz_to_right()

        elif face == "left":
            add_rizz_to_left()

        else:
            print("Put Valid Answer -_-")
            break

        print(f"Right Face Rizz: {Right_Face_Rizz}")
        print(f"Left Face Rizz: {Left_Face_Rizz}")
    
        if Right_Face_Rizz == Left_Face_Rizz:
            print("You Defeated the Game!!!")
            break
def credits():
    credit = '''\"Yahya\": Discovered the Milletus
Coded Introduction and Menu
Made the logic (not in code)
\"Hammad\": Made the foundation for the Milletus
Coded Logic
A \"Pure Milletus\"'''
    print(credit)
    back()
def menu():
    global menu1
    menu1 = input('''Play
Rules
Credits
Quit
Enter: ''').strip("").strip(" ")
    while True:
        if menu1.isalpha():
            if menu1.capitalize() == "Play":
                play()
            elif menu1.capitalize() == "Rules":
                rules()
            elif menu1.capitalize() == "Credits":
                credits()
            elif menu1.capitalize() == "Quit":
                break
        else:
            break
menu()

