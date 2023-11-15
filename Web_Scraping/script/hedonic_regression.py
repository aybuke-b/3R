import statsmodels.formula.api as smf
import statsmodels.formula as sm
from dataclasses import dataclass
import polars as pl
from statsmodels.regression.linear_model import RegressionResultsWrapper


@dataclass
class Formula:
    formula: str


def formula(y: str, X: list[str]):
    y = y
    X = " + ".join(X)
    f = f"{y} ~ {X}"
    return Formula(f)


def execute_ols(df: pl.DataFrame, f: Formula) -> RegressionResultsWrapper:
    ols_model = smf.ols(
        formula=f.formula,
        data=df,
    )
    res = ols_model.fit()
    return res


def feature_importance(df: pl.DataFrame, y: str):
    column_name = list()
    r2_list = list()
    bic_list = list()
    for column in df.columns:
        if column == y:
            pass
        else:
            ols_model = smf.ols(formula=f"{y}~{column}", data=df)
            res = ols_model.fit()
            column_name.append(column)
            r2_list.append(res.rsquared)
            bic_list.append(res.bic)

    feature_imp_df = pl.DataFrame(
        {"Column": column_name, "R2": r2_list, "BIC": bic_list}
    ).sort("R2", descending=True)
    return feature_imp_df
