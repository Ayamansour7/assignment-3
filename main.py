#assignment 3
#stacks and queues
#1 using stacks
class PalindromeChecker:
    def __init__(self):
        self.stack = []

    def is_palindrome(self, input_str):
        # Remove non-alphanumeric characters and convert to lowercase
        input_str = ''.join(char.lower() for char in input_str if char.isalnum())

        # Push each character to the stack
        for char in input_str:
            self.stack.append(char)

        # Compare each character in the input string with the characters popped from the stack
        for char in input_str:
            if char != self.stack.pop():
                return False

        return True


# Test the palindrome checker
checker = PalindromeChecker()

print(checker.is_palindrome("racecar"))  # True
print(checker.is_palindrome("hello"))  # False
print(checker.is_palindrome("12321"))  # True



#2 stacks
def is_balanced(expression):
    stack = []
    opening_parentheses = ['(', '[', '{']
    closing_parentheses = [')', ']', '}']
    parentheses_map = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in opening_parentheses:
            stack.append(char)
        elif char in closing_parentheses:
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            stack.pop()

    return len(stack) == 0


# Test the expression for balance
expressions = [
    "(1+2)-3*[41+6]",       # True
    "(1+2)-3*[41+6}",       # False
    "(1+2)-3*[41+6",        # False
    "(1+2)-3*]41+6[",       # False
    "(1+[2-3]*4{41+6})",    # True
]

for expression in expressions:
    print(is_balanced(expression))



#2 carwash

class Car:
    def __init__(self, make, color, plate_number):
        self.make = make
        self.color = color
        self.plate_number = plate_number

    def __str__(self):
        return f"Make: {self.make}, Color: {self.color}, Plate Number: {self.plate_number}"


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, car):
        self.queue.append(car)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.queue[0]


def print_menu():
    print("Car Wash Program Menu:")
    print("1. Insert a car to the queue")
    print("2. Remove a car from the queue")
    print("3. Exit the program")


# Create an instance of the Queue class
car_queue = Queue()

# Car Wash Program
print("Welcome to the Car Wash Program!")

while True:
    print_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        make = input("Enter the make of the car: ")
        color = input("Enter the color of the car: ")
        plate_number = int(input("Enter the plate number of the car: "))

        car = Car(make, color, plate_number)
        car_queue.enqueue(car)
        print("Car added to the queue.")

    elif choice == '2':
        if car_queue.isEmpty():
            print("No cars in the queue.")
        else:
            car = car_queue.dequeue()
            print("Car removed from the queue:")
            print(car)

    elif choice == '3':
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")