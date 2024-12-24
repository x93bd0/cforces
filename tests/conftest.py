import json
import os
from random import randint

from cforces import Client, types
from typing import Dict, Any, Tuple, Optional, List, Type

import pytest
import glob


class MockedClient(Client):
    __slots__ = ("expected_method_name", "expected_params", "expected_output")
    expected_method_name: Optional[str]
    expected_params: Optional[Dict[str, Any]]
    expected_output: Optional[Any]

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.expected_method_name = None

    def expect_api_call(
        self, method_name: str, params: Dict[str, Any], expected_output: Any
    ) -> None:
        assert self.expected_method_name is None
        self.expected_method_name = method_name
        self.expected_params = params
        self.expected_output = expected_output

    async def api_call(
        self, method_name: str, params: Dict[str, Any], convert_case: bool = False
    ) -> Any:
        assert self.expected_method_name is not None
        assert self.expected_method_name == method_name
        assert self.expected_params == params
        self.expected_method_name = None
        return self.expected_output


class TestHelper:
    last_call_params: Dict[str, Any]
    client: MockedClient

    def __init__(self) -> None:
        self.client = MockedClient(None)

    @staticmethod
    def params_from_tuple(
        params: Tuple[str, ...], input_data: Tuple[Any, ...]
    ) -> Dict[str, Any]:
        output: Dict[str, Any] = {}
        for x in range(min(len(params), len(input_data))):
            output[params[x]] = input_data[x]
        return output

    @property
    def randno(self):
        return randint(1, 10**8)


@pytest.fixture()
def helper() -> TestHelper:
    return TestHelper()


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if "testdata" in metafunc.fixturenames:
        testdata: List[Tuple[Type, List[Any]]] = []
        path: str = os.path.join(os.path.dirname(__file__), "testdata")

        for file in os.listdir(path):
            file_path: str = os.path.join(path, file)

            with open(file_path) as inp:
                obj_type: Type = getattr(types, file.split("_", 1)[0])
                for obj in json.load(inp):
                    testdata.append((obj_type, obj))

        metafunc.parametrize("testdata", testdata)
