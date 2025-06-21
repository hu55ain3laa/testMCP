# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from testmcp import Testmcp, AsyncTestmcp
from tests.utils import assert_matches_type
from testmcp.types import CurrencyGetRatesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCurrency:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_rates(self, client: Testmcp) -> None:
        currency = client.currency.get_rates(
            date="date",
            from_currency_code="fromCurrencyCode",
            to_currency_code="toCurrencyCode",
            api_key="apiKey",
        )
        assert_matches_type(CurrencyGetRatesResponse, currency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_rates(self, client: Testmcp) -> None:
        response = client.currency.with_raw_response.get_rates(
            date="date",
            from_currency_code="fromCurrencyCode",
            to_currency_code="toCurrencyCode",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = response.parse()
        assert_matches_type(CurrencyGetRatesResponse, currency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_rates(self, client: Testmcp) -> None:
        with client.currency.with_streaming_response.get_rates(
            date="date",
            from_currency_code="fromCurrencyCode",
            to_currency_code="toCurrencyCode",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = response.parse()
            assert_matches_type(CurrencyGetRatesResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCurrency:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_rates(self, async_client: AsyncTestmcp) -> None:
        currency = await async_client.currency.get_rates(
            date="date",
            from_currency_code="fromCurrencyCode",
            to_currency_code="toCurrencyCode",
            api_key="apiKey",
        )
        assert_matches_type(CurrencyGetRatesResponse, currency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_rates(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.currency.with_raw_response.get_rates(
            date="date",
            from_currency_code="fromCurrencyCode",
            to_currency_code="toCurrencyCode",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        currency = await response.parse()
        assert_matches_type(CurrencyGetRatesResponse, currency, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_rates(self, async_client: AsyncTestmcp) -> None:
        async with async_client.currency.with_streaming_response.get_rates(
            date="date",
            from_currency_code="fromCurrencyCode",
            to_currency_code="toCurrencyCode",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            currency = await response.parse()
            assert_matches_type(CurrencyGetRatesResponse, currency, path=["response"])

        assert cast(Any, response.is_closed) is True
