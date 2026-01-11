class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = nums[:k] #putting first k elements in the heap
        heapq.heapify(heap) #Since it is in place, time complexity is O(k)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num) 
                #Since we are deleting (log n) and inserting (log n) 
                #For n-k elements the time complexity is O((n-k)* 2log k)

        return heap[0] # time complexity O(1)

        
