def solve(line):
    rocks = [ # could replace sets and list with tuples, maybe
        {(0,0),(1,0),(2,0),(3,0)},
        {(1,0),(0,1),(1,1),(2,1),(1,2)},
        {(0,0),(1,0),(2,0),(2,1),(2,2)},
        {(0,0),(0,1),(0,2),(0,3)},
        {(0,0),(1,0),(0,1),(1,1)},
    ]
    tick, n, tower, cycles, heights, bottom = 0, 0, [], [[],[],[],[],[]], [], 0
    while n < 20222:
        heights.append(len(tower))
        if tick >= len(line) * sum([len(l) for l in cycles]):
            cycles[n%5].append({'tick': tick, 'height': len(tower), 'rock_no': n, 'bottom': bottom})
            if len(cycles[n%5]) >= 3:
                print(cycles[n%5])
                prev, last, this = cycles[n%5][-3:]
                if (
                  this['tick'] - last['tick'] == last['tick'] - prev['tick']
                  and this['height'] - last['height'] == last['height'] - prev['height']
                  and this['rock_no'] - last['rock_no'] == last['rock_no'] - prev['rock_no']
                  and this['bottom'] - last['bottom'] == last['bottom'] - prev['bottom']
                  #and ''.join([''.join(l) for l in tower[bottom:len(tower)]]) == ''.join([''.join(l) for l in tower[last[3]:last[1]]])
                ):
                    cycle_height = this['height'] - last['height']
                    cycle_rocks = this['rock_no'] - last['rock_no']
                    remaining_rocks = 1000000000000 - this['rock_no']
                    whole_cycles_left = remaining_rocks // cycle_rocks
                    height_at_last_full_cycle = this['height'] + whole_cycles_left * cycle_height
                    rocks_in_last_partial_cycle = remaining_rocks % cycle_rocks
                    cycle_start = last['rock_no']
                    partial_cycle_height = heights[cycle_start + rocks_in_last_partial_cycle] - heights[cycle_start]
                    print('assert 10**x', this['rock_no'] + whole_cycles_left*cycle_rocks + rocks_in_last_partial_cycle, n , whole_cycles_left,cycle_rocks , rocks_in_last_partial_cycle)
                    print(                this['height'] + whole_cycles_left*cycle_height + partial_cycle_height)
                    return ("Cycle detected at height {} and rock {}.".format(this['height'], this['rock_no'])
                            + " Each cycle adds {} lines to tower and {} rocks.".format(cycle_height, cycle_rocks)
                            + " There are {} more rocks to add, which adds {} cycles and a bit.".format(remaining_rocks, whole_cycles_left)
                            + " Adding those cycles lands us at height {} with {} more rocks to add.".format(height_at_last_full_cycle, rocks_in_last_partial_cycle)
                            + " Candidate for answer is {}, but it was too low.".format(height_at_last_full_cycle+partial_cycle_height))
        #print(cycles)
        bottom = len(tower)
        x,y = 2,3
        rock = {(x+p[0],y+p[1]+len(tower)) for p in rocks[ n % 5 ]}
        # grow tower
        tower.extend([[' ' for _ in range(7)] for _ in range(10)])
        while True:
            # blow
            blow = 1 if line[tick % len(line)] == '>' else -1
            tick += 1
            for r in rock:
                # these can be optimised to a single check, albeit less readable
                if blow == -1 and (r[0] == 0 or tower[r[1]][r[0]-1] != ' '):
                    blow = False
                    break
                elif blow == 1 and (r[0] == 6 or tower[r[1]][r[0]+1] != ' '):
                    blow = False
                    break
            if blow:
                rock = {(p[0]+blow,p[1]) for p in rock}
            # fall
            fall = 1
            for r in rock:
                if tower[r[1]-fall][r[0]] != ' ' or r[1] == 0:
                    fall = False
                    break
            if fall:
                rock = {(p[0],p[1]-fall) for p in rock}
            else:
                for r in rock:
                    tower[r[1]][r[0]] = "#"
                    if bottom > r[1]:
                        bottom = r[1]
                break
        while ''.join(tower[-1]) == '       ':
            tower.pop()
        n += 1
    return [len(c) for c in cycles]

if __name__ == '__main__':
    lines = []
    with open('17.txt') as f:
        for line in f.readlines():
            line = line.strip()
            lines.append(line)
    print(solve(lines[0]))
