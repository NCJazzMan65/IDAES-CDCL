#------------------------------------------------------------------#
#                                                                  #
#           10 MW Coal Direct Chemical Looping Model               #
#                                                                  #
#------------------------------------------------------------------#
#
#  This is an IDAES model of a 10 MW coal direct chemical looping  #
#  plant.                                                          #
#                                                                  #
#------------------------------------------------------------------#
#                                                                  #
#  Author:  T.A. Fuller                                            #
#  Date:  5/21/2020                                                #
#                                                                  #
#  Revision: 1.0                                                   #
#  Revision Date:  5/21/2020                                       #
#                                                                  #
#------------------------------------------------------------------#

"""
Process flowheet model for a 10 MW CDCL plant
"""

# System imports
import sys
import os
import time

# Pyomo imports
from pyomo.environ import ConcreteModel, SolverFactory

# IDAES imports
