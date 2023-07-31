
from webex_bot.models.command import Command
import logging
import requests
import json
from webex_bot.models.response import Response
from adaptivecardbuilder import * 


with open("cards/initial_card.json", "r") as card:
    INPUT_CARD = json.load(card)
    print(INPUT_CARD)

with open("cards/lab-setup-card.json", "r") as card:
    LAB_INPUT_CARD = json.load(card)
    print(LAB_INPUT_CARD)   

log = logging.getLogger(__name__)

class InitialRequest(Command):
    def __init__(self):
        super().__init__(
            command_keyword="services",
            help_message="Get the list of services offered by SE lab.",
            card=INPUT_CARD,
        )
    
    def execute(self, message, attachment_actions, activity):

        # card_data = json.loads(INPUT_CARD)
        #print(card_data)
        
        #card_payload = {
         #   "contentType": "application/vnd.microsoft.card.adaptive",
          #  "card": INPUT_CARD,
        #}
        selectd_input = attachment_actions.inputs['choice']

        print(selectd_input)

        if selectd_input == "1":
            print("_____ Set up a new lab _______")
            card_payload = {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content": LAB_INPUT_CARD
            }

        
            response = Response()
            response.text = "Test card"
            response.attachments = card_payload

            print(response)

            return [response]

class AddNewLab(Command):
    def __init__(self):
        super().__init__(
            command_keyword="addnewlab",
            help_message="Add new lab",
        )
    def execute(self, message, attachment_actions, activity):
         Num_of_devices = attachment_actions.inputs['Num_of_devices']
         Num_of_IPs = attachment_actions.inputs['Num_of_IPs']
         Status = attachment_actions.inputs['Status']
         VMs = attachment_actions.inputs['VMs']
         description = attachment_actions.inputs['description']
        # print(Person)
         print(Num_of_IPs)
         print(Num_of_devices)
         print(Status)
         print(VMs)
         card = AdaptiveCard()
         card.add(TextBlock(text="Lab details"))
         card.add(ColumnSet())
         card.add(Column(width="stretch"))
         card.add(FactSet())
         card.add(Fact(title="Number of devices", value=f"{Num_of_devices}"))
         card.add(Fact(title="Number of IPs", value=f"{Num_of_IPs}"))
         card.add(Fact(title="Status", value=f"{Status}"))
         card.add(Fact(title="VMs", value=f"{VMs}"))
         card.add(Fact(title="Description", value=f"{description}"))

         card_data = json.loads(asyncio.run(card.to_json()))
            #print(card_data)

         card_payload = {
                "contentType": "application/vnd.microsoft.card.adaptive",
                "content" : card_data
            }
         print(card_payload)

         response = Response()
         response.text = "Test card"
         response.attachments = card_payload

         print(response)

         return [response]
            