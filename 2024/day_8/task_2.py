from task_1 import next_an, p_dist, valid, places, combinations

antinodes, antennas = set(), set()
for antenna, locations in places().items():
    pairs: [] = combinations(values=locations)

    for a1, a2 in pairs:
        antennas.add(a1), antennas.add(a2)

        dist1, dist2 = p_dist(x=a1, y=a2), p_dist(x=a2, y=a1)
        an1, an2 = a1, a2
        while True:
            an1, an2 = next_an(x=an1, dist=dist1), next_an(x=an2, dist=dist2)
            v1, v2 = valid(x=an1, visited=antinodes), valid(x=an2, visited=antinodes)
            if not v1 and not v2:
                break

antinodes.update(antennas)
print(f'Result: {len(antinodes)}')
