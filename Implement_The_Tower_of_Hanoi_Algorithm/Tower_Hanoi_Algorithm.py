def hanoi_solver(n):
    """Return a string showing every state of the Tower of Hanoi puzzle.

    The three rods are represented in order: left, middle, right. Each state is
    shown on a new line as lists of integers, with the starting configuration
    included.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    rods = [[disk for disk in range(n, 0, -1)], [], []]

    def format_rods():
        return " ".join(str(rod) for rod in rods)

    states = [format_rods()]

    def move(disk, source, helper, destination):
        if disk == 1:
            rods[destination].append(rods[source].pop())
            states.append(format_rods())
            return

        move(disk - 1, source, destination, helper)
        rods[destination].append(rods[source].pop())
        states.append(format_rods())
        move(disk - 1, helper, source, destination)

    if n > 0:
        move(n, 0, 1, 2)

    return "\n".join(states)

hanoi = hanoi_solver(4)

print(hanoi)