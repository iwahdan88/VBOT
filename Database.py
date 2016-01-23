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
import io
import xml

class MemDataBase:
    """ Class for Handling Members Data """

    # Active Working Members Buffer
    ActiveMembers = []

    def SerilaizeMember(self, member):
        """
        :param member:
        :return: bool
        """
        