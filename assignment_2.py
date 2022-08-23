#Qn 1. Print the first 10 natural numbers
counter = 0
while counter <= 9:
    print(counter)
    counter = counter + 1

#Qn 2. Calculate the sum of all numbers from 1 to a given number
counter = 0
total = 0
while counter<50:
    total += counter
    counter+=1
print(total)

#Qn 3. Write a program to print a multiplication table of a given number. e.g if number is 2, then output should be 2, 4, 4, 8
n = 2
for i in range(1, 11, 1):
    product = n * i
    print(product)

#Qn 4. Write a program to display only those numbers from a list that satisfy the following condition
numbers = [12, 75, 150, 180, 145, 525, 50] 
for item in numbers:
    if item > 500:
     break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)
#Qn 5. Write a program to count the total number of digits in a number using a while loop given number 4673453

num = 4673453
var = 0
while num != 0:
    num = num // 10
    count = count + 1
    print("Total Number of Digits Include:", var)

#Qn 6. Display numbers from -10 to -1 using while loop

counter = -1
while counter >= -10:
    print(counter)
    counter = counter - 1
