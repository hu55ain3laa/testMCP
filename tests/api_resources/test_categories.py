# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from testmcp import Testmcp, AsyncTestmcp
from tests.utils import assert_matches_type
from testmcp.types import CategoryRetrieveTreeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCategories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_tree(self, client: Testmcp) -> None:
        category = client.categories.retrieve_tree(
            api_key="apiKey",
        )
        assert_matches_type(CategoryRetrieveTreeResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_tree(self, client: Testmcp) -> None:
        response = client.categories.with_raw_response.retrieve_tree(
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = response.parse()
        assert_matches_type(CategoryRetrieveTreeResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_tree(self, client: Testmcp) -> None:
        with client.categories.with_streaming_response.retrieve_tree(
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = response.parse()
            assert_matches_type(CategoryRetrieveTreeResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCategories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_tree(self, async_client: AsyncTestmcp) -> None:
        category = await async_client.categories.retrieve_tree(
            api_key="apiKey",
        )
        assert_matches_type(CategoryRetrieveTreeResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_tree(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.categories.with_raw_response.retrieve_tree(
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        category = await response.parse()
        assert_matches_type(CategoryRetrieveTreeResponse, category, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_tree(self, async_client: AsyncTestmcp) -> None:
        async with async_client.categories.with_streaming_response.retrieve_tree(
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            category = await response.parse()
            assert_matches_type(CategoryRetrieveTreeResponse, category, path=["response"])

        assert cast(Any, response.is_closed) is True
