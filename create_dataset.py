import math
import random

BODY_SIZE = 30.0
ENV_WIDTH = 400.0
ENV_MIN_HEIGHT = 200.0
ENV_MAX_HEIGHT = 400.0

LINE = 0
CIRCLE = 1

HIGHT_DIST = 3
WIDTH_DIST = 5
RANDOM_DATA_COUNT = 10


def gen_data(x1, x2, y2, type=LINE):
    pass


def get_random_X12Y():
    x1 = random.randint(-ENV_WIDTH / 2 * BODY_SIZE/2,
                        ENV_WIDTH / 2 * BODY_SIZE/2)
    x2 = random.randint(-ENV_WIDTH / 2 * BODY_SIZE/2,
                        ENV_WIDTH / 2 * BODY_SIZE/2)
    y = random.randint()

    return (x1, x2, y)


if __name__ == '__main__':
    with open('dataset.csv', 'w') as fi:
        for i in range(WIDTH_DIST):
            x1 = int((-ENV_WIDTH / 2 + BODY_SIZE/2) +
                     (ENV_WIDTH - BODY_SIZE) / WIDTH_DIST * i)
            for j in range(WIDTH_DIST):
                x2 = int((-ENV_WIDTH / 2 + BODY_SIZE/2) +
                         (ENV_WIDTH - BODY_SIZE) / WIDTH_DIST * j)

                for k in range(HIGHT_DIST):
                    y = int(ENV_MAX_HEIGHT -
                            (ENV_MAX_HEIGHT - ENV_MIN_HEIGHT) / HIGHT_DIST * k)

                    fi.write(gen_data(x1, x2, y, LINE))
                    fi.write(gen_data(x1, x2, y, CIRCLE))

        for i in range(RANDOM_DATA_COUNT):
            x1, x2, y = get_random_X12Y()

            fi.write(gen_data(x1, x2, y, LINE))
            fi.write(gen_data(x1, x2, y, CIRCLE))
