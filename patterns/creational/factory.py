from abc import ABCMeta, abstractmethod
from sklearn.naive_bayes import GaussianNB

class IModel(metaclass=ABCMeta):
    """The Model Interface"""

    @abstractmethod
    def fit(self, X, y):
        raise NotImplementedError()

    @abstractmethod
    def predict(self, X):
        raise NotImplementedError()

class NaiveBayesModel(IModel):

    def __init__(self, **params):
        self.params = **params
        self.model = None

    def fit(self, X, y):
        self.nb = GaussianNB(**self.params)
        self.nb.fit(X, y)

    def predict(self, X):
        return self.nb.predict(X)

class RandomForestClassifierModel(IModel):

    def fit(self, X, y):
        raise NotImplementedError()

    def predict(self, X):
        raise NotImplementedError()

class ModelFactory:
    def get_model(model_name='naive_bayes', **params):
        models = dict(
            naive_bayes=NaiveBayesModel(params),
            random_forest=RandomForestClassifierModel(params)
        )
        return models[model_name]

if __name__ == '__main__':
    factory = ModelFactory()
    p = dict(n_classes=[.22, .54, .....], var_smoothing=1e-9)
    X = [1, 2, 3, 4, 5, ...]
    y = [1, 0, 0, 1, 0, ...]
    X_test = [11, 90]
    model = factory.get_model('random_forest', p)
    model.fit(X, y)
    predictions = model.predict(X_test)
    print(predictions)
