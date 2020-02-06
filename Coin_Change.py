# time limited solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        Memo_table = {}
        for item in coins:
            Memo_table[item] = [item]
        print(Memo_table)
        
        while True:
            keys_list = list(Memo_table.keys())
            for key1 in keys_list:
                for key2 in keys_list:
                    if key1+key2 > amount:
                        break
                    if key1+key2 not in Memo_table.keys(): # 키없으면 생성
                        Memo_table[key1+key2] = Memo_table[key1] + Memo_table[key2]
                    else: # 키있으면 길이 비교
                        if len(Memo_table[key1+key2])>len(Memo_table[key1] + Memo_table[key2]):
                            Memo_table[key1+key2] = Memo_table[key1] + Memo_table[key2] #if len(Memo_table[key1+key2]) > len(Memo_table[key1] + Memo_table[key2]) else Memo_table[key1+key2]
                    
            
            if keys_list == list(Memo_table.keys()):
                break
            else:
                keys_list = list(Memo_table.keys())
        try:
            output = len(Memo_table[amount])
        except:
            output = -1
        print(Memo_table[8839])
        return output
                    
# O(Coin*amount)/O(amount)            
class Solution(object):
    def coinChange(self, coins, amount): ## index가 amount 의미 (맨 마지막 인덱스가 target index)
        dp = [0] + [float('inf')] * amount
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1) ## 해당 동전을 추가하는 과정
        
        return dp[-1] if dp[-1] != float('inf') else -1
