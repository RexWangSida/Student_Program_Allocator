## @file ReadAllocationData.py
#  @author Sida Wang
#  @brief This is the module for Assignment 1 Part 1 Step 1, which including three functions : readStdnts, readFreeChoice, and readDeptCapacity
#  @date Jan 14th 2019

## @brief function readStdnts
#  @details This function takes a String input(which is the input filename) and returns a list of dictionaries(individual dictionaries represent individual students)
#  @param s a String input representing the input filename
#  @return a list of dictionaries(individual dictionaries represent individual students)
def readStdnts(s):
	
	data = []
	#counting how many students
	num_of_lines = 0
	
	line_count = open(s,"r")

	for line in line_count:

    		num_of_lines += 1

  	line_count.close()

 

 	info = open(s,"r")

	num_of_student = num_of_lines/8
	#provide infomation with students
	for individual in range(num_of_student):

		student = {}

		content = info.readline()
		new_content = content.strip()

		student['macid'] = new_content

		content = info.readline()
		new_content = content.strip()

		student['fname'] = new_content

		content = info.readline()
		new_content = content.strip()

		student['lname'] = new_content

		content = info.readline()
		new_content = content.strip()

		student['gender'] = new_content

		content = info.readline()
		new_content = content.strip()

		gpa = float(new_content)

		student['gpa'] = gpa

		choices = []

		for i in range(3):

 		        content = info.readline()
			new_content = content.strip()

          		choices.append(new_content)

		student['choices'] = choices

    		data.append(student)

 

	info.close()
	return data

 

## @brief function readFreeChoice
#  @details This function takes a String input(which is the input filename) and returns a list of Strings(individual Strings represent individual students who are granted "freechoice")
#  @param s a String input representing the input filename
#  @return a list of Strings(individual Strings represent individual students who are granted "freechoice")

def readFreeChoice(s):

	data = []
	#counting how many students
	num_of_lines = 0
	line_count = open(s,"r")
	for line in line_count:

    		num_of_lines += 1

  	line_count.close()

	student_num = num_of_lines / 2
	#adding students with "free choice" to list
	info = open(s,"r")
	for i in range(student_num):
		name = info.readline()
		new_name = name.strip()
		eligibility = info.readline()
		new_eligibility = eligibility.strip()
		if(new_eligibility == "Y"):
			data.append(new_name)
	info.close()
	return data

## @brief function readDeptCapacity
#  @details This function takes a String input(which is the input filename) and returns a dictionary with its keys representing "Programs" and values representing "Capacities"
#  @param s a String input representing the input filename
#  @return a dictionary with its keys representing "Programs" and values representing "Capacities"


def readDeptCapacity(s):
	
	data = {}
	#couting how many programs
	num_of_lines = 0
	line_count = open(s,"r")
	for line in line_count:

    		num_of_lines += 1

  	line_count.close()
	dept_number = num_of_lines / 2
	#link capacity with program
	info = open(s,"r")
	for i in range(dept_number):
		name = info.readline()
		new_name = name.strip()
		capacity = info.readline()
		new_capacity = capacity.strip()
		data[new_name] = int(new_capacity)
	info.close()
	return data
