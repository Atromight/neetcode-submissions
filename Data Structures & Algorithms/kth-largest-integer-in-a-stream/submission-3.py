class MaxHeap:
    def __init__(self) -> None:
        self.arr = []
        self.size = 0

    # Returns index of parent node for ith node (in array)
    def parent(self, i: int) -> int:
        return (i - 1) // 2

    # Returns index of left child node for ith node (in array)
    def left(self, i: int) -> int:
        return (2 * i + 1)

    # Returns index of right child node for ith node (in array)
    def right(self, i: int) -> int:
        return (2 * i + 2)

    def swap(self, i: int, j: int) -> None:
        print(f"Swapping i: {i} and j: {j}")
        arr = self.arr
        print(f"Array before swap: {arr}")
        arr[i], arr[j] = arr[j], arr[i]
        print(f"Array after swap: {arr}")

    def shift_up(self, i: int) -> None:
        print(f"Trying shift_up for i: {i}")
        parent = self.parent(i)
        if self.arr[i] > self.arr[parent]:
            self.swap(i, parent)
            if parent > 0:
                self.shift_up(parent)

    def shift_down(self, i: int) -> None:
        print(f"Trying shift_down for i: {i}")
        l = self.left(i)
        if l < self.size and self.arr[i] < self.arr[l]:
            self.swap(i, l)
            self.shift_down(l)
        
        r = self.right(i)
        if r < self.size and self.arr[i] < self.arr[r]:
            self.swap(i, r)
            self.shift_down(r)

    def insert(self, val: int) -> None:
        print("")
        print(f"Inserting val: {val} to array: {self.arr} with size: {self.size}")
        self.arr.append(val)
        self.size += 1
        print()
        if self.size > 1:
            self.shift_up(self.size - 1)
    
    def extract_max(self) -> int:
        print(f"Extracting max from array: {self.arr}")
        # Swap max (root node) with last array item
        self.swap(0, self.size - 1)
        # Extract max by removing last array item
        max_val = self.arr.pop()
        self.size -= 1
        # Shift root down (to ensure max heap maintains priority)
        self.shift_down(0)
        return max_val

    def get_max(self) -> int:
        return self.arr[0]

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = MaxHeap()
        for num in nums:
            self.heap.insert(num)
        
        print("Current heap is: ", self.heap.arr)


    def add(self, val: int) -> int:
        print(f"Adding val: {val} to array: {self.heap.arr}")
        self.heap.insert(val)
        l = []
        for i in range(self.k):
            num = self.heap.extract_max()
            l.append(num)

        for num in l:
            self.heap.insert(num)

        return l[-1]

        









