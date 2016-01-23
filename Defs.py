#!usr/bin/python

########################################################################################################################
#                                                                                                                      #
#       File Name:    Defs.py                                                                                          #
#                                                                                                                      #
#       Author:       Islam Wahdan                                                                                     #
#                                                                                                                      #
#       Description:  File Containing Type definitions and Defines for the project                                     #
#                                                                                                                      #
#       Language:     Python                                                                                           #
#                                                                                                                      #
########################################################################################################################
#                                                                                                                      #
#                                               History Description                                                    #
#                                                                                                                      #
########################################################################################################################
#                                                                                                                      #
#   Version: 1.0                                                                                                       #
#       Initial Revision                                                                                               #
# -------------------------------------------------------------------------------------------------------------------- #

from enum import Enum

# Enum Defining Bus Members Types
MembershipType = Enum('Regular', 'Irregular')
# Enum Defining Member's Registration status to a Trip
TripRegStatus = Enum('UNKNOWN', 'CONFIRMED', 'REJECTED')
# Member Data Directory
DATADIR = "C:/BusMembersData"
