import numpy as np
import time
import pyttsx3
from random import randint
from random import seed

arr1 = [] #initialise an empty array
arr2 = [] #initialise an empty array 

engine = pyttsx3.init() #initialise the pyttsx3 functions
gameState = 1 #initialises the loop in code on 1st build

#function to create random arrays of 4 integers 
def random_arr(arr):
	for _ in range(4):
			value = randint(0, 10)
			arr.append(value)		
	return [arr]	
#function to compute the combinations within the array to match the target
def twoSum(arr,target):
	values = dict()
	for i, elem in enumerate(arr): #we iterate over the array
		comp = target - elem #minus the target from the element in each position
		if comp in values:#if the compliment is found in the values 
			#print(comp)
			#print(i)
			return [values[comp],i] #we return the position relating to the comp & loop iteration
		values[elem]=i	#if no combinations found we return error message
	return["No combination of pairs equal the target value"]

#loop 
while gameState == 1:
	#Loop begining warning
	engine.say("This is a message to state a new loop is starting")

	target1 = np.random.randint(0,10)#generate random target1
	target2 = np.random.randint(0,10)#generate random target2

	random_arr(arr1) #pass arr1 to random_arr function to generate random array of 4 integers
	random_arr(arr2) #pass arr2 to random_arr function to generate random array of 4 integers

	print("---------------------------------")
	print("Target Value no.1 is",int(target1))#prints target1 value
	print("---------------------------------")
	print("The randomised array is:",arr1)   #prints the randomised arr1
	print("---------------------------------")
	list1 = twoSum(arr1,target1)              #passes arr1 & target1 to twoSum function
	print("The result of the twoSum function returns:",list1)#prints the result returned from the twoSum function
	print("---------------------------------")
	print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>")
	print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>")
	print("---------------------------------")
	print("Target Value no.2 is",int(target2))#prints target2 value
	print("---------------------------------")
	print("The randomised array is:",arr2)  #prints the randomised arr2
	print("---------------------------------")	 
	list2 = twoSum(arr2,target2)             #passes arr2 & target2 to twoSum function
	print("The result of the twoSum function returns:",list2)#prints the result returned from the twoSum function
	print("---------------------------------")
	gameState=0 #stops the loop

	if(len(list1) == 2):#if a two combination array is found succes voiceover is started
		engine.say("Correct combination of pairs to equal the target have been found in list one")
	else:#if no combinations found then failure voiceover is started
		engine.say("No combination of pairs equal the target value in list one")

	if(len(list2) == 2):#if a two combination array is found succes voiceover is started
		engine.say("Correct combination of pairs to equal the target have been found in list two")
	else:#if no combinations found then failure voiceover is started
		engine.say("No combination of pairs equal the target value in list two")

	engine.runAndWait()#engine run and wait function 

	arr1 = []#empty arr1 for next randomisation call
	arr2 = []#empty arr2 for nexr randomisation call
	
	time.sleep(60) #freeze the code for 60 seconds
	print('\n'*100)#clears a gap for clearer viewing on console
	gameState=1#restart loop





