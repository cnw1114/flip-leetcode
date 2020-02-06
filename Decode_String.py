class Solution:
    def decodeString(self, s: str) -> str:
        string = [['']]
        integer = ''
        for item in s:
            print(string)
            if item.isdigit():
                integer += item
            elif item == '[':
                string.append(['', int(integer)])
                integer = ''
            elif item.isalpha():
                string[-1][0]+=item
            elif item == ']':
                st, int_repeat = string.pop()
                string[-1][0] += st*int_repeat
        return string[0][0]
