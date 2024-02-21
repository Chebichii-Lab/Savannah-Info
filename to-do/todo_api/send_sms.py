import africastalking

class SMSSender:
    def __init__(self):
        africastalking.initialize(
            username='[YOUR_USERNAME_GOES_HERE]',
            api_key='[YOUR_API_KEY_GOES_HERE]'
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
