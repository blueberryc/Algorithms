from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        ans = []
        if (not s or not p or len(s) < len(p)):
            return ans

        # 申请一个散列，用于记录窗口中具体元素的个数情况
        words = Counter(p)

        # left 表示左指针
        # count 记录当前的条件
        # ans 存放结果
        left = 0
        count = 0
        for right in range(len(s)):
            # 更新新元素在散列中的数量
            words[s[right]] -= 1

            if (words[s[right]] >= 0):
                count += 1

            if (right - left > len(p) - 1):
                # 子串长度大于固定窗口，左指针左移
                words[s[left]] += 1
                if (words[s[left]] > 0):
                    count -= 1
                left += 1

            if (count == len(p)):
                ans.append(left)
        return ans


def main():
    s = "cbaebabacd"
    p = "abc"
    solution = Solution()
    print(solution.findAnagrams(s, p))


if __name__ == "__main__":
    main()
