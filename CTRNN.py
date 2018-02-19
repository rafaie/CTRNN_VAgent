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
            states[i] = value
            outputs[i] = sigmoid(gains[i]*(states[i] + biases[i]))

        def neuron_output(self, i):
            return outputs[i]

        # double &NeuronOutputReference(int i) {return outputs[i];};

        def set_neuron_output(int i, double value)
            {outputs[i] = value; states[i] = InverseSigmoid(value)/gains[i] - biases[i];};
        double NeuronBias(int i) {return biases[i];};
        void SetNeuronBias(int i, double value) {biases[i] = value;};
        double NeuronGain(int i) {return gains[i];};
        void SetNeuronGain(int i, double value) {gains[i] = value;};
        double NeuronTimeConstant(int i) {return taus[i];};
        void SetNeuronTimeConstant(int i, double value) {taus[i] = value;Rtaus[i] = 1/value;};
        double NeuronExternalInput(int i) {return externalinputs[i];};
        double &NeuronExternalInputReference(int i) {return externalinputs[i];};
        void SetNeuronExternalInput(int i, double value) {externalinputs[i] = value;};
        double ConnectionWeight(int from, int to) {return weights[from][to];};
        void SetConnectionWeight(int from, int to, double value) {weights[from][to] = value;};
        void LesionNeuron(int n)
        {
            for (int i = 1; i<= size; i++) {
                SetConnectionWeight(i,n,0);
                SetConnectionWeight(n,i,0);
            }
        }
        void SetCenterCrossing(void);

        // Input and output
        friend ostream& operator<<(ostream& os, CTRNN& c);
        friend istream& operator>>(istream& is, CTRNN& c);

        // Control
        void RandomizeCircuitState(double lb, double ub);
        void RandomizeCircuitState(double lb, double ub, RandomState &rs);
        void RandomizeCircuitOutput(double lb, double ub);
        void RandomizeCircuitOutput(double lb, double ub, RandomState &rs);
        void EulerStep(double stepsize);
        void RK4Step(double stepsize);

        int size;
        TVector<double> states, outputs, biases, gains, taus, Rtaus, externalinputs;
        TMatrix<double> weights;
        TVector<double> TempStates,TempOutputs,k1,k2,k3,k4;
