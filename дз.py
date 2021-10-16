class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_list(first):
    # Выводим список
    print("!!!!!")
    current = first
    while current is not None:
        print(current.value)
        current = current.next
    print(current)  # None


# задача 6


def list_len(first):
    current = first
    count = 0
    while current is not None:
        current = current.next
        count += 1
    return count


# задача 5


def get_by_index(first, position):
    current = first
    count = 0
    while count != position:
        count += 1
        current = current.next
    return current.value


# задача 3


def addition(first, second):
    current1, current2 = first, second
    third = Node(int(current1.value + current2.value))
    current3 = third
    current1, current2 = current1.next, current2.next
    while current1 is not None:
        node = Node(int(current1.value + current2.value))
        current3.next = node
        current3 = current3.next
        current1 = current1.next
        current2 = current2.next
    return third



first = Node(1)
second = Node(1)
current1 = first
current2 = second

for i in range(2, 10):
    node = Node(i)
    current1.next = node
    current1 = current1.next

for i in range(2, 10):
    node = Node(i)
    current2.next = node
    current2 = current2.next

print_list(addition(first, second))
