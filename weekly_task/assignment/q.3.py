# Q3. Tuple Filter and Transform
# Problem:
# Input: A tuple of integers
# Tasks:
# 1. Convert to list.
# 2. Remove numbers < 10.
# 3. Multiply each by 2.
# 4. Return as tuple.
def tu_filter(tu1):
    lst1=[i*2 for i in tu1 if(i>=10)]
    return tuple(lst1)

tu1=(12,8,29,63,92,45)
print(tu_filter(tu1))