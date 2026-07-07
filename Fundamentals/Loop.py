# Print even num range from 1 -100
"""for i in range(1, 101):
    if i % 2 == 0:
        print(i)

for i in range(2,101, 2): #1, 1+2=3, 3+2=5  || 2, 2+2=4, 4+2=6
    print(i)
"""

#Sum of first N numbers
"""
n = int(input("Enter any number: ")) #n=5
sum = 0 # sum = 0
for i in range(1, n+1): #(1,2,3,4,5,6) i= 1, i=2, i=3 , i=4, i=5
                        #[0,1,2,3,4,5]
    sum = sum + i # sum = 0 + 1 = 1, sum = 1 + 2 = 3, sum = 3 + 3 = 6, sum = 6 + 4 = 10, sum = 10 + 5 = 15
    print("Sum of first", n, "numbers is:", sum)
"""

#Factorial of a Number
"""n = int(input("Enter any number: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
    print(fact)"""


#Reverse a number
"""n = int(input("Enter any number: ")) #n=12345 output = 54321
reverse = 0 #543
while n > 0:
    digit = n % 10 #digit = 5, digit = 4, digit = 3, digit = 2, digit = 1  (123%10= 3)
    reverse = reverse * 10 + digit #reverse = 0*10 + 5 , 5*10+4, 54*10+3
    n = n // 10 #n = 5//10 = 0 1234 123 12
print("Reverse of the number is:", reverse)"""


#Check Palindrome Number - Madam
"""n = int(input("Enter any number: "))
original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if original == reverse:
    print(original, "is a palindrome number")
else:
    print(original, "is not a palindrome number")"""



"""
*
* *
* * *
* * * *
* * * * *
"""

rows = 5
for i in range(1,rows+1): #(1,2,3,4,5,6) i(rows)=1, 2, 3
    for j in range(i): #j(Column)=0 1 2 3
        print("*", end=" ") #* \n * * \n * * * \n
    print()


