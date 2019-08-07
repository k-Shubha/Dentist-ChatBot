from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/doctornlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-384335543633-511091822530-642038309238-e943deb5e9b5496d48c46b2558c99f02', #app verification token
							'xoxb-384335543633-642038311398-a7Q5hnmtNS96V0mzo41herzn', # bot verification token
							'tBlWb7GkLm03xfcTMaJC9KR4', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
