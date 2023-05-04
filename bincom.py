import random
import statistics
from fractions import Fraction


colors = [
    "GREEN",
    "YELLOW",
    "BROWN",
    "BLUE",
    "PINK",
    "ORANGE",
    "CREAM",
    "RED",
    "WHITE",
    "BLACK",
    "ARSH",
]

monday_colors = [
    "GREEN",
    "YELLOW",
    "GREEN",
    "BROWN",
    "BLUE",
    "PINK",
    "BLUE",
    "YELLOW",
    "ORANGE",
    "CREAM",
    "ORANGE",
    "RED",
    "WHITE",
    "BLUE",
    "WHITE",
    "BLUE",
    "BLUE",
    "BLUE",
    "GREEN",
]
tuesday_colors = [
    "ARSH",
    "BROWN",
    "GREEN",
    "BROWN",
    "BLUE",
    "BLUE",
    "BLEW",
    "PINK",
    "PINK",
    "ORANGE",
    "ORANGE",
    "RED",
    "WHITE",
    "BLUE",
    "WHITE",
    "WHITE",
    "BLUE",
    "BLUE",
    "BLUE",
]
wednesday_colors = [
    "GREEN",
    "YELLOW",
    "GREEN",
    "BROWN",
    "BLUE",
    "PINK",
    "RED",
    "YELLOW",
    "ORANGE",
    "RED",
    "ORANGE",
    "RED",
    "BLUE",
    "BLUE",
    "WHITE",
    "BLUE",
    "BLUE",
    "WHITE",
    "WHITE",
]
thursday_colors = [
    "BLUE",
    "BLUE",
    "GREEN",
    "WHITE",
    "BLUE",
    "BROWN",
    "PINK",
    "YELLOW",
    "ORANGE",
    "CREAM",
    "ORANGE",
    "RED",
    "WHITE",
    "BLUE",
    "WHITE",
    "BLUE",
    "BLUE",
    "BLUE",
    "GREEN",
]
friday_colors = [
    "GREEN",
    "WHITE",
    "GREEN",
    "BROWN",
    "BLUE",
    "BLUE",
    "BLACK",
    "WHITE",
    "ORANGE",
    "RED",
    "RED",
    "RED",
    "WHITE",
    "BLUE",
    "WHITE",
    "BLUE",
    "BLUE",
    "BLUE",
    "WHITE",
]

total_colors = (
    monday_colors + tuesday_colors + wednesday_colors + thursday_colors + friday_colors
)

# MEAN
mean_color = statistics.mode(total_colors)
print(f"Mean color is {mean_color}")
# MODE
most_worn_color = statistics.mode(total_colors)
print(f"Most worn color is {most_worn_color}")
# MEDIAN
median_color = statistics.median(total_colors)
print(f"Median color is {median_color}")

# Probability that red is chosen
red_count = total_colors.count("RED")
total_count = len(total_colors)
red_probability = Fraction(red_count, total_count)
print(f"The probability that the color is red is {red_probability}")

# 4 Digit Binary Number Generator with Decimal Equivalent
binary = "".join(str(random.randint(0, 1)) for _ in range(4))
decimal = int(binary, 2)
print(f"Binary: {binary}")
print(f"Decimal: {decimal}")


# FIBONACCI
fibonacci = [0, 1]
for i in range(2, 50):
    next_num = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_num)
sum_fibonacci = sum(fibonacci)
print(f"The sum of the first 50 Fibonacci numbers is: {sum_fibonacci}")
