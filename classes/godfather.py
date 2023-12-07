from dataclasses import dataclass


@dataclass
class GodFather:
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
    def factory(cls, mail, name, sex, number, level, speciality) -> "GodFather":
        name = name.upper()
        return cls(mail, name, sex, number, level, speciality)
