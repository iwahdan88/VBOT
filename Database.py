#!usr/bin/python

########################################################################################################################
#                                                                                                                      #
#       File Name:    Database.py                                                                                      #
#                                                                                                                      #
#       Author:       Islam Wahdan                                                                                     #
#                                                                                                                      #
#       Description:  Module to handel serialization/Retrieval of Members Data                                         #
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
import PyMySQL

class MemDataBase:
    """ Class for Handling Members Data """

    # Active Working Members Buffer
    ActiveMembers = []
    Admins = []

    def __init__(self):

        self.DbConnection = PyMySQL.connect(host='localhost', user='adminfBZBGAJ',
                                            password='9WhbQL6DcdlD', db='vbothome',
                                            charset='utf8mb4', cursorclass=PyMySQL.cursors.DictCursor)

    def __del__(self):
        # Close Connection
        self.DbConnection.close()

    def AddToDB(self, member):
        """
        :param member: Member Object
        :return: Boolean
        """
        try:
            cursor = self.DbConnection.cursor()
            # Create a new record
            sql = "INSERT INTO `users` (`FullName`, `IsAdmin`) VALUES (%s, %s)"
            cursor.execute(sql, (member.GetUserName(), member.GetAdminRights()))
            # Execute
            self.DbConnection.commit()
        finally:
            # Operation Unsuccessful
            return False
        # Operation Successful
        return True

    def RemoveFromDB(self, member):
        """

        :param member: Member Object
        :return: Boolean
        """
        try:
            cursor = self.DbConnection.cursor()
            # Create a new record
            sql = "DELETE FROM `bus_members` WHERE FullName = %s"
            cursor.execute(sql, (member.GetUserName()))
            # Execute
            self.DbConnection.commit()
        finally:
            # Operation Unsuccessful
            return False
        # Operation Successful
        return True
    def SearchDB(self, member):
        """

        :param member: Member Object
        :return: UCHAR
        """
        # Search in Working Buffer First
        if member.GetUserName() in MemDataBase.ActiveMembers:
            # Member Found
            return 1
        else:
            # Search DB
            try:
                cursor = self.DbConnection.cursor()
                # Create a new record
                sql = "SELECT * FROM `bus_members` WHERE `FullName`=%s"
                cursor.execute(sql, member.GetUserName())
                result = cursor.fetchone()
            finally:
                # Operation Unsuccessful
                return 255
            if result:
                return 1
            else:
                return 0

