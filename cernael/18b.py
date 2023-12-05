def solve(lines):
    res = set()
    a,b,c = map(int,lines[0].split(','))
    xmin, xmax, ymin, ymax, zmin, zmax = a,a,b,b,c,c
    for l in lines:
        (x,y,z) = map(int,l.split(','))
        xmin, xmax, ymin, ymax, zmin, zmax = min(x, xmin), max(x, xmax), min(y, ymin), max(y, ymax), min(z, zmin), max(z, zmax)
        res.add((x,y,z))

    xmin, xmax, ymin, ymax, zmin, zmax = xmin-1, xmax+2, ymin-1, ymax+2, zmin-1, zmax+2
    queue = set()
    air = set()
    for y in range(ymin, ymax):
        for z in range(zmin, zmax):
            queue.add((xmin, y,z))
            queue.add((xmax,y,z))
            air.add((xmin, y,z))
            air.add((xmax,y,z))
    for x in range(xmin, xmax):
        for z in range(zmin, zmax):
            queue.add((x, ymin,z))
            queue.add((x, ymax,z))
            air.add((x, ymin,z))
            air.add((x, ymax,z))
        for y in range(ymin, ymax):
            queue.add((x, y,zmin))
            queue.add((x,y,zmax))
            air.add((x, y,zmin))
            air.add((x,y,zmax))

    while queue:
        (x,y,z) = queue.pop()
        for d in [(x-1,y,z),(x+1,y,z),(x,y-1,z),(x,y+1,z),(x,y,z-1),(x,y,z+1)]:
            if (d not in res
            and d not in queue
            and d not in air
            and xmin <= d[0] <= xmax
            and ymin <= d[1] <= ymax
            and zmin <= d[2] <= zmax):
                queue.add(d)
                air.add(d)


    acc = 0

    for (x,y,z) in res:
        if (x+1,y,z) in air: acc += 1
        if (x-1,y,z) in air: acc += 1
        if (x,y+1,z) in air: acc += 1
        if (x,y-1,z) in air: acc += 1
        if (x,y,z+1) in air: acc += 1
        if (x,y,z-1) in air: acc += 1
    return acc

if __name__ == '__main__':
    lines = []
    with open('18.txt') as f:
        for line in f.readlines():
            line = line.strip()
            lines.append(line)
    print(solve(lines))
