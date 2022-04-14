# <---coding: utf-8--->
# @Time:  2021/12/31/15:28
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for price in prices:
            maxprofit = max(price - minprice, maxprofit)
            minprice = min(price, minprice)
        return maxprofit