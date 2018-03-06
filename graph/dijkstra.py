def minDistance(self, dist, sptSet):
      for v in self.V:
          min = sys.maxint
          if dist[v] < min and v not in sptSet:
              min = dist[v]
              min_node = v
      return min_node
