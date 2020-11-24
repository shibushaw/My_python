
import random

def first_dice():
	print(" ---------")
	print("|         |")
	print("|         |")
	print("|    0    |")
	print("|         |")
	print("|         |")
	print(" ---------")

def second_dice():

	print(" ---------")
	print("| 0       |")
	print("|         |")
	print("|         |")
	print("|         |")
	print("|       0 |")
	print(" ---------")


def third_dice():
	print(" ---------")
	print("| 0       |")
	print("|         |")
	print("|    0    |")
	print("|         |")
	print("|       0 |")
	print(" ---------")


def fourth_dice():
	print(" ---------")
	print("| 0     0 |")
	print("|         |")
	print("|         |")
	print("|         |")
	print("| 0     0 |")
	print(" ---------")

def fifth_dice():
	print(" ---------")
	print("| 0     0 |")
	print("|         |")
	print("|    0    |")
	print("|         |")
	print("| 0     0 |")
	print(" ---------")



def sixth_dice():
	print(" ---------")
	print("| 0     0 |")
	print("|         |")
	print("| 0     0 |")
	print("|         |")
	print("| 0     0 |")
	print(" ---------")

player1_result = []


def my_fun():
	
		
	my_dict = {1:[1,2,3,4,5,6],
				2:[2,3,4,5,6,1],
				3:[3,4,5,6,1,2],
				4:[4,5,6,1,2,3],
				5:[5,6,1,2,3,4],
				6:[6,1,2,3,4,5]}
	user_int = int(input("Enter an number 1-6 : "))


	for rand_int in my_dict[user_int]:
	

		if rand_int == 1 and rand_int not in player1_result :
			first_dice()
			player1_result.append(rand_int)
			
		elif rand_int == 2 and rand_int not in player1_result :
			second_dice()
			player1_result.append(rand_int)
			
		elif rand_int == 3 and rand_int not in player1_result :
			third_dice()
			player1_result.append(rand_int)
			
		elif rand_int == 4 and rand_int not in player1_result :
			fourth_dice()
			player1_result.append(rand_int)
			
		elif rand_int == 5 and rand_int not in player1_result :
			fifth_dice()
			player1_result.append(rand_int)	
			
		elif rand_int == 6 and rand_int not in player1_result :
			sixth_dice()
			player1_result.append(rand_int)
		



count = 0

print("Welcome to DICE_GAME")
print("RULES : ")
print(" * You have only 6 rolls ")
print(" * Try to win the game.......!!!!!")
print(" ----------------------------------------")
print("|                                        |")
print("|               GAME-STARTS              |")
print("|                                        |")
print(" ----------------------------------------")


my_fun()


print("Your rolls = ",player1_result)
print(" ----------------------------------------")
print("|                                        |")
print("|               GAME-OVER                |")
print("|                                        |")
print(" ----------------------------------------")






