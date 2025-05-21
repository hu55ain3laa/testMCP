# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from testmcp import Testmcp, AsyncTestmcp
from tests.utils import assert_matches_type
from testmcp.types import (
    AttendanceCreateResponse,
    AttendanceDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttendance:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Testmcp) -> None:
        attendance = client.attendance.create(
            body=[
                [
                    {
                        "employee_code": "1234",
                        "machine_name": "office",
                        "status": "IN",
                        "timestamp": "2025-05-06T08:14:00.000Z",
                    }
                ]
            ],
            api_key="apiKey",
        )
        assert_matches_type(AttendanceCreateResponse, attendance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Testmcp) -> None:
        response = client.attendance.with_raw_response.create(
            body=[
                [
                    {
                        "employee_code": "1234",
                        "machine_name": "office",
                        "status": "IN",
                        "timestamp": "2025-05-06T08:14:00.000Z",
                    }
                ]
            ],
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attendance = response.parse()
        assert_matches_type(AttendanceCreateResponse, attendance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Testmcp) -> None:
        with client.attendance.with_streaming_response.create(
            body=[
                [
                    {
                        "employee_code": "1234",
                        "machine_name": "office",
                        "status": "IN",
                        "timestamp": "2025-05-06T08:14:00.000Z",
                    }
                ]
            ],
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attendance = response.parse()
            assert_matches_type(AttendanceCreateResponse, attendance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Testmcp) -> None:
        attendance = client.attendance.delete(
            employee_codes="employeeCodes",
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
        )
        assert_matches_type(AttendanceDeleteResponse, attendance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Testmcp) -> None:
        response = client.attendance.with_raw_response.delete(
            employee_codes="employeeCodes",
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attendance = response.parse()
        assert_matches_type(AttendanceDeleteResponse, attendance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Testmcp) -> None:
        with client.attendance.with_streaming_response.delete(
            employee_codes="employeeCodes",
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attendance = response.parse()
            assert_matches_type(AttendanceDeleteResponse, attendance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAttendance:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTestmcp) -> None:
        attendance = await async_client.attendance.create(
            body=[
                [
                    {
                        "employee_code": "1234",
                        "machine_name": "office",
                        "status": "IN",
                        "timestamp": "2025-05-06T08:14:00.000Z",
                    }
                ]
            ],
            api_key="apiKey",
        )
        assert_matches_type(AttendanceCreateResponse, attendance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.attendance.with_raw_response.create(
            body=[
                [
                    {
                        "employee_code": "1234",
                        "machine_name": "office",
                        "status": "IN",
                        "timestamp": "2025-05-06T08:14:00.000Z",
                    }
                ]
            ],
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attendance = await response.parse()
        assert_matches_type(AttendanceCreateResponse, attendance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTestmcp) -> None:
        async with async_client.attendance.with_streaming_response.create(
            body=[
                [
                    {
                        "employee_code": "1234",
                        "machine_name": "office",
                        "status": "IN",
                        "timestamp": "2025-05-06T08:14:00.000Z",
                    }
                ]
            ],
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attendance = await response.parse()
            assert_matches_type(AttendanceCreateResponse, attendance, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncTestmcp) -> None:
        attendance = await async_client.attendance.delete(
            employee_codes="employeeCodes",
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
        )
        assert_matches_type(AttendanceDeleteResponse, attendance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.attendance.with_raw_response.delete(
            employee_codes="employeeCodes",
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attendance = await response.parse()
        assert_matches_type(AttendanceDeleteResponse, attendance, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTestmcp) -> None:
        async with async_client.attendance.with_streaming_response.delete(
            employee_codes="employeeCodes",
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attendance = await response.parse()
            assert_matches_type(AttendanceDeleteResponse, attendance, path=["response"])

        assert cast(Any, response.is_closed) is True
