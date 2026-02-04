# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        product,
        currency,
        vouchers,
        customers,
        employees,
        suppliers,
        attendance,
        categories,
        sales_invoices,
        sales_quotations,
        purchase_quotations,
        purchase_requisitions,
    )
    from .resources.product import ProductResource, AsyncProductResource
    from .resources.currency import CurrencyResource, AsyncCurrencyResource
    from .resources.vouchers import VouchersResource, AsyncVouchersResource
    from .resources.customers import CustomersResource, AsyncCustomersResource
    from .resources.employees import EmployeesResource, AsyncEmployeesResource
    from .resources.suppliers import SuppliersResource, AsyncSuppliersResource
    from .resources.attendance import AttendanceResource, AsyncAttendanceResource
    from .resources.categories import CategoriesResource, AsyncCategoriesResource
    from .resources.purchase_quotations import PurchaseQuotationsResource, AsyncPurchaseQuotationsResource
    from .resources.purchase_requisitions import PurchaseRequisitionsResource, AsyncPurchaseRequisitionsResource
    from .resources.sales_invoices.sales_invoices import SalesInvoicesResource, AsyncSalesInvoicesResource
    from .resources.sales_quotations.sales_quotations import SalesQuotationsResource, AsyncSalesQuotationsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Testmcp", "AsyncTestmcp", "Client", "AsyncClient"]


