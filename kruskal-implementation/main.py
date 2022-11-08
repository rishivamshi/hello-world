class Kruskal:
    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def MinimumSpanningTree(self, g_from, g_to, g_weight):
        edges = []
        s = []
        for i in range(0, len(g_from)):
            s.append(g_from[i] - 1)
            s.append(g_to[i] - 1)
            s.append(g_weight[i])
            edges.append(s)
            s = []
        result = []
        i, e = 0, 0
        print(edges)
        edges = sorted(edges, key=lambda item: item[2])
        parent = g_from + g_to
        parent = list(set(parent))
        for k in range(0, len(parent)):
            parent[k] = parent[k] - 1
        rank = [0] * (len(parent))

        while e < len(parent) - 1:
            u, v, w = edges[i]
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)

        for i in range(0, len(result)):
            g_weight.remove(result[i][2])
        anot = 0
        for u, v, weight in result:
            print("Edge:", u + 1, v + 1, end=" ")
            print("-", weight)
        for i in range(0, len(g_weight)):
            if g_weight[i] > 0:
                anot = anot + g_weight[i]
        return anot


k = Kruskal()
k.MinimumSpanningTree([1, 2, 2, 3, 3], [2, 1, 3, 1, 2], [2, 2, 3, 10, 3])
