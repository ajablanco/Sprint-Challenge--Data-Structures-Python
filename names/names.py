# original time takes 10.854222059249878 seconds
from bst import BSTNode as bst
import time
# new run time: runtime: 0.18173003196716309 seconds !!!!

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# iterate over list 1
new_bst = bst(names_1[0])
for el in names_1:
    new_bst.insert(el)

# see if any elements in names_2 are also in new_bst, if so add them to the duplicates array
for el in names_2:
    if new_bst.contains(el):
        duplicates.append(el)

# stretch
# runtime increase to  2.353788137435913 seconds
# not more optimized will stick with original solution
for el in names_1:
    duplicates.append(el)
duplicates = [el for el in names_2 if el in duplicates]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
