def intro():
    print("Welcome to the Adventure Game!")
    print("You are standing at the entrance of a mysterious forest.")
    print("Do you want to enter the forest or leave?")
    
    choice = input("Enter '1' to go into the forest or '2' to leave: ")
    
    if choice == '1':
        enter_forest()
    elif choice == '2':
        leave_forest()
    else:
        print("Invalid input, please try again.")
        intro()

def enter_forest():
    print("\nYou step into the forest. The trees tower above you, and it's very quiet.")
    print("After walking for a while, you come to a fork in the path.")
    print("Do you want to take the left path or the right path?")
    
    choice = input("Enter '1' for the left path or '2' for the right path: ")
    
    if choice == '1':
make_wish()
    elif choice == '2':
        explore_more()
    else:
        print("Invalid input, please try again.")
        right_path()

def fight_spider():
    print("\nYou bravely charge at the giant spider with your sword!")
    print("After a fierce battle, you defeat the spider and open the treasure chest.")
    print("You find a magical gem that grants you eternal wisdom!")
    print("Congratulations, you won the game!")
    
def sneak_around_spider():
    print("\nYou quietly sneak around the spider and reach the treasure chest.")
    print("Inside the chest, you find gold coins and a map to a hidden kingdom!")
    print("You feel victorious and decide to return to the village.")
    print("Congratulations, you won the game!")
    def sneak_around_spider():
    print("\nYou quietly sneak around the spider and reach the treasure chest.")
    print("Inside the chest, you find gold coins and a map to a hidden kingdom!")
    print("You feel victorious and decide to return to the village.")
    print("Congratulations, you won the game!")

def make_wish():
    print("\nYou close your eyes and wish for unlimited wealth.")
    print("The fairy grants your wish, and a mountain of gold appears before you!")
    print("You leave the forest, richer than ever. Congratulations, you won the game!")

def explore_more():
    print("\nYou decide to explore the clearing more, but a wild bear appears!")
    print("It looks angry. You have no choice but to run back to the forest entrance.")
    print("Unfortunately, you were too late. The bear catches you. Game over.")
    
def leave_forest():
    print("\nYou decide not to enter the forest and return home.")
    print("However, you always wonder what could have been. Game over.")

# Start the game
intro()