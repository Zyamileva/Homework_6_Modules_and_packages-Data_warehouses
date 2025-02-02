class MessageSender:
    def send_message(self, message: str):
        pass


"""Send a message.
This method sends a message to a recipient.

Args:
    message: The message to send.

Returns:
    None
"""


class SMSService:
    def send_sms(self, phone_number, message):
        if not phone_number:
            raise ValueError("Phone number not provided")
        if not message:
            raise ValueError("Message not provided")
        print(f"Відправка SMS на {phone_number}: {message}")


class EmailService:
    def send_email(self, email_address, message):
        if not email_address:
            raise ValueError("Email is not specified")
        if not message:
            raise ValueError("Message not provided")
        print(f"Відправка Email на {email_address}: {message}")


class PushService:
    def send_push(self, device_id, message):
        if not device_id:
            raise ValueError("Device ID is not specified")
        if not message:
            raise ValueError("Message not provided")
        print(f"Відправка Push-повідомлення на пристрій {device_id}: {message}")


class SMSAdapter(MessageSender):
    def __init__(self, sms_service, phone_number):
        self.sms_service = sms_service
        self.phone_number = phone_number

    def send_message(self, message: str):
        try:
            self.sms_service.send_sms(self.phone_number, message)
        except Exception as e:
            print(f"Помилка при відправці SMS: {e}")


class EmailAdapter(MessageSender):
    def __init__(self, email_service, email_address):
        self.email_service = email_service
        self.email_address = email_address

    def send_message(self, message: str):
        try:
            self.email_service.send_email(self.email_address, message)
        except Exception as e:
            print(f"Error sending email: {e}")


class PushAdapter(MessageSender):
    def __init__(self, push_service, device_id):
        self.push_service = push_service
        self.device_id = device_id

    def send_message(self, message: str):
        try:
            self.push_service.send_push(self.device_id, message)
        except Exception as e:
            print(f"An error occurred when sending a push message: {e}")


def send_all_message(adapters, message):
    for adapter in adapters:
        adapter.send_message(message)


sms_service = SMSService()
email_service = EmailService()
push_service = PushService()

sms_adapter = SMSAdapter(sms_service, "")
email_adapter = EmailAdapter(email_service, "example@ukr.net")
push_adapter = PushAdapter(push_service, "iphone")


message = "Hello!!!!!!"
send_all_message([sms_adapter, email_adapter, push_adapter], message)
