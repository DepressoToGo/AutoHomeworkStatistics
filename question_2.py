import pandas as pd
import math
import scipy as sp


def question_a(colonne_kilometres: pd.DataFrame):
    print("a)",end="")
    mu0 = 57000
    alpha = 0.05
    n = colonne_kilometres.index.size
    moyenne_echantillon = colonne_kilometres.mean()
    ecart_type_echantillon = colonne_kilometres.std()
    decision = test_unilateral_droit(mu0, alpha, n, moyenne_echantillon, ecart_type_echantillon)
    confirmation = confirmation_test_droit(mu0, alpha, n, moyenne_echantillon, ecart_type_echantillon)
    if decision:
        print("Le nombre moyen de kilomètres parcourus par une voiture du marché indien est supérieur à 57000 km", end="")
        if decision_comfortable(decision, confirmation):
            print(" et nous sommes confortable avec cette décision.")
        else:
            print(" et nous ne sommes pas confortable avec cette décision.")
    else:
        print("Le nombre moyen de kilomètres parcourus par une voiture du marché indien n'est pas supérieur à 57000 km", end="")
        if decision_comfortable(decision, confirmation):
            print(" et nous sommes confortable avec cette décision.")
        else:
            print(" et nous ne sommes pas confortable avec cette décision.")
    return


def question_b(colonne_cylindree: pd.DataFrame):
    print("b)", end="")
    mu0 = 1660
    alpha = 0.05
    n = colonne_cylindree.index.size
    moyenne_echantillon = colonne_cylindree.mean()
    ecart_type_echantillon = colonne_cylindree.std()
    decision = test_unilateral_gauche(mu0, alpha, n, moyenne_echantillon, ecart_type_echantillon)
    confirmation = confirmation_test_gauche(mu0, alpha, n, moyenne_echantillon, ecart_type_echantillon)
    if decision:
        print("La cylindrée moyenne d'une voiture du marché indien est inférieure à 1660 cm3", end="")
        if decision_comfortable(decision, confirmation):
            print(" et nous sommes confortable avec cette décision.")
        else:
            print(" et nous ne sommes pas confortable avec cette décision.")
    else:
        print("La cylindrée moyenne d'une voiture du marché indien n'est pas inférieure à 1660 cm3", end="")
        if decision_comfortable(decision, confirmation):
            print(" et nous sommes confortable avec cette décision.")
        else:
            print(" et nous ne sommes pas confortable avec cette décision.")
    return


def question_c(df: pd.DataFrame):
    print("c)", end="")
    mu0 = 110
    mu = 110
    alpha = 0.05
    alphademi = alpha / 2.0
    n = df.index.size
    moyenne_echantillon = df.mean()
    ecart_type_echantillon = df.std()
    h0 = mu == mu0
    h1 = mu != mu0
    decision = test_bilateral(mu0, alphademi, n, moyenne_echantillon, ecart_type_echantillon)
    confirmation = confirmation_test_bilateral(mu0, alpha, n, moyenne_echantillon, ecart_type_echantillon)
    if decision:
        print("La puissance moyenne de frein d'une voiture du marché indien est différente de 110 bhp", end="")
        if(decision_comfortable(decision,confirmation)):
            print(" et nous sommes confortable avec cette décision.")
        else:
            print(" et nous ne sommes pas confortable avec cette décision.")
    else:
        print("La puissance moyenne de frein d'une voiture du marché indien n'est pas différente de 110 bhp", end="")
        if decision_comfortable(decision, confirmation):
            print(" et nous sommes confortable avec cette décision.")
        else:
            print(" et nous ne sommes pas confortable avec cette décision.")
    return


def question_d(colonne_sieges: pd.DataFrame):
    print("d)", end="")
    mu0 = 5
    alpha = 0.05
    n = colonne_sieges.index.size
    moyenne_echantillon = colonne_sieges.mean()
    ecart_type_echantillon = colonne_sieges.std()
    decision = test_unilateral_droit(mu0, alpha, n, moyenne_echantillon, ecart_type_echantillon)
    confirmation = confirmation_test_droit(mu0, alpha, n, moyenne_echantillon, ecart_type_echantillon)
    if decision:
        print("Le nombre moyen de sièges d'une voiture du marché indien est supérieur à 5", end="")
        if(decision_comfortable(decision,confirmation)):
            print(" et nous sommes confortable avec cette décision.")
        else:
            print(" et nous ne sommes pas confortable avec cette décision.")
    else:
        print("Le nombre moyen de sièges d'une voiture du marché indien n'est pas supérieur à 5", end="")
        if decision_comfortable(decision, confirmation):
            print(" et nous sommes confortable avec cette décision.")
        else:
            print(" et nous ne sommes pas confortable avec cette décision.")
    return


