import enum
from typing import Dict, Any, get_type_hints, Type, Union, Tuple, TypeVar
from cforces import types, utils

T = TypeVar("T")


def type_test(obj: T, testdata: Dict[str, Any]) -> None:
    type_hints: Dict[str, Type] = get_type_hints(obj)

    for slot in obj.__slots__:
        assert slot in type_hints

        if isinstance(type_hints[slot], type):
            assert isinstance(getattr(obj, slot), type_hints[slot]), (
                "slot '"
                + slot
                + "' should have a[n] "
                + str(type_hints[slot])
                + " type, but it has a[n] "
                + str(type(getattr(obj, slot)))
                + " type"
            )

        if getattr(obj, slot) is None:
            continue

        camel_case_slot: str = utils.sc2cc_key(slot)

        if (
            isinstance(testdata[camel_case_slot], list)
            and len(getattr(obj, slot)) > 0
            and isinstance(getattr(obj, slot)[0], types.Object)
        ):
            for e in range(0, len(testdata[camel_case_slot])):
                type_test(getattr(obj, slot)[e], testdata[camel_case_slot][e])

        elif type(getattr(obj, slot)) == type(testdata[camel_case_slot]):
            assert getattr(obj, slot) == testdata[camel_case_slot]

        elif isinstance(getattr(obj, slot), enum.Enum):
            assert getattr(obj, slot).value == testdata[camel_case_slot]

        elif isinstance(getattr(obj, slot), types.Object):
            type_test(getattr(obj, slot), testdata[camel_case_slot])


def test_objects(testdata: Tuple[Type[T], Dict[str, Any]]) -> None:
    obj: T = testdata[0].from_dict(utils.cc2sc(testdata[1]))
    type_test(obj, testdata[1])
