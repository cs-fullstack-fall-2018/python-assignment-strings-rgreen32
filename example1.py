import os

os.system('clear')

bandMate = "Ringo"

print(len(bandMate))

print(bandMate.upper())

print(bandMate[2])

print(bandMate[1:4])

print(bandMate[3:])

print(bandMate.lower())

print(bandMate.swapcase())

##############################################################

bandMate2 = input("Name? ")

print(len(bandMate2))

wordCase = input("Upper or lower case? ").lower()

if (wordCase == "upper" ):
    print(bandMate2.upper())

if (wordCase == "lower"):
    print(bandMate2.lower())



############################################################################################################




first = input("First bandmate? ")

second = input("Second bandmate? ")

third = input("Third bandmate? ")

bandMates = [first, second, third]

if (len(bandMates[0]) > len(bandMates[1]) and len(bandMates[1]) > len(bandMates[2])):
    print("First Bandmate is longest")

elif (len(bandMates[1]) > len(bandMates[0]) and len(bandMates[0]) > len(bandMates[2])):
    print("Second Bandnate is longest")

else:
    print("Third Bandmate is longest")





