class Testmcp(SyncAPIClient):
    __test__ = False
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def product(self) -> ProductResource:
        from .resources.product import ProductResource

        return ProductResource(self)

    @cached_property
    def categories(self) -> CategoriesResource:
        from .resources.categories import CategoriesResource

        return CategoriesResource(self)

    @cached_property
    def currency(self) -> CurrencyResource:
        from .resources.currency import CurrencyResource

        return CurrencyResource(self)

    @cached_property
    def vouchers(self) -> VouchersResource:
        from .resources.vouchers import VouchersResource

        return VouchersResource(self)

    @cached_property
    def customers(self) -> CustomersResource:
        from .resources.customers import CustomersResource

        return CustomersResource(self)

    @cached_property
    def suppliers(self) -> SuppliersResource:
        from .resources.suppliers import SuppliersResource

        return SuppliersResource(self)

    @cached_property
    def purchase_requisitions(self) -> PurchaseRequisitionsResource:
        from .resources.purchase_requisitions import PurchaseRequisitionsResource

        return PurchaseRequisitionsResource(self)

    @cached_property
    def purchase_quotations(self) -> PurchaseQuotationsResource:
        from .resources.purchase_quotations import PurchaseQuotationsResource

        return PurchaseQuotationsResource(self)

    @cached_property
    def sales_quotations(self) -> SalesQuotationsResource:
        from .resources.sales_quotations import SalesQuotationsResource

        return SalesQuotationsResource(self)

    @cached_property
    def sales_invoices(self) -> SalesInvoicesResource:
        from .resources.sales_invoices import SalesInvoicesResource

        return SalesInvoicesResource(self)

    @cached_property
    def employees(self) -> EmployeesResource:
        from .resources.employees import EmployeesResource

        return EmployeesResource(self)

    @cached_property
    def attendance(self) -> AttendanceResource:
        from .resources.attendance import AttendanceResource

        return AttendanceResource(self)

    @cached_property
    def with_raw_response(self) -> TestmcpWithRawResponse:
        return TestmcpWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestmcpWithStreamedResponse:
        return TestmcpWithStreamedResponse(self)

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
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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

    @cached_property
    def product(self) -> AsyncProductResource:
        from .resources.product import AsyncProductResource

        return AsyncProductResource(self)

    @cached_property
    def categories(self) -> AsyncCategoriesResource:
        from .resources.categories import AsyncCategoriesResource

        return AsyncCategoriesResource(self)

    @cached_property
    def currency(self) -> AsyncCurrencyResource:
        from .resources.currency import AsyncCurrencyResource

        return AsyncCurrencyResource(self)

    @cached_property
    def vouchers(self) -> AsyncVouchersResource:
        from .resources.vouchers import AsyncVouchersResource

        return AsyncVouchersResource(self)

    @cached_property
    def customers(self) -> AsyncCustomersResource:
        from .resources.customers import AsyncCustomersResource

        return AsyncCustomersResource(self)

    @cached_property
    def suppliers(self) -> AsyncSuppliersResource:
        from .resources.suppliers import AsyncSuppliersResource

        return AsyncSuppliersResource(self)

    @cached_property
    def purchase_requisitions(self) -> AsyncPurchaseRequisitionsResource:
        from .resources.purchase_requisitions import AsyncPurchaseRequisitionsResource

        return AsyncPurchaseRequisitionsResource(self)

    @cached_property
    def purchase_quotations(self) -> AsyncPurchaseQuotationsResource:
        from .resources.purchase_quotations import AsyncPurchaseQuotationsResource

        return AsyncPurchaseQuotationsResource(self)

    @cached_property
    def sales_quotations(self) -> AsyncSalesQuotationsResource:
        from .resources.sales_quotations import AsyncSalesQuotationsResource

        return AsyncSalesQuotationsResource(self)

    @cached_property
    def sales_invoices(self) -> AsyncSalesInvoicesResource:
        from .resources.sales_invoices import AsyncSalesInvoicesResource

        return AsyncSalesInvoicesResource(self)

    @cached_property
    def employees(self) -> AsyncEmployeesResource:
        from .resources.employees import AsyncEmployeesResource

        return AsyncEmployeesResource(self)

    @cached_property
    def attendance(self) -> AsyncAttendanceResource:
        from .resources.attendance import AsyncAttendanceResource

        return AsyncAttendanceResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncTestmcpWithRawResponse:
        return AsyncTestmcpWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestmcpWithStreamedResponse:
        return AsyncTestmcpWithStreamedResponse(self)

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
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
    _client: Testmcp

    def __init__(self, client: Testmcp) -> None:
        self._client = client

    @cached_property
    def product(self) -> product.ProductResourceWithRawResponse:
        from .resources.product import ProductResourceWithRawResponse

        return ProductResourceWithRawResponse(self._client.product)

    @cached_property
    def categories(self) -> categories.CategoriesResourceWithRawResponse:
        from .resources.categories import CategoriesResourceWithRawResponse

        return CategoriesResourceWithRawResponse(self._client.categories)

    @cached_property
    def currency(self) -> currency.CurrencyResourceWithRawResponse:
        from .resources.currency import CurrencyResourceWithRawResponse

        return CurrencyResourceWithRawResponse(self._client.currency)

    @cached_property
    def vouchers(self) -> vouchers.VouchersResourceWithRawResponse:
        from .resources.vouchers import VouchersResourceWithRawResponse

        return VouchersResourceWithRawResponse(self._client.vouchers)

    @cached_property
    def customers(self) -> customers.CustomersResourceWithRawResponse:
        from .resources.customers import CustomersResourceWithRawResponse

        return CustomersResourceWithRawResponse(self._client.customers)

    @cached_property
    def suppliers(self) -> suppliers.SuppliersResourceWithRawResponse:
        from .resources.suppliers import SuppliersResourceWithRawResponse

        return SuppliersResourceWithRawResponse(self._client.suppliers)

    @cached_property
    def purchase_requisitions(self) -> purchase_requisitions.PurchaseRequisitionsResourceWithRawResponse:
        from .resources.purchase_requisitions import PurchaseRequisitionsResourceWithRawResponse

        return PurchaseRequisitionsResourceWithRawResponse(self._client.purchase_requisitions)

    @cached_property
    def purchase_quotations(self) -> purchase_quotations.PurchaseQuotationsResourceWithRawResponse:
        from .resources.purchase_quotations import PurchaseQuotationsResourceWithRawResponse

        return PurchaseQuotationsResourceWithRawResponse(self._client.purchase_quotations)

    @cached_property
    def sales_quotations(self) -> sales_quotations.SalesQuotationsResourceWithRawResponse:
        from .resources.sales_quotations import SalesQuotationsResourceWithRawResponse

        return SalesQuotationsResourceWithRawResponse(self._client.sales_quotations)

    @cached_property
    def sales_invoices(self) -> sales_invoices.SalesInvoicesResourceWithRawResponse:
        from .resources.sales_invoices import SalesInvoicesResourceWithRawResponse

        return SalesInvoicesResourceWithRawResponse(self._client.sales_invoices)

    @cached_property
    def employees(self) -> employees.EmployeesResourceWithRawResponse:
        from .resources.employees import EmployeesResourceWithRawResponse

        return EmployeesResourceWithRawResponse(self._client.employees)

    @cached_property
    def attendance(self) -> attendance.AttendanceResourceWithRawResponse:
        from .resources.attendance import AttendanceResourceWithRawResponse

        return AttendanceResourceWithRawResponse(self._client.attendance)


