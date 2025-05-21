# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date

import httpx

from ..types import purchase_quotation_list_params, purchase_quotation_create_params, purchase_quotation_update_params
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
from ..types.purchase_quotation_list_response import PurchaseQuotationListResponse
from ..types.purchase_quotation_create_response import PurchaseQuotationCreateResponse
from ..types.purchase_quotation_update_response import PurchaseQuotationUpdateResponse

__all__ = ["PurchaseQuotationsResource", "AsyncPurchaseQuotationsResource"]


class PurchaseQuotationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PurchaseQuotationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return PurchaseQuotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PurchaseQuotationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return PurchaseQuotationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        date: Union[str, date],
        supplier_id: str,
        api_key: str,
        add_products: Iterable[purchase_quotation_create_params.AddProduct] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseQuotationCreateResponse:
        """
        Create new purchase quotation

        Args:
          date: Date of The Purchase Quotation in `yyyy-MM-dd`

          supplier_id: Supplier ID

          add_products: Products to be added

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._post(
            "/purchaseQuotations/",
            body=maybe_transform(
                {
                    "date": date,
                    "supplier_id": supplier_id,
                    "add_products": add_products,
                    "description": description,
                },
                purchase_quotation_create_params.PurchaseQuotationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseQuotationCreateResponse,
        )

    def update(
        self,
        id: str,
        *,
        api_key: str,
        add_products: Iterable[purchase_quotation_update_params.AddProduct] | NotGiven = NOT_GIVEN,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        del_products: Iterable[purchase_quotation_update_params.DelProduct] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        mod_products: Iterable[purchase_quotation_update_params.ModProduct] | NotGiven = NOT_GIVEN,
        supplier_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseQuotationUpdateResponse:
        """
        Update purchase quotation

        Args:
          add_products: Products to be deleted

          date: Date of The Purchase Quotation in `yyyy-MM-dd`

          del_products: Products to be deleted

          mod_products: Products to be modified

          supplier_id: Supplier ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._put(
            f"/purchaseQuotations/{id}",
            body=maybe_transform(
                {
                    "add_products": add_products,
                    "date": date,
                    "del_products": del_products,
                    "description": description,
                    "mod_products": mod_products,
                    "supplier_id": supplier_id,
                },
                purchase_quotation_update_params.PurchaseQuotationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseQuotationUpdateResponse,
        )

    def list(
        self,
        *,
        from_date: str,
        to_date: str,
        api_key: str,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseQuotationListResponse:
        """
        Get All Purchase Quotations

        Args:
          from_date: starting date in format yyyy-MM-dd

          to_date: ending date in format yyyy-MM-dd

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._get(
            "/purchaseQuotations/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_date": from_date,
                        "to_date": to_date,
                        "limit": limit,
                        "page": page,
                    },
                    purchase_quotation_list_params.PurchaseQuotationListParams,
                ),
            ),
            cast_to=PurchaseQuotationListResponse,
        )


class AsyncPurchaseQuotationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPurchaseQuotationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return AsyncPurchaseQuotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPurchaseQuotationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return AsyncPurchaseQuotationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        date: Union[str, date],
        supplier_id: str,
        api_key: str,
        add_products: Iterable[purchase_quotation_create_params.AddProduct] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseQuotationCreateResponse:
        """
        Create new purchase quotation

        Args:
          date: Date of The Purchase Quotation in `yyyy-MM-dd`

          supplier_id: Supplier ID

          add_products: Products to be added

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._post(
            "/purchaseQuotations/",
            body=await async_maybe_transform(
                {
                    "date": date,
                    "supplier_id": supplier_id,
                    "add_products": add_products,
                    "description": description,
                },
                purchase_quotation_create_params.PurchaseQuotationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseQuotationCreateResponse,
        )

    async def update(
        self,
        id: str,
        *,
        api_key: str,
        add_products: Iterable[purchase_quotation_update_params.AddProduct] | NotGiven = NOT_GIVEN,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        del_products: Iterable[purchase_quotation_update_params.DelProduct] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        mod_products: Iterable[purchase_quotation_update_params.ModProduct] | NotGiven = NOT_GIVEN,
        supplier_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseQuotationUpdateResponse:
        """
        Update purchase quotation

        Args:
          add_products: Products to be deleted

          date: Date of The Purchase Quotation in `yyyy-MM-dd`

          del_products: Products to be deleted

          mod_products: Products to be modified

          supplier_id: Supplier ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._put(
            f"/purchaseQuotations/{id}",
            body=await async_maybe_transform(
                {
                    "add_products": add_products,
                    "date": date,
                    "del_products": del_products,
                    "description": description,
                    "mod_products": mod_products,
                    "supplier_id": supplier_id,
                },
                purchase_quotation_update_params.PurchaseQuotationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseQuotationUpdateResponse,
        )

    async def list(
        self,
        *,
        from_date: str,
        to_date: str,
        api_key: str,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseQuotationListResponse:
        """
        Get All Purchase Quotations

        Args:
          from_date: starting date in format yyyy-MM-dd

          to_date: ending date in format yyyy-MM-dd

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._get(
            "/purchaseQuotations/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_date": from_date,
                        "to_date": to_date,
                        "limit": limit,
                        "page": page,
                    },
                    purchase_quotation_list_params.PurchaseQuotationListParams,
                ),
            ),
            cast_to=PurchaseQuotationListResponse,
        )


class PurchaseQuotationsResourceWithRawResponse:
    def __init__(self, purchase_quotations: PurchaseQuotationsResource) -> None:
        self._purchase_quotations = purchase_quotations

        self.create = to_raw_response_wrapper(
            purchase_quotations.create,
        )
        self.update = to_raw_response_wrapper(
            purchase_quotations.update,
        )
        self.list = to_raw_response_wrapper(
            purchase_quotations.list,
        )


class AsyncPurchaseQuotationsResourceWithRawResponse:
    def __init__(self, purchase_quotations: AsyncPurchaseQuotationsResource) -> None:
        self._purchase_quotations = purchase_quotations

        self.create = async_to_raw_response_wrapper(
            purchase_quotations.create,
        )
        self.update = async_to_raw_response_wrapper(
            purchase_quotations.update,
        )
        self.list = async_to_raw_response_wrapper(
            purchase_quotations.list,
        )


class PurchaseQuotationsResourceWithStreamingResponse:
    def __init__(self, purchase_quotations: PurchaseQuotationsResource) -> None:
        self._purchase_quotations = purchase_quotations

        self.create = to_streamed_response_wrapper(
            purchase_quotations.create,
        )
        self.update = to_streamed_response_wrapper(
            purchase_quotations.update,
        )
        self.list = to_streamed_response_wrapper(
            purchase_quotations.list,
        )


class AsyncPurchaseQuotationsResourceWithStreamingResponse:
    def __init__(self, purchase_quotations: AsyncPurchaseQuotationsResource) -> None:
        self._purchase_quotations = purchase_quotations

        self.create = async_to_streamed_response_wrapper(
            purchase_quotations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            purchase_quotations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            purchase_quotations.list,
        )
