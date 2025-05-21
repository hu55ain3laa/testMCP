# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from testmcp import Testmcp, AsyncTestmcp
from tests.utils import assert_matches_type
from testmcp.types import (
    ProductListResponse,
    ProductRetrieveDetailsResponse,
    ProductRetrieveCreatedAfterResponse,
    ProductRetrievePromotedAfterResponse,
    ProductRetrieveUpdatedPricesAfterResponse,
    ProductRetrieveUpdatedAvailabilityAfterResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProduct:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Testmcp) -> None:
        product = client.product.list(
            api_key="apiKey",
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Testmcp) -> None:
        product = client.product.list(
            api_key="apiKey",
            cat_id="catId",
            limit=0,
            page=0,
            sub_cat_id="subCatId",
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Testmcp) -> None:
        response = client.product.with_raw_response.list(
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Testmcp) -> None:
        with client.product.with_streaming_response.list(
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductListResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_created_after(self, client: Testmcp) -> None:
        product = client.product.retrieve_created_after(
            date="date",
            api_key="apiKey",
        )
        assert_matches_type(ProductRetrieveCreatedAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_created_after_with_all_params(self, client: Testmcp) -> None:
        product = client.product.retrieve_created_after(
            date="date",
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(ProductRetrieveCreatedAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_created_after(self, client: Testmcp) -> None:
        response = client.product.with_raw_response.retrieve_created_after(
            date="date",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductRetrieveCreatedAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_created_after(self, client: Testmcp) -> None:
        with client.product.with_streaming_response.retrieve_created_after(
            date="date",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductRetrieveCreatedAfterResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_details(self, client: Testmcp) -> None:
        product = client.product.retrieve_details(
            api_key="apiKey",
        )
        assert_matches_type(ProductRetrieveDetailsResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_details_with_all_params(self, client: Testmcp) -> None:
        product = client.product.retrieve_details(
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(ProductRetrieveDetailsResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_details(self, client: Testmcp) -> None:
        response = client.product.with_raw_response.retrieve_details(
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductRetrieveDetailsResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_details(self, client: Testmcp) -> None:
        with client.product.with_streaming_response.retrieve_details(
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductRetrieveDetailsResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_promoted_after(self, client: Testmcp) -> None:
        product = client.product.retrieve_promoted_after(
            date="date",
            api_key="apiKey",
        )
        assert_matches_type(ProductRetrievePromotedAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_promoted_after_with_all_params(self, client: Testmcp) -> None:
        product = client.product.retrieve_promoted_after(
            date="date",
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(ProductRetrievePromotedAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_promoted_after(self, client: Testmcp) -> None:
        response = client.product.with_raw_response.retrieve_promoted_after(
            date="date",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductRetrievePromotedAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_promoted_after(self, client: Testmcp) -> None:
        with client.product.with_streaming_response.retrieve_promoted_after(
            date="date",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductRetrievePromotedAfterResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_updated_availability_after(self, client: Testmcp) -> None:
        product = client.product.retrieve_updated_availability_after(
            date="date",
            api_key="apiKey",
        )
        assert_matches_type(ProductRetrieveUpdatedAvailabilityAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_updated_availability_after_with_all_params(self, client: Testmcp) -> None:
        product = client.product.retrieve_updated_availability_after(
            date="date",
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(ProductRetrieveUpdatedAvailabilityAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_updated_availability_after(self, client: Testmcp) -> None:
        response = client.product.with_raw_response.retrieve_updated_availability_after(
            date="date",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductRetrieveUpdatedAvailabilityAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_updated_availability_after(self, client: Testmcp) -> None:
        with client.product.with_streaming_response.retrieve_updated_availability_after(
            date="date",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductRetrieveUpdatedAvailabilityAfterResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_updated_prices_after(self, client: Testmcp) -> None:
        product = client.product.retrieve_updated_prices_after(
            date="date",
            api_key="apiKey",
        )
        assert_matches_type(ProductRetrieveUpdatedPricesAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_updated_prices_after_with_all_params(self, client: Testmcp) -> None:
        product = client.product.retrieve_updated_prices_after(
            date="date",
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(ProductRetrieveUpdatedPricesAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_updated_prices_after(self, client: Testmcp) -> None:
        response = client.product.with_raw_response.retrieve_updated_prices_after(
            date="date",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductRetrieveUpdatedPricesAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_updated_prices_after(self, client: Testmcp) -> None:
        with client.product.with_streaming_response.retrieve_updated_prices_after(
            date="date",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductRetrieveUpdatedPricesAfterResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProduct:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTestmcp) -> None:
        product = await async_client.product.list(
            api_key="apiKey",
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTestmcp) -> None:
        product = await async_client.product.list(
            api_key="apiKey",
            cat_id="catId",
            limit=0,
            page=0,
            sub_cat_id="subCatId",
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.product.with_raw_response.list(
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTestmcp) -> None:
        async with async_client.product.with_streaming_response.list(
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductListResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_created_after(self, async_client: AsyncTestmcp) -> None:
        product = await async_client.product.retrieve_created_after(
            date="date",
            api_key="apiKey",
        )
        assert_matches_type(ProductRetrieveCreatedAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_created_after_with_all_params(self, async_client: AsyncTestmcp) -> None:
        product = await async_client.product.retrieve_created_after(
            date="date",
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(ProductRetrieveCreatedAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_created_after(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.product.with_raw_response.retrieve_created_after(
            date="date",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductRetrieveCreatedAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_created_after(self, async_client: AsyncTestmcp) -> None:
        async with async_client.product.with_streaming_response.retrieve_created_after(
            date="date",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductRetrieveCreatedAfterResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_details(self, async_client: AsyncTestmcp) -> None:
        product = await async_client.product.retrieve_details(
            api_key="apiKey",
        )
        assert_matches_type(ProductRetrieveDetailsResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_details_with_all_params(self, async_client: AsyncTestmcp) -> None:
        product = await async_client.product.retrieve_details(
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(ProductRetrieveDetailsResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_details(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.product.with_raw_response.retrieve_details(
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductRetrieveDetailsResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_details(self, async_client: AsyncTestmcp) -> None:
        async with async_client.product.with_streaming_response.retrieve_details(
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductRetrieveDetailsResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_promoted_after(self, async_client: AsyncTestmcp) -> None:
        product = await async_client.product.retrieve_promoted_after(
            date="date",
            api_key="apiKey",
        )
        assert_matches_type(ProductRetrievePromotedAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_promoted_after_with_all_params(self, async_client: AsyncTestmcp) -> None:
        product = await async_client.product.retrieve_promoted_after(
            date="date",
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(ProductRetrievePromotedAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_promoted_after(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.product.with_raw_response.retrieve_promoted_after(
            date="date",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductRetrievePromotedAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_promoted_after(self, async_client: AsyncTestmcp) -> None:
        async with async_client.product.with_streaming_response.retrieve_promoted_after(
            date="date",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductRetrievePromotedAfterResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_updated_availability_after(self, async_client: AsyncTestmcp) -> None:
        product = await async_client.product.retrieve_updated_availability_after(
            date="date",
            api_key="apiKey",
        )
        assert_matches_type(ProductRetrieveUpdatedAvailabilityAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_updated_availability_after_with_all_params(self, async_client: AsyncTestmcp) -> None:
        product = await async_client.product.retrieve_updated_availability_after(
            date="date",
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(ProductRetrieveUpdatedAvailabilityAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_updated_availability_after(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.product.with_raw_response.retrieve_updated_availability_after(
            date="date",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductRetrieveUpdatedAvailabilityAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_updated_availability_after(self, async_client: AsyncTestmcp) -> None:
        async with async_client.product.with_streaming_response.retrieve_updated_availability_after(
            date="date",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductRetrieveUpdatedAvailabilityAfterResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_updated_prices_after(self, async_client: AsyncTestmcp) -> None:
        product = await async_client.product.retrieve_updated_prices_after(
            date="date",
            api_key="apiKey",
        )
        assert_matches_type(ProductRetrieveUpdatedPricesAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_updated_prices_after_with_all_params(self, async_client: AsyncTestmcp) -> None:
        product = await async_client.product.retrieve_updated_prices_after(
            date="date",
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(ProductRetrieveUpdatedPricesAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_updated_prices_after(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.product.with_raw_response.retrieve_updated_prices_after(
            date="date",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductRetrieveUpdatedPricesAfterResponse, product, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_updated_prices_after(self, async_client: AsyncTestmcp) -> None:
        async with async_client.product.with_streaming_response.retrieve_updated_prices_after(
            date="date",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductRetrieveUpdatedPricesAfterResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True
