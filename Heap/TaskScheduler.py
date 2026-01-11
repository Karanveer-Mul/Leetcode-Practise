class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)
        max_heap = []

        for value in counts.values():
            heapq.heappush(max_heap, -value)

        wait_queue = deque()
        curr_int = 0

        while max_heap or wait_queue:
            curr_int += 1

            if max_heap:
                curr_op = heapq.heappop(max_heap)
                curr_op += 1 #Decrease the time, +1 since task value is in negative

                if curr_op != 0:
                    wait_queue.append((curr_op, curr_int + n))

            if wait_queue and wait_queue[0][1] == curr_int:
                heapq.heappush(max_heap, wait_queue.popleft()[0]) 

        return curr_int