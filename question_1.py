import pandas as pd
import numpy as np
import math
import scipy as sp


def question_a():
    print("a) Population Infinie")
    return


def question_b(df: pd.DataFrame):
    print("b) L'échantillon est de taille", df.index.size)


def question_c(colonnes: pd.DataFrame):
    print("c)")
    for col in colonnes.select_dtypes(exclude='category'):
        s3_s4_sd = get_s3sd_s4sd(df[col])
        s3_sd = s3_s4_sd[0]
        s4_sd = s3_s4_sd[1]
        isnormal = isNormal(s3_sd, s4_sd)
        if not isnormal:
            print(
                "La variable {} ne suit pas la loi normale, car s3(sd)={:0.4f} et/ou s4(sd)={:0.4f} ne se situe(nt) pas dans l'intervalle [-2,2]".format(
                    colonnes[col].name, s3_sd, s4_sd))
        else:
            print(
                "La variable {} suit la loi normale, car s3(sd)={:0.4f} et/ou s4(sd)={:0.4f} se situe(nt) pas dans l'intervalle [-2,2]".format(
                    colonnes[col].name, s3_sd, s4_sd))
    return


def question_d(df: pd.DataFrame):
    n = df.index.size
    print("d) Il faut garantir que l'échantillon est suffisamment grand.")
    if (n >= 30):
        print("   Cette garantie est satisfaite, car le nombre d'observations dans l'échantillon(n=", n,
              ")est plus grand que 30")
    else:
        print("   Cette garantie n'est pas satisfaite, car le nombre d'observations dans l'échantillon(n=",
              n, ")est plus petit que 30")
    return


def question_e(colonnes: pd.DataFrame, confiance: float):
    print("e)")
    for col in colonnes.select_dtypes(exclude='category'):
        n = colonnes[col].index.size
        intervalle = moyenne_intervalle_confiance(n, confiance, colonnes[col].mean(), colonnes[col].std())
        print("La moyenne de {} se situe entre {:0.4f} et {:0.4f} avec {:0.4f}% de confiance".format(colonnes[col].name,
                                                                                                     intervalle[0],
                                                                                                     intervalle[1],
                                                                                                     confiance*100.0))
    return


def question_f():
    print("f)")
    print("Pour Carburant, la variable aléatoire de Bernouilli est la probabilité d'avoir une voiture avec Carburant Diesel")
    print("Pour Transmission, la variable aléatoire de Bernouilli d'avoir une voiture avec Transmission Automatique")
    return


def question_g(colonne_carburant: pd.DataFrame, confiance: float, variable_aleatoire: str):
    print("g) ")
    proportion_Diesel = estimer_proportion(colonne_carburant, variable_aleatoire)
    n = colonne_carburant.index.size

    intervalle = moyenne_intervalle_confiance_bernoulli(n, confiance, proportion_Diesel)

    if (intervalle is not False):
        print(
            "On estime que la probabilité d'avoir une voiture avec {} au {} se situe entre {:0.4f}% et {:0.4f}% avec {:0.4f}% de confiance".format(
                colonne_carburant.name, variable_aleatoire, intervalle[0] * 100.0, intervalle[1] * 100.0, confiance * 100.0))
    else:
        print("Les conditions d'applications de l'intervalle ne sont pas satisfaites.")
    return


def question_h(colonne_transmission: pd.DataFrame, confiance: float, variable_aleatoire: str):
    print("h)")
    proportion_Automatique = estimer_proportion(colonne_transmission, variable_aleatoire)
    n = colonne_transmission.index.size
    intervalle = moyenne_intervalle_confiance_bernoulli(n, confiance, proportion_Automatique)
    if (intervalle is not False):
        print(
            "On estime que la probabilité d'avoir une voiture avec {} {} se situe entre {:0.4f}% et {:0.4f}% avec {:0.4f}% de confiance".format(
                colonne_transmission.name, variable_aleatoire, (intervalle[0] * 100.0), (intervalle[1] * 100.0),
                (confiance * 100.0)))
    else:
        print("Les conditions d'applications de l'intervalle ne sont pas satisfaites.")
    return


def isNormal(s3_sd: float, s4_sd: float):
    return ((-2.0 <= s3_sd <= 2.0) and (-2.0 <= s4_sd <= 2.0))


def get_s3sd_s4sd(colonne: pd.DataFrame):
    n = colonne.index.size
    s3_sd = colonne.skew() / math.sqrt(6 / n)
    s4_sd = colonne.kurtosis() / math.sqrt(24 / n)
    return s3_sd, s4_sd


def moyenne_intervalle_confiance(n: int, confiance: float, moyenne: float, ecart_type: float):
    alpha = 1 - confiance
    alphademi = alpha / 2.0
    surface = confiance + alphademi
    nb_sauts = sp.special.stdtrit(n - 1, surface)
    erreur_type = ecart_type / (math.sqrt(n))
    marge_erreur = nb_sauts * erreur_type
    intervalle = [np.around(moyenne - marge_erreur, decimals=4), np.around(moyenne + marge_erreur, decimals=4)]
    return intervalle


def moyenne_intervalle_confiance_bernoulli(n: int, confiance: float, proportion: float):
    if (n >= 30 and n * proportion >= 5 and n * (1 - proportion) >= 5):
        alpha = 1 - confiance
        alphademi = alpha / 2.0
        surface = confiance + alphademi
        nb_sauts = sp.stats.norm.ppf(surface)
        estimation_p = math.sqrt((proportion * (1 - proportion)) / n)
        marge_erreur = nb_sauts * estimation_p
        intervalle = [np.around(proportion - marge_erreur, decimals=4),
                      np.around(proportion + marge_erreur, decimals=4)]
        return intervalle
    else:
        return False


def estimer_proportion(colonne: pd.DataFrame, variable_aleatoire: str):
    n = colonne.index.size
    nb_succes = colonne.value_counts()[variable_aleatoire]
    return nb_succes / n


if __name__ == '__main__':
    df = pd.read_excel("./classeurs/Voitures.xlsx")
    df.set_index('ID', inplace=True)
    df['Carburant'] = df['Carburant'].astype('category')
    df['Transmission'] = df['Transmission'].astype('category')

    question_a()
    question_b(df)
    question_c(df)
    question_d(df)
    question_e(df, 0.95)
    question_f()
    question_g(df['Carburant'], 0.95, 'Diesel')
    question_h(df['Transmission'], 0.95, 'Automatique')
    print("\n")
    print(df)
