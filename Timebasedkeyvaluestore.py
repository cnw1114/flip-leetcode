from collections import defaultdict
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.ktimestamp = defaultdict(list)
        self.kv = defaultdict(list)

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        self.kv[key].append(value)
        self.ktimestamp[key].append(timestamp)

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if key not in self.kv: return ''
        idx = bisect_right(self.ktimestamp[key], timestamp)
        return '' if idx == 0 else self.kv[key][idx-1] ## idx가 0이면 빈리스트 한번도 set없는 상태
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
