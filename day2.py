# Day 2 coding challenge - Operators

# Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax
# percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

import sys

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    totalCost = round(meal_cost + (meal_cost*(tip_percent/100)) + (meal_cost*(tax_percent/100)))

    print('The total meal cost is ' + str(totalCost) +  ' dollars.')