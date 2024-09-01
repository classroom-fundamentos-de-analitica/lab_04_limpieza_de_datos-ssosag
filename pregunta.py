"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""

import pandas as pd


def clean_data():

    def load_data():
        df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
        return df

    def clean_sexo_column(df):
        df = df.copy()
        df.sexo = df.sexo.str.lower()
        return df

    def clean_tipo_de_emprendimiento_column(df):
        df = df.copy()
        df["tipo_de_emprendimiento"] = df["tipo_de_emprendimiento"].str.lower()
        return df

    def clean_barrio_column(df):
        df = df.copy()
        df["barrio"] = df["barrio"].str.lower()
        return df

    def clean_idea_negocio_column(df):
        df = df.copy()
        df["idea_negocio"] = df["idea_negocio"].str.lower().str.strip()
        return df

    def clean_linea_credito_column(df):
        df = df.copy()
        df["línea_credito"] = df["línea_credito"].str.lower().str.strip()
        return df

    def clean_comuna_ciudadano_column(df):
        df = df.copy()
        df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
        return df

    def clean_fecha_de_beneficio_column(df):
        df = df.copy()
        df["fecha_de_beneficio"] = pd.to_datetime(
            df.fecha_de_beneficio, format="%d/%m/%Y", errors="coerce"
        ).fillna(
            pd.to_datetime(df.fecha_de_beneficio, format="%Y/%m/%d", errors="coerce")
        )
        return df

    def clean_monto_del_credito_column(df):
        df = df.copy()
        df.monto_del_credito = df.monto_del_credito.str.rstrip()
        df.monto_del_credito = df.monto_del_credito.replace("[,$]", "", regex=True)
        df.monto_del_credito = df.monto_del_credito.replace("(\\.00$)", "", regex=True)
        df.monto_del_credito = df.monto_del_credito.astype(float)
        return df

    df = load_data()
    df = df.replace("-", " ", regex=True).replace("_", " ", regex=True)
    df = clean_sexo_column(df)
    df = clean_tipo_de_emprendimiento_column(df)
    df = clean_barrio_column(df)
    df = clean_idea_negocio_column(df)
    df = clean_linea_credito_column(df)
    df = clean_comuna_ciudadano_column(df)
    df = clean_fecha_de_beneficio_column(df)
    df = clean_monto_del_credito_column(df)
    df = df.drop_duplicates().dropna()
    return df
