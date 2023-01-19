import json
from dataclasses import dataclass
from datetime import datetime
from random import shuffle, choice
from typing import List

import pandas as pd


# ===================== GODFATHER SECTION ==============================================================
@dataclass
class Godfather:
    _mail: str
    _name: str
    _sex: str
    _number: str
    _level: str
    _speciality: str

    @property
    def mail(self) -> str:
        return self._mail

    @property
    def name(self) -> str:
        return self._name

    @property
    def sex(self) -> str:
        return self._sex

    @property
    def number(self) -> str:
        return self._number

    @property
    def level(self) -> str:
        return self._level

    @property
    def speciality(self) -> str:
        return self._speciality

    def object_description(self):
        print("Godfather description:")
        print(f"Mail: {self.mail}")
        print(f"Name: {self.name}")
        print(f"Sex: {self.sex}")
        print(f"Number: {self.number}")
        print(f"Level: {self.level}")
        print(f"Speciality: {self.speciality}\n")

    @classmethod
    def factory(cls, mail, name, sex, number, level, speciality) -> "Godfather":
        name = name.upper()
        return cls(mail, name, sex, number, level, speciality)


df_godfather = pd.read_csv("Parrains.csv", sep=",")

GODFATHERS = []
for index, row in df_godfather.iterrows():
    godfather = Godfather.factory(
        mail=row["Adresse e-mail"],
        name=row["Nom(s) et Prénom(s) "],
        sex=row["Sexe"],
        number=row["Numéro de téléphone "],
        level=row["Niveau académique "],
        speciality=row["Spécialité "],
    )
    # print(index)
    # godfather.object_description()
    GODFATHERS.append(godfather)


# ======================================================================================================

# ===================== GODSON SECTION =================================================================

@dataclass
class Godson:
    _mail: str
    _name: str
    _sex: str
    _number: str
    _level: str
    _specialities: list

    @property
    def mail(self) -> str:
        return self._mail

    @property
    def name(self) -> str:
        return self._name

    @property
    def sex(self) -> str:
        return self._sex

    @property
    def number(self) -> str:
        return self._number

    @property
    def level(self) -> str:
        return self._level

    @property
    def specialities(self) -> list:
        return self._specialities

    def object_description(self):
        print("Godson description:")
        print(f"Mail: {self._mail}")
        print(f"Name: {self._name}")
        print(f"Sex: {self._sex}")
        print(f"Number: {self._number}")
        print(f"Level: {self._level}")
        print(f"Specialities: {self._specialities}")

    @classmethod
    def factory(cls, mail, name, sex, number, level, speciality) -> "Godson":
        name = name.upper()
        return cls(mail, name, sex, number, level, speciality)


df_godson = pd.read_csv("Filleuls.csv", sep=",")

GODSONS = []
for index, row in df_godson.iterrows():
    # print(index)
    # Check specialities' compliance
    # Convert each selected speciality to list of string
    specialities = row["Future Spécialité "].split(",")
    # print("PHASE 1")
    # print(specialities)

    # Remove all spaces
    specialities = [speciality.strip() for speciality in specialities]
    # print("PHASE 2")
    # print(specialities)

    # Remove all empty strings
    specialities = [speciality for speciality in specialities if speciality != ""]
    # print("PHASE 3")
    # print(specialities)

    # Take only valid specialities
    specialities = [speciality for speciality in specialities if
                    speciality in ("Génie Logiciel", "Sécurité Informatique", "Réseau", "Data Science")]
    # print("PHASE 4")
    # print(specialities)

    godson = Godson.factory(
        mail=row["Adresse e-mail"],
        name=row["Nom(s) et Prénom(s) "],
        sex=row["Sexe"],
        number=row["Numéro de téléphone "],
        level=row["Niveau académique "],
        speciality=specialities,
    )

    # godson.object_description()
    GODSONS.append(godson)

# ======================================================================================================

# ===================== SPONSORSHIP SECTION ============================================================

print(f"Number of godfathers: {len(GODFATHERS)}")
print(f"Number of godsons: {len(GODSONS)}")
print(f"Godson by godfather: {len(GODSONS) // len(GODFATHERS)}\n")
NUMBER_OF_GODSONS_BY_GODFATHER = len(GODSONS) // len(GODFATHERS)


