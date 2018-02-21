from CTRNN import CTRNN


if __name__ == "__main__":
    run_duration = 250
    step_size = 0.01

    c = CTRNN(2)
    c.set_neuron_bias(1, -2.75)
    c.set_neuron_bias(2, -1.75)
    c.set_connection_weight(1, 1, 4.5)
    c.set_connection_weight(1, 2, -1)
    c.set_connection_weight(2, 1, 1)
    c.set_connection_weight(2, 2, 4.5)

    c.randomize_circuit_state(-0.5, 0.5)
    print(0.0, c.neuron_output(1), c.neuron_output(2))
    for time in range(int(run_duration/step_size)):
        c.euler_step(step_size)
        print(time*step_size, c.neuron_output(1), c.neuron_output(2))
