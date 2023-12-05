def solve(lines):
    res = set()
    a,b,c = map(int,lines[0].split(','))
    for l in lines:
        (x,y,z) = map(int,l.split(','))
        res.add((x,y,z))

    acc = 0

    for (x,y,z) in res:
        if (x+1,y,z) not in res: acc += 1
        if (x-1,y,z) not in res: acc += 1
        if (x,y+1,z) not in res: acc += 1
        if (x,y-1,z) not in res: acc += 1
        if (x,y,z+1) not in res: acc += 1
        if (x,y,z-1) not in res: acc += 1
    return acc

if __name__ == '__main__':
    lines = []
    with open('18.txt') as f:
        for line in f.readlines():
            line = line.strip()
            lines.append(line)
    print(solve(lines))
