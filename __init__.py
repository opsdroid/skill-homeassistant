import json
import logging

from aiohttp.web import Request

import requests
from urllib.parse import urljoin

from opsdroid.matchers import match_webhook, match_regex, match_always
from opsdroid.message import Message


_LOGGER = logging.getLogger(__name__)


@match_always()
async def hass_passthrough(opsdroid, config, message):
    """Pass messages directly through to the Home Assistant Conversation Component.

    See https://www.home-assistant.io/components/conversation/ for more information
    on how to configure the component.
    """
    if config.get('conversation-passthrough', False) is not True:
        return

    url = urljoin(config.get('hass-url', 'http://127.0.0.1:8123'), "/api/services/conversation/process")
    headers = {'x-ha-access': config.get('hass-password', 'YOUR_PASSWORD'),
               'content-type': 'application/json'}
    data = json.dumps({"text": message.text})
    r = requests.post(url, headers=headers, data=data)
    if r.status_code == requests.codes.ok:
        response = r.json()
        _LOGGER.debug(response)
        if response:
            await message.respond('Ok')
    else:
        _LOGGER.error(r.json())


@match_webhook("notify")
async def notify(opsdroid, config, message):
    """A webhook for Home Assistant to notify through opsdroid."""
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
