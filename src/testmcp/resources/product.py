# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    product_list_params,
    product_retrieve_details_params,
    product_retrieve_created_after_params,
    product_retrieve_promoted_after_params,
    product_retrieve_updated_prices_after_params,
    product_retrieve_updated_availability_after_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.product_list_response import ProductListResponse
from ..types.product_retrieve_details_response import ProductRetrieveDetailsResponse
from ..types.product_retrieve_created_after_response import ProductRetrieveCreatedAfterResponse
from ..types.product_retrieve_promoted_after_response import ProductRetrievePromotedAfterResponse
from ..types.product_retrieve_updated_prices_after_response import ProductRetrieveUpdatedPricesAfterResponse
from ..types.product_retrieve_updated_availability_after_response import ProductRetrieveUpdatedAvailabilityAfterResponse

__all__ = ["ProductResource", "AsyncProductResource"]


class ProductResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProductResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return ProductResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return ProductResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        api_key: str,
        cat_id: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sub_cat_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductListResponse:
        """
        Get All Products Information

        Args:
          cat_id: products category id

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          sub_cat_id: products sub category id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._get(
            "/product/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cat_id": cat_id,
                        "limit": limit,
                        "page": page,
                        "sub_cat_id": sub_cat_id,
                    },
                    product_list_params.ProductListParams,
                ),
            ),
            cast_to=ProductListResponse,
        )

    def retrieve_created_after(
        self,
        *,
        date: str,
        api_key: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRetrieveCreatedAfterResponse:
        """
        Get Created Products and Updated Products After A Specific Date

        Args:
          date: Date of products created | Date Format : yyyy-MM-dd

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._get(
            "/product/createdProduct",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "page": page,
                    },
                    product_retrieve_created_after_params.ProductRetrieveCreatedAfterParams,
                ),
            ),
            cast_to=ProductRetrieveCreatedAfterResponse,
        )

    def retrieve_details(
        self,
        *,
        api_key: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRetrieveDetailsResponse:
        """
        Get All Your Products Details

        Args:
          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._get(
            "/product/details",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    product_retrieve_details_params.ProductRetrieveDetailsParams,
                ),
            ),
            cast_to=ProductRetrieveDetailsResponse,
        )

    def retrieve_promoted_after(
        self,
        *,
        date: str,
        api_key: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRetrievePromotedAfterResponse:
        """
        Get Promoted Products After A Specific Date

        Args:
          date: Date Of Promotion | Date Format : yyyy-MM-dd

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._get(
            "/product/promotionPrices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "page": page,
                    },
                    product_retrieve_promoted_after_params.ProductRetrievePromotedAfterParams,
                ),
            ),
            cast_to=ProductRetrievePromotedAfterResponse,
        )

    def retrieve_updated_availability_after(
        self,
        *,
        date: str,
        api_key: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRetrieveUpdatedAvailabilityAfterResponse:
        """
        Get Products Available Quantity After A Specific Date

        Args:
          date: Date Of Stock Movment | Date Format : yyyy-MM-dd

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._get(
            "/product/updatedAvailability",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "page": page,
                    },
                    product_retrieve_updated_availability_after_params.ProductRetrieveUpdatedAvailabilityAfterParams,
                ),
            ),
            cast_to=ProductRetrieveUpdatedAvailabilityAfterResponse,
        )

    def retrieve_updated_prices_after(
        self,
        *,
        date: str,
        api_key: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRetrieveUpdatedPricesAfterResponse:
        """
        Get Updated Products Prices After A Specific Date

        Args:
          date: Date Of Products Prices Updates | Date Format : yyyy-MM-dd

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._get(
            "/product/updatedPrice",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "page": page,
                    },
                    product_retrieve_updated_prices_after_params.ProductRetrieveUpdatedPricesAfterParams,
                ),
            ),
            cast_to=ProductRetrieveUpdatedPricesAfterResponse,
        )


class AsyncProductResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProductResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return AsyncProductResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return AsyncProductResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        api_key: str,
        cat_id: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        sub_cat_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductListResponse:
        """
        Get All Products Information

        Args:
          cat_id: products category id

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          sub_cat_id: products sub category id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._get(
            "/product/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cat_id": cat_id,
                        "limit": limit,
                        "page": page,
                        "sub_cat_id": sub_cat_id,
                    },
                    product_list_params.ProductListParams,
                ),
            ),
            cast_to=ProductListResponse,
        )

    async def retrieve_created_after(
        self,
        *,
        date: str,
        api_key: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRetrieveCreatedAfterResponse:
        """
        Get Created Products and Updated Products After A Specific Date

        Args:
          date: Date of products created | Date Format : yyyy-MM-dd

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._get(
            "/product/createdProduct",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "page": page,
                    },
                    product_retrieve_created_after_params.ProductRetrieveCreatedAfterParams,
                ),
            ),
            cast_to=ProductRetrieveCreatedAfterResponse,
        )

    async def retrieve_details(
        self,
        *,
        api_key: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRetrieveDetailsResponse:
        """
        Get All Your Products Details

        Args:
          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._get(
            "/product/details",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    product_retrieve_details_params.ProductRetrieveDetailsParams,
                ),
            ),
            cast_to=ProductRetrieveDetailsResponse,
        )

    async def retrieve_promoted_after(
        self,
        *,
        date: str,
        api_key: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRetrievePromotedAfterResponse:
        """
        Get Promoted Products After A Specific Date

        Args:
          date: Date Of Promotion | Date Format : yyyy-MM-dd

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._get(
            "/product/promotionPrices",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "page": page,
                    },
                    product_retrieve_promoted_after_params.ProductRetrievePromotedAfterParams,
                ),
            ),
            cast_to=ProductRetrievePromotedAfterResponse,
        )

    async def retrieve_updated_availability_after(
        self,
        *,
        date: str,
        api_key: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRetrieveUpdatedAvailabilityAfterResponse:
        """
        Get Products Available Quantity After A Specific Date

        Args:
          date: Date Of Stock Movment | Date Format : yyyy-MM-dd

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._get(
            "/product/updatedAvailability",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "page": page,
                    },
                    product_retrieve_updated_availability_after_params.ProductRetrieveUpdatedAvailabilityAfterParams,
                ),
            ),
            cast_to=ProductRetrieveUpdatedAvailabilityAfterResponse,
        )

    async def retrieve_updated_prices_after(
        self,
        *,
        date: str,
        api_key: str,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRetrieveUpdatedPricesAfterResponse:
        """
        Get Updated Products Prices After A Specific Date

        Args:
          date: Date Of Products Prices Updates | Date Format : yyyy-MM-dd

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._get(
            "/product/updatedPrice",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "limit": limit,
                        "page": page,
                    },
                    product_retrieve_updated_prices_after_params.ProductRetrieveUpdatedPricesAfterParams,
                ),
            ),
            cast_to=ProductRetrieveUpdatedPricesAfterResponse,
        )


class ProductResourceWithRawResponse:
    def __init__(self, product: ProductResource) -> None:
        self._product = product

        self.list = to_raw_response_wrapper(
            product.list,
        )
        self.retrieve_created_after = to_raw_response_wrapper(
            product.retrieve_created_after,
        )
        self.retrieve_details = to_raw_response_wrapper(
            product.retrieve_details,
        )
        self.retrieve_promoted_after = to_raw_response_wrapper(
            product.retrieve_promoted_after,
        )
        self.retrieve_updated_availability_after = to_raw_response_wrapper(
            product.retrieve_updated_availability_after,
        )
        self.retrieve_updated_prices_after = to_raw_response_wrapper(
            product.retrieve_updated_prices_after,
        )


class AsyncProductResourceWithRawResponse:
    def __init__(self, product: AsyncProductResource) -> None:
        self._product = product

        self.list = async_to_raw_response_wrapper(
            product.list,
        )
        self.retrieve_created_after = async_to_raw_response_wrapper(
            product.retrieve_created_after,
        )
        self.retrieve_details = async_to_raw_response_wrapper(
            product.retrieve_details,
        )
        self.retrieve_promoted_after = async_to_raw_response_wrapper(
            product.retrieve_promoted_after,
        )
        self.retrieve_updated_availability_after = async_to_raw_response_wrapper(
            product.retrieve_updated_availability_after,
        )
        self.retrieve_updated_prices_after = async_to_raw_response_wrapper(
            product.retrieve_updated_prices_after,
        )


class ProductResourceWithStreamingResponse:
    def __init__(self, product: ProductResource) -> None:
        self._product = product

        self.list = to_streamed_response_wrapper(
            product.list,
        )
        self.retrieve_created_after = to_streamed_response_wrapper(
            product.retrieve_created_after,
        )
        self.retrieve_details = to_streamed_response_wrapper(
            product.retrieve_details,
        )
        self.retrieve_promoted_after = to_streamed_response_wrapper(
            product.retrieve_promoted_after,
        )
        self.retrieve_updated_availability_after = to_streamed_response_wrapper(
            product.retrieve_updated_availability_after,
        )
        self.retrieve_updated_prices_after = to_streamed_response_wrapper(
            product.retrieve_updated_prices_after,
        )


class AsyncProductResourceWithStreamingResponse:
    def __init__(self, product: AsyncProductResource) -> None:
        self._product = product

        self.list = async_to_streamed_response_wrapper(
            product.list,
        )
        self.retrieve_created_after = async_to_streamed_response_wrapper(
            product.retrieve_created_after,
        )
        self.retrieve_details = async_to_streamed_response_wrapper(
            product.retrieve_details,
        )
        self.retrieve_promoted_after = async_to_streamed_response_wrapper(
            product.retrieve_promoted_after,
        )
        self.retrieve_updated_availability_after = async_to_streamed_response_wrapper(
            product.retrieve_updated_availability_after,
        )
        self.retrieve_updated_prices_after = async_to_streamed_response_wrapper(
            product.retrieve_updated_prices_after,
        )