@dataclass
class Sponsorship:
    _godfather: Godfather
    _godsons: List[Godson]

    @property
    def godfather(self) -> Godfather:
        return self._godfather

    @property
    def godsons(self) -> List[Godson]:
        return self._godsons

    def object_description(self):
        print("Sponsorship description:")
        print(f"Godfather: {self.godfather.name}")
        print(f"Godsons: {[son.name for son in self.godsons]}")
        print(f"Length of godsons: {len(self.godsons)}\n")

    def toJSON(self) -> dict:
        return {
            "godfather": self.godfather.name,
            "godsons": [son.name for son in self.godsons]
        }

    @classmethod
    def factory(cls, mfather, mgodsons) -> "Sponsorship":
        return cls(mfather, mgodsons)


SPONSORSHIPS = []
for father in GODFATHERS:
    godsons = []

    spec = father.speciality  # Retrieve the father speciality
    # Retrieve sons who have selected the father speciality
    sons_speciality = [son for son in GODSONS if spec in son.specialities]
    if sons_speciality:
        # Retrieve sons who take only the father speciality
        sons_spec_unique = [son for son in sons_speciality if len(son.specialities) == 1]
        if sons_spec_unique:
            # Shuffle the list
            shuffle(sons_spec_unique)
            while len(godsons) < NUMBER_OF_GODSONS_BY_GODFATHER and len(sons_spec_unique) > 0:
                godsons.append(sons_spec_unique.pop())
                sons_speciality.remove(godsons[-1])
                GODSONS.remove(godsons[-1])

        else:
            # Shuffle the list
            shuffle(sons_speciality)
            while len(godsons) < NUMBER_OF_GODSONS_BY_GODFATHER and len(sons_speciality) > 0:
                godsons.append(sons_speciality.pop())
                GODSONS.remove(godsons[-1])

    else:
        # Retrieve sons who have no speciality selected
        sons_no_spec = [son for son in GODSONS if len(son.specialities) == 0]
        if sons_no_spec:
            # Shuffle the list
            shuffle(sons_no_spec)
            while len(godsons) < NUMBER_OF_GODSONS_BY_GODFATHER and len(sons_no_spec) > 0:
                godsons.append(sons_no_spec.pop())
                GODSONS.remove(godsons[-1])

        # Do this when all last conditions are not satisfied
        else:
            # Shuffle the list
            shuffle(GODSONS)
            while len(godsons) < NUMBER_OF_GODSONS_BY_GODFATHER and len(GODSONS) > 0:
                godsons.append(GODSONS.pop())

    # Create the sponsorship
    sponsorship = Sponsorship.factory(father, godsons)
    # sponsorship.object_description()
    SPONSORSHIPS.append(sponsorship)

# Operation to check if all godsons have been assigned to a godfather and complete godfather who have less than 5
# godsons
if len(GODSONS) > 0:
    # Retrieve the godfathers who have less than 5 godsons
    fathers = [father for father in SPONSORSHIPS if len(father.godsons) < 5]
    for father in fathers:
        while len(father.godsons) < NUMBER_OF_GODSONS_BY_GODFATHER and len(GODSONS) > 0:
            father.godsons.append(GODSONS.pop())
        # father.object_description()

# Operation to do when we have godsons again after the previous operation
if len(GODSONS) > 0:
    shuffle(SPONSORSHIPS)
    while len(GODSONS) > 0:
        sponsorship = choice(SPONSORSHIPS)
        sponsorship.godsons.append(GODSONS.pop())
        # sponsorship.object_description()

# Count assigned godsons
count = 0
# for sponsorship in SPONSORSHIPS:
#     sponsorship.object_description()
#     count += len(sponsorship.godsons)
#
# print(f"Number of godsons assigned: {count}\n")

# ======================================================================================================

# ===================== JSON GENERATION SECTION ========================================================


# Function who will be used to sort the list of sponsorship by godfather name
def extract_name(json_file):
    try:
        return json_file["godfather"]
    except KeyError:
        return "No name"


SPONSORSHIPS_JSON = [sponsorship.toJSON() for sponsorship in SPONSORSHIPS]

# Sort the list of sponsorship by godfather name
SPONSORSHIPS_JSON.sort(key=extract_name)
print(json.dumps(SPONSORSHIPS_JSON, indent=4, ensure_ascii=False))

# Generate the json file
with open(f"sponsorships_{datetime.now().timestamp()}.json", "w") as file:
    json.dump(SPONSORSHIPS_JSON, file, indent=4, ensure_ascii=False)
