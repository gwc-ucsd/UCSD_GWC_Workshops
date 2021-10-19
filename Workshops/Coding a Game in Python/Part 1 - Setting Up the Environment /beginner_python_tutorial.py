### PRINT STATEMENTS 
print("Hello World")
print(11)

# After typing the above line, run this on VS Code's 
# terminal python3 beginner_python_tutorial.py

# -----------------------------------------------------------------------------------------------------------

### DATA TYPES 
# In Python, Strings are arrays of bytes representing Unicode characters. 
# A string is a collection of one or more characters put in a single quote, double-quote or triple quote.
string_1 = 'girlswhocode' 
string_2 = "GWC" 
string_3 = """UCSD_GWC"""

# Integers contains positive or negative whole numbers (without fraction or decimal). 
# In Python there is no limit to how long an integer value can be.
integer_1 = 10
integer_2 = 100000000000000000

# Floats are specified by a decimal point. 
# Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation.
float_1 = 10.0
float_2 = 1.456

# Data type with one of the two built-in values, True or False. 
# Non-Boolean objects can be evaluated in Boolean context as well and determined to be true or false.
boolean_0 = True
boolean_1 = False

print(boolean_0 == boolean_1)
print(1 == 4)

# -----------------------------------------------------------------------------------------------------------
### SIMPLE ARITHMETIC
x = 6
y = 4

print(x+y) # addition
print(x-y) # subtraction
print(x*y) # multiplication
print(x/y) # division
print(10**2) # exponential
print(x%3) # modulo
print(x%y) # modulo
print(x//y) # floor division
