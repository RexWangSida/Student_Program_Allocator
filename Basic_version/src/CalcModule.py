## @file CalcModule.py
#  @author Sida Wang
#  @brief This is the module for Assignment 1 Part 1 Step 2, which including three function: sort, average, and allocate
#  @date Jan 16th 2019

## @brief function sort
#  @details This function takes a list of dictionaries(individual dictionaries represent individual students) and returns a sorted list which is sorted by "gpa" values in the decending order
#  @param s a list of dictionaries(individual dictionaries represent individual students)
#  @return a sorted list which is sorted by "gpa" values in the decending order
def sort(S):
	
	
	return sorted(S, key = lambda a: a['gpa'], reverse = True)

## @brief function average
#  @details This function takes a list of dictionaries(individual dictionaries represent individual students) and a string of "gender", and returns an average of "gpa" for that specific "gender"
#  @param L a list of dictionaries(individual dictionaries represent individual students)
#  @param g a string represent specific "gender" ("male" or "female")
#  @return a double representing the "gpa" for that specific "gender"
def average(L, g):
	gpa = float(0);
	numbers = float(0);
	for i in L:
		if(i['gender'] == g ):
			numbers += float(1)
			gpa += i['gpa']
	if(numbers == 0):
		return 0
	else:
		result = float(gpa/numbers)
		return round(result, 4)


## @brief function allocate
#  @details This function takes a list of dictionaries(individual dictionaries represent individual students), a list of strings representing "students who are granted 'free choice'" and a dictionary including "program capacity", and returns a program allocation list for students
#  @param S a list of dictionaries(individual dictionaries represent individual students)
#  @param F a list of Strings representing "students who are granted 'free choice'"
#  @param C a dictionary including "program capacity
#  @return a program allocation list for students
def allocate(S, F, C):

	res_dic = {'civil' : [], 'chemical' : [], 'electrical' :[] , 'mechanical' :[], 'software' :[], 'materials' :[], 'engphys':[]}
	list_withoutBad = []
	#deteting those who have gpa < 4.0
	for i in S:
		gpa = i['gpa']
		if (gpa > 4.0):
			list_withoutBad.append(i)
	#dealing with free choice
	list_withoutFree = []

	for student in list_withoutBad:
		if (student["macid"] in F):
			hisprogram = student["choices"][0]
			res_dic[hisprogram].append(student)
			C[hisprogram] -= 1
		else:
			list_withoutFree.append(student)

	
	#sort the list_of_student having gpa >= 4.0 by function sort
	sorted_S = sort(list_withoutFree);



	#allocate the rest 
	for student in sorted_S:
		hisChoice = student['choices']
		hisprogram = hisChoice[0]
		if(C[hisprogram] == 0):
			hisprogram = hisChoice[1]
			if(C[hisprogram] == 0):
				hisprogram = hisChoice[2]
				temp_list = res_dic[hisprogram]
				temp_list.append(student)
				res_dic[hisprogram] = temp_list
				C[hisprogram] -= 1
				
			else:
				temp_list = res_dic[hisprogram]
				temp_list.append(student)
				res_dic[hisprogram] = temp_list
				C[hisprogram] -= 1
				sorted_S.remove(student)
				
		else:
			temp_list = res_dic[hisprogram]
			temp_list.append(student)
			res_dic[hisprogram] = temp_list
			C[hisprogram] -= 1

	return res_dic
				


		
	
