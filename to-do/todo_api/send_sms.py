import africastalking

class SMSSender:
    def __init__(self):
        africastalking.initialize(
            username='natasha',
            api_key='88a1738345c397c385e6994d281f7650dacf77f78d8898d9ac22681752d804e2'
        )
        self.sms = africastalking.SMS

    def send(self, message, recipients, sender):
        try:
            response = self.sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print(f'Houston, we have a problem: {e}')

# Instantiate SMSSender class
sms_sender = SMSSender()
