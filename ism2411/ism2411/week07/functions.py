
# ISM2411 - Module 7 Lab: Functions

# Self-Assessment Question 1:
# The first bug I noticed was the missing colon after the second for loop.
# A SyntaxError points to a problem with how the code is written, so it
# reminded me to check the basic syntax before trying to fix the logic.

# Self-Assessment Question 2:
# apply_discount(price, tier) takes an original price and a customer tier.
# It checks which tier the customer has, subtracts the correct discount,
# and returns the new price. A coworker could use it by passing a price
# and a tier like "gold" without needing to know the steps inside.


# --- Exercise 1 ---
print("--- Exercise 1: Calculate Tax ---")

def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---
print("\n--- Exercise 2: Apply Discount ---")

def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    return price - (price * discount)

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier + ':':<8}${apply_discount(200, tier):.2f}")


# --- Exercise 3 ---
print("\n--- Exercise 3: Final Price ---")

discounted_price = apply_discount(200, "gold")
price_with_tax = discounted_price + calculate_tax(discounted_price, 0.07)

print(f"After gold discount: ${discounted_price:.2f}")
print(f"After tax: ${price_with_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---
print("\n--- Exercise 4: Sales Report ---")

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
print("\n--- Exercise 5: Debugging Sales ---")

sales = [120, 80, 250, 175, 90]

# Fix 1: Add each sale to total instead of replacing total each time.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Fix 2: A for loop needs a colon at the end of its first line.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")


i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---
print("\n--- Exercise 6: Scope Experiment ---")

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)
