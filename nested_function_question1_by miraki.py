# Question number
# eligible_for_vote name ka function likho jo ki user ko bataye ki vo (he/she) vote de sakta hai ya nahi. ( Consider minimum age of voting to be 18. ) Example:- Agar user input me 18 se kam deta hai to “not eligible “ print kare aur agar user 18 ya 18 se jyaada input kare to “you are eligible” print kare. 

def age(my_age):
    if my_age>=18:
        print("she/he is eligible to giving vote")
    else:
        print("she/he is not eligible to giving vote")
my_age=int(input("Enter the age:"))
age(my_age)