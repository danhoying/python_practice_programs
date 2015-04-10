# BLOCKS
# Recreates the half-pyramid of blocks at the end of world
# 1-1 of mario bros. using a user-defined height


def getHeight(): # function to get a valid integer height (<23 blocks high)
    while True:
        try:
            towerHeight = int(input("Enter the tower height desired: "))
        except ValueError:
            print("Please enter a number")
        else:
            if 1 < towerHeight <23:
                return towerHeight
    

height = getHeight()
for i in range(2, height + 2): # start at 2 because top is always 2 blocks
    print(" " * (height + 1 - i) + "#" * i) # add empty spaces to right-justify
                                            # the pyramid
    

