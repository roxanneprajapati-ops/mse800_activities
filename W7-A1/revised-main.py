from factory import NotificationFactory
from notification import EmailNotification, SMSNotification, PushNotification

def main():
    # use else-if condition to send notification instead of using factory
    notification_type = input("Enter notification type (email/sms/push): ").lower()
    notification = None
    if notification_type == "sms":
        notification = SMSNotification
    elif notification_type == "email":
        notification = EmailNotification
    elif notification_type == "push":
        notification = PushNotification

    if notification is not None:
        notification.send("Hello! This is a Factory Pattern example.")

    # Demonstrate the factory pattern
    # notification = NotificationFactory.create_notification(notification_type)
    # notification.send("Hello! This is a Factory Pattern example.")

if __name__ == "__main__":
    main()
