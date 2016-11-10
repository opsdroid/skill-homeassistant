from opsdroid.skills import match_regex
import logging
import random

def setup(opsdroid):
    logging.debug("Loaded hello module")

@match_regex(r'hi|hello|hey|hallo')
async def hello(opsdroid, message):
    text = random.choice(["Hi {}", "Hello {}", "Hey {}"]).format(message.user)
    await message.respond(text)

@match_regex(r'bye( bye)?|see y(a|ou)|au revoir|gtg|I(\')?m off')
async def goodbye(opsdroid, message):
    text = random.choice(["Bye {}", "See you {}", "Au revoir {}"]).format(message.user)
    await message.respond(text)
