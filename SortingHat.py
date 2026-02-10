# The Sorting Hat!

input("Let's find out your House for yor time at Hogwarts School of Witchcraft and Wizardry! Are you ready?: ")

Gry = 0              # Variable assignment for each house. All starting at 0. 
Rav = 0
Huf = 0
Sly = 0

# Question One

print("Question One: Do you prefer Dawn or Dusk?: ")
print("  1. Dawn")
print("  2. Dusk")

Answer = int(input("Your answer (1 or 2) is: "))     # 'Answer' variable will be the integer the user provides.

if Answer == 1:
  Gry = Gry + 1      # Gry = Gry + 1 NOT JUST Gry + 1.
  Rav = Rav + 1      # THIS WAY, VARIABLE GRY GETS ASSIGNED A NEW VALUE.
elif Answer == 2:    # THIS VALUE CARRIES THROUGH THE PROGRAM.
  Huf = Huf + 1 
  Sly = Sly + 1
else:
  print("Invalid Input.")

# Question Two

print("Question Two: When I'm dead, I want people to remember me as:")
print("  1. The Good")
print("  2. The Great")
print("  3. The Wise")
print("  4. The Bold")

Answer = int(input("Your answer (1 - 4) is: "))

if Answer == 1:
  Huf = Huf + 2
elif Answer == 2:
  Sly = Sly + 2
elif Answer == 3:
  Rav = Rav + 2
elif Answer == 4:
  Gry = Gry + 2
else:
  print("Invalid input.")

# Question Three

print("Question Three: Which kind of instrument most pleases your ear?: ")
print("  1. The violin")
print("  2. The trumpet")
print("  3. The piano")
print("  4. The drum")

Answer = int(input("Your answer (1 - 4) is: "))

if Answer == 1:
  Sly = Sly + 4
elif Answer == 2:
  Huf = Huf + 4
elif Answer == 3:
  Rav = Rav + 4
elif Answer == 4:
  Gry = Gry + 4
else:
  print("Invalid input.")

# Your house is...

if Gry >= Sly and Gry >= Huf and Gry >= Rav:
  print("Congratulations! Your house is Gryffindor!")
  print("Have a great time in the years to come!")
elif Sly >= Huf and Sly >= Rav:                            # In this elif statement (and the other elif and else proceeding it) Gryffindor is not included as if Gryffindor had the highest score, the program would have already printed that as the house. These statements wouldn't have been reached and executed.
  print("Congratulations! Your house is Slytherin!")
  print("Have a great time in the years to come!")
elif Rav >= Huf:
  print("Congratulations! Your house is Ravenclaw!")
  print("Have a great time in the years to come!")
else:                                                      # Only house left so. only 'else' is needed.
  print("Congratulations! Your house is Hufflepuff!")
  print("Have a great time in the years to come!")