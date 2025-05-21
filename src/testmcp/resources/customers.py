# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import customer_list_params, customer_create_params, customer_update_params
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
from ..types.customer import Customer
from ..types.documents_info_param import DocumentsInfoParam
from ..types.customer_list_response import CustomerListResponse
from ..types.customer_create_response import CustomerCreateResponse
from ..types.customer_update_response import CustomerUpdateResponse

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return CustomersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_type: str,
        api_key: str,
        company_name: str | NotGiven = NOT_GIVEN,
        customer_address: str | NotGiven = NOT_GIVEN,
        customer_city: str | NotGiven = NOT_GIVEN,
        customer_code: int | NotGiven = NOT_GIVEN,
        customer_comm_reg_number: str | NotGiven = NOT_GIVEN,
        customer_email: str | NotGiven = NOT_GIVEN,
        customer_fax: str | NotGiven = NOT_GIVEN,
        customer_first_name: str | NotGiven = NOT_GIVEN,
        customer_last_name: str | NotGiven = NOT_GIVEN,
        customer_middle_name: str | NotGiven = NOT_GIVEN,
        customer_phone1: str | NotGiven = NOT_GIVEN,
        customer_phone2: str | NotGiven = NOT_GIVEN,
        customer_phone3: str | NotGiven = NOT_GIVEN,
        customer_website: str | NotGiven = NOT_GIVEN,
        documents: Iterable[DocumentsInfoParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerCreateResponse:
        """
        Save New Customer

        Args:
          customer_type: always required, values ('company' 'individual' 'cash' 'potential')

          company_name: Customer company name , required for type company and potential

          customer_address: Customer Address

          customer_city: Customer city , must exist in cities defintions

          customer_code: Customer code

          customer_comm_reg_number: Customer Commercial Registration No.

          customer_email: Customer Email

          customer_fax: Customer Fax

          customer_first_name: Customer first name , required for type individual and cash

          customer_last_name: Customer last Name , required for type individual and cash

          customer_middle_name: Customer middle Name

          customer_phone1: Customer Phone 1 , required for type individual and cash

          customer_phone2: Customer Phone 2

          customer_phone3: Customer Phone 3

          customer_website: Customer Website

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._post(
            "/customers/",
            body=maybe_transform(
                {
                    "customer_type": customer_type,
                    "company_name": company_name,
                    "customer_address": customer_address,
                    "customer_city": customer_city,
                    "customer_code": customer_code,
                    "customer_comm_reg_number": customer_comm_reg_number,
                    "customer_email": customer_email,
                    "customer_fax": customer_fax,
                    "customer_first_name": customer_first_name,
                    "customer_last_name": customer_last_name,
                    "customer_middle_name": customer_middle_name,
                    "customer_phone1": customer_phone1,
                    "customer_phone2": customer_phone2,
                    "customer_phone3": customer_phone3,
                    "customer_website": customer_website,
                    "documents": documents,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerCreateResponse,
        )

    def retrieve(
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
    ) -> Customer:
        """
        Get Single Customer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._get(
            f"/customers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    def update(
        self,
        id: str,
        *,
        api_key: str,
        company_name: str | NotGiven = NOT_GIVEN,
        customer_address: str | NotGiven = NOT_GIVEN,
        customer_city: str | NotGiven = NOT_GIVEN,
        customer_code: int | NotGiven = NOT_GIVEN,
        customer_comm_reg_number: str | NotGiven = NOT_GIVEN,
        customer_email: str | NotGiven = NOT_GIVEN,
        customer_fax: str | NotGiven = NOT_GIVEN,
        customer_first_name: str | NotGiven = NOT_GIVEN,
        customer_last_name: str | NotGiven = NOT_GIVEN,
        customer_middle_name: str | NotGiven = NOT_GIVEN,
        customer_phone1: str | NotGiven = NOT_GIVEN,
        customer_phone2: str | NotGiven = NOT_GIVEN,
        customer_phone3: str | NotGiven = NOT_GIVEN,
        customer_website: str | NotGiven = NOT_GIVEN,
        documents: Iterable[DocumentsInfoParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerUpdateResponse:
        """
        Update Single Customer

        Args:
          company_name: Customer company name

          customer_address: Customer Address

          customer_city: Customer city , must exist in cities defintions

          customer_code: Customer code

          customer_comm_reg_number: Customer Commercial Registration No.

          customer_email: Customer Email

          customer_fax: Customer Fax

          customer_first_name: Customer first name

          customer_last_name: Customer last Name

          customer_middle_name: Customer middle Name

          customer_phone1: Customer Phone 1

          customer_phone2: Customer Phone 2

          customer_phone3: Customer Phone 3

          customer_website: Customer Website

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._put(
            f"/customers/{id}",
            body=maybe_transform(
                {
                    "company_name": company_name,
                    "customer_address": customer_address,
                    "customer_city": customer_city,
                    "customer_code": customer_code,
                    "customer_comm_reg_number": customer_comm_reg_number,
                    "customer_email": customer_email,
                    "customer_fax": customer_fax,
                    "customer_first_name": customer_first_name,
                    "customer_last_name": customer_last_name,
                    "customer_middle_name": customer_middle_name,
                    "customer_phone1": customer_phone1,
                    "customer_phone2": customer_phone2,
                    "customer_phone3": customer_phone3,
                    "customer_website": customer_website,
                    "documents": documents,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerUpdateResponse,
        )

    def list(
        self,
        *,
        api_key: str,
        conversion_date: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        search_filter: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerListResponse:
        """
        Get All Customers

        Args:
          conversion_date:
              get customers that were created or converted after the sent date | Date format :
              yyyy-MM-dd

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          search_filter: general search filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return self._get(
            "/customers/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "conversion_date": conversion_date,
                        "limit": limit,
                        "page": page,
                        "search_filter": search_filter,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            cast_to=CustomerListResponse,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/hu55ain3laa/testMCP#with_streaming_response
        """
        return AsyncCustomersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_type: str,
        api_key: str,
        company_name: str | NotGiven = NOT_GIVEN,
        customer_address: str | NotGiven = NOT_GIVEN,
        customer_city: str | NotGiven = NOT_GIVEN,
        customer_code: int | NotGiven = NOT_GIVEN,
        customer_comm_reg_number: str | NotGiven = NOT_GIVEN,
        customer_email: str | NotGiven = NOT_GIVEN,
        customer_fax: str | NotGiven = NOT_GIVEN,
        customer_first_name: str | NotGiven = NOT_GIVEN,
        customer_last_name: str | NotGiven = NOT_GIVEN,
        customer_middle_name: str | NotGiven = NOT_GIVEN,
        customer_phone1: str | NotGiven = NOT_GIVEN,
        customer_phone2: str | NotGiven = NOT_GIVEN,
        customer_phone3: str | NotGiven = NOT_GIVEN,
        customer_website: str | NotGiven = NOT_GIVEN,
        documents: Iterable[DocumentsInfoParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerCreateResponse:
        """
        Save New Customer

        Args:
          customer_type: always required, values ('company' 'individual' 'cash' 'potential')

          company_name: Customer company name , required for type company and potential

          customer_address: Customer Address

          customer_city: Customer city , must exist in cities defintions

          customer_code: Customer code

          customer_comm_reg_number: Customer Commercial Registration No.

          customer_email: Customer Email

          customer_fax: Customer Fax

          customer_first_name: Customer first name , required for type individual and cash

          customer_last_name: Customer last Name , required for type individual and cash

          customer_middle_name: Customer middle Name

          customer_phone1: Customer Phone 1 , required for type individual and cash

          customer_phone2: Customer Phone 2

          customer_phone3: Customer Phone 3

          customer_website: Customer Website

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._post(
            "/customers/",
            body=await async_maybe_transform(
                {
                    "customer_type": customer_type,
                    "company_name": company_name,
                    "customer_address": customer_address,
                    "customer_city": customer_city,
                    "customer_code": customer_code,
                    "customer_comm_reg_number": customer_comm_reg_number,
                    "customer_email": customer_email,
                    "customer_fax": customer_fax,
                    "customer_first_name": customer_first_name,
                    "customer_last_name": customer_last_name,
                    "customer_middle_name": customer_middle_name,
                    "customer_phone1": customer_phone1,
                    "customer_phone2": customer_phone2,
                    "customer_phone3": customer_phone3,
                    "customer_website": customer_website,
                    "documents": documents,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerCreateResponse,
        )

    async def retrieve(
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
    ) -> Customer:
        """
        Get Single Customer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._get(
            f"/customers/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Customer,
        )

    async def update(
        self,
        id: str,
        *,
        api_key: str,
        company_name: str | NotGiven = NOT_GIVEN,
        customer_address: str | NotGiven = NOT_GIVEN,
        customer_city: str | NotGiven = NOT_GIVEN,
        customer_code: int | NotGiven = NOT_GIVEN,
        customer_comm_reg_number: str | NotGiven = NOT_GIVEN,
        customer_email: str | NotGiven = NOT_GIVEN,
        customer_fax: str | NotGiven = NOT_GIVEN,
        customer_first_name: str | NotGiven = NOT_GIVEN,
        customer_last_name: str | NotGiven = NOT_GIVEN,
        customer_middle_name: str | NotGiven = NOT_GIVEN,
        customer_phone1: str | NotGiven = NOT_GIVEN,
        customer_phone2: str | NotGiven = NOT_GIVEN,
        customer_phone3: str | NotGiven = NOT_GIVEN,
        customer_website: str | NotGiven = NOT_GIVEN,
        documents: Iterable[DocumentsInfoParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerUpdateResponse:
        """
        Update Single Customer

        Args:
          company_name: Customer company name

          customer_address: Customer Address

          customer_city: Customer city , must exist in cities defintions

          customer_code: Customer code

          customer_comm_reg_number: Customer Commercial Registration No.

          customer_email: Customer Email

          customer_fax: Customer Fax

          customer_first_name: Customer first name

          customer_last_name: Customer last Name

          customer_middle_name: Customer middle Name

          customer_phone1: Customer Phone 1

          customer_phone2: Customer Phone 2

          customer_phone3: Customer Phone 3

          customer_website: Customer Website

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._put(
            f"/customers/{id}",
            body=await async_maybe_transform(
                {
                    "company_name": company_name,
                    "customer_address": customer_address,
                    "customer_city": customer_city,
                    "customer_code": customer_code,
                    "customer_comm_reg_number": customer_comm_reg_number,
                    "customer_email": customer_email,
                    "customer_fax": customer_fax,
                    "customer_first_name": customer_first_name,
                    "customer_last_name": customer_last_name,
                    "customer_middle_name": customer_middle_name,
                    "customer_phone1": customer_phone1,
                    "customer_phone2": customer_phone2,
                    "customer_phone3": customer_phone3,
                    "customer_website": customer_website,
                    "documents": documents,
                },
                customer_update_params.CustomerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerUpdateResponse,
        )

    async def list(
        self,
        *,
        api_key: str,
        conversion_date: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        search_filter: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerListResponse:
        """
        Get All Customers

        Args:
          conversion_date:
              get customers that were created or converted after the sent date | Date format :
              yyyy-MM-dd

          limit: the number of records per page | 250 by default | 500 maximum

          page: the page offset | page 1 by default

          search_filter: general search filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"apiKey": api_key, **(extra_headers or {})}
        return await self._get(
            "/customers/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "conversion_date": conversion_date,
                        "limit": limit,
                        "page": page,
                        "search_filter": search_filter,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            cast_to=CustomerListResponse,
        )


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            customers.retrieve,
        )
        self.update = to_raw_response_wrapper(
            customers.update,
        )
        self.list = to_raw_response_wrapper(
            customers.list,
        )


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            customers.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            customers.update,
        )
        self.list = async_to_raw_response_wrapper(
            customers.list,
        )


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            customers.update,
        )
        self.list = to_streamed_response_wrapper(
            customers.list,
        )


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            customers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            customers.list,
        )
