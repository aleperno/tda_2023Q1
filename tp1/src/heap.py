class Heap():
    def __init__(self):
        self.heap = []
        self.size = 0

    def heapify(self, element_idx):
        left_child = 2 * element_idx + 1
        right_child = 2 * element_idx + 2
        largest_idx = element_idx

        if((left_child < self.size) and (self.heap[left_child] < self.heap[largest_idx])):
            largest_idx = left_child
        
        if((right_child < self.size) and (self.heap[right_child] < self.heap[largest_idx])):
            largest_idx = right_child
        
        if(largest_idx != element_idx):
            self.heap[largest_idx], self.heap[element_idx] = self.heap[element_idx], self.heap[largest_idx]
            self.heapify(largest_idx)

    def insert_element(self, new_element):
        self.heap.append(new_element)
        self.size = len(self.heap)
        if(self.size != 1):
            for idx in range((self.size // 2) - 1, -1, -1):
                self.heapify(idx)

    def remove_element(self, element_idx):
        if(element_idx > self.size - 1):
            return
        self.heap[element_idx], self.heap[self.size-1] = self.heap[self.size-1], self.heap[element_idx]
        removed_element = self.heap[self.size-1]
        self.heap = self.heap[0:self.size-1]
        
        self.size -= 1
        for idx in range((self.size // 2) -1, -1, -1):
            self.heapify(idx)
        return removed_element


def k_merge_heap(arrays, heap, result):
    if(len(arrays) == 0):
        for i in range(len(heap.heap)):
            result.append(heap.remove_element(0))
        return
    smallest = heap.remove_element(0)
    for i in arrays:
        if(i[0] == smallest):
            i.pop(0)
            if(len(i) > 0):
                heap.insert_element(i[0])
            break
    arrays = [element for element in arrays if element != []]
    result.append(smallest)
    return k_merge_heap(arrays, heap, result)


def heap_sort(listas):
    arrays = [list(sublist) for sublist in listas]
    result = []
    if(len(arrays) == 1):
        return arrays
    heap = Heap()
    for i in arrays:
        heap.insert_element(i[0])
        continue
    k_merge_heap(arrays, heap, result)
    return result
