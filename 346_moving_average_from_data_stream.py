# Using list REALLY BAD
# O(N) N = size of the sliding window
# O(M) M = length of the queue which would grow at each call


class MovingAverage1:
    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        # calculate the sum of the moving window
        window_sum = sum(queue[-size:])

        return window_sum / min(len(queue), size)

# Using a Deque
# O(1)
# O(N) for sliding window


class MovingAverage2:
    def __init__(self, size: int):
        self.size = size
        self.queue = collections.deque()
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        if self.count > self.size:
            tail = self.queue.popleft()
        else:
            tail = 0
        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, self.count)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Circular Queue
# O(1)
# O(N)


class MovingAverage3:
    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = 0
        self.window_sum = 0
        self.coun = 0

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)