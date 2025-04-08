class Notification:
    def __init__(self,user_name,message):
        self.user_name=user_name
        self._message=message

    def send(self):
        print("You have got a new message")

    def get_message(self):
        return self._message

    def set_message(self, message):
        if isinstance(message,str):
            self._message=message
        else:
            print("Error: message should be a string.")


class SMSNotification(Notification):
    def send(self):
        print(f"{self.user_name} send you a message.")



class EmailNotification(Notification):
    def send(self):
        print(f"You have got a new email from {self.user_name}.")
    

notification_list=[SMSNotification("@alien","Just kidding =P"),EmailNotification("PKI Infocom","Nothing")]
notification_list[0].set_message("Hello")
notification_list[1].set_message("Your cloud electronic signature is about to expire.")

for notification in notification_list:
    notification.send()
    print(notification.get_message())