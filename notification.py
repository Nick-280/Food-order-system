class Notification:
    def send(self, message):
        raise NotImplementedError("Notification method must implement send()")
    

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

        