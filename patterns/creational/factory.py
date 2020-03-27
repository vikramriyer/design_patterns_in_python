class NaiveBayesModel(**params):
    pass

class RandomForestClassifierModel(**params):
    pass

def get_model(model_name='naive_bayes', params=None):
    models = dict(
        naive_bayes=NaiveBayesModel(**params),
        random_forest=RandomForestClassifierModel(**params)
    )
    return models[model_name]