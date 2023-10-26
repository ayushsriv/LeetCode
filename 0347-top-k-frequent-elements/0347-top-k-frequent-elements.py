class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for i in nums:
            if i not in freq_map:
                freq_map[i] = 1
            else:
                freq_map[i]+=1
        
        uno_reverse = {}

        for i in freq_map:
            j = freq_map[i]
            if j in uno_reverse:
                uno_reverse[j].append(i)
            else:
                uno_reverse[j] = [i]

        Heap = maxHeap(len(freq_map))
        for i in uno_reverse:
            for _ in uno_reverse[i]:
                Heap.push(i)

        result = []
        for _ in range(k):
            result.append(uno_reverse[Heap.pop()].pop())

        return result 


# MaxHeap is an array where arr[k] > arr[2k] and arr[2k+1]
class maxHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize+1)
        self.heap[0] = 10001 #sys.maxsize

    def parent(self, pos) -> int:
        return (pos//2)

    def left(self, pos) -> int:
        return 2*pos

    def right(self, pos) -> int:
        return (2*pos)+1

    def isLeaf(self, pos) -> bool:
        if pos > (self.size//2) and pos <= self.size:
            return True
        else:
            return False

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def push(self, num: int):
        if self.size+1 > self.maxsize:
            return
        self.size+=1
        self.heap[self.size]=num

        #HeapifyUp
        current = self.size
        while self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def pop(self) -> int:
        res = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heapify(1)
        return res
    
    def heapify(self, parent):
        if self.size <= 1:
            return
        if not self.isLeaf(parent):
            left = self.left(parent)
            right = self.right(parent)

            if self.heap[parent] < self.heap[left] or self.heap[parent] < self.heap[right]:
                if  self.heap[right] > self.heap[left] :
                    self.swap(parent,right)                    
                    self.heapify(right)
                else:
                    self.swap(parent,left)                    
                    self.heapify(left)
        
    def print(self):
        print("Heap is: ", self.heap[:self.size+1])

