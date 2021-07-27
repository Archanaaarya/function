# Q2. Aapko sum function ka use krke di hue list ke element ka sum print krvana hai. Input
 
numbers = [1, 2, 3, 4, 5] 

print(sum(numbers))

# or

numbers = [1, 2, 3, 4, 5] 

i = 0

sum = 0

while i<len(numbers):

    sum = numbers[i]+sum

    i = i+1

print(sum)

