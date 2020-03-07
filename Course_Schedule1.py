import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edge = collections.defaultdict(lambda: [])
        for cur, pre in prerequisites:
            edge[pre].append(cur)
        in_info = collections.Counter(list(map(lambda x: x[0], prerequisites)))
        zero_in = [item for item in range(numCourses) if in_info[item] == 0]
        output = []
        while zero_in:
            zero_in_course = zero_in.pop(0)
            output.append(zero_in_course)
            while edge[zero_in_course]:
                course = edge[zero_in_course].pop(0)
                in_info[course] = in_info[course] - 1
                if in_info[course] == 0: zero_in.append(course)
        return len(output) == numCourses and True or False
