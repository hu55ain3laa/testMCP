# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import attendance_create_params, attendance_delete_params
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
from ..types.attendance_create_response import AttendanceCreateResponse
from ..types.attendance_delete_response import AttendanceDeleteResponse

__all__ = ["AttendanceResource", "AsyncAttendanceResource"]


class AttendanceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttendanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return AttendanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttendanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return AttendanceResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        body: Iterable[Iterable[attendance_create_params.Body]],
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttendanceCreateResponse:
        """
        Saves attendance records for employees

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._post(
            "/attendance/",
            body=maybe_transform(body, Iterable[Iterable[attendance_create_params.Body]]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttendanceCreateResponse,
        )

    def delete(
        self,
        *,
        employee_codes: str,
        from_date: str,
        to_date: str,
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttendanceDeleteResponse:
        """
        Delete attendance records for employees

        Args:
          employee_codes: Commpa seperated employee codes

          from_date: starting date in format yyyy-MM-dd

          to_date: ending date in format yyyy-MM-dd

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._delete(
            "/attendance/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "employee_codes": employee_codes,
                        "from_date": from_date,
                        "to_date": to_date,
                    },
                    attendance_delete_params.AttendanceDeleteParams,
                ),
            ),
            cast_to=AttendanceDeleteResponse,
        )


class AsyncAttendanceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttendanceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return AsyncAttendanceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttendanceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return AsyncAttendanceResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        body: Iterable[Iterable[attendance_create_params.Body]],
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttendanceCreateResponse:
        """
        Saves attendance records for employees

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._post(
            "/attendance/",
            body=await async_maybe_transform(body, Iterable[Iterable[attendance_create_params.Body]]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AttendanceCreateResponse,
        )

    async def delete(
        self,
        *,
        employee_codes: str,
        from_date: str,
        to_date: str,
        api_key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttendanceDeleteResponse:
        """
        Delete attendance records for employees

        Args:
          employee_codes: Commpa seperated employee codes

          from_date: starting date in format yyyy-MM-dd

          to_date: ending date in format yyyy-MM-dd

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._delete(
            "/attendance/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "employee_codes": employee_codes,
                        "from_date": from_date,
                        "to_date": to_date,
                    },
                    attendance_delete_params.AttendanceDeleteParams,
                ),
            ),
            cast_to=AttendanceDeleteResponse,
        )


class AttendanceResourceWithRawResponse:
    def __init__(self, attendance: AttendanceResource) -> None:
        self._attendance = attendance

        self.create = to_raw_response_wrapper(
            attendance.create,
        )
        self.delete = to_raw_response_wrapper(
            attendance.delete,
        )


class AsyncAttendanceResourceWithRawResponse:
    def __init__(self, attendance: AsyncAttendanceResource) -> None:
        self._attendance = attendance

        self.create = async_to_raw_response_wrapper(
            attendance.create,
        )
        self.delete = async_to_raw_response_wrapper(
            attendance.delete,
        )


class AttendanceResourceWithStreamingResponse:
    def __init__(self, attendance: AttendanceResource) -> None:
        self._attendance = attendance

        self.create = to_streamed_response_wrapper(
            attendance.create,
        )
        self.delete = to_streamed_response_wrapper(
            attendance.delete,
        )


class AsyncAttendanceResourceWithStreamingResponse:
    def __init__(self, attendance: AsyncAttendanceResource) -> None:
        self._attendance = attendance

        self.create = async_to_streamed_response_wrapper(
            attendance.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            attendance.delete,
        )
