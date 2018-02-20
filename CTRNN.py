from utils import sigmoid, inverse_sigmoid


class CTRNN:
        def __init__(self, new_size=0):
            pass

        # Show the Model details
        def print_model(sefl):
            pass

        # Accessors
        def circuit_size(self):
            return self.size

        def set_circuit_size(self, newsize):
            pass

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

        # Control
        # def randomize_circuit_state(self, lb, ub):
        #     pass

        def randomize_circuit_state(self, lb, ub, rs):
            pass

        # def randomize_circuit_output(self, lb, ub):
            # pass

        def randomize_circuit_output(self, lb, ub, rs):
            pass

        def euler_step(self, stepsize):
            pass

        def RK4_step(self, stepsize):
            pass

        # int size;
        # TVector<double> states, outputs, biases, gains, taus,
        # Rtaus, externalinputs;
        # TMatrix<double> weights;
        # TVector<double> TempStates,TempOutputs,k1,k2,k3,k4;
