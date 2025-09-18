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
    print("A dragon flies overhead, and just as you think you're safe it swoops down towards you")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

def center_path():
    print("You walk straight and stumble upon a mysterious shrine nestled in the forest")

if __name__ == "__main__":
    intro()
