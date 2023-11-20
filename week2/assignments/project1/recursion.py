
def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

def loop1Rec(num, odd_sum):
    # Duplicate the loop1 function using recursion
    if num > odd_sum:
        return 0
    else:
        return num + loop1Rec(num + 2, odd_sum)

loop1Num = 1
odd_sum = 20
    
def loop2Rec(num,even_sum):
    # Duplicate the loop2 function using recursion
    if num >= even_sum: 
        return 0
    else:
        return num + loop2Rec(num + 2, even_sum)

loop2Num = 0
even_sum = 20
    
print(f"Sum of odds between 1 and 20 using 'for' loop = {loop1()}")
print(f"Sum of odds between 1 and 20 using recursion = {loop1Rec(loop1Num,odd_sum)}")
print(f"Sum of evens between 1 and 20 using 'while' loop = {loop2()}")
print(f"Sum of evens between 1 and 20 using recursion = {loop2Rec(loop2Num,even_sum)}")
