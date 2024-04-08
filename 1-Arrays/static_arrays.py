# Array
# stored as contiguous block of data

# Read: O(1), constant time operation
# Accesses data in RAM, O(1) to get memory there
my_arr = [1,3,5]
my_arr[0] # = 1
my_arr[1] # = 3
my_arr[2] # = 5

# Traversal:
# my_arr => 1, 3, 5
for val in my_arr:
    print(val)

# range(0, 6) => 0, 1, 2, 3, 4, 5
for i in range(0, len(my_arr)):
    print(i + ". " + my_arr[i])

# Write: O(1) operation
    # A static array is fixed sized
my_arr[1] = 6

# In python, all lists are dynamic arrays
# C has static arrays
    # static array is stored on the stack
    # the stack CANNOT be modified by a program
    # the stack also contains program information
    # dynamic array is a pointer to the first
    # position of an allocated block of memory
    # inside of the heap, which CAN be modified
    # by a program using malloc(), realloc(), free()

# Insert at an empty is O(1)
# Insert between is NOT EFFICIENT
# Have to shift down the values
# [5, 6, X]
#  ->  ->
# [4, 5, 6]
#  ^ before 4 can be inserted, 5 & 6 have to be shifted
# Runtime? O(n) worst case, shifting all items in list