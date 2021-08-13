question_list = [
    "Question 1. How many continents are there?",              
    "Question 2. What is the capital of India?",            
    "Question 3. NG mei kaun se course padhaya jaata hai?",
    "Question 4. NG mai F.M kon he?",
    "Question 5. NG mai Disco post par kon hai",
    "Question 6. NG mai jo cource padhaya jata he vo kitne years mai khatm hota hai?",
    "Question 7. NG mai archana aarya kis post par hai",
    "Question 8. NG mai kitne rooms he",
    "Question 9. NG mai abhi kitne students he",
    "Question 10. NG mai laptop kya karne ke bad milta he"  
]

options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal= ", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],
    ["rohini","Archana aarya","sharda suman","lucky"],
    ["rohini","Archana aarya","sharda suman","lucky"],
    ["1 years","2 years","2.5 years","1.5 years"],
    ["Disco","F.M","health coordinator","F.C"],
    ["2","16","12","2"],
    ["70","45","80","30"],
    ["Fuction ke baad","loop ke baad","if else ke baad","files ke baad"],

]
fiftyfifty=[['four','seven'],
['Delhi','Bhopal'],
['Tourism','software engineering'],
['Archana aarya','sharda'],
['rohini','Archana aarya'],
['1 years','1.5 years'],
['F.M','F.C'],
['16','12'],
['70','80'],
['loop ke baad','function ke baad']
]

# har ek question ke liye, uski solution key (yeh index nahi hai)
solutions=[2,1,2,1,2,2,1,1,2,2]
solution_list = [3, 4, 1, 2, 1, 4, 2, 2, 3, 1] 

print("Co-Powered by ARCHANA AARYA presents,KAUN BANEGA CARODPATI mein apka swagat hai!!")
print("Sadab,Aadab aur Shastriyakal.")
print("Pehla Question yeh rha apke screen ke upar:")
i= 0
c= 0
while i<len(question_list):
	print('your question is')
	print(i+1,question_list[i])
	
	a= 0
	while a<=len(options_list):
		print(a+1,options_list[i][a])
		a= a+1
	j= int(input('enter solution'))
	if j==solution_list[i]:
			print('congrats')
	elif j==5050:
		if c==0:
			m = 0
			while m<len(fiftyfifty[i]):
				print(m+1,fiftyfifty[i][m])
				m = m+1
			c = c+1
			num = int(input('enter no.'))
			if num==solutions[i]:
				print('correct')
			else:
				print('your option is wrong')
				print('quit')

		else:
			print('you used 5050 lifeline')
			num1= int(input('enter your option'))
			if num1==solution_list[i]:
				print('congrats,ap jeet gye 10000 rupaiye')
				break
			else:
				print('your option is wrong')
				break
	else:
				print('your answer is wrong')
				print('quit')
				break
	i= i+1