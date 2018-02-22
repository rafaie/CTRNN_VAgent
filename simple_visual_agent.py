from visual_object import Line, Circle
from visual_agent import VisualAgent
import numpy as np
import os
import sys
import random
import time
import csv

RANDOM_SEED = 1


# The main program
def run_process(outfile_csv, step_size, X1, Y1, X2, Y2, is_circle=False):
    visual_agent = VisualAgent()
    obj = Line()
    obj_id = 1
    if is_circle is True:
        obj = Circle()
        obj_id = 2

    path = "categorize.ns"
    if os.path.exists(path) is False:
        print('The network file is Not exit')
        sys.exit(1)

    visual_agent.nervous_system.load(path)

    # Run the agent
    random.seed()
    agent.reset(0, Y1)
    agent.set_positionX(X1)
    obj.set_positionX(X2)
    obj.set_positionY(Y2)

    timer = 0
    status = 0
    strt_time = time.time()

    t = 0
    while obj.positionY() > BodySize/2:
        t += step_size
        timer += 1
        print("------------------")
        print(agent.positionX(), agent.positionY())
        print(obj.positionX(), obj.positionY())
        outfile_csv.writerow([obj_id, timer, step_size, X1, Y1, X2, Y2,
                              agent.positionX(), agent.positionY,
                              obj.positionX(), obj.positionY(), status])
        status = 1
        agent.step(step_size, obj)
        obj.step(step_size)

    end_time = time.time()
    print('finished computation at', end_time, ', elapsed time: ',
          end_time - start_time)

    outfile_csv.writerow([obj_id, timer, step_size, X1, Y1, X2, Y2,
                          agent.positionX(), agent.positionY,
                          obj.positionX(), obj.positionY(), status])


if __name__ == "__main__":
    outfile = open('output.csv', 'w')
    outfile_csv = csv.writer(outfile, delimiter=',',
                             quotechar="'", quoting=csv.QUOTE_MINIMAL)
    outfile_csv.writerow(['obj_type', 'timer', 'step_size', 'X1', 'Y1',
                          'X2', 'Y2', 'agent_X', 'agent_Y', 'obj_X',
                          'obj_Y', 'status'])

    for j1 in range(150, 270, 20):
        for j2 in range(-30, 30, 15):
            for i in np.arange(0.1, 0.2, 0.01):
                print("------------------------------------")
                run_process(outfile_csv, i, j2, 0, -32 + int((275-j1)/2), j1)
                run_process(outfile_csv, i, j2, 0, -32 + int((275-j1)/2), j1,
                            True)

    outfile_csv.close()
