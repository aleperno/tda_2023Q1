import heapq
import random

K = 4
H = 4

LISTAS = [
    sorted(random.randint(0, 100) for _ in range(H)) for _ in range(K)
]

l = [(n, i) for i, n in enumerate(next(zip(*LISTAS)))]

heapq.heapify(l)

print("hola")
print(l)

while l:
    print("foo")
    i = heapq.heappop(l)
    print(i)
