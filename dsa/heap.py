class Heap:
    def __init__(self):
        self.heap = []

    def add(self, item):
        self.heap.append(item)
        cid = self.last_item()

        while cid > 0:
            pid = len(self.heap) // 2
            if self.heap[cid] > self.heap[pid]:
                self.heap[cid], self.heap[pid] = self.heap[pid], self.heap[cid]
            else:
                break

            cid = pid

    def remove(self):
        if len(self.heap) == 0:
            return None

        rid = self.heap[0]
        self.heap[0] = self.heap[self.last_item()]
        self.heap.pop(self.last_item())

        cid = 0
        while cid < self.last_item() + 1:
            lci = 2 * cid + 1
            rci = 2 * cid + 2

            if lci > self.last_item() + 1:
                break
            maxid = lci
            if rci < self.last_item() + 1:
                if self.heap[maxid] < self.heap[rci]:
                    maxid = rci

            if self.heap[cid] < self.heap[maxid]:
                self.heap[maxid], self.heap[cid] = self.heap[cid], self.heap[maxid]
                cid = maxid
            else:
                break
        return rid

    def last_item(self):
        return len(self.heap) - 1

    def get_size(self):
        return len(self.heap)

    def is_empty(self):
        return self.get_size == 0

    def peak(self):
        return self.heap[0]

    def get_heap(self):
        return self.heap

heap = Heap()

heap.add(1)
heap.add(5)
heap.add(9)

print(heap.get_size())
print(heap.get_heap())
heap.remove()
print(heap.get_size())

print(heap.get_heap())


def heap_sort(lst):
    heap = Heap()
    for i in lst:
        heap.add(i)
    
    for i in range(len(lst)):
        lst[len(lst)-1-i] = heap.remove()
    
lst = [-44,-3,0,-1,2,-5,10]
heap_sort(lst)