# ===============================
# Errors.py ---- "Break on purpose"

# -- Warm-up: a program that works ------
# print("Hello, World")

# -- Experiment 1: Syntax. Error (translation time)
# print("Hellow, World!)

# ----- Experiment 2: Syntax Error ----
# print(Hello, World!)

# ----- Experiment 3: Name Error ------
# Print("Hellow, World!")

#----  Experiment 4: Indentation Error ------ 
# print("Hellow")
#    print("World!")

#------ Experiment 5: Division Error-----
# print("About to divide")
# print(1/0)

#---- Experiment 6: Logic Errors with numbers ---
# We want the average of three test scores.
# Expected: (90++80+70) / 3 = 80.0
score1 = 90
score2= 80
score3= 70

average= (score1 + score2 + score3) / 3

print("average", average)