from typing import Dict, Any, TypeVar, List, Type

T = TypeVar("T")


def cc2sc(input_dict: Dict[str, Any]) -> Dict[str, Any]:
    output: Dict[str, Any] = {}
    for key in input_dict.keys():
        parsed_key: str = ""
        for e in key:
            if e.isupper():
                parsed_key += "_"
                e = e.lower()

            parsed_key += e

        output[parsed_key] = input_dict[key]
    return output


def parse_type_list(input_list: List[Dict[str, Any]], output_type: Type[T]) -> List[T]:
    output: List[output_type] = []
    iterator: Dict[str, Any]

    for iterator in input_list:
        output.append(output_type.from_dict(cc2sc(iterator)))

    return output
