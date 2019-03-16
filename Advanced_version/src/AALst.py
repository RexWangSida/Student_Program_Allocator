## @file AALst.py
#  @author Sida Wang
#  @brief This a module including the methods to initialize and generate an allocation association list.
#  @date Feb 11th 2019

from StdntAllocTypes import *
#  @brief This class initializes and generates an allocation association list.
class AALst:
    ## A list of tuple representing a allocation of a department including department name and a list of students allocated to it.
    s = []  
    ## @brief This function initialize an allocation association list including all departments and no students allocated.
    @staticmethod
    def init():
        for d in DeptT:
            AllocAssocListT = (d,[])
            AALst.s.append(AllocAssocListT)
    ## @brief This function adds a student to department allocation list.
    #  @param dep A department represented by DepT types.
    #  @param m A string which represents the macid of a student.
    @staticmethod
    def add_stdnt(dep,m):
        for AllocAssocListT in AALst.s:
            if(AllocAssocListT[0] == dep):
                AllocAssocListT[1].append(m)
    ## @brief This function returns a list of macids that allocated in a department.
    #  @param d A department represented by DepT types.
    #  @return A list of macids representing the student allocations in a department.
    @staticmethod
    def lst_alloc(d):
        for AllocAssocListT in AALst.s:
            if (AllocAssocListT[0] == d):
                return AllocAssocListT[1]
    ## @brief This function returns a list of macids that allocated in a department.
    #  @param d A department represented by DepT types.
    #  @return An integer representing the number of student allocations in a department.
    @staticmethod
    def num_alloc(d):
        for AllocAssocListT in AALst.s:
            if (AllocAssocListT[0] == d):
                return len(AllocAssocListT[1])
