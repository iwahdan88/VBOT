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

    def __init__(self, username, memtype, status, admin):
        """
        :type username: String
        :type memtype: MembershipType
        :type status: TripRegStatusject
        :type admin: boolean
        """
        self.UserName = username
        self.MemType = memtype
        self.TripStatus = status
        self.IsAdmin = admin

    def GetUserName(self):
        """

        :return: String
        """
        return self.UserName

    def GetMemType(self):
        """

        :return: Defs.MembershipType
        """
        return self.MemType

    def GetTripStatus(self):
        """

        :return: Defs.TripRegStatus
        """
        return self.TripStatus

    def GetAdminRights(self):
        """

        :return: Boolean
        """
        return self.IsAdmin

    def SetUserName(self, user):
        """

        :param user: User name
        :return: None
        """
        self.UserName = user

    def SetMemType(self, memtype):
        """

        :param memtype: Membership Type
        :return: None
        """
        self.MemType = memtype

    def SetTripStatus(self, status):
        """

        :param status: Member Trip Status
        :return: None
        """
        self.TripStatus = status

    def SetAdmin(self, admin):
        """

        :param admin: Member Admin Rights
        :return: None
        """
        self.IsAdmin = admin
