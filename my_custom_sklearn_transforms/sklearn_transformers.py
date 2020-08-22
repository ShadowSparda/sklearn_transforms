from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler
# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        col_names = [
        'AVG_SCORE_DATASCIENCE',
        'AVG_SCORE_BACKEND',
        'AVG_SCORE_FRONTEND']  
        features = data[col_names]
        scaler = StandardScaler().fit(features.values)
        features = scaler.transform(features.values)
        data[col_names] = features
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        return data.drop(labels=self.columns, axis='columns')
