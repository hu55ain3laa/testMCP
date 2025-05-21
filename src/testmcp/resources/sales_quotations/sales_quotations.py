# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .by_purchase_requisition import (
    ByPurchaseRequisitionResource,
    AsyncByPurchaseRequisitionResource,
    ByPurchaseRequisitionResourceWithRawResponse,
    AsyncByPurchaseRequisitionResourceWithRawResponse,
    ByPurchaseRequisitionResourceWithStreamingResponse,
    AsyncByPurchaseRequisitionResourceWithStreamingResponse,
)

__all__ = ["SalesQuotationsResource", "AsyncSalesQuotationsResource"]


class SalesQuotationsResource(SyncAPIResource):
    @cached_property
    def by_purchase_requisition(self) -> ByPurchaseRequisitionResource:
        return ByPurchaseRequisitionResource(self._client)

    @cached_property
    def with_raw_response(self) -> SalesQuotationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/testmcp-python#accessing-raw-response-data-eg-headers
        """
        return SalesQuotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SalesQuotationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/testmcp-python#with_streaming_response
        """
        return SalesQuotationsResourceWithStreamingResponse(self)


class AsyncSalesQuotationsResource(AsyncAPIResource):
    @cached_property
    def by_purchase_requisition(self) -> AsyncByPurchaseRequisitionResource:
        return AsyncByPurchaseRequisitionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSalesQuotationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/testmcp-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSalesQuotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSalesQuotationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/testmcp-python#with_streaming_response
        """
        return AsyncSalesQuotationsResourceWithStreamingResponse(self)


class SalesQuotationsResourceWithRawResponse:
    def __init__(self, sales_quotations: SalesQuotationsResource) -> None:
        self._sales_quotations = sales_quotations

    @cached_property
    def by_purchase_requisition(self) -> ByPurchaseRequisitionResourceWithRawResponse:
        return ByPurchaseRequisitionResourceWithRawResponse(self._sales_quotations.by_purchase_requisition)


class AsyncSalesQuotationsResourceWithRawResponse:
    def __init__(self, sales_quotations: AsyncSalesQuotationsResource) -> None:
        self._sales_quotations = sales_quotations

    @cached_property
    def by_purchase_requisition(self) -> AsyncByPurchaseRequisitionResourceWithRawResponse:
        return AsyncByPurchaseRequisitionResourceWithRawResponse(self._sales_quotations.by_purchase_requisition)


class SalesQuotationsResourceWithStreamingResponse:
    def __init__(self, sales_quotations: SalesQuotationsResource) -> None:
        self._sales_quotations = sales_quotations

    @cached_property
    def by_purchase_requisition(self) -> ByPurchaseRequisitionResourceWithStreamingResponse:
        return ByPurchaseRequisitionResourceWithStreamingResponse(self._sales_quotations.by_purchase_requisition)


class AsyncSalesQuotationsResourceWithStreamingResponse:
    def __init__(self, sales_quotations: AsyncSalesQuotationsResource) -> None:
        self._sales_quotations = sales_quotations

    @cached_property
    def by_purchase_requisition(self) -> AsyncByPurchaseRequisitionResourceWithStreamingResponse:
        return AsyncByPurchaseRequisitionResourceWithStreamingResponse(self._sales_quotations.by_purchase_requisition)
