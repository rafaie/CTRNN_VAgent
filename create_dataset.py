import math


BODY_SIZE = 30.0
ENV_WIDTH = 400.0
ENV_MIN_HEIGHT = 200.0
ENV_MAX_HEIGHT = 400.0

LINE = 0
CIRCLE = 1

SEQUNTIAL_DATA_COUNT = 64
RANDOM_DATA_COUNT = 20


def gen_sequential_data(x, y, type=LINE):
    pass


def get_random_XY():
    pass


if __name__ == '__main__':
    with open('dataset.csv', 'w') as fi:
        for i in range(math.sqrt(SEQUNTIAL_DATA_COUNT)):
            x = int(-ENV_WIDTH / 2 + (ENV_WIDTH - 2 * BODY_SIZE) /
                    math.sqrt(SEQUNTIAL_DATA_COUNT) * i)

            for j in range(math.sqrt(SEQUNTIAL_DATA_COUNT)):
                y = int(ENV_MAX_HEIGHT - (ENV_MAX_HEIGHT - ENV_MIN_HEIGHT) /
                        math.sqrt(SEQUNTIAL_DATA_COUNT) * j)

                fi.write(gen_sequential_data(x, y, LINE))
                fi.write(gen_sequential_data(x, y, CIRCLE))

        for i in range(RANDOM_DATA_COUNT):
            x, y = get_random_XY()

            fi.write(gen_sequential_data(x, y, LINE))
            fi.write(gen_sequential_data(x, y, CIRCLE))
