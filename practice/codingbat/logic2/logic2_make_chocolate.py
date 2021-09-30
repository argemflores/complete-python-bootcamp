# make_chocolate

# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2

def make_chocolate(small, big, goal):
    small_counter = 0

    # deduct big bars first from goal
    for _ in range(big):
        goal = goal - 5

        # big bar exceeds goal, so restock goal
        if goal < 0:
            goal += 5
            break

    # goal is not met, so check small bars
    if goal > 0:
        # deduct small bars from goal
        for _ in range(small):
            goal = goal - 1

            # valid bar, add to counter
            if goal >= 0:
                small_counter += 1

    # goal is not met, so return -1
    if goal > 0:
        return -1

    # return valid small bars
    return small_counter
