## @file StdntAllocTypes.py
#  @author Sida Wang
#  @brief This a generic module defines an abstract data type.
#  @date Feb 11th 2019

#  @brief This class represents a Sequence ADT.
class SeqADT:

## @brief This is the constructor of Sequence ADT.
#  @details Constructor accpets one parameter, a sequence of departments represented by DepT.
#  @param x A sequence of departments represented by DepT.
	def __init__(self, x):
		self.s = x
		self.i = 0

## @brief This function sets the index to zero 
	def start(self):
		self.i = 0

## @brief This function increments the index number by one
#  @return The department at the present index
	def next(self):
		if(self.i >= len(self.s)):
			raise StopIteration
		self.i = self.i + 1
		return self.s[self.i-1]

## @brief This function determine if the iteration is over
#  @return A boolean to determine if the iteration is over
	def end(self):
		return (self.i>=len(self.s))	


	
