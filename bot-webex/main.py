import importlib
import sys
from webex_bot.webex_bot import WebexBot
from webex_bot.commands.echo import EchoCommand
from Initial_message import InitialRequest, AddNewLab

api_token = "NzkzMWFkMDMtZGFlNS00NGQ3LThlYjAtZDVlZGI0Y2FkYmM1NDk1OTNmZDYtODhh_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"

bot = WebexBot(api_token, approved_domains=["cisco.com"], approved_users=["hsingh5@cisco.com"])

bot.add_command(EchoCommand())
bot.add_command(InitialRequest())
bot.add_command(AddNewLab())
bot.run()