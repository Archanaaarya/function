
def my_list(list):
    sum=0
    i=0
    while i<len(list):
        if list[i]%2==0:
            sum=sum+list[i]
        i=i+1
    print(sum)
list=[2,4,3,1,2,3,2,3]
my_list(list)