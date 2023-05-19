import math

f = open("DOLECH.inp")
line1 = f.readline().strip().split()
line2 = f.readline().strip().split()
f.close()
line1 = [int(i) for i in line1]
line2 = [int(i) for i in line2]

line2.sort()

K = line1[1]


def DOLECH():
    result = 0
    for i in line2:
        print()
        j = binarySearch(line2,i + K)
        if j != None:
            result += 1
    return result

# - Binary search work by put an anchor in the middle of the array and cut it in
#   half after each time
# - If the anchor bigger than the target, remove all smaller target in the search 
#   range, and the other way around if the anchor is smaller than the target
# - Rinse and repeat until find the target's index or the search range become 0 (target not inside list)

# - You can also just use "in" to check if a value inside the array for an easier time. But where's the fun in that?

def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    anchor = math.floor((left + right) / 2)
    
    while arr[anchor] != target and left <= right:
        if arr[anchor] < target:
            left = anchor + 1
        else:
            right = anchor - 1
        anchor = math.floor((left + right) / 2)
        
    return anchor if arr[anchor] == target else None

f = open("DOLECH.out","w")
f.write(str(DOLECH()))
f.close()   