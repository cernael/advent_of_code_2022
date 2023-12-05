class Plan:
    def __init__(self, blueprint):
        self.resources = {
            'ore': 0,
            'clay': 0,
            'obsidian': 0,
            'geode': 0
        }
        self.robots = {
            'ore': 1,
            'clay': 0,
            'obsidian': 0,
            'geode': 0
        }
        self.costs = blueprint

    def mine(self):
        for k,v in self.robots.items():
            self.resources


def solve(lines):
    blueprints = {int(l[0].split()[1]): {r[1]: {r[4:][i+1]: int(r[4:][i]) for i in range(0, len(r[4:]),3)} for r in map(lambda x: x.split(), l[1].split('.')) if r} for l in map(lambda x: x.split(':'), lines)}
    acc = 0
    time = 24
    for k,v in blueprints.items():
        plans = [Plan(v)]

    return acc
if __name__ == '__main__':
    lines = []
    with open('19test.txt') as f:
        for line in f.readlines():
            line = line.strip()
            lines.append(line)
    print(solve(lines))
