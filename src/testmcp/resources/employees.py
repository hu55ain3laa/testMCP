# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import employee_list_params
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
from ..types.employee_list_response import EmployeeListResponse

__all__ = ["EmployeesResource", "AsyncEmployeesResource"]


class EmployeesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return EmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return EmployeesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        api_key: str,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeListResponse:
        """
        Get all employees

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
            "/employees/",
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
                    employee_list_params.EmployeeListParams,
                ),
            ),
            cast_to=EmployeeListResponse,
        )


class AsyncEmployeesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEmployeesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return AsyncEmployeesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmployeesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return AsyncEmployeesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        api_key: str,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmployeeListResponse:
        """
        Get all employees

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
            "/employees/",
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
                    employee_list_params.EmployeeListParams,
                ),
            ),
            cast_to=EmployeeListResponse,
        )


class EmployeesResourceWithRawResponse:
    def __init__(self, employees: EmployeesResource) -> None:
        self._employees = employees

        self.list = to_raw_response_wrapper(
            employees.list,
        )


class AsyncEmployeesResourceWithRawResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.list = async_to_raw_response_wrapper(
            employees.list,
        )


class EmployeesResourceWithStreamingResponse:
    def __init__(self, employees: EmployeesResource) -> None:
        self._employees = employees

        self.list = to_streamed_response_wrapper(
            employees.list,
        )


class AsyncEmployeesResourceWithStreamingResponse:
    def __init__(self, employees: AsyncEmployeesResource) -> None:
        self._employees = employees

        self.list = async_to_streamed_response_wrapper(
            employees.list,
        )
