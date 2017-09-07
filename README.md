# opsdroid skill homeassistant

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to interact with [homeassistant](https://home-assistant.io/).

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
## Configuration

```yaml
skills:
  - name: homeassistant
    room: "#homeassistant"  # (Optional) room to send notifications to
```
## Usage

#### Notification

When a notification is triggered in homeassistant it will be sent to opsdroid.

> opsdroid: Here is your homeassistant notificaion

## License

GNU General Public License Version 3 (GPLv3)
