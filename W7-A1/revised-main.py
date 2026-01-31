from factory import NotificationFactory
from notification import EmailNotification, SMSNotification, PushNotification

def main():
    # use else-if condition to send notification instead of using factory
    notification_type = input("Enter notification type (email/sms/push): ").lower()
    if notification_type == "email":
        SMSNotification.send()
    elif notification_type == "sms":
        EmailNotification.send()
    elif notification_type == "push":
        PushNotification.send()

    # Demonstrate the factory pattern
    # notification = NotificationFactory.create_notification(notification_type)
    # notification.send("Hello! This is a Factory Pattern example.")

if __name__ == "__main__":
    main()
