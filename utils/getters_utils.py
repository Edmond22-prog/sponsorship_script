import pandas as pd

from typing import Tuple, List

from classes.godfather import GodFather
from classes.godson import GodSon
from utils.formating_utils import _format_phone_number, _format_specialities


def retrieve_godfathers(
    filename, display: bool = False
) -> Tuple[List[GodFather], List[GodFather]]:
    df_godfather = pd.read_csv(filename, sep=",")

    validated = []
    unvalidated = []
    for _, row in df_godfather.iterrows():
        godfather = GodFather.factory(
            mail=row["Nom d'utilisateur"],
            name=row["Nom(s) et Prénom(s) "],
            sex=row["Sexe"],
            number=row["Numéro de téléphone "],
            level=row["Niveau académique "],
            speciality=row["Spécialité "],
        )
        if len(row["Motivation "]) < 5:
            unvalidated.append(godfather)
        else:
            validated.append(godfather)
    
    if display:
        # Display of godfathers
        print("=====| Display validated godfathers |=====")
        for idx, godfather in enumerate(validated):
            print(f"GodFather {idx+1}")
            godfather.object_description()

    return validated, unvalidated


def retrieve_godsons(
    filename, display: bool = False
) -> Tuple[List[GodSon], List[GodSon]]:
    df_godson = pd.read_csv(filename, sep=",")

    validated = []
    unvalidated = []
    for _, row in df_godson.iterrows():
        original_number = row["Numéro de téléphone "]
        phone_number = _format_phone_number(original_number)
        if phone_number.startswith("INVALID PHONE NUMBER"):
            godson = GodSon.factory(
                mail=row["Nom d'utilisateur"],
                name=row["Nom(s) et Prénom(s) "],
                sex=row["Sexe"],
                number=phone_number,
                level=row["Niveau académique "],
                specialities=_format_specialities(
                    row[
                        "Future spécialité. Vous pouvez choisir plusieurs, mais attention, ca jouera sur l'attribution de votre parrain/marraine"
                    ]
                ),
            )
            unvalidated.append(godson)

        else:
            godson = GodSon.factory(
                mail=row["Nom d'utilisateur"],
                name=row["Nom(s) et Prénom(s) "],
                sex=row["Sexe"],
                number=phone_number,
                level=row["Niveau académique "],
                specialities=_format_specialities(
                    row[
                        "Future spécialité. Vous pouvez choisir plusieurs, mais attention, ca jouera sur l'attribution de votre parrain/marraine"
                    ]
                ),
            )
            validated.append(godson)
    
    if display:
        # Display of godsons
        print("=====| Display validated godsons |=====")
        for idx, godson in enumerate(validated):
            print(f"GodSon {idx+1}")
            godson.object_description()

    return validated, unvalidated
