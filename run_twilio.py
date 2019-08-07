from rasa.core.channels import HttpInputChannel
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa_twilio_connector import TwilioInput

print("initial")
nlu_interpreter = RasaNLUInterpreter('./models/20190720-123019/nlu')
agent = Agent.load('./models/20190720-123019/core', interpreter = nlu_interpreter)
print("before")
input_channel = TwilioInput('ACf11ed3930668c68e3ea357bb6543902e',
						'012d8bd5856136d5fac10fc05514bd1d',
						#'012d8bd5856136d5fac10fc05514bd',
						'+13367938385')

print(input_channel)
agent.handle_channels(HttpInputChannel(5500,input_channel))
