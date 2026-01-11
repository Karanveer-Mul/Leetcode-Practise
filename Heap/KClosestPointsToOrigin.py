class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        heapq.heapify(heap)

        for point in points:
            distance = -(point[0]**2 + point[1]**2) 
            #since python defaults to min heap by default
            #we negate the distance to get largest value 

            if len(heap) == k:
                heapq.heappushpop(heap, (distance, point))
            else:
                heapq.heappush(heap, (distance, point))


        result = []

        for (distance, point) in heap:
            result.append(point)
        
        return result
