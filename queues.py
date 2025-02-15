from collections import deque
queque=deque([])
queque.append(1)
queque.append(2)
queque.append(3)
queque.popleft()
print(queque)

if not queque:
    print("empty")