__author__ = 'Jorge Cotillo'

import Entity.training_set_entity as tse


class BinaryLogisticRegression(object):

    def __init__(self):
        self._trainingSet = tse.TrainingSetEntity(True)

   # def get_training_set(self):
