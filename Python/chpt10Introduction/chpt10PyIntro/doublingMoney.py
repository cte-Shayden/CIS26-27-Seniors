# -------------------------
# Script Name: doublingMoney.py
# Lesson: Algorithm Design (Section 10.9)
#
#
# Problem (from the textbook):
# You put $10,000 into an account that earns 5% interest per year. how many years until the balance doubles.
# 
# Pseudocode (my algorithm):
#   Set year to 0, balance to 10000
#   While the balance ise less than 20000 
#       Add 1 to the year.
#       Set the interest rate to balance x 0.05.
#       Add the interest to the balance.
#   Report year as the answer.
# ================================

# Set year to 0, balance to 10000
year= 0
balance= 10000
# while the balance is less than 20000
while balance < 20000: # the loop will run until the balaance is >= 20000
    # add 1 to the year
    # year = year + 1
    year += 1
    #set the interest rate to balance x 0.05
    interest= balance * 0.05
    #add interest to the balance
    balance = balance + interest
#report year as the answer.
print("Years to double", year)
print("Final Balance", f"{balance:.2f}")
