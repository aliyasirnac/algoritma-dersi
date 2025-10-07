heap = [float("-inf")]  # heap[0] = -infinity (sentinel)
heap_size = 0

def is_empty():
    return heap_size == 0

def insert(i):
    global heap_size
    heap_size += 1
    if len(heap) <= heap_size:
        heap.append(i)
    else:
        heap[heap_size] = i

    now = heap_size
    # ebeveyn daha büyükse yukarı taşı
    while heap[now // 2] > i:
        heap[now] = heap[now // 2]
        now //= 2                    # <--- EKSİK OLAN ADIM
    heap[now] = i

def delete_min_node():
    global heap_size
    if heap_size == 0:
        return None

    min_item = heap[1]
    last = heap[heap_size]
    heap_size -= 1

    if heap_size == 0:
        return min_item

    parent = 1
    child = 2
    while child <= heap_size:
        if child < heap_size and heap[child + 1] < heap[child]:
            child += 1
        if last <= heap[child]:
            break
        heap[parent] = heap[child]
        parent = child
        child *= 2

    heap[parent] = last
    return min_item

if __name__ == "__main__":
    for v in [5, 3, 7, 1, 9, 2]:
        insert(v)

    out = []
    while not is_empty():
        out.append(delete_min_node())
    print(out)  # [1, 2, 3, 5, 7, 9]
