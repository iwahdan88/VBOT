#!usr/bin/python

########################################################################################################################
#                                                                                                                      #
#       File Name:    Application.py                                                                                   #
#                                                                                                                      #
#       Author:       Islam Wahdan                                                                                     #
#                                                                                                                      #
#       Description:  Application Handling User Interactions                                                           #
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
import Member
import Database
import telepot
import json

MyBot = telepot.Bot("102176437:AAFufVB0sWxKhJn34Mo8EmyOSJjeUb436WM")

def application(environ, start_response):

    if environ['REQUEST_METHOD'] == 'POST':

        ctype = 'text/html'
        rawdata = environ['wsgi.input'].read()
        DecaodedData = json.load(rawdata)
        ChatID = DecaodedData['chat']
        FirstName = DecaodedData['first_name']
        Lastname = DecaodedData['last_name']
        MessageID = DecaodedData['message_id']

        MyBot.sendMessage(chat_id=ChatID, text="ACKNOLEDGE", reply_to_message_id=MessageID)

    response_body = "OK"
    response_body = response_body.encode('utf-8')

    status = '200 OK'
    response_headers = [('Content-Type', ctype), ('Content-Length', str(len(response_body)))]
    #
    start_response(status, response_headers)
    return [response_body]