class AsyncTestmcpWithRawResponse:
    _client: AsyncTestmcp

    def __init__(self, client: AsyncTestmcp) -> None:
        self._client = client

    @cached_property
    def product(self) -> product.AsyncProductResourceWithRawResponse:
        from .resources.product import AsyncProductResourceWithRawResponse

        return AsyncProductResourceWithRawResponse(self._client.product)

    @cached_property
    def categories(self) -> categories.AsyncCategoriesResourceWithRawResponse:
        from .resources.categories import AsyncCategoriesResourceWithRawResponse

        return AsyncCategoriesResourceWithRawResponse(self._client.categories)

    @cached_property
    def currency(self) -> currency.AsyncCurrencyResourceWithRawResponse:
        from .resources.currency import AsyncCurrencyResourceWithRawResponse

        return AsyncCurrencyResourceWithRawResponse(self._client.currency)

    @cached_property
    def vouchers(self) -> vouchers.AsyncVouchersResourceWithRawResponse:
        from .resources.vouchers import AsyncVouchersResourceWithRawResponse

        return AsyncVouchersResourceWithRawResponse(self._client.vouchers)

    @cached_property
    def customers(self) -> customers.AsyncCustomersResourceWithRawResponse:
        from .resources.customers import AsyncCustomersResourceWithRawResponse

        return AsyncCustomersResourceWithRawResponse(self._client.customers)

    @cached_property
    def suppliers(self) -> suppliers.AsyncSuppliersResourceWithRawResponse:
        from .resources.suppliers import AsyncSuppliersResourceWithRawResponse

        return AsyncSuppliersResourceWithRawResponse(self._client.suppliers)

    @cached_property
    def purchase_requisitions(self) -> purchase_requisitions.AsyncPurchaseRequisitionsResourceWithRawResponse:
        from .resources.purchase_requisitions import AsyncPurchaseRequisitionsResourceWithRawResponse

        return AsyncPurchaseRequisitionsResourceWithRawResponse(self._client.purchase_requisitions)

    @cached_property
    def purchase_quotations(self) -> purchase_quotations.AsyncPurchaseQuotationsResourceWithRawResponse:
        from .resources.purchase_quotations import AsyncPurchaseQuotationsResourceWithRawResponse

        return AsyncPurchaseQuotationsResourceWithRawResponse(self._client.purchase_quotations)

    @cached_property
    def sales_quotations(self) -> sales_quotations.AsyncSalesQuotationsResourceWithRawResponse:
        from .resources.sales_quotations import AsyncSalesQuotationsResourceWithRawResponse

        return AsyncSalesQuotationsResourceWithRawResponse(self._client.sales_quotations)

    @cached_property
    def sales_invoices(self) -> sales_invoices.AsyncSalesInvoicesResourceWithRawResponse:
        from .resources.sales_invoices import AsyncSalesInvoicesResourceWithRawResponse

        return AsyncSalesInvoicesResourceWithRawResponse(self._client.sales_invoices)

    @cached_property
    def employees(self) -> employees.AsyncEmployeesResourceWithRawResponse:
        from .resources.employees import AsyncEmployeesResourceWithRawResponse

        return AsyncEmployeesResourceWithRawResponse(self._client.employees)

    @cached_property
    def attendance(self) -> attendance.AsyncAttendanceResourceWithRawResponse:
        from .resources.attendance import AsyncAttendanceResourceWithRawResponse

        return AsyncAttendanceResourceWithRawResponse(self._client.attendance)


