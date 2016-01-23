#!usr/bin/python

########################################################################################################################
#                                                                                                                      #
#       File Name:    Member.py                                                                                        #
#                                                                                                                      #
#       Author:       Islam Wahdan                                                                                     #
#                                                                                                                      #
#       Description:  Class Defining a Bus Member and all his/her attributes                                           #
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
import Defs

class BusMember:
    """Class Defining a Typical Bus Member"""

    def __init__(self, username, memtype, status):
        """
        :type username: String
        :type memtype: MembershipType
        :type status: TripRegStatusject
        """
        self.UserName = username
        self.MemType = memtype
        self.TripStatus = status


