from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from regression_model.processing import preprocessors as pp
from regression_model.config import config

price_pipe = Pipeline(
    [
        (
            "categorical_imputer",
            pp.CategoricalImputer(variables=config.CATEGORICAL_VARS_WITH_NA),
        ),
        (
            "numerical_imputer",
            pp.NumericalImputer(variables=config.NUMERICAL_VARS_WITH_NA),
        ),
        (
            "temporal_variables",
            pp.TemporalVariableEstimator(
                variables=config.TEMPORAL_VARS, reference_variable=config.DROP_FEATURES
            ),
        ),
        (
            "rare_label_encoder",
            pp.RareLabelCategoricalEncoder(tol=0.01, variables=config.CATEGORICAL_VARS),        
        ),
        (
            "categorical_encoder",
            pp.CategoricalEncoder(variables=config.CATEGORICAL_VARS),
        ),
        (
            "log_transformer",
            pp.LogTransformer(variables=config.NUMERICAL_LOG_VARS),
        ),
        (
            "scaler",
            MinMaxScaler()
        ),
        (
            "Liner_model",
            Lasso(alpha=0.005, random_state=0)
        )
    ]
)