import sys
from io import StringIO

class SpellRun:
    def __init__(self):
        # Create a restricted execution context
        self.restricted_globals = {
            '__builtins__': {
                '__import__': self.restricted_import,
                'print': self.restricted_print,  # Use custom print function
                'range': range,
                'len': len,
                '+': str.__add__,
                '[]': str.__getitem__
            },
            'class': None,
            'def': None,
            'try': None,
            'except': None,
            'finally': None
        }

        self.print_output = []  # To store printed output

    # Define a custom import hook that raises an ImportError for all modules
    def restricted_import(self, name, globals=None, locals=None, fromlist=(), level=0):
        raise ImportError(f"Importing {name} is not allowed.")

    # Define a custom print function to capture printed output
    def restricted_print(self, *args, **kwargs):
        output = " ".join(map(str, args))
        self.print_output.append(output)

    # Define a custom restricted `exec` function that allows string manipulation
    def restricted_exec_run(self, user_code):
        self.print_output = []
        try:
            # Redirect stdout to capture printed output
            original_stdout = sys.stdout
            sys.stdout = StringIO()

            # Execute user code in the restricted environment
            exec(user_code, self.restricted_globals)

            # Get the captured printed output
            captured_output = sys.stdout.getvalue()
            self.print_output.append(captured_output)
        except ImportError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Restore the original stdout
            sys.stdout = original_stdout

    def get_printed_outputs(self):
        return self.print_output
'''
my_spell = SpellRun()

# Some simple test cases many other have already been executed but there not of the interest of this partiqular exercise.
# Here a variable can be chnages by code inside exec programm doesn't finds it ands throws an exeption and after that the print_output doesn't get updated.
a = 10

user_code = """
arr = [64, 25, 12, 22, 11]

n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# a += 10
# print(a)

print("Sorted array is:", arr)
"""

# Execute the code and capture the printed output
my_spell.restricted_exec_run(user_code)

# Access the captured printed output
print("Printed Output:")
for output_line in my_spell.print_output:
    print(output_line)

print(len(my_spell.print_output))








my_spell = SpellRun()

user_code = """
string1 = "Hello, world!"
substring = "world"

if substring in string1:
    print(f"'{string1}' contains '{substring}'.")
else:
    print(f"'{string1}' does not contain '{substring}'.")
"""

# Execute the code and capture the printed output
my_spell.restricted_exec_run(user_code)

# Access the captured printed output
print("Printed Output:")
for output_line in my_spell.print_output:
    print(output_line)

print(len(my_spell.print_output))
'''