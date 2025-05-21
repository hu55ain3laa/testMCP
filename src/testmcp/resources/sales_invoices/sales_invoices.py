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
from .by_purchase_requisition import (
    ByPurchaseRequisitionResource,
    AsyncByPurchaseRequisitionResource,
    ByPurchaseRequisitionResourceWithRawResponse,
    AsyncByPurchaseRequisitionResourceWithRawResponse,
    ByPurchaseRequisitionResourceWithStreamingResponse,
    AsyncByPurchaseRequisitionResourceWithStreamingResponse,
)

__all__ = ["SalesInvoicesResource", "AsyncSalesInvoicesResource"]


class SalesInvoicesResource(SyncAPIResource):
    @cached_property
    def by_purchase_requisition(self) -> ByPurchaseRequisitionResource:
        return ByPurchaseRequisitionResource(self._client)

    @cached_property
    def with_raw_response(self) -> SalesInvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return SalesInvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SalesInvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return SalesInvoicesResourceWithStreamingResponse(self)

    def print_html(
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
    ) -> str:
        """
        Print Sales Invoice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/html", **(extra_headers or {})}
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._get(
            f"/salesInvoices/{id}/printHtml",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class AsyncSalesInvoicesResource(AsyncAPIResource):
    @cached_property
    def by_purchase_requisition(self) -> AsyncByPurchaseRequisitionResource:
        return AsyncByPurchaseRequisitionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSalesInvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return AsyncSalesInvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSalesInvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return AsyncSalesInvoicesResourceWithStreamingResponse(self)

    async def print_html(
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
    ) -> str:
        """
        Print Sales Invoice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "text/html", **(extra_headers or {})}
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._get(
            f"/salesInvoices/{id}/printHtml",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )


class SalesInvoicesResourceWithRawResponse:
    def __init__(self, sales_invoices: SalesInvoicesResource) -> None:
        self._sales_invoices = sales_invoices

        self.print_html = to_raw_response_wrapper(
            sales_invoices.print_html,
        )

    @cached_property
    def by_purchase_requisition(self) -> ByPurchaseRequisitionResourceWithRawResponse:
        return ByPurchaseRequisitionResourceWithRawResponse(self._sales_invoices.by_purchase_requisition)


class AsyncSalesInvoicesResourceWithRawResponse:
    def __init__(self, sales_invoices: AsyncSalesInvoicesResource) -> None:
        self._sales_invoices = sales_invoices

        self.print_html = async_to_raw_response_wrapper(
            sales_invoices.print_html,
        )

    @cached_property
    def by_purchase_requisition(self) -> AsyncByPurchaseRequisitionResourceWithRawResponse:
        return AsyncByPurchaseRequisitionResourceWithRawResponse(self._sales_invoices.by_purchase_requisition)


class SalesInvoicesResourceWithStreamingResponse:
    def __init__(self, sales_invoices: SalesInvoicesResource) -> None:
        self._sales_invoices = sales_invoices

        self.print_html = to_streamed_response_wrapper(
            sales_invoices.print_html,
        )

    @cached_property
    def by_purchase_requisition(self) -> ByPurchaseRequisitionResourceWithStreamingResponse:
        return ByPurchaseRequisitionResourceWithStreamingResponse(self._sales_invoices.by_purchase_requisition)


class AsyncSalesInvoicesResourceWithStreamingResponse:
    def __init__(self, sales_invoices: AsyncSalesInvoicesResource) -> None:
        self._sales_invoices = sales_invoices

        self.print_html = async_to_streamed_response_wrapper(
            sales_invoices.print_html,
        )

    @cached_property
    def by_purchase_requisition(self) -> AsyncByPurchaseRequisitionResourceWithStreamingResponse:
        return AsyncByPurchaseRequisitionResourceWithStreamingResponse(self._sales_invoices.by_purchase_requisition)
