# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from testmcp import Testmcp, AsyncTestmcp
from tests.utils import assert_matches_type
from testmcp.types import SupplierCreateResponse, SupplierUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSuppliers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Testmcp) -> None:
        supplier = client.suppliers.create(
            name="Supplier Name",
            api_key="apiKey",
        )
        assert_matches_type(SupplierCreateResponse, supplier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Testmcp) -> None:
        supplier = client.suppliers.create(
            name="Supplier Name",
            api_key="apiKey",
            city="Supplier City",
            code="1234",
            comm_reg_number="123456781",
            email="contact@supplier.com",
            phone1="+961 1 123456",
        )
        assert_matches_type(SupplierCreateResponse, supplier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Testmcp) -> None:
        response = client.suppliers.with_raw_response.create(
            name="Supplier Name",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supplier = response.parse()
        assert_matches_type(SupplierCreateResponse, supplier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Testmcp) -> None:
        with client.suppliers.with_streaming_response.create(
            name="Supplier Name",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supplier = response.parse()
            assert_matches_type(SupplierCreateResponse, supplier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Testmcp) -> None:
        supplier = client.suppliers.update(
            id="id",
            api_key="apiKey",
        )
        assert_matches_type(SupplierUpdateResponse, supplier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Testmcp) -> None:
        supplier = client.suppliers.update(
            id="id",
            api_key="apiKey",
            city="Supplier City",
            code="1234",
            comm_reg_number="123456781",
            email="contact@supplier.com",
            name="Supplier Name",
            phone1="+961 1 123456",
        )
        assert_matches_type(SupplierUpdateResponse, supplier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Testmcp) -> None:
        response = client.suppliers.with_raw_response.update(
            id="id",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supplier = response.parse()
        assert_matches_type(SupplierUpdateResponse, supplier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Testmcp) -> None:
        with client.suppliers.with_streaming_response.update(
            id="id",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supplier = response.parse()
            assert_matches_type(SupplierUpdateResponse, supplier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Testmcp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.suppliers.with_raw_response.update(
                id="",
                api_key="apiKey",
            )


class TestAsyncSuppliers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTestmcp) -> None:
        supplier = await async_client.suppliers.create(
            name="Supplier Name",
            api_key="apiKey",
        )
        assert_matches_type(SupplierCreateResponse, supplier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTestmcp) -> None:
        supplier = await async_client.suppliers.create(
            name="Supplier Name",
            api_key="apiKey",
            city="Supplier City",
            code="1234",
            comm_reg_number="123456781",
            email="contact@supplier.com",
            phone1="+961 1 123456",
        )
        assert_matches_type(SupplierCreateResponse, supplier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.suppliers.with_raw_response.create(
            name="Supplier Name",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supplier = await response.parse()
        assert_matches_type(SupplierCreateResponse, supplier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTestmcp) -> None:
        async with async_client.suppliers.with_streaming_response.create(
            name="Supplier Name",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supplier = await response.parse()
            assert_matches_type(SupplierCreateResponse, supplier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTestmcp) -> None:
        supplier = await async_client.suppliers.update(
            id="id",
            api_key="apiKey",
        )
        assert_matches_type(SupplierUpdateResponse, supplier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTestmcp) -> None:
        supplier = await async_client.suppliers.update(
            id="id",
            api_key="apiKey",
            city="Supplier City",
            code="1234",
            comm_reg_number="123456781",
            email="contact@supplier.com",
            name="Supplier Name",
            phone1="+961 1 123456",
        )
        assert_matches_type(SupplierUpdateResponse, supplier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.suppliers.with_raw_response.update(
            id="id",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        supplier = await response.parse()
        assert_matches_type(SupplierUpdateResponse, supplier, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTestmcp) -> None:
        async with async_client.suppliers.with_streaming_response.update(
            id="id",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            supplier = await response.parse()
            assert_matches_type(SupplierUpdateResponse, supplier, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTestmcp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.suppliers.with_raw_response.update(
                id="",
                api_key="apiKey",
            )
