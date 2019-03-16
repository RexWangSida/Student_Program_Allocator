## @file Read.py
#  @author Sida Wang
#  @brief This a module including the methods to read data from input.
#  @date Feb 11th 2019
from StdntAllocTypes import *
from DCapALst import *
from SALst import *
## @brief This function reads student information from input textfile and store them into student association list using SALst.add method.
#  @param s An input textfile including information of students, seperate line representing individual student.
def load_stdnt_data(s):
    SALst.init()
    with open(s, 'r') as stdnt_data:
	
        info = [[x.strip().strip('[').strip(']') for x in info.split(',')] for info in stdnt_data.readlines()]


        for individual in info:


            choices = []
            for new in individual[5:-1]:
                choices.append(DeptT(new))
            student_info = (str(individual[1]), str(individual[2]), GenT(individual[3]), float(individual[4]), SeqADT(choices), individual[-1] == "True")

            SALst.add(individual[0],student_info)
	

## @brief This function reads department information from input textfile and store them into department capacity association list using DCapALst.add method.
#  @param s An input textfile including capacity of departments, seperate line representing individual department.
def load_dcap_data(s):
    DCapALst.init()
    with open(s, 'r') as dept_capacity:

        data = dept_capacity.readlines()
    data = [x.strip().split(',') for x in data]
    for individual_program in data:
        DCapALst.add(DeptT(individual_program[0]),individual_program[1])

load_stdnt_data("StdntData.txt")
print(SALst.s)
load_dcap_data("DeptCap.txt")
print(DCapALst.s)