def question_e(colonne_carburant: pd.DataFrame):
    print("e)", end="")
    n = colonne_carburant.index.size
    proportion_hypothese = 0.55
    proportion_observation = colonne_carburant.value_counts()['Diesel'] / n
    proportion_supposition = 0.55
    h0 = (proportion_supposition == proportion_hypothese)
    h1 = (proportion_supposition < proportion_hypothese)
    alpha = 0.05
    estimation_p = math.sqrt((proportion_hypothese * (1 - proportion_hypothese)) / n)
    decision = test_proportion_gauche(n, alpha, proportion_observation, proportion_hypothese)
    confirmation = confirmation_test_proportion_gauche(alpha, proportion_observation, proportion_hypothese,
                                                       estimation_p)
    if decision:
        print("La proportion de voitures à diesel du marché indien est inférieure à 55%", end="")
        if(decision_comfortable(decision,confirmation)):
            print(" et nous sommes confortable avec cette décision.")
        else:
            print(" et nous ne sommes pas confortable avec cette décision.")
    else:
        print("La proportion de voitures à diesel du marché indien n'est pas inférieure à 55%", end="")
        if decision_comfortable(decision, confirmation):
            print(" et nous sommes confortable avec cette décision.")
        else:
            print(" et nous ne sommes pas confortable avec cette décision.")
    return


def question_f(colonne_transmission: pd.DataFrame):
    print("f)", end="")
    n = colonne_transmission.index.size
    proportion_hypothese = 0.80
    proportion_observation = colonne_transmission.value_counts()['Manuelle'] / n
    proportion_supposition = 0.80
    h0 = (proportion_supposition == proportion_hypothese)
    h1 = (proportion_supposition != proportion_hypothese)
    alpha = 0.05
    alphademi = 0.05 / 2.0
    estimation_p = math.sqrt((proportion_hypothese * (1 - proportion_hypothese)) / n)
    decision = test_proportion_bilateral(n, alphademi, proportion_observation, proportion_hypothese)
    confirmation = confirmation_test_proportion_bilateral(alpha, proportion_observation, proportion_hypothese,
                                                          estimation_p)
    if decision:
        print("La proportion de voitures à transmission manuelle du marché indien est différente de 80%", end="")
        if(decision_comfortable(decision,confirmation)):
            print(" et nous sommes confortable avec cette décision.")
        else:
            print(" et nous ne sommes pas confortable avec cette décision.")
    else:
        print("La proportion de voitures à transmission manuelle du marché indien n'est pas différente de 80%", end="")
        if decision_comfortable(decision, confirmation):
            print(" et nous sommes confortable avec cette décision.")
        else:
            print(" et nous ne sommes pas confortable avec cette décision.")
    return


def decision_comfortable(decision: bool, confirmation: bool):
    confortable=False
    if(decision==confirmation):
        confortable=True
    return confortable


def test_proportion_gauche(n: int, alpha: float, proportion_observation: float, proportion_hypothese: float):
    rejetterh0 = False
    surface = 1 - alpha
    nb_sauts = sp.stats.norm.ppf(surface)
    estimation_p = math.sqrt((proportion_hypothese * (1 - proportion_hypothese)) / n)
    marge_erreur = nb_sauts * estimation_p
    val_critique = proportion_hypothese - marge_erreur
    if (proportion_observation <= val_critique):
        h0 = False
        h1 = True
        rejetterh0 = True
    return rejetterh0


def confirmation_test_proportion_gauche(alpha: float, proportion_observation: float, proportion_hypothese: float,
                                        estimation_p: float):
    confirmer_rejet_h0 = False
    alpha_p = sp.stats.norm.cdf(proportion_observation, loc=proportion_hypothese, scale=estimation_p)
    if (alpha_p < alpha):
        h0 = False
        h1 = True
        confirmer_rejet_h0 = True
    return confirmer_rejet_h0


def test_proportion_bilateral(n: int, alphademi: float, proportion_observation: float, proportion_hypothese: float):
    rejetterh0 = False
    surface = 1 - alphademi
    nb_sauts = sp.stats.norm.ppf(surface)
    estimation_p = math.sqrt((proportion_hypothese * (1 - proportion_hypothese)) / n)
    marge_erreur = nb_sauts * estimation_p
    val_critique_1 = proportion_hypothese - marge_erreur
    val_critique_2 = proportion_hypothese + marge_erreur
    if (proportion_observation <= val_critique_1 or proportion_observation >= val_critique_2):
        h0 = False
        h1 = True
        rejetterh0 = True
    return rejetterh0


