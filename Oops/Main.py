from Oops.Product import Product
from Oops.Student import Student

student = Student("Nitin",24,85.5)
student2 = Student("Pavan",24,86.5)
student3 = Student("Sashi",26,87.5)

"""print("Student: "+student.name)
print("Student2: "+student2.name)
print("Student3: "+student3.name)

print("Age: " + str(student.age))
print("Age2: " + str(student2.age))
print("Age3: " + str(student3.age))

print("Marks: " + str(student.marks))
print("Marks2: " + str(student2.marks))
print("Marks3: " + str(student3.marks)) """


product = Product("Laptop", 999.99, "Excellent", 10)
product2 = Product("Pen",10.0)
product3 = Product("Notebook",0.0,"",10)

print("Product: "+product.name, " Price: "+str(product.price), "Quantity: "+str(product.quantity), "Stock: "+str(product.stock))
print("Product2: "+product2.name, "Price: "+str(product2.price))
print("Product3: "+product3.name, "Price: "+str(product3.price), "Quantity: "+str(product3.quantity), "Stock: "+str(product3.stock))