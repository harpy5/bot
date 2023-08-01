import importlib
import sys
from webex_bot.webex_bot import WebexBot
from webex_bot.commands.echo import EchoCommand
from labdevices import DevicesByHostname, RegisterDevice
from subnets import SubnetByVlan
from hyperflex import GetHyperflexAlarms
from deployLab import DeployLab
from runcommand import GetCommand

api_token = ""

bot = WebexBot(api_token, approved_domains=["cisco.com"], approved_users=["hsingh5@cisco.com"])

bot.add_command(SubnetByVlan())    # Search any subnet by Vlan
bot.add_command(DevicesByHostname()) # Search Device by hostname
bot.add_command(RegisterDevice()) # Add Device 
bot.add_command(GetHyperflexAlarms()) # Get Hyperflex Alarms
bot.add_command(DeployLab())
bot.add_command(EchoCommand())
bot.add_command(GetCommand())
bot.run()
