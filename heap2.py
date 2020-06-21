class Heap(object):

    def __init__(self):
        self.heap = []
        self.current_position = -1

    # Don't actually need this method
    # def get_length(self):
    #     return len(self.heap)

    def insert(self, value):

        self.current_position += 1
        self.heap.append(value)
        self.fix_heap(self.current_position)

    def fix_heap(self, index):

        if self.current_position < 1:
            return
        elif self.current_position == 1:
            if self.heap[0] < self.heap[1]:
                self.heap[0], self.heap[1] = self.heap[1], self.heap[0]
        else:
            parent_index = int((index - 1) / 2)
            child_index = index
            while parent_index >= 0 and child_index != 0:
                if self.heap[child_index] > self.heap[parent_index]:
                    self.heap[child_index], self.heap[parent_index] = self.heap[parent_index], self.heap[child_index]
                child_index = parent_index
                parent_index = int((child_index - 1) / 2)
        return

    def print_heap(self):
        print(self.heap)
        # print('length of heap', len(self.heap))

    def heapsort(self):
        # will attempt to heapsort the given heap
        last_index = self.current_position
        while last_index > 0:
            self.heap[0], self.heap[last_index] = self.heap[last_index], self.heap[0]
            last_index -= 1
            if last_index != 0:
                self.fix_for_heapsort(0, last_index)

        # print(self.heap)

    def fix_for_heapsort(self, start, end):
        if end < 2:
            return
        parent_index = start
        child_left = 2*parent_index + 1
        child_right = 2*parent_index + 2

        while child_left <= end:
            if child_right > end:
                child_to_swap = child_left
            elif self.heap[child_left] > self.heap[child_right]:
                child_to_swap = child_left
            else:
                child_to_swap = child_right

            self.heap[parent_index], self.heap[child_to_swap] = self.heap[child_to_swap], self.heap[parent_index]
            parent_index = child_to_swap
            child_left = 2*parent_index + 1
            child_right = 2*parent_index + 2
        return

heap = Heap()
heap.insert(45)
heap.insert(86)
heap.insert(25)
heap.insert(32)
heap.insert(16)
heap.insert(9)
heap.insert(51)
heap.insert(13)
heap.insert(6)
heap.insert(2)

heap.print_heap()
heap.heapsort()
# print(heap.heap)
heap.print_heap()