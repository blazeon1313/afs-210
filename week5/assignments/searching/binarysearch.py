def binsearch(sortedlist, target):
    low = 0
    high = len(sortedlist) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = sortedlist[mid]
        
        if mid_element == target:
            return True  
        elif mid_element < target:
            low = mid + 1  
        else:
            high = mid - 1  
    
    return False

sortedlist = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
mylist = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
wordlist = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

print(binsearch(sortedlist, 31))
print(binsearch(mylist, 77))
print(binsearch(wordlist, "Delta"))