#make a game rock, paper, scissor where 
#rock beats scissor
#scissor beats paper
#paper beats rock
#use random module to generate computer's choice
#use input to get user's choice
#use if-elif-else to determine the winner
#use while loop to keep the game going until user wants to quit
#the game should inform the user if the choice is invalid
#Check if the game is terminated and if it displays your score, informing you of the number of wins and rounds.
import random
wins = 0
rounds = 0

def game():
    global wins, rounds
    while True:
        print("Welcome to Rock, Paper, Scissor Game!")
        user = input("Enter your choice: rock, paper, or scissor: ")
        if user not in ["rock", "paper", "scissor"]:
            print("Invalid choice. Please try again.")
            continue
        computer = random.choice(["rock", "paper", "scissor"])
        print(f"Computer chose: {computer}")
        if user == computer:
            print("It's a tie!")
        elif user == "rock":
            if computer == "scissor":
                print("You win!")
                wins += 1
            else:
                print("Computer wins!")
        elif user == "paper":
            if computer == "rock":
                print("You win!")
                wins += 1
            else:
                print("Computer wins!")
        elif user == "scissor":
            if computer == "paper":
                print("You win!")
                wins += 1
            else:
                print("Computer wins!")
        else:
            print("Invalid choice. Please try again.")
        rounds += 1
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":

            break

game()

print("Thanks for playing!")


print(f"Number of wins: {wins}")
print(f"Number of rounds played: {rounds}")
#Welcome to Rock, Paper, Scissor Game!
#Enter your choice: rock, paper, or scissor: rock
#Computer chose: scissor
#You win!

#Do you want to play again? (yes/no): yes
#Welcome to Rock, Paper, Scissor Game!
#Enter your choice: rock, paper, or scissor: paper
#Computer chose: rock
#You win!

