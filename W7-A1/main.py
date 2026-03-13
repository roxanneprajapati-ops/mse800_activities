from factory import NotificationFactory

def main():
    notification_type = input("Enter notification type (email/sms/push): ").lower()
    # Demonstrate the factory pattern
    notification = NotificationFactory.create_notification(notification_type)
    notification.send("Hello! This is a Factory Pattern example.")

if __name__ == "__main__":
    main()
