def intro():
    print("You wake up in a dark forest. You can go left, right, or center.")
    choice = input("Which direction do you choose? (left/right/center): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    elif choice =="center":
	center_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a friendly duel.")
    print("You draw you sword and defeat the squirrel swiftly")
    print("The forest begins to speak to you, telling you to take the squirrel's wallet")
    print("You listen to it's commands, and relieve the squirrel of $4.50")

def center_path():
    print("You walk straight and stumble upon a mysterious shrine nestled in the forest")

if __name__ == "__main__":
    intro()
