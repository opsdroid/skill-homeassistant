import json
import logging

from aiohttp.web import Request

from opsdroid.matchers import match_webhook
from opsdroid.message import Message


_LOGGER = logging.getLogger(__name__)


@match_webhook("notify")
async def notify(opsdroid, config, message):
    if type(message) is not Message and type(message) is Request:

        # Capture the request POST data
        request = await message.post()

        # Set message to a default message
        message = Message("",
                          None,
                          config.get("room", opsdroid.default_connector.default_room),
                          opsdroid.default_connector)

        # Respond with message from homeassistant
        await message.respond(request["message"])