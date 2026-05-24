import random

# Variables
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
        add_rizz_to_left()

    elif face == "left":
        add_rizz_to_right()

    else:
        print("Put Valid Answer -_-")
        break

    print(f"Right Face Rizz: {Right_Face_Rizz}")
    print(f"Left Face Rizz: {Left_Face_Rizz}")
    
    if Right_Face_Rizz == Left_Face_Rizz:
        print("You Defeated the Game!!!")
        break