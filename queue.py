#큐
#먼저 들어온 데이터가 먼저 출력(FIF)

from collections import deque

queue=deque()

queue.append(5)
queue.append(2)
queue.append(3)
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)

queue.popleft()
print(queue)