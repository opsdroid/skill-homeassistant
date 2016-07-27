from opsdroid.skills import match_regex
import logging
import random

def setup(opsdroid):
    logging.debug("Loaded hello module")

@match_regex(r'hi|hello|hey|hallo')
def hello(opsdroid, message):
    message.message = random.choice(["Hi {}", "Hello {}", "Hey {}"]).format(message.user)
    message.respond(message)

@match_regex(r'bye( bye)?|see y(a|ou)|au revoir|gtg|I(\')?m off')
def goodbye(opsdroid, message):
    message.message = random.choice(["Bye {}", "See you {}", "Au revoir {}"]).format(message.user)
    message.respond(message)
