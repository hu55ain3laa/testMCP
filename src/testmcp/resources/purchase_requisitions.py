# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import purchase_requisition_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.documents_info_param import DocumentsInfoParam
from ..types.purchase_requisition_create_response import PurchaseRequisitionCreateResponse

__all__ = ["PurchaseRequisitionsResource", "AsyncPurchaseRequisitionsResource"]


class PurchaseRequisitionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PurchaseRequisitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/testmcp-python#accessing-raw-response-data-eg-headers
        """
        return PurchaseRequisitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PurchaseRequisitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/testmcp-python#with_streaming_response
        """
        return PurchaseRequisitionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        purchase_requisition_date: str,
        api_key: str,
        add_products: Iterable[purchase_requisition_create_params.AddProduct] | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        date_format: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        documents: Iterable[DocumentsInfoParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseRequisitionCreateResponse:
        """
        Create new purchase requisition

        Args:
          purchase_requisition_date: Date of The Purchase Requisition | Date Format is the sent `dateFormat` or
              default `yyyy-MM-dd`

          customer_id: Customer ID

          date_format: Date format to be used

          description: any purchase requisition description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._post(
            "/purchaseRequisitions/",
            body=maybe_transform(
                {
                    "purchase_requisition_date": purchase_requisition_date,
                    "add_products": add_products,
                    "customer_id": customer_id,
                    "date_format": date_format,
                    "description": description,
                    "documents": documents,
                },
                purchase_requisition_create_params.PurchaseRequisitionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseRequisitionCreateResponse,
        )

    def add_document(
        self,
        id: str,
        *,
        body: Iterable[DocumentsInfoParam],
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Create new purchase requisition document.

        **Important Note: reuploading same
        file name will replace previous file**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"apiKey": api_key})
        return self._post(
            f"/purchaseRequisitions/{id}/documents",
            body=maybe_transform(body, Iterable[DocumentsInfoParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPurchaseRequisitionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPurchaseRequisitionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/testmcp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPurchaseRequisitionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPurchaseRequisitionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/testmcp-python#with_streaming_response
        """
        return AsyncPurchaseRequisitionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        purchase_requisition_date: str,
        api_key: str,
        add_products: Iterable[purchase_requisition_create_params.AddProduct] | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        date_format: str | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        documents: Iterable[DocumentsInfoParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurchaseRequisitionCreateResponse:
        """
        Create new purchase requisition

        Args:
          purchase_requisition_date: Date of The Purchase Requisition | Date Format is the sent `dateFormat` or
              default `yyyy-MM-dd`

          customer_id: Customer ID

          date_format: Date format to be used

          description: any purchase requisition description

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._post(
            "/purchaseRequisitions/",
            body=await async_maybe_transform(
                {
                    "purchase_requisition_date": purchase_requisition_date,
                    "add_products": add_products,
                    "customer_id": customer_id,
                    "date_format": date_format,
                    "description": description,
                    "documents": documents,
                },
                purchase_requisition_create_params.PurchaseRequisitionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurchaseRequisitionCreateResponse,
        )

    async def add_document(
        self,
        id: str,
        *,
        body: Iterable[DocumentsInfoParam],
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Create new purchase requisition document.

        **Important Note: reuploading same
        file name will replace previous file**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"apiKey": api_key})
        return await self._post(
            f"/purchaseRequisitions/{id}/documents",
            body=await async_maybe_transform(body, Iterable[DocumentsInfoParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PurchaseRequisitionsResourceWithRawResponse:
    def __init__(self, purchase_requisitions: PurchaseRequisitionsResource) -> None:
        self._purchase_requisitions = purchase_requisitions

        self.create = to_raw_response_wrapper(
            purchase_requisitions.create,
        )
        self.add_document = to_raw_response_wrapper(
            purchase_requisitions.add_document,
        )


class AsyncPurchaseRequisitionsResourceWithRawResponse:
    def __init__(self, purchase_requisitions: AsyncPurchaseRequisitionsResource) -> None:
        self._purchase_requisitions = purchase_requisitions

        self.create = async_to_raw_response_wrapper(
            purchase_requisitions.create,
        )
        self.add_document = async_to_raw_response_wrapper(
            purchase_requisitions.add_document,
        )


class PurchaseRequisitionsResourceWithStreamingResponse:
    def __init__(self, purchase_requisitions: PurchaseRequisitionsResource) -> None:
        self._purchase_requisitions = purchase_requisitions

        self.create = to_streamed_response_wrapper(
            purchase_requisitions.create,
        )
        self.add_document = to_streamed_response_wrapper(
            purchase_requisitions.add_document,
        )


class AsyncPurchaseRequisitionsResourceWithStreamingResponse:
    def __init__(self, purchase_requisitions: AsyncPurchaseRequisitionsResource) -> None:
        self._purchase_requisitions = purchase_requisitions

        self.create = async_to_streamed_response_wrapper(
            purchase_requisitions.create,
        )
        self.add_document = async_to_streamed_response_wrapper(
            purchase_requisitions.add_document,
        )
