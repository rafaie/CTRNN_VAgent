import random
import csv

BODY_SIZE = 30.0
ENV_WIDTH = 400.0
ENV_MIN_HEIGHT = 200.0
ENV_MAX_HEIGHT = 400.0

LINE = 1
CIRCLE = 2

HIGHT_DIST = 3
WIDTH_DIST = 5
RANDOM_DATA_COUNT = 10


def gen_data(x1, x2, y2, type=CIRCLE):
    y1 = 0
    if type == CIRCLE:
        return (CIRCLE, x1, y1, x2, y2, x2, 0)
    else:
        if abs(x2 - x1) > BODY_SIZE * 2:
            return (LINE, x1, y1, x2, y2, x1, 0)
        elif x2 > 0:
            return (LINE, x1, y1, x2, y2, -int(ENV_WIDTH / 2 - BODY_SIZE/2), 0)
        else:
            return (LINE, x1, y1, x2, y2, int(ENV_WIDTH / 2 - BODY_SIZE/2), 0)


def get_random_X12Y():
    x1 = random.randint(-ENV_WIDTH / 2 + BODY_SIZE/2,
                        ENV_WIDTH / 2 - BODY_SIZE/2)
    x2 = random.randint(-ENV_WIDTH / 2 + BODY_SIZE/2,
                        ENV_WIDTH / 2 - BODY_SIZE/2)
    y = random.randint(ENV_MAX_HEIGHT - ENV_MIN_HEIGHT, ENV_MAX_HEIGHT)

    return (x1, x2, y)


if __name__ == '__main__':
    with open('dataset.csv', 'w') as fi:
        outfile_csv = csv.writer(fi, delimiter=',',
                                 quotechar="'", quoting=csv.QUOTE_MINIMAL)
        for i in range(WIDTH_DIST):
            x1 = int((-ENV_WIDTH / 2 + BODY_SIZE/2) +
                     (ENV_WIDTH - BODY_SIZE) / WIDTH_DIST * i)
            for j in range(WIDTH_DIST):
                x2 = int((-ENV_WIDTH / 2 + BODY_SIZE/2) +
                         (ENV_WIDTH - BODY_SIZE) / WIDTH_DIST * j)

                for k in range(HIGHT_DIST):
                    y = int(ENV_MAX_HEIGHT -
                            (ENV_MAX_HEIGHT - ENV_MIN_HEIGHT) / HIGHT_DIST * k)

                    outfile_csv.writerow(gen_data(x1, x2, y, LINE))
                    outfile_csv.writerow(gen_data(x1, x2, y, CIRCLE))

        for i in range(RANDOM_DATA_COUNT):
            x1, x2, y = get_random_X12Y()

            outfile_csv.writerow(gen_data(x1, x2, y, LINE))
            outfile_csv.writerow(gen_data(x1, x2, y, CIRCLE))
