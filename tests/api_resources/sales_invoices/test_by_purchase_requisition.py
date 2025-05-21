# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from testmcp import Testmcp, AsyncTestmcp
from tests.utils import assert_matches_type
from testmcp.types.sales_invoices import ByPurchaseRequisitionGenerateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestByPurchaseRequisition:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_generate(self, client: Testmcp) -> None:
        by_purchase_requisition = client.sales_invoices.by_purchase_requisition.generate(
            id="id",
            api_key="apiKey",
        )
        assert_matches_type(ByPurchaseRequisitionGenerateResponse, by_purchase_requisition, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_generate(self, client: Testmcp) -> None:
        response = client.sales_invoices.by_purchase_requisition.with_raw_response.generate(
            id="id",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_purchase_requisition = response.parse()
        assert_matches_type(ByPurchaseRequisitionGenerateResponse, by_purchase_requisition, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_generate(self, client: Testmcp) -> None:
        with client.sales_invoices.by_purchase_requisition.with_streaming_response.generate(
            id="id",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_purchase_requisition = response.parse()
            assert_matches_type(ByPurchaseRequisitionGenerateResponse, by_purchase_requisition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_generate(self, client: Testmcp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sales_invoices.by_purchase_requisition.with_raw_response.generate(
                id="",
                api_key="apiKey",
            )


class TestAsyncByPurchaseRequisition:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_generate(self, async_client: AsyncTestmcp) -> None:
        by_purchase_requisition = await async_client.sales_invoices.by_purchase_requisition.generate(
            id="id",
            api_key="apiKey",
        )
        assert_matches_type(ByPurchaseRequisitionGenerateResponse, by_purchase_requisition, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_generate(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.sales_invoices.by_purchase_requisition.with_raw_response.generate(
            id="id",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        by_purchase_requisition = await response.parse()
        assert_matches_type(ByPurchaseRequisitionGenerateResponse, by_purchase_requisition, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_generate(self, async_client: AsyncTestmcp) -> None:
        async with async_client.sales_invoices.by_purchase_requisition.with_streaming_response.generate(
            id="id",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            by_purchase_requisition = await response.parse()
            assert_matches_type(ByPurchaseRequisitionGenerateResponse, by_purchase_requisition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_generate(self, async_client: AsyncTestmcp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sales_invoices.by_purchase_requisition.with_raw_response.generate(
                id="",
                api_key="apiKey",
            )
