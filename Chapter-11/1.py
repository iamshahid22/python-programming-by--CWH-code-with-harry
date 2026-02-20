# 1. We use input() to get data and float() to turn it into a number
goal = float(input("Enter your goal weight: "))
current = float(input("Enter your current weight: "))

# 2. Logic: If current is already at or above goal, you're done!
if current >= goal:
    print("Goal achieved!")
else:
    # 3. Otherwise, calculate the difference
    diff = goal - current
    print("Need to gain", diff)