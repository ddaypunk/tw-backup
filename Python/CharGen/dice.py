import random

class die():
	def __init__(self,number,sides,flag):
		#number of times to roll the die
		self.number = number
		#number of sides on the die
		self.sides = sides
		#flag for now is just to turn on and off re-rolling of 1's a single time
		self.flag = flag

	def roll_dice(self):
		results = []
		for each in range(self.number):
			roll = random.randrange(1,self.sides+1,1)
			#if ruleset allows for reroll of 1's
			if self.flag == 1:
				if roll == 1:
					#just reroll it once?
					roll = random.randrange(1,self.sides,1)
			results.append(roll)

		return results

	#for DnD ruleset, its add the top three of the dice rolls
	#dice roll list is always length 4 so you only need to find the max 3 times
	def add_top3(self,rollList):
		rollCopy = rollList
		sumVal = 0

		#check 3 times for the max, and add to total
		for each in range(0,3):
			maxVal = max(rollCopy)
			sumVal += maxVal
			i = rollCopy.index(maxVal)
			rollCopy.pop(i)
		return str(sumVal) + "\t(Lowest removed: " + str(rollCopy[0]) + ")"

	def print_rolls(self,rollList):
		for each in rollList:
			print each,
			


"""*** START of MAIN"""
#select your dice, no user input at this point
dice_to_roll = die(4,6,1)
rolls = []

#for DnD, roll each die set 6 times
#this could probably be worked in the class so its automatic
for each in range(6):
	rolls.append(dice_to_roll.roll_dice())

dice_to_roll.print_rolls(rolls)

#print each set of rolls with its total
#for each in rolls:
	#print each,
	#print "= " + dice_to_roll.add_top3(each)