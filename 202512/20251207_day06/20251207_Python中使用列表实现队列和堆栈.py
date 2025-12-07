# 开发者：Annona
# 创建时间：2025/12/7 12:26
# 1、使用列表方法实现堆栈非常容易，最后插入的最先取出（“后进先出”）。
# 把元素添加到堆栈的顶端，使用append()；从堆栈顶部取出元素，使用pop()不用指定索引
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
stack.pop()
print(stack)

# 2、列表也可以用作队列，最先加入的元素，最先取出（“先进先出”）；
# 然而，列表作为队列的效率很低。因为，在列表末尾添加和删除元素非常快，
# 但在列表开头插入或移除元素却很慢（因为所有其他元素都必须移动一位）
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.popleft())
print(queue.pop())
print(queue)