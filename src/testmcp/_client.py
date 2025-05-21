# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import (
    product,
    currency,
    vouchers,
    customers,
    employees,
    suppliers,
    attendance,
    categories,
    purchase_quotations,
    purchase_requisitions,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.sales_invoices import sales_invoices
from .resources.sales_quotations import sales_quotations

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Testmcp", "AsyncTestmcp", "Client", "AsyncClient"]


class Testmcp(SyncAPIClient):
    __test__ = False
    product: product.ProductResource
    categories: categories.CategoriesResource
    currency: currency.CurrencyResource
    vouchers: vouchers.VouchersResource
    customers: customers.CustomersResource
    suppliers: suppliers.SuppliersResource
    purchase_requisitions: purchase_requisitions.PurchaseRequisitionsResource
    purchase_quotations: purchase_quotations.PurchaseQuotationsResource
    sales_quotations: sales_quotations.SalesQuotationsResource
    sales_invoices: sales_invoices.SalesInvoicesResource
    employees: employees.EmployeesResource
    attendance: attendance.AttendanceResource
    with_raw_response: TestmcpWithRawResponse
    with_streaming_response: TestmcpWithStreamedResponse

    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Testmcp client instance.

        This automatically infers the `api_key` argument from the `TESTMCP_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("TESTMCP_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("TESTMCP_BASE_URL")
        if base_url is None:
            base_url = f"/webapi/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.product = product.ProductResource(self)
        self.categories = categories.CategoriesResource(self)
        self.currency = currency.CurrencyResource(self)
        self.vouchers = vouchers.VouchersResource(self)
        self.customers = customers.CustomersResource(self)
        self.suppliers = suppliers.SuppliersResource(self)
        self.purchase_requisitions = purchase_requisitions.PurchaseRequisitionsResource(self)
        self.purchase_quotations = purchase_quotations.PurchaseQuotationsResource(self)
        self.sales_quotations = sales_quotations.SalesQuotationsResource(self)
        self.sales_invoices = sales_invoices.SalesInvoicesResource(self)
        self.employees = employees.EmployeesResource(self)
        self.attendance = attendance.AttendanceResource(self)
        self.with_raw_response = TestmcpWithRawResponse(self)
        self.with_streaming_response = TestmcpWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncTestmcp(AsyncAPIClient):
    product: product.AsyncProductResource
    categories: categories.AsyncCategoriesResource
    currency: currency.AsyncCurrencyResource
    vouchers: vouchers.AsyncVouchersResource
    customers: customers.AsyncCustomersResource
    suppliers: suppliers.AsyncSuppliersResource
    purchase_requisitions: purchase_requisitions.AsyncPurchaseRequisitionsResource
    purchase_quotations: purchase_quotations.AsyncPurchaseQuotationsResource
    sales_quotations: sales_quotations.AsyncSalesQuotationsResource
    sales_invoices: sales_invoices.AsyncSalesInvoicesResource
    employees: employees.AsyncEmployeesResource
    attendance: attendance.AsyncAttendanceResource
    with_raw_response: AsyncTestmcpWithRawResponse
    with_streaming_response: AsyncTestmcpWithStreamedResponse

    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncTestmcp client instance.

        This automatically infers the `api_key` argument from the `TESTMCP_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("TESTMCP_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("TESTMCP_BASE_URL")
        if base_url is None:
            base_url = f"/webapi/"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.product = product.AsyncProductResource(self)
        self.categories = categories.AsyncCategoriesResource(self)
        self.currency = currency.AsyncCurrencyResource(self)
        self.vouchers = vouchers.AsyncVouchersResource(self)
        self.customers = customers.AsyncCustomersResource(self)
        self.suppliers = suppliers.AsyncSuppliersResource(self)
        self.purchase_requisitions = purchase_requisitions.AsyncPurchaseRequisitionsResource(self)
        self.purchase_quotations = purchase_quotations.AsyncPurchaseQuotationsResource(self)
        self.sales_quotations = sales_quotations.AsyncSalesQuotationsResource(self)
        self.sales_invoices = sales_invoices.AsyncSalesInvoicesResource(self)
        self.employees = employees.AsyncEmployeesResource(self)
        self.attendance = attendance.AsyncAttendanceResource(self)
        self.with_raw_response = AsyncTestmcpWithRawResponse(self)
        self.with_streaming_response = AsyncTestmcpWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class TestmcpWithRawResponse:
    __test__ = False

    def __init__(self, client: Testmcp) -> None:
        self.product = product.ProductResourceWithRawResponse(client.product)
        self.categories = categories.CategoriesResourceWithRawResponse(client.categories)
        self.currency = currency.CurrencyResourceWithRawResponse(client.currency)
        self.vouchers = vouchers.VouchersResourceWithRawResponse(client.vouchers)
        self.customers = customers.CustomersResourceWithRawResponse(client.customers)
        self.suppliers = suppliers.SuppliersResourceWithRawResponse(client.suppliers)
        self.purchase_requisitions = purchase_requisitions.PurchaseRequisitionsResourceWithRawResponse(
            client.purchase_requisitions
        )
        self.purchase_quotations = purchase_quotations.PurchaseQuotationsResourceWithRawResponse(
            client.purchase_quotations
        )
        self.sales_quotations = sales_quotations.SalesQuotationsResourceWithRawResponse(client.sales_quotations)
        self.sales_invoices = sales_invoices.SalesInvoicesResourceWithRawResponse(client.sales_invoices)
        self.employees = employees.EmployeesResourceWithRawResponse(client.employees)
        self.attendance = attendance.AttendanceResourceWithRawResponse(client.attendance)


class AsyncTestmcpWithRawResponse:
    def __init__(self, client: AsyncTestmcp) -> None:
        self.product = product.AsyncProductResourceWithRawResponse(client.product)
        self.categories = categories.AsyncCategoriesResourceWithRawResponse(client.categories)
        self.currency = currency.AsyncCurrencyResourceWithRawResponse(client.currency)
        self.vouchers = vouchers.AsyncVouchersResourceWithRawResponse(client.vouchers)
        self.customers = customers.AsyncCustomersResourceWithRawResponse(client.customers)
        self.suppliers = suppliers.AsyncSuppliersResourceWithRawResponse(client.suppliers)
        self.purchase_requisitions = purchase_requisitions.AsyncPurchaseRequisitionsResourceWithRawResponse(
            client.purchase_requisitions
        )
        self.purchase_quotations = purchase_quotations.AsyncPurchaseQuotationsResourceWithRawResponse(
            client.purchase_quotations
        )
        self.sales_quotations = sales_quotations.AsyncSalesQuotationsResourceWithRawResponse(client.sales_quotations)
        self.sales_invoices = sales_invoices.AsyncSalesInvoicesResourceWithRawResponse(client.sales_invoices)
        self.employees = employees.AsyncEmployeesResourceWithRawResponse(client.employees)
        self.attendance = attendance.AsyncAttendanceResourceWithRawResponse(client.attendance)


class TestmcpWithStreamedResponse:
    __test__ = False

    def __init__(self, client: Testmcp) -> None:
        self.product = product.ProductResourceWithStreamingResponse(client.product)
        self.categories = categories.CategoriesResourceWithStreamingResponse(client.categories)
        self.currency = currency.CurrencyResourceWithStreamingResponse(client.currency)
        self.vouchers = vouchers.VouchersResourceWithStreamingResponse(client.vouchers)
        self.customers = customers.CustomersResourceWithStreamingResponse(client.customers)
        self.suppliers = suppliers.SuppliersResourceWithStreamingResponse(client.suppliers)
        self.purchase_requisitions = purchase_requisitions.PurchaseRequisitionsResourceWithStreamingResponse(
            client.purchase_requisitions
        )
        self.purchase_quotations = purchase_quotations.PurchaseQuotationsResourceWithStreamingResponse(
            client.purchase_quotations
        )
        self.sales_quotations = sales_quotations.SalesQuotationsResourceWithStreamingResponse(client.sales_quotations)
        self.sales_invoices = sales_invoices.SalesInvoicesResourceWithStreamingResponse(client.sales_invoices)
        self.employees = employees.EmployeesResourceWithStreamingResponse(client.employees)
        self.attendance = attendance.AttendanceResourceWithStreamingResponse(client.attendance)


class AsyncTestmcpWithStreamedResponse:
    def __init__(self, client: AsyncTestmcp) -> None:
        self.product = product.AsyncProductResourceWithStreamingResponse(client.product)
        self.categories = categories.AsyncCategoriesResourceWithStreamingResponse(client.categories)
        self.currency = currency.AsyncCurrencyResourceWithStreamingResponse(client.currency)
        self.vouchers = vouchers.AsyncVouchersResourceWithStreamingResponse(client.vouchers)
        self.customers = customers.AsyncCustomersResourceWithStreamingResponse(client.customers)
        self.suppliers = suppliers.AsyncSuppliersResourceWithStreamingResponse(client.suppliers)
        self.purchase_requisitions = purchase_requisitions.AsyncPurchaseRequisitionsResourceWithStreamingResponse(
            client.purchase_requisitions
        )
        self.purchase_quotations = purchase_quotations.AsyncPurchaseQuotationsResourceWithStreamingResponse(
            client.purchase_quotations
        )
        self.sales_quotations = sales_quotations.AsyncSalesQuotationsResourceWithStreamingResponse(
            client.sales_quotations
        )
        self.sales_invoices = sales_invoices.AsyncSalesInvoicesResourceWithStreamingResponse(client.sales_invoices)
        self.employees = employees.AsyncEmployeesResourceWithStreamingResponse(client.employees)
        self.attendance = attendance.AsyncAttendanceResourceWithStreamingResponse(client.attendance)


Client = Testmcp

AsyncClient = AsyncTestmcp
