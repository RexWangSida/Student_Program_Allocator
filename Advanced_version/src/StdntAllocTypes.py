
## @file StdntAllocTypes.py
#  @author Sida Wang
#  @brief This module generates the templates for data types including enumerations GenT & DeptT and namedtuple SInfoT.
#  @date Feb 11th 2019
from SeqADT import *
from enum import Enum
from typing import NamedTuple
#  @brief This class defines an enumeration named GenT which defines gender type.
class GenT(Enum):
    male = "male"
    female = "female"
#  @brief This class defines an enumeration named DeptT which defines department type.
class DeptT(Enum):
    civil = "civil"
    chemical = "chemical"
    electrical = "electrical"
    mechanical = "mechanical"
    software = "software"
    materials = "materials"
    engphys = "engphys"
#  @brief This class defines an namedtuple named SInfoT, each model of this structure stands for an individual student.
class SInfoT(NamedTuple):
    fname: str
    lname: str
    gender: GenT
    gpa: float
    choices: SeqADT
    freechoice: bool
