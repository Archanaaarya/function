question_list=["what is the full form of KBC in programming?", "which company is the best for software engeneers ?", "Which course is taught in navgurukul?"]
option_list=[["1.kon banega cat", "2.kon banega carodpati", "3.kon banega coder ", "4.kon banega chor"],["1.twitter", "2.insta", "3.facebook", "4.google"],["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
answer_list5050=[3,4,1]
fifty_list=[['1.kon banega carodpati','3.kon banega coder'],['2.twitter','4.google'],['1.Software Engineering','2.Counseling']]
solution_list=[3,4,1]
lifelinecount = 0
print("WELCOME TO KAUN BANEGA CODER IT'S PRASENTED BY ARCHANA AARYA")
print("YEH RAHA AAPKA QUESTION AAPKI SCREEN PER")
def lifeline(index):  
    global lifelinecount
    j=0 
    if(lifelinecount==0): 
        while j<len(fifty_list[index]):
            print(j+1,fifty_list[index][j])
            j=j+1
        user_ans = int(input('Enter your answer'))
        lifelinecount+=1
        if user_ans==solution_list[index]:
            return True
        else:
            return False
    else:
        print('you Already used 5050')
        return "no"
        
def option(index):
    j=0
    while j<len(option_list[index]):
        print(j+1,option_list[index][j])
        j=j+1
    user_ans = int(input('Do you want 50-50'))
    if user_ans==answer_list5050[index]:
        return True
    if user_ans == 5050:
        return(lifeline(index))
    else:
        return False

def que():
    index=0
    while index<len(question_list):
        print("Q.",index+1,question_list[index],"?")
        result=option(index)
        if result=="no":
            index-=1
        elif result==True:
            print("CONGRAGULATION YOU WIN RS. 100000 ")
            print("OR YE RAHA AAPKA NEXT QUESTION AAPKI SCREEN PER")
        else:
            print("SORRY AAP IS GAME KO HAR CHUKE HE")
            break   
        index+=1

def main():
    que()
main()
print("CONGRAGULATION AAP IS GAME KO JEET CHUKE HE")        

