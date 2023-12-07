from dataclasses import dataclass


@dataclass
class GodSon:
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
        print(f"Specialities: {self._specialities}\n")

    @classmethod
    def factory(cls, mail, name, sex, number, level, specialities) -> "GodSon":
        name = name.upper()
        return cls(mail, name, sex, number, level, specialities)
