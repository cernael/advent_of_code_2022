def solve(lines):
    pass

if __name__ == '__main__':
    lines = []
    with open('£test.txt') as f:
        for line in f.readlines():
            line = line.strip()
            lines.append(line)
    print(solve(lines))
