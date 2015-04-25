
class ILogisticRegression(object):

    def predict(self):
        raise NotImplementedError()

    def retrieve_training_set(self):
        raise NotImplementedError()

    def get_cost(self):
        raise NotImplementedError()

    def get_gradient_descent(self):
        raise NotImplementedError()

    def set_hypothesis(self):
        raise NotImplementedError()

