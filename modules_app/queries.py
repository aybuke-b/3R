import polars as pl


def create_context() -> pl.SQLContext:
    """`create_context`: Permet de créer un contexte `SQL` pour permettre de requêter un dataframe avec du SQL.

    `Returns`
    --------- ::

        _type_

    `Example(s)`
    ---------

    >>> create_context()
    ... #_test_return_"""
    return pl.SQLContext()


def execute_query_phone(
    context: pl.SQLContext,
    df: pl.DataFrame,
    column: str,
    model: str,
    storage: str,
    color: str,
) -> str | float:
    """`query_single_phone`: Utilise le contexte `SQL` pour sélectionner une colonne du dataframe filtrée sur :

    - Le modèle sélectionné par l'utilisateur
    - Le stockage sélectionné par l'utilisateur
    - La couleur sélectionnée par l'utilisateur

    Ensuite, les résultats de la requête sont collectés.

    /!\\ La combinaison de ces 3 colonnes devrait créer une clé unique
    mais il existe cependant des doublons dans les données, ce qui explique l'utilisation de
    `.item(0, 0)` pour filtrer ces doublons.

    ---------
    `Parameters`
    --------- ::

        context (pl.SQLContext): # Le contexte SQL
        df (pl.DataFrame): # Le DataFrame à requêter
        column (str): # La colonne à sélectionner
        model (str): # Le modèle de téléphone
        storage (str): # Le stockage du téléphone
        color (str): # La couleur du téléphone

    `Returns`
    --------- ::

        str | float

    `Example(s)`
    ---------

    >>> execute_query_phone()
    ... #_test_return_"""

    if (
        df.schema[column] == pl.Boolean
    ):  # Si la colonne est booléenne, on fait d'abord un CASE WHEN
        query_result = (
            context.register("df", df)
            .execute(
                f"""
            SELECT 
                CASE WHEN {column} = True 
                THEN 'Oui' 
                ELSE 'Non' 
                END 
            FROM 
                df 
            WHERE 
                model = '{model}' 
            AND 
                storage = CAST({storage} AS FLOAT) 
            AND 
                color = '{color}'
            """
            )
            .collect()
            .item(0, 0)
        )
    else:
        query_result = (
            context.register("df", df)
            .execute(
                f"""
                SELECT 
                    {column} 
                FROM 
                    df 
                WHERE 
                    model = '{model}' 
                AND 
                    storage = CAST({storage} AS FLOAT) 
                AND
                    color = '{color}'
                """
            )
            .collect()
            .item(0, 0)
        )
    return query_result
