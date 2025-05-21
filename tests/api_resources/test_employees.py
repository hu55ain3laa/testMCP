# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from testmcp import Testmcp, AsyncTestmcp
from tests.utils import assert_matches_type
from testmcp.types import EmployeeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEmployees:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Testmcp) -> None:
        employee = client.employees.list(
            api_key="apiKey",
        )
        assert_matches_type(EmployeeListResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Testmcp) -> None:
        employee = client.employees.list(
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(EmployeeListResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Testmcp) -> None:
        response = client.employees.with_raw_response.list(
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = response.parse()
        assert_matches_type(EmployeeListResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Testmcp) -> None:
        with client.employees.with_streaming_response.list(
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = response.parse()
            assert_matches_type(EmployeeListResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEmployees:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTestmcp) -> None:
        employee = await async_client.employees.list(
            api_key="apiKey",
        )
        assert_matches_type(EmployeeListResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTestmcp) -> None:
        employee = await async_client.employees.list(
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(EmployeeListResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.employees.with_raw_response.list(
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        employee = await response.parse()
        assert_matches_type(EmployeeListResponse, employee, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTestmcp) -> None:
        async with async_client.employees.with_streaming_response.list(
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            employee = await response.parse()
            assert_matches_type(EmployeeListResponse, employee, path=["response"])

        assert cast(Any, response.is_closed) is True