class TestmcpWithStreamedResponse:
    __test__ = False
    _client: Testmcp

    def __init__(self, client: Testmcp) -> None:
        self._client = client

    @cached_property
    def product(self) -> product.ProductResourceWithStreamingResponse:
        from .resources.product import ProductResourceWithStreamingResponse

        return ProductResourceWithStreamingResponse(self._client.product)

    @cached_property
    def categories(self) -> categories.CategoriesResourceWithStreamingResponse:
        from .resources.categories import CategoriesResourceWithStreamingResponse

        return CategoriesResourceWithStreamingResponse(self._client.categories)

    @cached_property
    def currency(self) -> currency.CurrencyResourceWithStreamingResponse:
        from .resources.currency import CurrencyResourceWithStreamingResponse

        return CurrencyResourceWithStreamingResponse(self._client.currency)

    @cached_property
    def vouchers(self) -> vouchers.VouchersResourceWithStreamingResponse:
        from .resources.vouchers import VouchersResourceWithStreamingResponse

        return VouchersResourceWithStreamingResponse(self._client.vouchers)

    @cached_property
    def customers(self) -> customers.CustomersResourceWithStreamingResponse:
        from .resources.customers import CustomersResourceWithStreamingResponse

        return CustomersResourceWithStreamingResponse(self._client.customers)

    @cached_property
    def suppliers(self) -> suppliers.SuppliersResourceWithStreamingResponse:
        from .resources.suppliers import SuppliersResourceWithStreamingResponse

        return SuppliersResourceWithStreamingResponse(self._client.suppliers)

    @cached_property
    def purchase_requisitions(self) -> purchase_requisitions.PurchaseRequisitionsResourceWithStreamingResponse:
        from .resources.purchase_requisitions import PurchaseRequisitionsResourceWithStreamingResponse

        return PurchaseRequisitionsResourceWithStreamingResponse(self._client.purchase_requisitions)

    @cached_property
    def purchase_quotations(self) -> purchase_quotations.PurchaseQuotationsResourceWithStreamingResponse:
        from .resources.purchase_quotations import PurchaseQuotationsResourceWithStreamingResponse

        return PurchaseQuotationsResourceWithStreamingResponse(self._client.purchase_quotations)

    @cached_property
    def sales_quotations(self) -> sales_quotations.SalesQuotationsResourceWithStreamingResponse:
        from .resources.sales_quotations import SalesQuotationsResourceWithStreamingResponse

        return SalesQuotationsResourceWithStreamingResponse(self._client.sales_quotations)

    @cached_property
    def sales_invoices(self) -> sales_invoices.SalesInvoicesResourceWithStreamingResponse:
        from .resources.sales_invoices import SalesInvoicesResourceWithStreamingResponse

        return SalesInvoicesResourceWithStreamingResponse(self._client.sales_invoices)

    @cached_property
    def employees(self) -> employees.EmployeesResourceWithStreamingResponse:
        from .resources.employees import EmployeesResourceWithStreamingResponse

        return EmployeesResourceWithStreamingResponse(self._client.employees)

    @cached_property
    def attendance(self) -> attendance.AttendanceResourceWithStreamingResponse:
        from .resources.attendance import AttendanceResourceWithStreamingResponse

        return AttendanceResourceWithStreamingResponse(self._client.attendance)


