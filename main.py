while True:
    user_action1 = input("Player 1 enter a choice (rock, paper, scissors): ").lower()
    
    user_action2 = input("Player 2 enter a choice (rock, paper, scissors): ").lower()
    
    if user_action1 == user_action2:
        print('\nIt\'s a tie!')
    
    elif user_action1 == "rock":
        if user_action2 == "scissors":
            print('\nPlayer 1 wins!')
        elif user_action2 == "paper":
            print('\nPlayer 2 wins!')
        else: 
            print("\nPlease reenter your choice as lower caseor use a valid answer!")
    
    elif user_action1 == "paper":
        if user_action2 == "rock":
            print('\nPlayer 1 wins!')
        elif user_action2 == "scissors":
            print('\nPlayer 2 wins!')
        else: 
            print("\nPlease use a valid answer!")
    
    elif user_action1 == "scissors":
        if user_action2 == "paper":
            print('\nPlayer 1 wins!')
        elif user_action2 == "rock":
            print('\nPlayer 2 wins!')
        else: 
            print("\nPlease use a valid answer!")
    
    else: 
        print("\nPlease use a valid answer!")
    
    
    play_again = input("\nPlay again? (y/n): ")
    print()
    if not play_again.lower().startswith("y"):
      break