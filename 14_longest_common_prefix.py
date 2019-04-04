#/usr/local/bin/python3.6

##reduce function
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


def long_common(strs:[str]):
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