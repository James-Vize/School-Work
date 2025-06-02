#asks user for the height of the pyramid
height = int(input("Enter the height of the pyramid: "))
print()

#building the pyramid
for i in range(height):
    #printing the spaces for the row
    for j in range(height - i -1):
        print(" ", end="")
    #printing the numbers
    for k in range (1, 2 * i + 2):
        print(k, end="")
    #moving to the next line
    print()