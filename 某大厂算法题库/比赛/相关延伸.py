# map的使用方法
"""
map()函数的核心作用是：将一个函数应用到一个或多个可迭代对象的每个元素上，返回一个迭代器，可理解为批量处理元素的工具
基本语法：
    map(function, iterable, ...)
    function: 要执行的函数（可以是普通函数、匿名函数lambda、内置函数）
    iterable: 一个或多个可迭代对象（列表、元组、字符串、集合等）
    返回值: map对象（迭代器），需通过list()/tuple()等转为具体序列才能直观查看结果
"""
# 示例
# 批量转化
nums1 = ['11', '14', '13', '22']
result1 = map(int, nums1)
print(list(result1))

# 批量计算
nums2 = [2, 3, 4, 5, 6]
result2 = map(lambda x: x ** 2, nums2)
print(list(result2))

# 多个可迭代对象
lst1 = [1, 2, 3]
lst2 = [10, 20, 30]
result3 = map(lambda x, y: x + y, lst1, lst2)
print(list(result3))

# 可迭代对象不一致时，以最短的可迭代对象为准，超出部分直接忽略
lst3 = [1, 2, 3]
lst4 = [10, 20, 30, 40, 50]
result4 = map(lambda x, y: x + y, lst3, lst4)
print(list(result4))

# cmp_to_key的使用方法
"""
functools.cmp_to_key()是处理自定义排序规则的关键工具，核心作用是将传统的比较函数转换为排序所需的key函数，让我们能自定义更灵活的排序逻辑。
基本语法：
    from functools import cmp_to_key
    
    def compare(a, b):
        # 返回规则
        # -1: a排在b前面
        #  1: a排在b后面
        #  0: a和b位置不变
        if 条件1:
            return -1
        elif 条件2:
            return 1
        else:
            return 0
            
    sorted_result = sorted(iterable, key=cmp_to_key(compare))
"""

# 示例1
# 对数字列表按绝对值从大到小排序
from functools import cmp_to_key


def compare(a, b):
    abs_a = abs(a)
    abs_b = abs(b)
    if abs_a > abs_b:
        return -1  # a的绝对值大，a排前面
    elif abs_a < abs_b:
        return 1  # a的绝对值小，a排后面
    else:
        return 0  # 绝对值相等，位置不变


nums = [3, -5, 1, -2, 4]
sorted_nums = sorted(nums, key=cmp_to_key(compare))
print(sorted_nums)

# 示例2
# 多条件自定义排序，对学生列表先按分数降序，分数相同再按年龄升序
students = [
    {"name": "张三", "score": 90, "age": 18},
    {"name": "李四", "score": 85, "age": 19},
    {"name": "王五", "score": 90, "age": 17},
    {"name": "赵六", "score": 88, "age": 20}
]

from functools import cmp_to_key


def cmp(a, b):
    # 先比较分数，降序
    if a["score"] > b["score"]:
        return -1
    elif a["score"] < b["score"]:
        return 1
    else:
        # 分数相同，在比较年龄，升序
        if a["age"] < b["age"]:
            return -1
        elif a["age"] > b["age"]:
            return 1
        else:
            return 0


sorted_students = sorted(students, key=cmp_to_key(cmp))
print(sorted_students)
