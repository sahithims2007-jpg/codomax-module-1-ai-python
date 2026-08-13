# Conditions and Loops

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("\nNumbers from 1 to 10:")

for i in range(1, 11):
    print(i)
