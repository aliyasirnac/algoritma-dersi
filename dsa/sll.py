import heapq

CUSTOMERS = [
    {"id": 1, "name": "Ali Demir", "city": "İstanbul"},
    {"id": 2, "name": "Ayşe Yılmaz", "city": "Ankara"},
    {"id": 3, "name": "Zehra Kaya", "city": "İzmir"},
    {"id": 4, "name": "Mehmet Can", "city": "Bursa"},
    {"id": 5, "name": "Elif Güneş", "city": "Antalya"},
]

ORDERS = [
    {"order_id": 101, "customer_id": 1, "amount": 1250, "priority": 2},
    {"order_id": 102, "customer_id": 3, "amount": 980,  "priority": 1},
    {"order_id": 103, "customer_id": 2, "amount": 3400, "priority": 3},
    {"order_id": 104, "customer_id": 4, "amount": 1750, "priority": 1},
    {"order_id": 105, "customer_id": 5, "amount": 560,  "priority": 4},
]


class SLL:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, x):
        self.head = self.Node(x, self.head)
        self.size += 1

    def push_back(self, x):
        if not self.head:
            self.push(x)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = self.Node(x)
        self.size += 1

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        return f"SLL({list(self)})"


class DLL:
    class Node:
        def __init__(self, data, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, x):
        node = self.Node(x, None, self.head)
        if self.head:
            self.head.prev = node
        else:
            self.tail = node
        self.head = node

    def push_back(self, x):
        node = self.Node(x, self.tail, None)
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def forward(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def backward(self):
        current = self.tail
        while current:
            yield current.data
            current = current.prev

    def __repr__(self):
        return f"DLL({list(self.forward())})"


class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        node = QueueNode(x)
        if not self.front:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if not self.front:
            return None
        val = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return val

    def __repr__(self):
        cur = self.front
        vals = []
        while cur:
            vals.append(cur.data)
            cur = cur.next
        return f"LinkedQueue({vals})"


class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._count = 0

    def enqueue(self, priority, item):
        heapq.heappush(self._heap, (priority, self._count, item))
        self._count += 1

    def dequeue(self):
        if not self._heap:
            return None
        _, _, item = heapq.heappop(self._heap)
        return item

    def __repr__(self):
        return f"PriorityQueue(size={len(self._heap)})"


def menu():
    print("\n=== Veri Yapıları Menüsü ===")
    print("1 - Singly Linked List (Müşteri listesi)")
    print("2 - Doubly Linked List (Sipariş geçmişi)")
    print("3 - Queue (Teslimat kuyruğu)")
    print("4 - Priority Queue (Öncelikli siparişler)")
    print("0 - Çıkış")


def demo_sll():
    sll = SLL()
    for c in CUSTOMERS:
        sll.push_back(c)
    print("Müşteri listesi:")
    for c in sll:
        print(f"  {c['id']} - {c['name']} ({c['city']})")


def demo_dll():
    dll = DLL()
    for o in ORDERS:
        dll.push_back(o)
    print("İlk sipariş:", next(dll.forward()))
    print("Son sipariş:", next(dll.backward()))


def demo_queue():
    q = LinkedQueue()
    for o in ORDERS:
        q.enqueue(o)
    print("Teslimat kuyruğu oluşturuldu.")
    print("İlk teslimat:", q.dequeue())


def demo_pq():
    pq = PriorityQueue()
    for o in ORDERS:
        pq.enqueue(o["priority"], o)
    print("Siparişler önceliğe göre işleniyor:")
    while True:
        order = pq.dequeue()
        if not order:
            break
        print(f"  Order {order['order_id']} (priority={order['priority']})")


if __name__ == "__main__":
    while True:
        menu()
        sec = input("Seçiminiz: ")
        if sec == "1":
            demo_sll()
        elif sec == "2":
            demo_dll()
        elif sec == "3":
            demo_queue()
        elif sec == "4":
            demo_pq()
        elif sec == "0":
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim.")
