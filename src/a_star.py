def heuristic(node: tuple[int, int], goal: tuple[int, int]):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)


def astar_search(current_node: tuple[int, int], g_score: dict[tuple[int, int], int]):
    neighbors = []
    for dx, dy in [(0, -11), (0, 1), (-1, 0), (1, 0)]:
        x, y = current_node[0] + dx, current_node[1] + dy

        if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
            neighbors.append((x, y, g_score[current_node] + 1)) #-01-
    return neighbors


def reconstruct_path(came_from: dict, current_node: tuple[int, int]) -> list[tuple[int, int]]:
    path: list[tuple[int, int]] = []
    while current_node in came_from:
        path.insert(0, current_node) #-02-
        current_node = came_from[current_node]
    path.insert(0, start)
    return path


def astar(grid: list[list[int]], start: tuple[int, int], goal: tuple[int, int]):
    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0} #-03-
    f_score = {start: heuristic(start, goal)}

    while open_list:
        current_cost, current_node = min(open_list) #-04-

        if current_node == goal:
            path = reconstruct_path(came_from, current_node)
            return path

        open_list.remove((current_cost, current_node)) #-05-

        neighbors = astar_search(current_node, g_score)

        for x, y, tentative_g_score in neighbors:
            neighbor = x, y
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)

                if (f_score[neighbor], neighbor) not in open_list:
                    open_list.append((f_score[neighbor], neighbor))
    return None


grid: list[list[int]] = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

start: tuple[int, int] = 0, 0 # 시작노드
goal: tuple[int, int] = 3, 6 # 목표노드

path = astar(grid, start, goal)

if path:
    print("최적 경로: ", path)
else:
    print("경로를 찾을 수 없음")
