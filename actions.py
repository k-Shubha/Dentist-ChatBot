from  __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa.core.events import SlotSet
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk import ActionExecutionRejection
import pandas as pd
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from typing import Dict, Text, Any, List, Union, Optional

class UserForm(FormAction):
     def name(self):
        return "usr_form"

     @staticmethod
     def required_slots(tracker: Tracker) -> List[Text]:
         """A list of required slots that the form has to fill"""
         return ["FirstName", "LastName","Mail","TelNumber"]
		 
     def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "FirstName": [self.from_entity(entity="FirstName")],
            "LastName": [self.from_entity(entity="LastName")],
            "Mail": [self.from_entity(entity="Mail")],
            "TelNumber": [self.from_entity(entity="TelNumber")]

        }
             
     def submit(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict]:
         """Define what the form has to do
             after all required slots are filled"""

         # utter submit template
         dispatcher.utter_template('utter_confirm_appointment_for', tracker)
         return []
print("out hello")


class sendAppointmentMessage(Action):
    print("in hello")
    def name(self):
        print("self hello")
        return 'action_send_apt_msg'

    def run(self,dispatcher,tracker,domain):
        print("run hello")
        sender_email = "shubhakarnam14@gmail.com"
        password = "gmail@2019"
        receiver_email = tracker.get_slot('Mail')
        print("receiver_email",receiver_email)
        FirstName = tracker.get_slot('FirstName')
        LastName = tracker.get_slot('LastName')
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.ehlo()
        s.starttls()
        s.login(sender_email,password)
        print("hello1")
        print( receiver_email,FirstName,LastName)
        message = MIMEMultipart("alternative")
		
        message["Subject"] = "Appointment Confirmation!"
        message["From"] = sender_email
        message["To"] = receiver_email

        msg = "Hi {FirstName} {LastName}, \n Your appointment to see Doctor {FirstName} is scheduled for {date} and {Time}. If you have any queries, please follow this link or call.\n Thank you. \n XYZ."
        text = MIMEText(msg, "plain")
        message.attach(text)
        print("hello2")
        # sending the mail
        receiver_id = "k.shubha434@outlook.com"
        s.sendmail(sender_email, receiver_id, message.as_string())

        response = "Message sent"
        dispatcher.utter_message(response)
        print("hello3")
        return []
        return[SlotSet('name',user_name)]
    
		
		
         

			
		 
	  