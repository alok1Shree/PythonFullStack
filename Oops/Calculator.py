# This is the example for  Polymorphsim - Compile Time Polymorphism

class Calculator:
    # Default parameters handle optional arguments
    def add(self, a, b, c=None):
        if c is not None:
            print("Three numbers")
            return a + b + c
        print("Two numbers")
        return a + b

    # *args handles truly variable number of arguments
    def add_many(self, *numbers):
        print(f"Adding {len(numbers)} numbers")
        return sum(numbers)

    # Type-aware using isinstance
    def smart_add(self, a, b):
        if isinstance(a, str) and isinstance(b, str):
            print("String concatenation")
            return a + " " + b
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            print("Numeric addition")
            return a + b
        else:
            raise TypeError(f"Cannot add {type(a)} and {type(b)}")


calc = Calculator()

print("==== PYTHON EQUIVALENT OF OVERLOADING ====")
print(calc.add(5, 3))           # Two numbers    → 8
print(calc.add(5, 3, 2))        # Three numbers  → 10
print(calc.add_many(1,2,3,4,5)) # Adding 5 numbers → 15
print(calc.smart_add("Hello", "World"))   # String → Hello World
print(calc.smart_add(5.5, 3.3))           # Numeric → 8.8