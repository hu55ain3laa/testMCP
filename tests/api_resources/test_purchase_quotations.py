# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from testmcp import Testmcp, AsyncTestmcp
from tests.utils import assert_matches_type
from testmcp.types import (
    PurchaseQuotationListResponse,
    PurchaseQuotationCreateResponse,
    PurchaseQuotationUpdateResponse,
)
from testmcp._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPurchaseQuotations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Testmcp) -> None:
        purchase_quotation = client.purchase_quotations.create(
            date=parse_date("2019-12-27"),
            supplier_id="1234",
            api_key="apiKey",
        )
        assert_matches_type(PurchaseQuotationCreateResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Testmcp) -> None:
        purchase_quotation = client.purchase_quotations.create(
            date=parse_date("2019-12-27"),
            supplier_id="1234",
            api_key="apiKey",
            add_products=[
                {
                    "product_id": "12345",
                    "description": "description",
                    "product_qty": 0,
                    "unit_price": 0,
                }
            ],
            description="description",
        )
        assert_matches_type(PurchaseQuotationCreateResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Testmcp) -> None:
        response = client.purchase_quotations.with_raw_response.create(
            date=parse_date("2019-12-27"),
            supplier_id="1234",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase_quotation = response.parse()
        assert_matches_type(PurchaseQuotationCreateResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Testmcp) -> None:
        with client.purchase_quotations.with_streaming_response.create(
            date=parse_date("2019-12-27"),
            supplier_id="1234",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase_quotation = response.parse()
            assert_matches_type(PurchaseQuotationCreateResponse, purchase_quotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Testmcp) -> None:
        purchase_quotation = client.purchase_quotations.update(
            id="id",
            api_key="apiKey",
        )
        assert_matches_type(PurchaseQuotationUpdateResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Testmcp) -> None:
        purchase_quotation = client.purchase_quotations.update(
            id="id",
            api_key="apiKey",
            add_products=[
                {
                    "product_id": "12345",
                    "description": "description",
                    "product_qty": 0,
                    "unit_price": 0,
                }
            ],
            date=parse_date("2019-12-27"),
            del_products=[{"id": "id"}],
            description="description",
            mod_products=[
                {
                    "id": "id",
                    "description": "description",
                    "product_code": "productCode",
                    "product_id": "productId",
                    "product_qty": 0,
                    "spec_id": "specId",
                    "unit_price": 0,
                }
            ],
            supplier_id="1234",
        )
        assert_matches_type(PurchaseQuotationUpdateResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Testmcp) -> None:
        response = client.purchase_quotations.with_raw_response.update(
            id="id",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase_quotation = response.parse()
        assert_matches_type(PurchaseQuotationUpdateResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Testmcp) -> None:
        with client.purchase_quotations.with_streaming_response.update(
            id="id",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase_quotation = response.parse()
            assert_matches_type(PurchaseQuotationUpdateResponse, purchase_quotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Testmcp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.purchase_quotations.with_raw_response.update(
                id="",
                api_key="apiKey",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Testmcp) -> None:
        purchase_quotation = client.purchase_quotations.list(
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
        )
        assert_matches_type(PurchaseQuotationListResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Testmcp) -> None:
        purchase_quotation = client.purchase_quotations.list(
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(PurchaseQuotationListResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Testmcp) -> None:
        response = client.purchase_quotations.with_raw_response.list(
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase_quotation = response.parse()
        assert_matches_type(PurchaseQuotationListResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Testmcp) -> None:
        with client.purchase_quotations.with_streaming_response.list(
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase_quotation = response.parse()
            assert_matches_type(PurchaseQuotationListResponse, purchase_quotation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPurchaseQuotations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTestmcp) -> None:
        purchase_quotation = await async_client.purchase_quotations.create(
            date=parse_date("2019-12-27"),
            supplier_id="1234",
            api_key="apiKey",
        )
        assert_matches_type(PurchaseQuotationCreateResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTestmcp) -> None:
        purchase_quotation = await async_client.purchase_quotations.create(
            date=parse_date("2019-12-27"),
            supplier_id="1234",
            api_key="apiKey",
            add_products=[
                {
                    "product_id": "12345",
                    "description": "description",
                    "product_qty": 0,
                    "unit_price": 0,
                }
            ],
            description="description",
        )
        assert_matches_type(PurchaseQuotationCreateResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.purchase_quotations.with_raw_response.create(
            date=parse_date("2019-12-27"),
            supplier_id="1234",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase_quotation = await response.parse()
        assert_matches_type(PurchaseQuotationCreateResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTestmcp) -> None:
        async with async_client.purchase_quotations.with_streaming_response.create(
            date=parse_date("2019-12-27"),
            supplier_id="1234",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase_quotation = await response.parse()
            assert_matches_type(PurchaseQuotationCreateResponse, purchase_quotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncTestmcp) -> None:
        purchase_quotation = await async_client.purchase_quotations.update(
            id="id",
            api_key="apiKey",
        )
        assert_matches_type(PurchaseQuotationUpdateResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncTestmcp) -> None:
        purchase_quotation = await async_client.purchase_quotations.update(
            id="id",
            api_key="apiKey",
            add_products=[
                {
                    "product_id": "12345",
                    "description": "description",
                    "product_qty": 0,
                    "unit_price": 0,
                }
            ],
            date=parse_date("2019-12-27"),
            del_products=[{"id": "id"}],
            description="description",
            mod_products=[
                {
                    "id": "id",
                    "description": "description",
                    "product_code": "productCode",
                    "product_id": "productId",
                    "product_qty": 0,
                    "spec_id": "specId",
                    "unit_price": 0,
                }
            ],
            supplier_id="1234",
        )
        assert_matches_type(PurchaseQuotationUpdateResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.purchase_quotations.with_raw_response.update(
            id="id",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase_quotation = await response.parse()
        assert_matches_type(PurchaseQuotationUpdateResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncTestmcp) -> None:
        async with async_client.purchase_quotations.with_streaming_response.update(
            id="id",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase_quotation = await response.parse()
            assert_matches_type(PurchaseQuotationUpdateResponse, purchase_quotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncTestmcp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.purchase_quotations.with_raw_response.update(
                id="",
                api_key="apiKey",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncTestmcp) -> None:
        purchase_quotation = await async_client.purchase_quotations.list(
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
        )
        assert_matches_type(PurchaseQuotationListResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTestmcp) -> None:
        purchase_quotation = await async_client.purchase_quotations.list(
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
            limit=0,
            page=0,
        )
        assert_matches_type(PurchaseQuotationListResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.purchase_quotations.with_raw_response.list(
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase_quotation = await response.parse()
        assert_matches_type(PurchaseQuotationListResponse, purchase_quotation, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTestmcp) -> None:
        async with async_client.purchase_quotations.with_streaming_response.list(
            from_date="fromDate",
            to_date="toDate",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase_quotation = await response.parse()
            assert_matches_type(PurchaseQuotationListResponse, purchase_quotation, path=["response"])

        assert cast(Any, response.is_closed) is True
