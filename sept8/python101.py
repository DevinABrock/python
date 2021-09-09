#######################################################################################################################
# Question 1 - Done
#######################################################################################################################

print('**question 1**')

total_bill_amount = 1577
tip_amount = ""

level_of_service = input("How was the service?\n Was it good, fair, or bad:")

if (level_of_service.lower() == "good"):
    tip_amount = (total_bill_amount * 0.2)
elif (level_of_service.lower() == "fair"):
    tip_amount = (total_bill_amount * 0.15)
elif (level_of_service.lower() == "bad"):
    tip_amount = (total_bill_amount * 0.1)
else:
    print("That's not a valid response.")

print("Here is your tip amount.")
print (float(tip_amount))
print("And here is your total.")
print (float(tip_amount + total_bill_amount))

#######################################################################################################################
# Question 2 - Question
#######################################################################################################################

print('**question 2**')

number = ''
print ('Number of people eating')
x = input()
# I tryed doing this next part different ways and I kept running into the same error.
# TypeError: unsupported operand type(s) for //: 'int' and 'str'
# I also tried using x = input(float()) on line 34.
new_total = total_bill_amount // x
print("amount per person")
print(new_total)

#######################################################################################################################
# Question 3 - Done
#######################################################################################################################

print('**question 3**')

coins = 0
print("It looks like you're out of coins.\n I can spot you some if you want.")
giver = input("type y for yes, n for no.")

while giver == 'y':
    coins += 1
    print (f'Here, now you have {coins} coins')
    giver = input("Do you need some more?\n type y for yes, n for no.")

print('okay, bye.')

#######################################################################################################################
# Question 4 - Not Finished Yet
#######################################################################################################################

print('**question 4**')

print ('How long do you want your box?')
width = input(int())
print ('Now how high do you want your box?')
height = input(int())

print("give me a sec...")

print((width) * "*")
print(height)

#######################################################################################################################
# Question 5 - Done
#######################################################################################################################

print('**question 5**')

print(""" 
    *  
   ***
  *****
 *******""" )