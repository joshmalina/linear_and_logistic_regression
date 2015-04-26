
class IMultivariateLinearRegression(object):

    def predict(self, x_vector):
        raise NotImplementedError()

    def retrieve_training_set(self):
        raise NotImplementedError()

    def get_cost(self):
        raise NotImplementedError()

    def get_gradient_descent(xs, ys, step_size, when_stop):
        raise NotImplementedError()

    def set_hypothesis(self):
        raise NotImplementedError()

