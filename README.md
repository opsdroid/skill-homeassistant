# opsdroid skill homeassistant

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to interact with [Home Assistant](https://home-assistant.io/). The skill provides a notification service and the ability to
pass opsdroid message through to the [conversation component](https://www.home-assistant.io/components/conversation/) in Home Assistant.

## Requirements

A homeassistant installation.

To use the opsdroid notification you must configure the [rest notify component](https://home-assistant.io/components/notify.rest/) in homeassistant to point to opsdroid.

```yaml
notify:
  - name: opsdroid
    platform: rest
    method: POST
    resource: http://<opsdroid ip>:<opsdroid port>/skill/homeassistant/notify
```

To use the conversation passthrough you must have the conversation component enabled in Home Assistant.

## Configuration

```yaml
skills:
  - name: homeassistant
    # Notification settings
    room: "#homeassistant"  # (Optional) room to send notifications to
    # Conversation component passthrough settings
    conversation-passthrough: false  # Enable/disable the conversation component passthrough
    hass-url: "http://127.0.0.1:8123"  # The URL of your Home Assistant
    hass-password: "YOURPASSWORD"  # Your Home Assistant auth password
```
## Usage

#### Notification

When a notification is triggered in homeassistant it will be sent to opsdroid.

> opsdroid: Here is your homeassistant notificaion

#### Conversation component passthrogh

When this is enabled all messages will be passed through to the Home Assistant conversation component.

> user: turn on the bedroom light
> opsdroid: ok
> *Light comes on*
