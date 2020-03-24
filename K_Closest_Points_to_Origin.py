class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        out=list(map(lambda x: sum(list(map(lambda y: y**2, x))),points))
        tot_answer = sorted(zip(points, out), key= lambda x:x[1])
        output = []
        for idx in range(K):
            output.append(tot_answer[idx][0])
        
        return output
