class Watcher:
    # Observer interface: Defines a method that all observers must implement
    def notice(self, msg):
        pass

class Screen(Watcher):
    # Concrete observer: Handles notification messages by displaying on screen
    def notice(self, msg):
        print(f"[Screen] {msg}")

class Record(Watcher):
    # Concrete observer: Handles notification messages by recording them
    def notice(self, msg):
        print(f"[Record] {msg}")
