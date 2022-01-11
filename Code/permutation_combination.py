def combination(arr, r):
    l = len(arr)
    chosen = [0] * r

    def generation(depth, node):
        if depth == r:
            print(*chosen)
            return

        for i in range(node, l):
            chosen[depth] = arr[i]
            generation(depth+1, i+1)
    generation(0, 0)


def permutation(arr, r):
    l = len(arr)
    visited = [0] * l
    chosen = [0] * r

    def generation(chosen, depth):
        if depth == r:
            print(*chosen)
            return

        for i in range(l):
            if not visited[i]:
                chosen[depth] = arr[i]
                visited[i] = 1
                generation(chosen, depth+1)
                visited[i] = 0
    generation(chosen, 0)

test = [1,2,3,4,5]

combination(test, 3)
# permutation(test, 3)