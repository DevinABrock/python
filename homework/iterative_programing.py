######################################################################################################################################################
# Question 1 - Done
######################################################################################################################################################

print("#1")

a1 = [2, 4, 5]
a2 = [2, 3, 6]

a3 = []
for index in range(3):
    a3.append(a1[index] * a2[index])
print(a3)

######################################################################################################################################################
# Question 2 - Done
######################################################################################################################################################

print("#2")

b1 = [ [2, -9], 
[23, 6]]

b2 = [ [8, -4], 
[6, 33]]

b3 = []
for x in range(len(b1)):
    for y in range(len(b1[0])):
        b3.append(b1[x][y] + b2[x][y])
    result = b3
print(result)

######################################################################################################################################################
# Question 3 - Done
######################################################################################################################################################

print("#3")

c1 = [ [2, -2], 
[5, 3], [7, 5]]

c2 = [ [1, -4], 
[7, 5], [2, -2]]

c3 = []
for x in range(len(c1)):
    for y in range(len(c1[0])):
        c3.append(c1[x][y] + c2[x][y])
    result = c3
print(result)

######################################################################################################################################################
# Question 4 - Done
######################################################################################################################################################

print("#4")

d1 = [0, 0, 1, 1, 2, 2, 3, 3]

d2 = []

for a in range(len(d1)):
    if a not in d2:
        d2.append(a)
print(d2[:4])

######################################################################################################################################################
# Question 5 - Done
######################################################################################################################################################

print("#5")

e1 = input("Please type a word:").upper()

e1 = e1.replace("A", "4")
e1 = e1.replace("E", "3")
e1 = e1.replace("G", "6")
e1 = e1.replace("I", "1")
e1 = e1.replace("O", "0")
e1 = e1.replace("S", "5")
e1 = e1.replace("T", "7")

print(e1)

######################################################################################################################################################
# Question 6 - Done
######################################################################################################################################################

print("#6")

f1 = input("Please enter a phrase: ").lower()

f1 = f1.replace('aa', 'aaaaa')
f1 = f1.replace('ee', 'eeeee')
f1 = f1.replace('ii', 'iiiii')
f1 = f1.replace('oo', 'ooooo')
f1 = f1.replace('uu', 'uuuuu')
print(f1)

######################################################################################################################################################
# Question 7 - Done
######################################################################################################################################################

print("#7 Part 1")

g1 = input("enter a word or phrase: ")
offset = 3

alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = alphabet[offset:] + alphabet [:offset]
word = str.maketrans(alphabet, shift)

answer = g1.translate(word)
print(answer)

#####

print("#7 Part 2")

g1 = "Lbh zhfg hayrnea, jung lbh unir yrnearq."
offset = 13

alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = alphabet[offset:] + alphabet [:offset]
word = str.maketrans(alphabet, shift)

answer = g1.translate(word)
print(answer)

# Translation = You must unlearn, what you have learned.


