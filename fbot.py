from fbchat import log, Client
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.parse.generate import generate, demo_grammar
from nltk import CFG
from fbchat.models import *


# Subclass fbchat.Client and override required methods
class EchoBot(Client):
	def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
		self.markAsDelivered(thread_id, message_object.uid)
		self.markAsRead(thread_id)

		log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
		log.info(message_object.text)

		# If you're not the author, echo
		if author_id != self.uid:
			grammar = CFG.fromstring(demo_grammar)
			self.send(Message(text=generate(grammar, depth=14)), thread_id=thread_id, thread_type=thread_type)
			self.send(Message(text='Chao'), thread_id=thread_id, thread_type=thread_type)
client = EchoBot("vladimirov_vladi@yahoo.com", "Test1234qwerty")
client.listen()


