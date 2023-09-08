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