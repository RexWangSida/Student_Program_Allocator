## @file SALst.py
#  @author Sida Wang
#  @brief This a module including the methods to initialize and generate a student association list.
#  @date Feb 11th 2019

from StdntAllocTypes import *
from AALst import *
from DCapALst import *
#  @brief This class initializes and generates a student association list.
class SALst:
    ## A set of tuple representing a student with macid and information.
    s = set()
    ## @brief This function initialize an empty student association list.
    @staticmethod
    def init():
        SALst.s = set()

    ## @brief This function adds a tuple representing a student to student association list.
    #  @param m A string which represents the macid of a student.
    #  @param i A namedtuple representing a student information of the type SInfoT.
    @staticmethod
    def add(m,i):
        for x in SALst.s:
            if(x[0] == m):
                raise KeyError

        StudentT = (m,i)
        new_set = {StudentT}
        merge = SALst.s.union(new_set)
        SALst.s = merge

    ## @brief This function removes a tuple representing a student from student association list if it exists in the list.
    #  @param m A string which represents the macid of a student.
    @staticmethod
    def remove(m):
        exist = 0
        for StudentT in SALst.s:
            if(StudentT[0] == m):
                exist += 1
        if(exist != 0):
            dif = SALst.s - {StudentT}
            SALst.s = dif
        else:
            raise KeyError

    ## @brief This function checks if a tuple of representing a student is in student association list.
    #  @param m A string which represents the macid of a student.	
    #  @return A boolean which True stands for existence and False stands for non-existence.
    @staticmethod 
    def elm(m):
        for StudentT in SALst.s:
            if(StudentT[0] == m):
                return True
        return False

    ## @brief This function returns the information of a student if that student exists in the list.
    #  @param m A string which represents the macid of a student.	
    #  @return A namedtuple representing a student information of the type SInfoT.
    @staticmethod
    def info(m):
        for StudentT in SALst.s:
            if(StudentT[0] == m):
                return StudentT[1]
        raise KeyError
    
    ## @brief This function returns a list of strings representing macids and the list is sorted based on students' gpa.
    #  @param f A function to qualify a student.
    #  @return A sorted list of strings representing macids.
    @staticmethod
    def sort(f):
        def get_gpa(m,s):
            for StudentT in s:
                if(StudentT[0] == m):
                    return StudentT[1].gpa
        L = []
        for StudentT in SALst.s:
            if(f(StudentT[1])):
                L.append(StudentT[0])
        return sorted(L, key = lambda i : get_gpa(i, SALst.s), reverse = True)

    ## @brief This function returns an average gpa for a certain gender.
    #  @param f A function to qualify a student.
    #  @return An average gpa for a certain gender.			
    @staticmethod
    def average(f):
        sum_all = 0.0
        fset_length = 0.0
        for StudentT in SALst.s:
            if(f(StudentT[1])):
                fset_length += 1.0
                sum_all += StudentT[1].gpa
        if(fset_length == 0.0):
            raise ValueError

        return (sum_all/fset_length)

    ## @brief This function allocates students to departments based on the 'free choice', their rank in sorted list and department capacity
    #  @details This function first initializes an allocation association list, and calls sort function to get a sorted list of who have been granted 'free choice' and gpa greater than or equal to 4.0, then allocate them to departments based on their rank in list. After that, it calls sort function to get a sorted list of who have not been granted 'free choice' and gpa greater than or equal to 4.0, then allocate them to departments based on their rank in list.
    @staticmethod
    def allocate():
        AALst.init()
        F = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for m in F:
            ch = SALst.info(m).choices
            AALst.add_stdnt(ch.next(), m)
	
        S = SALst.sort(lambda t: not t.freechoice and t.gpa >= 4.0)
        for m in S:
            ch = SALst.info(m).choices
            alloc = False
            while(not alloc and not ch.end()):
                d = ch.next()
                if(AALst.num_alloc(d) < DCapALst.capacity(d)):
                    AALst.add_stdnt(d,m)
                    alloc = True
            if(not alloc):
                raise RuntimeError

