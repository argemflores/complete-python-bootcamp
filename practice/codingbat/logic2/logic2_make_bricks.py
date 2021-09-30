# make_bricks

# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

def make_bricks(small, big, goal):
    # deduct big bricks first from goal
    for _ in range(big):
        goal = goal - 5

        # big brick exceeds goal, so restock goal
        if goal < 0:
            goal += 5
            break

    # goal is not met, so check small bricks
    if goal > 0:
        # deduct small bricks from goal
        for _ in range(small):
            goal = goal - 1

            # small brick exceeds goal, so stop
            if goal < 0:
                goal = 0
                break

    # True if goal is met, else False
    return goal == 0
