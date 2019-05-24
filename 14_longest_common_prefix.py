# /usr/local/bin/python3.6

# reduce function
from functools import reduce


class Solution:
    def get_common_prefix(self, x, y):
        LCP_length = 0

        for i in range(0, min(len(x), len(y))):
            if x[i] != y[i]:
                break

            LCP_length += 1

        return x[:LCP_length]


  # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''

        return reduce(self.get_common_prefix, strs)


def long_common(strs):
    if not strs:
        return ''

    #figure out the maximum common lengths
    minLen = len(strs[0])
    for i in range(len(strs)):
        minLen = min(len(strs[i]), minLen)

    #select the first item and compare to the other
    lcp =''
    i = 0
    while i < minLen:
        char = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != char:
                return lcp
        lcp = lcp + char
        i += 1

    return lcp


# print(long_common(['flow', 'flosedfe', 'flo0000']))

#对于每组数据，输出一个整数，代表最少需要删除的字符个数
def delete_num():
    n = input()
    for i in range(int(n)):
        i = input()
        num = 0


#输出中的大写字母后移

#n个数 两两数组 第一个数最小差数组个数 最大差数组个数
# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0] + int(a[1])))

def max_min_v():
    line = input().split()
    n = int(line[0])
    s = int(line[1])
    line2 = input().split()
    sumi = 0
    min_v_s = 0
    max_v = int(line2[0])
    min_v = int(line2[0])
    sum2 = 0
    for i in line2:
        sumi += int(i)
    if sumi < s:
        print(-1)
    if sumi == s:
        print(min_v_s)

    if sumi > s:
        for i in line2:
            if int(i) <= min_v:
                min_v = int(i)
        print(min_v)
        for i in line2:
            if int(i) > max_v:
                max_v = int(i)
        print(max_v)
        for i in line2:
            sum2 += (int(i) - min_v)
        print(sum2)
        if sum2 >= s:
            min_v_s = min_v
            print(min_v_s)
            return min_v_s
        elif max_v - min_v < s:
            min_v_s = (sumi - s) // n
            print(min_v_s)
            return min_v_s

# max_min_v()

def longest_sub():
    usedChar = {}
    s = input()
    start = maxLength = 0
    for i in range(len(s)):

        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
            print(usedChar)
        else:
            maxLength = max(maxLength, i - start + 1)
        usedChar[s[i]] = i
    print(maxLength)

class Solution:
    def longest_sub2(self):
        s = input()
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.is_unique(s, i, j):
                    ans = max(ans, j - i)
        print(ans)
        return ans

    def is_unique(self, s, start, end):
        res = 0
        for n in range(start, end):
            if s[n] not in s[start:n] and s[n] not in s[n+1:end]:
                res += 0
            else:
                res += 1
        if res == 0:
            return True
        else:
            return False

