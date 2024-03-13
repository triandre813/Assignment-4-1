"""
This program calculates prices for custom house signs.
"""

#Declare and initialize variables here.

charge = 0.00 # Charge for this sign.

# Prompt the user for input
numChars = int(input("Enter the number of characters: "))
color = input("Enter the color of the characters (black/gold): ")
woodType = input("Enter the type of wood (oak/pine): ")

# Write assignment and if statements here as appropriate.
# Calculated base charge

charge = 35.00

# Calculate additional charge based on number of characters
if numChars > 5:
  charge += (numChars - 5) * 4

# Add charge for oak wood type
if woodType == "oak":
  charge += 20.00

# Add charge for gold-leaf lettering
if color == "gold":
  charge += 15.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
