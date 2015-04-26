__author__ = 'Jorge Cotillo'


class TrainingSetEntity(object):

    # using init_y so it can be used in binary logistic regression or
    # multiple logistic regression where y is not true - false
    # instead is going to be some decimal perhaps

    def __init__(self, init_y=None):
        self._x = []
        self._y = 0.0

    @property
    def get_x(self):
        return self._x

    @get_x.setter
    def set_x(self, value):
        self._x = value

    @property
    def get_y(self):
        return self._y

    @get_y.setter
    def set_y(self, value):
        self._y = value