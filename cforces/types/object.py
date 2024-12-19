from abc import ABC, abstractmethod
from typing import Dict, Any


class Object(ABC):
    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            if k not in self.__slots__:
                raise KeyError(
                    "Object '" + str(self.__class__) + "' has no key '" + k + "'"
                )

            setattr(self, k, v)

    @staticmethod
    @abstractmethod
    def from_dict(raw_data: Dict[str, Any]) -> "Object":
        return Object()

    def __repr__(self):
        output: str = "cforces.types<" + self.__class__.__name__ + ">"
        data: Dict[str, Any] = {}

        for slot in self.__slots__:
            if hasattr(self, slot):
                data[slot] = getattr(self, slot)

            else:
                data[slot] = None

        return output + str(data)
