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


# задача 4


def switch(first, node1, node2):
    if first is None:
        return None
    current = first
    reserve = node2.next
    if first == node1:
        node2.next = first.next
        first = node2
    flag = False
    while current is not None:
        if current.next == node1:
            current.next = node2
        elif current.next == node2:
            if not flag:
                flag = True
            else:
                current.next = node1
                node1.next = reserve
        current = current.next
    return first


# задача 1


def reverse_by_links(first):
    if first is None:
        return None
    elif first.next is None:
        return first
    if first.next.next is None:
        return switch(first, first, first.next)
    var1 = first
    var2 = var1.next
    current = var2.next
    var2.next = var1
    var1.next = None
    while current.next is not None:
        var1 = var2
        var2 = current
        current = current.next
        var2.next = var1
    current.next = var2
    return current


first = Node(1)
second = Node(1)
current1 = first
current2 = second
target1, target2 = 0, 0  # понадобятся для задачи 4

for i in range(2, 10):
    node = Node(i)
    if i == 2:
        target1 = first
    if i == 9:
        target2 = node
    current1.next = node
    current1 = current1.next

for i in range(2, 10):
    node = Node(i)
    current2.next = node
    current2 = current2.next

print_list(reverse_by_links(first))