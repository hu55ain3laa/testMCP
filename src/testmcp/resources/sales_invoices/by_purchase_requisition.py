# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.sales_invoices.by_purchase_requisition_generate_response import ByPurchaseRequisitionGenerateResponse

__all__ = ["ByPurchaseRequisitionResource", "AsyncByPurchaseRequisitionResource"]


class ByPurchaseRequisitionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ByPurchaseRequisitionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return ByPurchaseRequisitionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ByPurchaseRequisitionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return ByPurchaseRequisitionResourceWithStreamingResponse(self)

    def generate(
        self,
        id: str,
        *,
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByPurchaseRequisitionGenerateResponse:
        """
        Generate or Retrieve Sales Invoice By Purchase Requisition ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._post(
            f"/salesInvoices/byPurchaseRequisition/{id}/generate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByPurchaseRequisitionGenerateResponse,
        )


class AsyncByPurchaseRequisitionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncByPurchaseRequisitionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return AsyncByPurchaseRequisitionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncByPurchaseRequisitionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return AsyncByPurchaseRequisitionResourceWithStreamingResponse(self)

    async def generate(
        self,
        id: str,
        *,
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ByPurchaseRequisitionGenerateResponse:
        """
        Generate or Retrieve Sales Invoice By Purchase Requisition ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._post(
            f"/salesInvoices/byPurchaseRequisition/{id}/generate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ByPurchaseRequisitionGenerateResponse,
        )


class ByPurchaseRequisitionResourceWithRawResponse:
    def __init__(self, by_purchase_requisition: ByPurchaseRequisitionResource) -> None:
        self._by_purchase_requisition = by_purchase_requisition

        self.generate = to_raw_response_wrapper(
            by_purchase_requisition.generate,
        )


class AsyncByPurchaseRequisitionResourceWithRawResponse:
    def __init__(self, by_purchase_requisition: AsyncByPurchaseRequisitionResource) -> None:
        self._by_purchase_requisition = by_purchase_requisition

        self.generate = async_to_raw_response_wrapper(
            by_purchase_requisition.generate,
        )


class ByPurchaseRequisitionResourceWithStreamingResponse:
    def __init__(self, by_purchase_requisition: ByPurchaseRequisitionResource) -> None:
        self._by_purchase_requisition = by_purchase_requisition

        self.generate = to_streamed_response_wrapper(
            by_purchase_requisition.generate,
        )


class AsyncByPurchaseRequisitionResourceWithStreamingResponse:
    def __init__(self, by_purchase_requisition: AsyncByPurchaseRequisitionResource) -> None:
        self._by_purchase_requisition = by_purchase_requisition

        self.generate = async_to_streamed_response_wrapper(
            by_purchase_requisition.generate,
        )
