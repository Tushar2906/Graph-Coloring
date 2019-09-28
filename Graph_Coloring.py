from collections import defaultdict

graph = defaultdict(list)

list1=[]

def is_safe(n, graph, colors, c):
    for i in range(n):
        if graph[n][i] and c == colors[i]:
            return False
    return True


def graphColoringUtil(graph, color_nb, colors, n):
    if vertex_nb  == n:
        return True

    for c in range(1, color_nb+1):
        if is_safe(n, graph, colors, c):
            colors[n] = c
            if graphColoringUtil(graph, color_nb, colors, n+1):
                return True
            colors[n] = 0


graph = [
    [0,1,0,0,0,1],
    [1,0,1,1,1,0],
    [0,1,0,1,0,0],
    [0,1,1,0,1,0],
    [0,1,0,1,0,1],
    [1,0,0,0,1,0]
]

vertex_nb = 6
color_nb = 3
colors = [0] * vertex_nb


if graphColoringUtil(graph, color_nb, colors, 0):
    print(colors)
else:
    print("No solutions")

