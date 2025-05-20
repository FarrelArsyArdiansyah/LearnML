# -------------------------------------------------------------------
# Variables in Python - Examples with English Naming Conventions
# -------------------------------------------------------------------

# 1. snake_case (Recommended by PEP 8 for regular variables)
# -------------------------------------------------------------------
favorite_car = "Toyota"  # Standard lowercase with underscores
car_price = 250_000_000  # Underscores can be used as number separators

print(favorite_car)  # Output: Toyota
print(car_price)     # Output: 250000000 (underscores are ignored)

# 2. UPPER_CASE (Convention for constants)
# -------------------------------------------------------------------
PI = 3.14            # Constant value (convention, not enforced by Python)
MAX_SPEED = 300      # Variables that shouldn't be changed

print(PI)            # Output: 3.14

# 3. Numbers in Middle/End (Allowed, but not at start)
# -------------------------------------------------------------------
car2 = "Pagani"      # Number at end is allowed
model_3 = "Tesla"    # Number in middle is allowed
# 2car = "Error"     # This would error (can't start with number)

print(car2)          # Output: Pagani
print(model_3)       # Output: Tesla

# 4. Dynamic Typing (Variables can change type)
# -------------------------------------------------------------------
data = 100           # Starts as integer
data = "One Hundred" # Changes to string

print(data)          # Output: One Hundred

# 5. Single Underscore (Temporary/unimportant variables)
# -------------------------------------------------------------------
_ = "Unused value"   # Typically for ignored values
name, _ = "Alice", 25 # Ignoring the second value

print(name)          # Output: Alice

# 6. Double Underscore (Name mangling for class-private variables)
# -------------------------------------------------------------------
__password = "secret" # Python will rename to _ClassName__password

print(__password)     # Output: secret (not truly private)

# 7. Multiple Assignment
# -------------------------------------------------------------------
x, y, z = 1, 2, 3
brand1, brand2 = "Ferrari", "Porsche"

print(y)              # Output: 2
print(brand2)         # Output: Porsche

# 8. Unpacking
# -------------------------------------------------------------------
cars = ["Toyota", "Honda", "Suzuki"]
first, second, third = cars

print(second)         # Output: Honda

# -------------------------------------------------------------------
# Important Notes:
# - Always use descriptive names (e.g., user_age instead of ua)
# - Avoid single-letter names except for trivial loop variables
# - Never use Python keywords (if, for, while, etc.) as variables
# -------------------------------------------------------------------