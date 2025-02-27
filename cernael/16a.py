class Room:
    def __init__(self, line):
        self.name = line[6:8]
        self.rate = int(line.split('=')[1].split(';')[0])
        self.tunnels = list(map(lambda x: x[-2:], line.split(', ')))
        self.map = {}
    def __repr__(self):
        return "Class Room. name: {}, rate: {}, tunnels: {}, map: {}".format(self.name, self.rate, ', '.join(self.tunnels), self.map)

    def map_cave(self, rooms):
        # The 1 here is the valve-opening cost
        unvisited = [(self.name, 1)]
        visited = set()
        while unvisited:
            r = unvisited.pop(0)
            if r[0] not in self.map.keys():
                room = rooms[r[0]]
                visited.add(r[0])
                if room.rate:
                    self.map[r[0]] = {'cost': r[1], 'flow': room.rate}
                unvisited.extend([(name, r[1] + 1) for name in room.tunnels if name not in visited])


class Path:
    def __init__(self, rooms, room, path=None):
        if path:
            self.unvisited = path.unvisited[:]
            self.unvisited.remove(room)
            self.path = path.path[:]
            self.time_left = (path.time_left - path.path[-1].map[room.name]["cost"])

            self.pressure_released = path.pressure_released + room.rate * self.time_left
        else:
            self.unvisited = [r for r in rooms.values() if r.rate]
            self.path = []

            self.pressure_released = 0
            self.time_left = 30
        self.path.append(room)
        self.max = (self.pressure_released +
            sum(
                map(
                    lambda x: x[0] * x[1].rate,
                    zip(
                        range(
                            self.time_left - min(map(lambda x: x['cost'], room.map.values())),
                            0,
                            -1),
                        sorted(
                            self.unvisited,
                            key=lambda x: x.rate,
                            reverse=True
                        )
                    )
                )
            )
        )
    def __repr__(self):
        return """unvisited: {},
        path: {},
        time left: {},
        pressure released: {},
        max: {}""".format(list(map(lambda x: x.name, self.unvisited)), list(map(lambda x: x.name, self.path)), self.time_left, self.pressure_released, self.max())

    def __lt__(self, other):
        if self.time_left < other.time_left:
            return True
        return self.max < other.max


def solve(lines):
    rooms = {name: Room(line) for (name, line) in map(lambda x: (x[6:8],x), lines)}
    for r in rooms.values():
        r.map_cave(rooms)
    #for r in rooms.values():
    #    print(r.name)
    #    for k,v in r.map.items():
    #        print(k,v)
    #    print()
    paths = [Path(rooms, rooms['AA'])]
    minn = 0
    n = 0
    p = 1
    while paths:
        n += 1
        #print(n, len(paths))
        #if n > 100: return
        paths.sort(key=lambda x: x.time_left)
        path = paths.pop(0)
        minn = max(minn, path.pressure_released)
        if path.max >= minn and path.time_left >= 0:
            p += len(path.unvisited) - 1
            paths.extend([Path(rooms, r, path) for r in path.unvisited])
    return minn, n, p

if __name__ == '__main__':
    lines = []
    with open('16.txt') as f:
        for line in f.readlines():
            line = line.strip()
            lines.append(line)
    print(solve(lines))
