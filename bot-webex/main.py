import importlib
import sys
from webex_bot.webex_bot import WebexBot
from webex_bot.commands.echo import EchoCommand
from Initial_message import InitialRequest, AddNewLab
import os

api_token = os.environ.get('API_TOKEN')
print(api_token)
bot = WebexBot(api_token, approved_domains=["cisco.com"], approved_users=["hsingh5@cisco.com"])

bot.add_command(EchoCommand())
bot.add_command(InitialRequest())
bot.add_command(AddNewLab())
bot.run()