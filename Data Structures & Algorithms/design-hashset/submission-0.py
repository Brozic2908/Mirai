class MyHashSet:

    def __init__(self):
        self.cap = []

    def add(self, key: int) -> None:
        if key not in self.cap:
            self.cap.append(key)

    def remove(self, key: int) -> None:
        while key in self.cap:
            self.cap.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.cap
