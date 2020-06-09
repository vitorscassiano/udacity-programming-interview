class Element():
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LikedList():
    def __init__(self, head=None):
        self.head = head

    def append(self, element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = element
        else:
            self.head = element

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < counter:
            return None

        while current and counter <= position:
            if counter is position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, element, position):
        counter = 1
        current = self.head
        if position > counter:
            while current and counter < position:
                if counter is position - 1:
                    element.next = current.next
                    current.next = element
                current = current.next
                counter += 1
        elif position is counter:
            element.next = self.head
            self.head = element

    def delete(self, value):
        current = self.head
        while current.next:
            if current.value is value:
                current.value = current.next.value
                current.next = current.next.next
            current = current.next

    def delete_by_position(self, position):
        counter = 1
        current = self.head
        while current and counter <= position:
            if counter is position - 1:
                current.next = current.next.next
            current = current.next
            counter += 1
