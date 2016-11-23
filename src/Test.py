def get_surrounding_til_values(self, x, y):
        values = []

        PT = [[-1, 1], [0, 1], [1, 1],
          [-1, 0],       [1, 0],
          [-1, -1], [0, -1], [1, -1]]

        for t in PT:
            try:
                if x + t[0] >= 0 and y + t[1] >= 0:
                    if self.map[x + t[0]][y + t[1]] is None:
                        pass
                    else:
                        values.append(self.map[x + t[0]][y + t[1]].value)
                        values.sort(reverse=True)
            except:
                pass

            return values