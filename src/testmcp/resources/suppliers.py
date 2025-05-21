# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import supplier_create_params, supplier_update_params
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
from ..types.supplier_create_response import SupplierCreateResponse
from ..types.supplier_update_response import SupplierUpdateResponse

__all__ = ["SuppliersResource", "AsyncSuppliersResource"]


class SuppliersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SuppliersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/testmcp-python#accessing-raw-response-data-eg-headers
        """
        return SuppliersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SuppliersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/testmcp-python#with_streaming_response
        """
        return SuppliersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        api_key: str,
        city: str | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        comm_reg_number: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        phone1: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupplierCreateResponse:
        """
        Save New Supplier

        Args:
          name: Supplier Name

          city: Supplier City

          code: Numeric Supplier Code

          comm_reg_number: Supplier Commercial Registration Number

          email: Supplier Email

          phone1: Supplier Phone 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._post(
            "/suppliers/",
            body=maybe_transform(
                {
                    "name": name,
                    "city": city,
                    "code": code,
                    "comm_reg_number": comm_reg_number,
                    "email": email,
                    "phone1": phone1,
                },
                supplier_create_params.SupplierCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupplierCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        api_key: str,
        city: str | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        comm_reg_number: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        phone1: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupplierUpdateResponse:
        """
        Update Supplier

        Args:
          city: Supplier City

          code: Numeric Supplier Code

          comm_reg_number: Supplier Commercial Registration Number

          email: Supplier Email

          name: Supplier Name

          phone1: Supplier Phone 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._put(
            f"/suppliers/{id}",
            body=maybe_transform(
                {
                    "city": city,
                    "code": code,
                    "comm_reg_number": comm_reg_number,
                    "email": email,
                    "name": name,
                    "phone1": phone1,
                },
                supplier_update_params.SupplierUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupplierUpdateResponse,
        )


class AsyncSuppliersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSuppliersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/testmcp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSuppliersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSuppliersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/testmcp-python#with_streaming_response
        """
        return AsyncSuppliersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        api_key: str,
        city: str | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        comm_reg_number: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        phone1: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupplierCreateResponse:
        """
        Save New Supplier

        Args:
          name: Supplier Name

          city: Supplier City

          code: Numeric Supplier Code

          comm_reg_number: Supplier Commercial Registration Number

          email: Supplier Email

          phone1: Supplier Phone 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._post(
            "/suppliers/",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "city": city,
                    "code": code,
                    "comm_reg_number": comm_reg_number,
                    "email": email,
                    "phone1": phone1,
                },
                supplier_create_params.SupplierCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupplierCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        api_key: str,
        city: str | NotGiven = NOT_GIVEN,
        code: str | NotGiven = NOT_GIVEN,
        comm_reg_number: str | NotGiven = NOT_GIVEN,
        email: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        phone1: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SupplierUpdateResponse:
        """
        Update Supplier

        Args:
          city: Supplier City

          code: Numeric Supplier Code

          comm_reg_number: Supplier Commercial Registration Number

          email: Supplier Email

          name: Supplier Name

          phone1: Supplier Phone 1

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._put(
            f"/suppliers/{id}",
            body=await async_maybe_transform(
                {
                    "city": city,
                    "code": code,
                    "comm_reg_number": comm_reg_number,
                    "email": email,
                    "name": name,
                    "phone1": phone1,
                },
                supplier_update_params.SupplierUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SupplierUpdateResponse,
        )


class SuppliersResourceWithRawResponse:
    def __init__(self, suppliers: SuppliersResource) -> None:
        self._suppliers = suppliers

        self.create = to_raw_response_wrapper(
            suppliers.create,
        )
        self.update = to_raw_response_wrapper(
            suppliers.update,
        )


class AsyncSuppliersResourceWithRawResponse:
    def __init__(self, suppliers: AsyncSuppliersResource) -> None:
        self._suppliers = suppliers

        self.create = async_to_raw_response_wrapper(
            suppliers.create,
        )
        self.update = async_to_raw_response_wrapper(
            suppliers.update,
        )


class SuppliersResourceWithStreamingResponse:
    def __init__(self, suppliers: SuppliersResource) -> None:
        self._suppliers = suppliers

        self.create = to_streamed_response_wrapper(
            suppliers.create,
        )
        self.update = to_streamed_response_wrapper(
            suppliers.update,
        )


class AsyncSuppliersResourceWithStreamingResponse:
    def __init__(self, suppliers: AsyncSuppliersResource) -> None:
        self._suppliers = suppliers

        self.create = async_to_streamed_response_wrapper(
            suppliers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            suppliers.update,
        )