class AsyncTestmcpWithStreamedResponse:
    _client: AsyncTestmcp

    def __init__(self, client: AsyncTestmcp) -> None:
        self._client = client

    @cached_property
    def product(self) -> product.AsyncProductResourceWithStreamingResponse:
        from .resources.product import AsyncProductResourceWithStreamingResponse

        return AsyncProductResourceWithStreamingResponse(self._client.product)

    @cached_property
    def categories(self) -> categories.AsyncCategoriesResourceWithStreamingResponse:
        from .resources.categories import AsyncCategoriesResourceWithStreamingResponse

        return AsyncCategoriesResourceWithStreamingResponse(self._client.categories)

    @cached_property
    def currency(self) -> currency.AsyncCurrencyResourceWithStreamingResponse:
        from .resources.currency import AsyncCurrencyResourceWithStreamingResponse

        return AsyncCurrencyResourceWithStreamingResponse(self._client.currency)

    @cached_property
    def vouchers(self) -> vouchers.AsyncVouchersResourceWithStreamingResponse:
        from .resources.vouchers import AsyncVouchersResourceWithStreamingResponse

        return AsyncVouchersResourceWithStreamingResponse(self._client.vouchers)

    @cached_property
    def customers(self) -> customers.AsyncCustomersResourceWithStreamingResponse:
        from .resources.customers import AsyncCustomersResourceWithStreamingResponse

        return AsyncCustomersResourceWithStreamingResponse(self._client.customers)

    @cached_property
    def suppliers(self) -> suppliers.AsyncSuppliersResourceWithStreamingResponse:
        from .resources.suppliers import AsyncSuppliersResourceWithStreamingResponse

        return AsyncSuppliersResourceWithStreamingResponse(self._client.suppliers)

    @cached_property
    def purchase_requisitions(self) -> purchase_requisitions.AsyncPurchaseRequisitionsResourceWithStreamingResponse:
        from .resources.purchase_requisitions import AsyncPurchaseRequisitionsResourceWithStreamingResponse

        return AsyncPurchaseRequisitionsResourceWithStreamingResponse(self._client.purchase_requisitions)

    @cached_property
    def purchase_quotations(self) -> purchase_quotations.AsyncPurchaseQuotationsResourceWithStreamingResponse:
        from .resources.purchase_quotations import AsyncPurchaseQuotationsResourceWithStreamingResponse

        return AsyncPurchaseQuotationsResourceWithStreamingResponse(self._client.purchase_quotations)

    @cached_property
    def sales_quotations(self) -> sales_quotations.AsyncSalesQuotationsResourceWithStreamingResponse:
        from .resources.sales_quotations import AsyncSalesQuotationsResourceWithStreamingResponse

        return AsyncSalesQuotationsResourceWithStreamingResponse(self._client.sales_quotations)

    @cached_property
    def sales_invoices(self) -> sales_invoices.AsyncSalesInvoicesResourceWithStreamingResponse:
        from .resources.sales_invoices import AsyncSalesInvoicesResourceWithStreamingResponse

        return AsyncSalesInvoicesResourceWithStreamingResponse(self._client.sales_invoices)

    @cached_property
    def employees(self) -> employees.AsyncEmployeesResourceWithStreamingResponse:
        from .resources.employees import AsyncEmployeesResourceWithStreamingResponse

        return AsyncEmployeesResourceWithStreamingResponse(self._client.employees)

    @cached_property
    def attendance(self) -> attendance.AsyncAttendanceResourceWithStreamingResponse:
        from .resources.attendance import AsyncAttendanceResourceWithStreamingResponse

        return AsyncAttendanceResourceWithStreamingResponse(self._client.attendance)


Client = Testmcp

AsyncClient = AsyncTestmcp
