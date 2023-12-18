import random
import time

def shuffle(list):

    n = len(list)
    
    # Time Complexity: O(n)
    for i in range(n - 1, 0, -1):
        # Generate a random index between 0 and i (inclusive)
        j = random.randint(0, i)
        
        # Swap the elements at positions i and j
        list[i], list[j] = list[j], list[i]





list_input = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print("Before shuffle:")
print(list_input)

# Measure the execution time 
start_time = time.time()
shuffle(list_input)
end_time = time.time()

print("Shuffled:")
print(list_input)

print(f"Shuffling time: {end_time - start_time} seconds")

#Time Complexity: O(n) indicates that the time complexity of the shuffle function is linear, 
# where "n" is the length of the input list. 
# This is because the loop iterates over each element of the list, 
# performing constant-time operations in each iteration.