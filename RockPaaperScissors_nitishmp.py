from random import randint     #Import statement to call random function
player_won = 0                  #Player score counter
computer_won = 0				#Computer Score counter
option_choice = 0
check = 0
player_choice = ['Rock' , 'Paper' , 'Scissors', 'Lizard' , 'Spock']               #List of game choices for the player

"""def main_menu():   #Main Menu fucntion of the game
	print("                  Main Menu               ")
	print("--------------------------------------------------")
	print("[1].Play\n[2].Score\n[3].Exit")"""

def view_scores():  #Function to view the scores
	print('player_score:',player_won ,' computer_score:  ',computer_won)

def play():			#Funtion for the game flow
	print("Game Option:")
	for choice in player_choice:
			print(choice)
	your_choice=(input("Enter your choice<x to exit to main menu>:")).lower()	 #To convert the user input to lower case so that player can enter input in any case 
	computer_choice=0
	while 1:
		if your_choice=='x':  #To exit to the main menu from the play menu
			break	
		if (your_choice not in ('rock' , 'paper' , 'scissors', 'lizard' , 'spock')): #To check the game choice is a valid input 
			print("Invalid Choice!!")
			print("Game Option:")
			for choice in player_choice:
				print(choice)
			your_choice=input("Enter your choice<X to exit to main menu>:")
			your_choice=your_choice.lower()
		else:
			break
	if your_choice!='x':     
		computer_choice=player_choice[randint(0,4)].lower()  #Random number generator for the computer choice to make the decision
		print("Computer Choice: ",computer_choice)  
		
	global player_won									#To declare the global varibles
	global computer_won
	
	if your_choice == computer_choice:				#Logic to compare the results of the game
		print("Tie!")
		player_won =  player_won +1
		computer_won = computer_won + 1
	elif your_choice == "rock" and computer_choice == "scissors":
		print("You win!")
		player_won +=2
	elif your_choice == "paper"and computer_choice == "rock":
		print("You win!")
		player_won +=2
	elif your_choice == "scissors" and computer_choice == "paper":
		print("You win!")
		player_won +=2
	elif your_choice == "spock" and computer_choice == "scissors":
		print("You win!")
		player_won +=2
	elif your_choice == "spock" and computer_choice == "rock":
		print("You win!")
		player_won +=2
	elif your_choice == "lizard" and computer_choice == "spock":
		print("You win!")
		player_won +=2
	elif your_choice == "paper" and computer_choice == "spock":
		print("You win!")
		player_won +=2
	elif your_choice == "lizard" and computer_choice == "paper":
		print("You win!")
		player_won +=2
	elif your_choice == "rock" and computer_choice == "lizard":
		print("You win!")
		player_won +=2
	elif your_choice == "scissors" and computer_choice == "lizard":
		print("You win!")
		player_won +=2	
	elif computer_choice == "rock" and your_choice == "scissors":
		print("Computer win!")
		computer_won+=2	
	elif computer_choice == "paper" and  your_choice == "rock":
		print("Computer win!")
		computer_won+=2	
	elif computer_choice == "scissors" and your_choice == "paper":
		print("Computer win!")
		computer_won+=2	
	elif computer_choice == "spock" and your_choice == "scissors":
		print("Computer win!")
		computer_won+=2	
	elif computer_choice == "spock" and your_choice == "rock":
		print("Computer win!")
		computer_won+=2	
	elif computer_choice == "lizard" and your_choice == "spock":
		print("Computer win!")
		computer_won+=2	
	elif computer_choice == "paper" and your_choice == "spock":
		print("Computer win!")
		computer_won+=2	
	elif computer_choice == "lizard" and  your_choice == "paper":
		print("Computer win")
		computer_won+=2	
	elif computer_choice == "rock" and your_choice == "lizard":
		print("Computer win!")
		computer_won+=2	
	elif computer_choice == "scissors" and your_choice == "lizard":
		print("Computer win!")
		computer_won+=2	
		
def main_menu():   #Main Menu fucntion of the game
	print("                  Main Menu               ")
	print("--------------------------------------------------")
	print("[1].Play\n[2].Score\n[3].Exit")
print("-------Rock Paper Scissors Lizard Spock GAME------")
while True:
	main_menu()
	menu_option=int(input("Select an option (3 to exit): "))
	if (menu_option==1):
		play()
	elif (menu_option==2):
		view_scores()
	else:
		break		
if ( player_won  == computer_won ): #Logic To compare the score and print who is the winner
	print("Tie")
elif ( player_won > computer_won):
	print("You are the winner!!!")
else:
	print("Sorry, Computer is the winner!!!")
print('--------Goooood Bye!!!!!!-------------')




		















