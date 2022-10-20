#Input answers
answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]
answer_left = ["Left", "L", "Left door"]
answer_right = ["Right", "R", "Right door"]
answer_front = ["Front", "F", "Front door"]

#Begining of the game, setting the scene for the player
print("""
WELCOME! LET THE ADVENTURE BEGIN. Lettuce set the scene...

You wake up in a room with no memory of who you are or how you got here. You stand up, get your shit together and look around.
Suddenly there is an urgent knock at the door. You open the door and there is a small penguin with a lil crown, and he hands you a note.

The notes says: "Your friends miss you, please come home."

Will you join me on this journey to go home? (Yes / No)
""")

#Begin door choosing
ans1 = input(">>")

if ans1 in answer_yes:
    print("\nYou look back up and the penguin has mysteriously disappeared. You close the door and go back inside. \n")
    print("\nYou take another look around the room. There are 3 different doors. One to your left, one to your right, and one in front of you. Which door do you choose?")
    ans2 = input(">>")

#Begin door to the left of the player
    if ans2 in answer_left:
        print("\nThe left door eh?")

#Begin door directly in front of the player
    if ans2 in answer_front:
        print("\nThe front door eh?")

#Begin door to the right of the player
    if ans2 in answer_right:
        print("\n The right door eh?")

#Begin elif args
    elif ans2 in answer_no:
        print("\nFine, I didn't want to play with you anyway.")

    else:
        print("\nI assume you know how to read if you've gotten this far, please type A REASONABLE ANSWER AND DONT MAKE ME HAVE TO DO MORE ERROR HANDLING. READ THE ROOM, READ THE MENU.")

elif ans1 in answer_no:
    print("\nTBD\n")

    ans3 = input(">>")

    if ans3 in answer_yes:
        print("\nTBD")

    elif ans3 in answer_no:
        print("\nTBD")

    else:
        print("\nI assume you know how to read if you've gotten this far, please type A REASONABLE ANSWER AND DONT MAKE ME HAVE TO DO MORE ERROR HANDLING. READ THE ROOM, READ THE MENU.")

else:
    print("\nI assume you know how to read if you've gotten this far, please type A REASONABLE ANSWER AND DONT MAKE ME HAVE TO DO MORE ERROR HANDLING. READ THE ROOM, READ THE MENU.")