# My first attempt to create a heap and heapsort algorithm

class Heap:

    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0] * Heap.HEAP_SIZE
        self.position = -1

    def insert(self, value):

        if self.heap_is_full():
            print("Heap is full..!")
            return

        self.position += 1
        self.heap[self.position] = value
        self.check_for_max_heap(self.position)
        return

    def check_for_max_heap(self, index):
        if index <= 0:
            return

        parent_index = int((index - 1) / 2)

        if self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.check_for_max_heap(parent_index)
        return

    def heap_is_full(self):

        if self.position >= self.HEAP_SIZE - 1:
            return True
        return False

    def print_max_heap(self):
        if self.position < 0:
            print("Empty heap..!")

        print(self.heap)
        return

    def fix_for_heapsort(self, index, upto):

        while index <= upto:

            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child < upto:
                # child_to_swap = None

                if right_child > upto:
                    child_to_swap = left_child
                else:
                    if self.heap[left_child] > self.heap[right_child]:
                        child_to_swap = left_child
                    else:
                        child_to_swap = right_child
                if self.heap[index] < self.heap[child_to_swap]:
                    self.heap[index], self.heap[child_to_swap] = self.heap[child_to_swap], self.heap[index]
                else:
                    break

                index = child_to_swap

            else:
                break


    def heapsort(self):

        for i in range(0, self.position + 1):
            self.heap[0], self.heap[self.position - i] = self.heap[self.position - i], self.heap[0]
            self.fix_for_heapsort(0, self.position - i - 1)


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

heap.print_max_heap()
heap.heapsort()
heap.print_max_heap()

