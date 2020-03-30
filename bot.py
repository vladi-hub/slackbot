import time
import event
from slackclient import SlackClient


 
class Bot(object):
	def __init__(self):
		self.slack_client = SlackClient("xoxb-2154537752-538739924402-2NWNlGQpRI8RKWK5j3eINNks")
		self.bot_name = "pscoektbot"
		self.bot_id = self.get_bot_id()
         
		self.event = event.Event(self)
		self.listen()
     
	def get_bot_id(self):
		channels = self.slack_client.api_call("channels.list")
		channel_id = None
		for channel in channels['channels']:
			if channel['name'] == 'testpscoebot':
				channel_id = channel['id']
				print("Channel id - " + channel_id)
				history = slack_client.api_call("channels.history", channel=channel_id, oldest=oldest, latest=latest)
				for message in history['messages']:
					print(message.text)
             
	def listen(self):
		if self.slack_client.rtm_connect(with_team_state=False):
			print ("Successfully connected, listening for commands")
			while True:
				self.event.wait_for_event()
                 
				time.sleep(1)
		else:
			exit("Error, Connection Failed")