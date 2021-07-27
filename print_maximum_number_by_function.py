# Q1 . Aapko max function ka use krke di hue list me se sbse bada value print krvani hai. Input
 
numbers = [3, 5, 7, 34, 2, 89, 2, 5] 

max = max(numbers)

print(max)

#  or

numbers = [3, 5, 7, 34, 2, 89, 2, 5] 

max = 0

index = 0

while index < len(numbers):

    if numbers[index] > max:

        max = numbers[index]

    index = index + 1
    
print(max)



# or    


numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]

print (max(numbers_list)) 