def confirmation_test_proportion_bilateral(alpha: float, proportion_observation: float, proportion_hypothese: float,
                                           estimation_p: float):
    confirmer_rejet_h0 = False
    alpha_p_a = 1 - sp.stats.norm.cdf(proportion_observation, loc=proportion_hypothese, scale=estimation_p)
    alpha_p_b = sp.stats.norm.cdf(proportion_observation, loc=proportion_hypothese, scale=estimation_p)
    alpha_p = 2 * min(alpha_p_a, alpha_p_b)
    if (alpha_p < alpha):
        h0 = False
        h1 = True
        confirmer_rejet_h0 = True
    return confirmer_rejet_h0


def test_unilateral_droit(mu0: float, alpha: float, n: int, moyenne_echantillon: float, ecart_type_echantillon: float):
    rejetterh0 = False
    mu = mu0
    h0 = (mu == mu0)
    h1 = (mu > mu0)
    surface = 1 - alpha
    nb_sauts = sp.special.stdtrit(n - 1, surface)
    erreur_type = ecart_type_echantillon / (math.sqrt(n))
    marge_erreur = nb_sauts * erreur_type
    val_critique = mu0 + marge_erreur
    if (moyenne_echantillon >= val_critique):
        h0 = False
        h1 = True
        rejetterh0 = True
    return rejetterh0


def confirmation_test_droit(mu0: float, alpha: float, n: int, moyenne_echantillon: float,
                            ecart_type_echantillon: float):
    confirmer_rejet_h0 = False
    valeur = (moyenne_echantillon - mu0) / ecart_type_echantillon
    alpha_p = 1 - sp.stats.t.cdf(valeur, df=n - 1)
    if (alpha_p < alpha):
        h0 = False
        h1 = True
        confirmer_rejet_h0 = True
    return confirmer_rejet_h0


def test_unilateral_gauche(mu0: float, alpha: float, n: int, moyenne_echantillon: float, ecart_type_echantillon: float):
    rejetterh0 = False
    mu = mu0
    h0 = (mu == mu0)
    h1 = (mu < mu0)
    surface = 1 - alpha
    nb_sauts = sp.special.stdtrit(n - 1, surface)
    erreur_type = ecart_type_echantillon / (math.sqrt(n))
    marge_erreur = nb_sauts * erreur_type
    val_critique = mu0 - marge_erreur
    if (moyenne_echantillon <= val_critique):
        h0 = False
        h1 = True
        rejetterh0 = True
    return rejetterh0


def confirmation_test_gauche(mu0: float, alpha: float, n: int, moyenne_echantillon: float,
                             ecart_type_echantillon: float):
    confirmer_rejet_h0 = False
    valeur = (moyenne_echantillon - mu0) / ecart_type_echantillon
    alpha_p = sp.stats.t.cdf(valeur, df=n - 1)
    if (alpha_p < alpha):
        h0 = False
        h1 = True
        confirmer_rejet_h0 = True
    return confirmer_rejet_h0


def test_bilateral(mu0: float, alphademi: float, n: int, moyenne_echantillon: float, ecart_type_echantillon: float):
    rejetterh0 = False
    mu = mu0
    h0 = (mu == mu0)
    h1 = (mu != mu0)
    surface = 1 - alphademi
    nb_sauts = sp.special.stdtrit(n - 1, surface)
    erreur_type = ecart_type_echantillon / (math.sqrt(n))
    marge_erreur = nb_sauts * erreur_type
    val_critique_1 = mu0 - marge_erreur
    val_critique_2 = mu0 + marge_erreur
    if (moyenne_echantillon <= val_critique_1 or moyenne_echantillon >= val_critique_2):
        h0 = False
        h1 = True
        rejetterh0 = True
    return rejetterh0


def confirmation_test_bilateral(mu0: float, alpha: float, n: int, moyenne_echantillon: float,
                                ecart_type_echantillon: float):
    confirmer_rejet_h0 = False
    valeur = (moyenne_echantillon - mu0) / ecart_type_echantillon
    alpha_p = 2 * (1 - sp.stats.t.cdf(abs(valeur), df=n - 1))
    if (alpha_p < alpha):
        h0 = False
        h1 = True
        confirmer_rejet_h0 = True
    return confirmer_rejet_h0


if __name__ == '__main__':
    df = pd.read_excel("./classeurs/Voitures.xlsx")
    df.set_index('ID', inplace=True)
    df['Carburant'] = df['Carburant'].astype('category')
    df['Transmission'] = df['Transmission'].astype('category')

    question_a(df['Kilomètres'])
    question_b(df['Cylindrée'])
    question_c(df['Puissance'])
    question_d(df['Sièges'])
    question_e(df['Carburant'])
    question_f(df['Transmission'])
    print("\n")
    print(df)
