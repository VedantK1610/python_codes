from collections import deque

def find_minimum_clicks(N, links, start_page, end_page):
    graph = {}
    for i in range(N):
        graph[i + 1] = links[i]

    queue = deque([(start_page, 0)])
    visited = set()

    while queue:
        current_page, clicks = queue.popleft()

        if current_page == end_page:
            return clicks

        if current_page in visited:
            continue

        visited.add(current_page)

        for linked_page in graph[current_page]:
            if linked_page not in visited:
                queue.append((linked_page, clicks + 1))

    return -1

# Read input
N = int(input())
links = []
for _ in range(N):
    linked_pages = list(map(int, input().split()))
    links.append(linked_pages)

start_page, end_page = map(int, input().split())

result = find_minimum_clicks(N, links, start_page, end_page)
print(result)
