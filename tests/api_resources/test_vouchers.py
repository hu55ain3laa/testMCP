# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from testmcp import Testmcp, AsyncTestmcp
from tests.utils import assert_matches_type
from testmcp.types import VoucherCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVouchers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Testmcp) -> None:
        voucher = client.vouchers.create(
            voucher_date="2025-02-01T00:00:00.000Z",
            voucher_reference="JV 1",
            voucher_type="JV",
            api_key="apiKey",
        )
        assert_matches_type(VoucherCreateResponse, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Testmcp) -> None:
        voucher = client.vouchers.create(
            voucher_date="2025-02-01T00:00:00.000Z",
            voucher_reference="JV 1",
            voucher_type="JV",
            api_key="apiKey",
            date_format="yyyy-MM-dd",
            delete_voucher_id="1234",
            voucher_description="very important voucher",
            voucher_details=[
                {
                    "account_number": "7011000000001",
                    "currency_code": "USD",
                    "type": "d",
                    "amount": 10,
                    "amount_fbc": 10,
                    "amount_sbc": 10,
                }
            ],
        )
        assert_matches_type(VoucherCreateResponse, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Testmcp) -> None:
        response = client.vouchers.with_raw_response.create(
            voucher_date="2025-02-01T00:00:00.000Z",
            voucher_reference="JV 1",
            voucher_type="JV",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = response.parse()
        assert_matches_type(VoucherCreateResponse, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Testmcp) -> None:
        with client.vouchers.with_streaming_response.create(
            voucher_date="2025-02-01T00:00:00.000Z",
            voucher_reference="JV 1",
            voucher_type="JV",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = response.parse()
            assert_matches_type(VoucherCreateResponse, voucher, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVouchers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTestmcp) -> None:
        voucher = await async_client.vouchers.create(
            voucher_date="2025-02-01T00:00:00.000Z",
            voucher_reference="JV 1",
            voucher_type="JV",
            api_key="apiKey",
        )
        assert_matches_type(VoucherCreateResponse, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTestmcp) -> None:
        voucher = await async_client.vouchers.create(
            voucher_date="2025-02-01T00:00:00.000Z",
            voucher_reference="JV 1",
            voucher_type="JV",
            api_key="apiKey",
            date_format="yyyy-MM-dd",
            delete_voucher_id="1234",
            voucher_description="very important voucher",
            voucher_details=[
                {
                    "account_number": "7011000000001",
                    "currency_code": "USD",
                    "type": "d",
                    "amount": 10,
                    "amount_fbc": 10,
                    "amount_sbc": 10,
                }
            ],
        )
        assert_matches_type(VoucherCreateResponse, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.vouchers.with_raw_response.create(
            voucher_date="2025-02-01T00:00:00.000Z",
            voucher_reference="JV 1",
            voucher_type="JV",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voucher = await response.parse()
        assert_matches_type(VoucherCreateResponse, voucher, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTestmcp) -> None:
        async with async_client.vouchers.with_streaming_response.create(
            voucher_date="2025-02-01T00:00:00.000Z",
            voucher_reference="JV 1",
            voucher_type="JV",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voucher = await response.parse()
            assert_matches_type(VoucherCreateResponse, voucher, path=["response"])

        assert cast(Any, response.is_closed) is True
