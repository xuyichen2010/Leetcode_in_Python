# Using heap (Priority Queue)
# O(N) insert and pop take logK where K = 26, and you do them N times so its N*log(26) = O(N)
# O(1) == O(26)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        task_to_count = {}
        for task in tasks:
            task_to_count[task] = task_to_count.get(task, 0) + 1
        heap = []
        for count in task_to_count.values():
            heapq.heappush(heap, (-count))
        time = 0

        while heap:
            i = 0
            temp = []
            while i <= n:
                if heap:
                    if heap[0] < -1:
                        temp.append(heapq.heappop(heap))
                    else:
                        heapq.heappop(heap)
                time += 1
                if not heap and not temp:
                    break
                i += 1

            for count in temp:
                count = -count - 1
                heapq.heappush(heap, -count)
        return time

# Greedy
# O(n)
# O(1) == O(26)

# ans = number of idles + number of tasks
# Evenly divide up the most frequent tasks (can be more than one)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        task_to_count = {}
        max_count = 0
        num_of_max = 0
        for task in tasks:
            task_to_count[task] = task_to_count.get(task, 0) + 1
            if task_to_count[task] == max_count:
                num_of_max += 1
            elif task_to_count[task] > max_count:
                max_count = task_to_count[task]
                num_of_max = 1

        part_count = max_count - 1
        part_length = n - (num_of_max - 1)

        empty_slots = part_count * part_length
        avaliable_tasks = len(tasks) - num_of_max * max_count
        idles = max(0, empty_slots - avaliable_tasks)

        return len(tasks) + idles