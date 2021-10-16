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


def switch_first_and_last_values(first):
    if first is None:
        return None
    last = first
    while last.next is not None:
        last = last.next
    first.value, last.value = last.value, first.value
    return first


def switch_first_and_last_links(first):
    if first is None or first.next is None:
        return first
    current = first
    while current.next.next is not None:
        current = current.next
    last = current.next
    last.next = first.next  # 1
    current.next = first
    first.next = None
    return last


first = Node(123)
node = first
for i in range(10):
    node = Node(i)
    node.next = node
    node = node.next


print_list(first)
first = switch_first_and_last_values(first)
print_list(first)
first = switch_first_and_last_links(first)
print_list(first)