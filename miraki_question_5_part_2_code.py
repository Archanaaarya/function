# Question (Part 2)

# Ab ek check_numbers_list naam ka ek function likho jo inetgers ki list ko arguments ki tarah le aur fir check kare ki same index waale dono integers even hain ya nahi. Yeh check karne ke liye pichle Part 1 mein likhe check_numbers function ka use karo. Agar aapne apne function ko [2, 6, 18, 10, 3, 75] aur [6, 19, 24, 12, 3, 87] Toh usko yeh output deni chaiye:

def check_number_list(list1,list2):
    i = 0
    while i<len(list1):

        if list1[i]%2==0 and list2[i]%2==0:

            print("both this is even")

        elif list1[i]%2!=0 and list2[i]%2==0:

            print("only list2 is even and list1 is odd")

        elif list1[i]%2==0 and list2[i]%2!=0:

            print("only list1 is even and list2 is odd")

        else:

            print("both are odd")

        i=i+1

check_number_list([2,6,18,10,3,75],[6,19,24,12,3,87])
