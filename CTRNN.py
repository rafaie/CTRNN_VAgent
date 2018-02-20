from utils import sigmoid, inverse_sigmoid
import numpy as np


class CTRNN:
        def __init__(self, new_size=0):
            self.set_circuit_size(new_size)

        # Show the Model details
        def print_model(sefl):
            pass

        # Accessors
        def circuit_size(self):
            return self.size

        def set_circuit_size(self, new_size):
            self.size = new_size
            self.states = np.full(new_size, 0.0, dtype=float)
            self.outputs = np.full(new_size, 0.0, dtype=float)
            self.biases = np.full(new_size, 0.0, dtype=float)
            self.gains = np.full(new_size, 1.0, dtype=float)
            self.taus = np.full(new_size, 1.0, dtype=float)
            self.Rtaus = np.full(new_size, 1.0, dtype=float)
            self.external_inputs = np.full(new_size, 0.0, dtype=float)
            self.weights = np.full((new_size, new_size), 0.0, dtype=float)
            self.temp_states = np.full(new_size, 0.0, dtype=float)
            self.temp_outputs = np.full(new_size, 0.0, dtype=float)
            self.k1 = np.full(new_size, 0.0, dtype=float)
            self.k2 = np.full(new_size, 0.0, dtype=float)
            self.k3 = np.full(new_size, 0.0, dtype=float)
            self.k4 = np.full(new_size, 0.0, dtype=float)

        def neuron_state(self, i):
            return self.states[i]

        # double &NeuronStateReference(int i) {return states[i];};

        def set_neuron_state(self, i, value):
            self.states[i] = value
            self.outputs[i] = sigmoid(self.gains[i]*(self.states[i] +
                                      self.biases[i]))

        def neuron_output(self, i):
            return self.outputs[i]

        # double &NeuronOutputReference(int i) {return outputs[i];};

        def set_neuron_output(self, i, value):
            self.outputs[i] = value
            self.states[i] = inverse_sigmoid(value)/self.gains[i] - \
                self.iases[i]

        def neuron_bias(self, i):
            return self.biases[i]

        def set_neuron_bias(self, i, value):
            self.biases[i] = value

        def neuron_gain(self, i):
            self.gains[i]

        def set_neuron_gain(self, i, value):
            self.gains[i] = value

        def neuron_time_constant(self, i):
            return self.taus[i]

        def set_neuron_time_constant(self, i, value):
            self.taus[i] = value
            self.Rtaus[i] = 1/value

        def neuron_external_input(self, i):
            return self.external_inputs[i]

        # double &NeuronExternalInputReference(int i)
        # {return externalinputs[i];};

        def set_neuron_external_input(self, i, value):
            self.external_inputs[i] = value

        def connection_weight(self, i, j):
            return self.weights[i][j]

        def set_connection_weight(self, i, j, value):
            self.weights[i][j] = value

        def lesion_neuron(self, n):
            for i in range(1, self.size + 1):
                self.set_connection_Weight(i, n, 0)
                self.set_connection_weight(n, i, 0)

        def set_center_crossing(self):
            pass

        # Input and output
        # friend ostream& operator<<(ostream& os, CTRNN& c);
        # friend istream& operator>>(istream& is, CTRNN& c);

        def randomize_circuit_state(self, lb, ub, rs=None):
            if rs is None:
                for i in range(self.size):
                    self.set_neuron_state(i, np.random.uniform(lb, ub))
            else:
                for i in range(self.size):
                    self.set_neuron_state(i, rs.uniform(lb, ub))

        def randomize_circuit_output(self, lb, ub, rs=None):
            if rs is None:
                for i in range(self.size):
                    self.set_neuron_output(i, np.random.uniform(lb, ub))
            else:
                for i in range(self.size):
                    self.set_neuron_output(i, rs.uniform(lb, ub))

        def euler_step(self, stepsize):
            pass

        def RK4_step(self, stepsize):
            pass
