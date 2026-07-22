fruits = ["apple","banana","cherry","mango"]

print(fruits[0]) # Accessing the first element
print(fruits[-1]) #Accessing last element
print(fruits[1:4]) # Accessing a range of elements
print(fruits[::2])
print(len(fruits)) # Getting the length of the list
fruits.append("Watermillon")
print(fruits)
fruits.insert(1,"grape")
print(fruits)
fruits.remove("cherry")
print(fruits)
fruits.pop()
print(fruits)
fruits[3] = "kiwi"
print(fruits)

fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)