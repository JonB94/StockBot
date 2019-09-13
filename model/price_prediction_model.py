import tensorflow as tf

class PricePredictionModel(object):
    """
    TODO: Define this such that it can be implemented in a with statement since tensorflow sessions are best run as this.
    """

    def __init__(self):
        self.sess = tf.Session()

    def _load_data(self):
        """
        TODO
        :return:
        """
        raise NotImplementedError

