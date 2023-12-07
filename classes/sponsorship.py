from dataclasses import dataclass
from typing import List

from .godfather import GodFather
from .godson import GodSon


@dataclass
class Sponsorship:
    _godfather: GodFather
    _godsons: List[GodSon]

    @property
    def godfather(self) -> GodFather:
        return self._godfather

    @property
    def godsons(self) -> List[GodSon]:
        return self._godsons

    def object_description(self):
        print("Sponsorship description:")
        print(f"Godfather: {self.godfather.name} ({self.godfather.sex[0]})")
        print("Godsons:", [f"{son.name} ({son.sex[0]})" for son in self.godsons])
        print(f"Length of godsons: {len(self.godsons)}\n")

    def toJSON(self) -> dict:
        return {
            "godfather": {"name": self.godfather.name, "sex": self.godfather.sex},
            "godsons": [{"name": son.name, "sex": son.sex} for son in self.godsons],
        }

    @classmethod
    def factory(cls, mfather, mgodsons) -> "Sponsorship":
        return cls(mfather, mgodsons)
