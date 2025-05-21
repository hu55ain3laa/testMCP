# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import currency_get_rates_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.currency_get_rates_response import CurrencyGetRatesResponse

__all__ = ["CurrencyResource", "AsyncCurrencyResource"]


class CurrencyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CurrencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return CurrencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return CurrencyResourceWithStreamingResponse(self)

    def get_rates(
        self,
        *,
        date: str,
        from_currency_code: str,
        to_currency_code: str,
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CurrencyGetRatesResponse:
        """
        Get Currencies Rates

        Args:
          date: Date Of Conversion | Date Format : yyyy-MM-dd

          from_currency_code: Currency You Want To Convert From

          to_currency_code: Currency You Want To Convert To

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._get(
            "/currency/rates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "from_currency_code": from_currency_code,
                        "to_currency_code": to_currency_code,
                    },
                    currency_get_rates_params.CurrencyGetRatesParams,
                ),
            ),
            cast_to=CurrencyGetRatesResponse,
        )


class AsyncCurrencyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCurrencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return AsyncCurrencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return AsyncCurrencyResourceWithStreamingResponse(self)

    async def get_rates(
        self,
        *,
        date: str,
        from_currency_code: str,
        to_currency_code: str,
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CurrencyGetRatesResponse:
        """
        Get Currencies Rates

        Args:
          date: Date Of Conversion | Date Format : yyyy-MM-dd

          from_currency_code: Currency You Want To Convert From

          to_currency_code: Currency You Want To Convert To

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._get(
            "/currency/rates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "from_currency_code": from_currency_code,
                        "to_currency_code": to_currency_code,
                    },
                    currency_get_rates_params.CurrencyGetRatesParams,
                ),
            ),
            cast_to=CurrencyGetRatesResponse,
        )


class CurrencyResourceWithRawResponse:
    def __init__(self, currency: CurrencyResource) -> None:
        self._currency = currency

        self.get_rates = to_raw_response_wrapper(
            currency.get_rates,
        )


class AsyncCurrencyResourceWithRawResponse:
    def __init__(self, currency: AsyncCurrencyResource) -> None:
        self._currency = currency

        self.get_rates = async_to_raw_response_wrapper(
            currency.get_rates,
        )


class CurrencyResourceWithStreamingResponse:
    def __init__(self, currency: CurrencyResource) -> None:
        self._currency = currency

        self.get_rates = to_streamed_response_wrapper(
            currency.get_rates,
        )


class AsyncCurrencyResourceWithStreamingResponse:
    def __init__(self, currency: AsyncCurrencyResource) -> None:
        self._currency = currency

        self.get_rates = async_to_streamed_response_wrapper(
            currency.get_rates,
        )
