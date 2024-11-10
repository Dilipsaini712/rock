import random
li=['rock','paper','scissors']

print("*****Welcome To Rock-Paper-Game*****\n")
while True:
    print("1. Play Game - Yes")
    print("2. Stop Game - No")
    choice=input("Enter your choice: ")
    user_count=0
    computer_count=0
    if choice == "1":
        play=int(input("How many time you play:"))
        for i in range(1,play+1):
            computer_choice= random.choice(li)
            user_choice= input("\nEnter your choice (rock/paper/scissors): ").lower()
            if user_choice not in li:
                print("Invalid choice. Please enter rock, paper or scissors.")
                continue
            else:
                print(f"\nComputer chose: {computer_choice}.\n")
                if user_choice == computer_choice:
                    print(f"Both players selected {user_choice}. It's a tie!\n")
                    user_count=user_count+1
                    computer_count=computer_count+1

                elif (user_choice=='rock' and computer_choice=='scissor') or (user_choice=='paper' and computer_choice=='rock') or (user_choice=='scissor' and computer_choice=='paper'):
                    print(f"{user_choice} beats {computer_choice}. You win!\n")
                    user_count=user_count+1
                else:
                    print(f"{computer_choice} beats {user_choice}. You lose!\n")
                    computer_count=computer_count+1

        if user_count==computer_count:
            print("It's a tie!")
            print(f"Computer count: {computer_count}.")
            print(f"User count: {user_count}.\n")
        elif user_count>computer_count:
            print("You win the game!")
            print(f"User count: {user_count}.")
            print(f"Computer count: {computer_count}.\n")
        else:
            print("Computer wins the game!")
            print(f"Computer count: {computer_count}.")
            print(f"User count: {user_count}.\n")

    elif choice == "2":
        print("Thanks for playing. Goodbye!\n")
        break
    
    else:
        print("Invalid choice. Please enter 1 or 2!\n")