## @file testCalc.py
#  @author Sida Wang 
#  @brief 
#  @date Jan 17th 2019
from CalcModule import *
from ReadAllocationData import *


############Normal Test Start
print("#####################  This is Normal Test  #####################")
#Test for sort()
data = readStdnts('src/test_text1')
result_of_sort = sort(data)

result1 = [{'gpa': 12.0, 'gender': 'female', 'choices': ['mechanical', 'materials', 'engphys'], 'lname': 'Powell', 'fname': 'Emma', 'macid': 'powelle'}, {'gender': 'female', 'gpa': 11.4, 'choices': ['civil', 'software', 'engphys'], 'lname': 'Yang', 'fname': 'Laura', 'macid': 'yangl'}, {'gender': 'male', 'gpa': 10.8, 'choices': ['software', 'engphys', 'electrical'], 'lname': 'Liu', 'fname': 'Hongxiao', 'macid': 'liuh88'}, {'gender': 'male', 'gpa': 9.8, 'choices': ['software', 'civil', 'materials'], 'lname': 'Wang', 'fname': 'Sida', 'macid': 'wangs132'}, {'gender': 'female', 'gpa': 7.8, 'choices': ['mechanical', 'civil', 'chemical'], 'lname': 'Fu', 'fname': 'Anyi', 'macid': 'fua6'}, {'gender': 'male', 'gpa': 1.8, 'choices': ['mechanical', 'software', 'chemical'], 'lname': 'Zhang', 'fname': 'Shuming', 'macid': 'zhans22'}]

if(result1 == result_of_sort):
	print("Test for sort() pass")
else:
	print("Test for sort() fail")


#Test for average()
result_of_average = average(data,'male')
result2 = round(22.4/3.0, 4)
if(result_of_average == result2):
	print("Test for average() pass")
else:
	print("Test for average() fail")
#Test for allocate()
f = readFreeChoice('src/test_text2')
c = readDeptCapacity('src/test_text3')
result_of_allocate = allocate(data,f,c)
result3 = {'software' : [{'gender': 'male', 'gpa': 9.8, 'choices': ['software', 'civil', 'materials'], 'lname': 'Wang', 'fname': 'Sida', 'macid': 'wangs132'}, {'gender': 'male', 'gpa': 10.8, 'choices': ['software', 'engphys', 'electrical'], 'lname': 'Liu', 'fname': 'Hongxiao', 'macid': 'liuh88'}], 'mechanical' : [{'gpa': 12.0, 'gender': 'female', 'choices': ['mechanical', 'materials', 'engphys'], 'lname': 'Powell', 'fname': 'Emma', 'macid': 'powelle'}], 'civil' : [{'gender': 'female', 'gpa': 11.4, 'choices': ['civil', 'software', 'engphys'], 'lname': 'Yang', 'fname': 'Laura', 'macid': 'yangl'}], 'electrical' : [], 'materials' : [], 'engphys' : [], 'chemical' : [{'gender': 'female', 'gpa': 7.8, 'choices': ['mechanical', 'civil', 'chemical'], 'lname': 'Fu', 'fname': 'Anyi', 'macid': 'fua6'}]}

if(result3 == result_of_allocate):
	print("Test for allocate() pass")
else:
	print("Test for allocate() fail")
print("#####################  Normal Test End  #####################\n\n\n")
############Normal Test End








############Boundary Value Test Start
print("#####################  This is Boundary Value Test Test  #####################")
#Test for sort()
data = readStdnts('src/test_text4')
result_of_sort = sort(data)

result1 = []

if(result1 == result_of_sort):
	print("Test for sort() pass")
else:
	print("Test for sort() fail")


#Test for average()
result_of_average = average(data,'male')
result2 = round(0,3)
if(result_of_average == result2):
	print("Test for average() pass")
else:
	print("Test for average() fail")
#Test for allocate()
f = readFreeChoice('src/test_text4')
c = readDeptCapacity('src/test_text4')
result_of_allocate = allocate(data,f,c)
result3 = {'engphys': [], 'civil': [], 'chemical': [], 'materials': [], 'electrical': [], 'mechanical': [], 'software': []}


if(result3 == result_of_allocate):
	print("Test for allocate() pass")
else:
	print("Test for allocate() fail")
print("#####################  Boundary Value Test End  #####################\n\n\n")
############Boundary Value Test End






############Reliability Test Start
print("#####################  This is Program Reliability Test  #####################\n\n\n")
test_code = 0;
for i in range(1000):
	#Test for sort()
	data = readStdnts('src/test_text1')
	result_of_sort = sort(data)

	result1 = [{'gpa': 12.0, 'gender': 'female', 'choices': ['mechanical', 'materials', 'engphys'], 'lname': 'Powell', 'fname': 'Emma', 'macid': 'powelle'}, {'gender': 'female', 'gpa': 11.4, 'choices': ['civil', 'software', 'engphys'], 'lname': 'Yang', 'fname': 'Laura', 'macid': 'yangl'}, {'gender': 'male', 'gpa': 10.8, 'choices': ['software', 'engphys', 'electrical'], 'lname': 'Liu', 'fname': 'Hongxiao', 'macid': 'liuh88'}, {'gender': 'male', 'gpa': 9.8, 'choices': ['software', 'civil', 'materials'], 'lname': 'Wang', 'fname': 'Sida', 'macid': 'wangs132'}, {'gender': 'female', 'gpa': 7.8, 'choices': ['mechanical', 'civil', 'chemical'], 'lname': 'Fu', 'fname': 'Anyi', 'macid': 'fua6'}, {'gender': 'male', 'gpa': 1.8, 'choices': ['mechanical', 'software', 'chemical'], 'lname': 'Zhang', 'fname': 'Shuming', 'macid': 'zhans22'}]

	if(result1 != result_of_sort):
		print("Test for sort() fail")
		test_code += 1



	#Test for average()
	result_of_average = average(data,'male')
	result2 = round(22.4/3.0, 4)
	if(result_of_average != result2):
		print("Test for average() fail")
		test_code += 1

	#Test for allocate()
	f = readFreeChoice('src/test_text2')
	c = readDeptCapacity('src/test_text3')
	result_of_allocate = allocate(data,f,c)
	result3 = {'software' : [{'gender': 'male', 'gpa': 9.8, 'choices': ['software', 'civil', 'materials'], 'lname': 'Wang', 'fname': 'Sida', 'macid': 'wangs132'}, {'gender': 'male', 'gpa': 10.8, 'choices': ['software', 'engphys', 'electrical'], 'lname': 'Liu', 'fname': 'Hongxiao', 'macid': 'liuh88'}], 'mechanical' : [{'gpa': 12.0, 'gender': 'female', 'choices': ['mechanical', 'materials', 'engphys'], 'lname': 'Powell', 'fname': 'Emma', 'macid': 'powelle'}], 'civil' : [{'gender': 'female', 'gpa': 11.4, 'choices': ['civil', 'software', 'engphys'], 'lname': 'Yang', 'fname': 'Laura', 'macid': 'yangl'}], 'electrical' : [], 'materials' : [], 'engphys' : [], 'chemical' : [{'gender': 'female', 'gpa': 7.8, 'choices': ['mechanical', 'civil', 'chemical'], 'lname': 'Fu', 'fname': 'Anyi', 'macid': 'fua6'}]}

	if(result3 != result_of_allocate):

		print("Test for allocate() fail")
		test_code += 1
if(test_code != 0):
	print("Program Reliability Test Fail\n\n\n")
else: 
	print("Program Reliability Test Pass\n\n\n")
print("#####################  Program Reliability Test End  #####################\n\n\n")
############Reliability Test End

