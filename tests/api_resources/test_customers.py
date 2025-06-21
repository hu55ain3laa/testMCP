# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from testmcp import Testmcp, AsyncTestmcp
from tests.utils import assert_matches_type
from testmcp.types import (
    Customer,
    CustomerListResponse,
    CustomerCreateResponse,
    CustomerUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Testmcp) -> None:
        customer = client.customers.create(
            customer_type="company",
            api_key="apiKey",
        )
        assert_matches_type(CustomerCreateResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Testmcp) -> None:
        customer = client.customers.create(
            customer_type="company",
            api_key="apiKey",
            company_name="Compp Name",
            customer_address="New York",
            customer_city="New York",
            customer_code=40,
            customer_comm_reg_number="1234",
            customer_email="john_harry_smith@test.com",
            customer_fax="01/012012",
            customer_first_name="John",
            customer_last_name="Smith",
            customer_middle_name="Harry",
            customer_phone1="01/012012",
            customer_phone2="01/012012",
            customer_phone3="01/012012",
            customer_website="test.com",
            documents=[
                {
                    "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                    "file_name": "image_name.png",
                    "description": "file description",
                }
            ],
        )
        assert_matches_type(CustomerCreateResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Testmcp) -> None:
        response = client.customers.with_raw_response.create(
            customer_type="company",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerCreateResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Testmcp) -> None:
        with client.customers.with_streaming_response.create(
            customer_type="company",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerCreateResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Testmcp) -> None:
        customer = client.customers.retrieve(
            id="id",
            api_key="apiKey",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Testmcp) -> None:
        response = client.customers.with_raw_response.retrieve(
            id="id",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Testmcp) -> None:
        with client.customers.with_streaming_response.retrieve(
            id="id",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: Testmcp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.customers.with_raw_response.retrieve(
                id="",
                api_key="apiKey",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Testmcp) -> None:
        customer = client.customers.update(
            id="id",
            api_key="apiKey",
        )
        assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Testmcp) -> None:
        customer = client.customers.update(
            id="id",
            api_key="apiKey",
            company_name="Compp Name",
            customer_address="New York",
            customer_city="New York",
            customer_code=40,
            customer_comm_reg_number="1234",
            customer_email="john_harry_smith@test.com",
            customer_fax="01/012012",
            customer_first_name="John",
            customer_last_name="Smith",
            customer_middle_name="Harry",
            customer_phone1="01/012012",
            customer_phone2="01/012012",
            customer_phone3="01/012012",
            customer_website="test.com",
            documents=[
                {
                    "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                    "file_name": "image_name.png",
                    "description": "file description",
                }
            ],
        )
        assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Testmcp) -> None:
        response = client.customers.with_raw_response.update(
            id="id",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Testmcp) -> None:
        with client.customers.with_streaming_response.update(
            id="id",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Testmcp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.customers.with_raw_response.update(
                id="",
                api_key="apiKey",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Testmcp) -> None:
        customer = client.customers.list(
            api_key="apiKey",
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Testmcp) -> None:
        customer = client.customers.list(
            api_key="apiKey",
            conversion_date="conversionDate",
            limit=0,
            page=0,
            search_filter="searchFilter",
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Testmcp) -> None:
        response = client.customers.with_raw_response.list(
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = response.parse()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Testmcp) -> None:
        with client.customers.with_streaming_response.list(
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = response.parse()
            assert_matches_type(CustomerListResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTestmcp) -> None:
        customer = await async_client.customers.create(
            customer_type="company",
            api_key="apiKey",
        )
        assert_matches_type(CustomerCreateResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTestmcp) -> None:
        customer = await async_client.customers.create(
            customer_type="company",
            api_key="apiKey",
            company_name="Compp Name",
            customer_address="New York",
            customer_city="New York",
            customer_code=40,
            customer_comm_reg_number="1234",
            customer_email="john_harry_smith@test.com",
            customer_fax="01/012012",
            customer_first_name="John",
            customer_last_name="Smith",
            customer_middle_name="Harry",
            customer_phone1="01/012012",
            customer_phone2="01/012012",
            customer_phone3="01/012012",
            customer_website="test.com",
            documents=[
                {
                    "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                    "file_name": "image_name.png",
                    "description": "file description",
                }
            ],
        )
        assert_matches_type(CustomerCreateResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.customers.with_raw_response.create(
            customer_type="company",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerCreateResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTestmcp) -> None:
        async with async_client.customers.with_streaming_response.create(
            customer_type="company",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerCreateResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTestmcp) -> None:
        customer = await async_client.customers.retrieve(
            id="id",
            api_key="apiKey",
        )
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.customers.with_raw_response.retrieve(
            id="id",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(Customer, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTestmcp) -> None:
        async with async_client.customers.with_streaming_response.retrieve(
            id="id",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(Customer, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTestmcp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.customers.with_raw_response.retrieve(
                id="",
                api_key="apiKey",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTestmcp) -> None:
        customer = await async_client.customers.update(
            id="id",
            api_key="apiKey",
        )
        assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTestmcp) -> None:
        customer = await async_client.customers.update(
            id="id",
            api_key="apiKey",
            company_name="Compp Name",
            customer_address="New York",
            customer_city="New York",
            customer_code=40,
            customer_comm_reg_number="1234",
            customer_email="john_harry_smith@test.com",
            customer_fax="01/012012",
            customer_first_name="John",
            customer_last_name="Smith",
            customer_middle_name="Harry",
            customer_phone1="01/012012",
            customer_phone2="01/012012",
            customer_phone3="01/012012",
            customer_website="test.com",
            documents=[
                {
                    "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                    "file_name": "image_name.png",
                    "description": "file description",
                }
            ],
        )
        assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.customers.with_raw_response.update(
            id="id",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTestmcp) -> None:
        async with async_client.customers.with_streaming_response.update(
            id="id",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerUpdateResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTestmcp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.customers.with_raw_response.update(
                id="",
                api_key="apiKey",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTestmcp) -> None:
        customer = await async_client.customers.list(
            api_key="apiKey",
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTestmcp) -> None:
        customer = await async_client.customers.list(
            api_key="apiKey",
            conversion_date="conversionDate",
            limit=0,
            page=0,
            search_filter="searchFilter",
        )
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.customers.with_raw_response.list(
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        customer = await response.parse()
        assert_matches_type(CustomerListResponse, customer, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTestmcp) -> None:
        async with async_client.customers.with_streaming_response.list(
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            customer = await response.parse()
            assert_matches_type(CustomerListResponse, customer, path=["response"])

        assert cast(Any, response.is_closed) is True
