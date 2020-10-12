from relay_sdk import Interface, WebhookServer
from quart import Quart, request, render_template_string

import logging, sys

relay = Interface()
app = Quart('incident-triggered')

logging.getLogger().setLevel(logging.INFO)

@app.route('/', methods=['POST'])
async def handler():
    data = await request.form

    event = { 'webhook_payload': {
                'static': 'test',
                'incident': '420',
                'entity_display_name': 'static test payload',
                'state_message': 'making a fake payload',
                'entity_id': 'd8e540fe-5e37-4ecb-89ff-3056769830e0',
              },
            'incident': '420'
            }

    print("emitting event about incident " + event['incident'] + ":::",file=sys.stderr)
    print(event,file=sys.stderr)

    relay.events.emit(event)

    return await render_template_string("Relay received payload about {{incident}}", incident=event['incident'])

if __name__ == '__main__':
    WebhookServer(app).serve_forever()
