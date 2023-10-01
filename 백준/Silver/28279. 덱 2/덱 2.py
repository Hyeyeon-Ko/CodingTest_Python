import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deck = deque()

for _ in range(n):
    command_line = input()
    command = int(command_line.split()[0])

    if command == 1:
        deck.insert(0, int(command_line.split()[1]))

    elif command == 2:
        deck.append(int(command_line.split()[1]))

    elif command == 3:
        print(deck.popleft()) if deck else print(-1)

    elif command == 4:
        print(deck.pop()) if deck else print (-1)

    elif command == 5: 
        print(len(deck))

    elif command == 6:
        print (1) if not deck else print(0)

    elif command == 7:
        print(deck[0]) if deck else print(-1)

    elif command == 8:
        print(deck[-1]) if deck else print(-1)
