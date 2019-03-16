## @file DCapALst.py
#  @author Sida Wang
#  @brief This a module including the methods to initialize and generate a department capacity association list.
#  @date Feb 11th 2019

from StdntAllocTypes import *
## @brief This class initializes and generates a department capacity association list.
class DCapALst:
    ## A set of tuples including a department name and its capacity.
    s = set()

    ## @brief This function initialize an empty department capacity association list.
    @staticmethod
    def init():
        DCapALst.s = set()

    ## @brief This function adds a tuple of department with its capacity to department capacity association list if that department does not exist in the list.
    #  @param d A department represented by DepT types.
    #  @param n The capacity of the department.
    @staticmethod
    def add(d,n):
        for x in DCapALst.s:
            if (x[0] == d):
                raise KeyError

        new_set = {(d,n)}
        merge = new_set.union(DCapALst.s)
        DCapALst.s = merge
		
    ## @brief This function removes the tuple of department with its capacity from department capacity association list if that department exists in the list.
    #  @param d A department represented by DepT types.	
    @staticmethod
    def remove(d):
        exist = 0
        for x in DCapALst.s:
            if(x[0] == d):
                new_set = x
                exist += 1
        if(exist != 0):
            dif = DCapALst.s - {new_set}
            DCapALst.s = dif
        else:
            raise KeyError

    ## @brief This function checks if a tuple of department with its capacity is in department capacity association list.
    #  @param d A department represented by DepT types.	
    #  @return A boolean which True stands for existence and False stands for non-existence. 
    @staticmethod	
    def elm(d):
        for x in DCapALst.s:
            if(x[0] == d):
                return True
        return False
    ## @brief This function returns the capacity of a department if that department exists in the list
    #  @param d A department represented by DepT types.
    #  @return An integer representing the capacity of a department.
    @staticmethod
    def capacity(d):
        for x in DCapALst.s:
            if(x[0] == d):
                return x[1]
        raise KeyError
		
