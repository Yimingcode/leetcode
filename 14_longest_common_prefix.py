#/usr/local/bin/python3.6


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


a = Solution()
print(a.longestCommonPrefix(['23xxxx','23xkoko', '23x00000']))

