# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from testmcp import Testmcp, AsyncTestmcp
from tests.utils import assert_matches_type
from testmcp.types import (
    PurchaseRequisitionCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPurchaseRequisitions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Testmcp) -> None:
        purchase_requisition = client.purchase_requisitions.create(
            purchase_requisition_date="2025-02-01T00:00:00.000Z",
            api_key="apiKey",
        )
        assert_matches_type(PurchaseRequisitionCreateResponse, purchase_requisition, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Testmcp) -> None:
        purchase_requisition = client.purchase_requisitions.create(
            purchase_requisition_date="2025-02-01T00:00:00.000Z",
            api_key="apiKey",
            add_products=[
                {
                    "product_id": "1234",
                    "description": "product description",
                    "product_code": "1234",
                    "product_qty": "1",
                    "spec_id": "1234",
                }
            ],
            customer_id="1234",
            date_format="yyyy-MM-dd",
            description="very important purchase requisition",
            documents=[
                {
                    "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                    "file_name": "image_name.png",
                    "description": "file description",
                }
            ],
        )
        assert_matches_type(PurchaseRequisitionCreateResponse, purchase_requisition, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Testmcp) -> None:
        response = client.purchase_requisitions.with_raw_response.create(
            purchase_requisition_date="2025-02-01T00:00:00.000Z",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase_requisition = response.parse()
        assert_matches_type(PurchaseRequisitionCreateResponse, purchase_requisition, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Testmcp) -> None:
        with client.purchase_requisitions.with_streaming_response.create(
            purchase_requisition_date="2025-02-01T00:00:00.000Z",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase_requisition = response.parse()
            assert_matches_type(PurchaseRequisitionCreateResponse, purchase_requisition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_add_document(self, client: Testmcp) -> None:
        purchase_requisition = client.purchase_requisitions.add_document(
            id="id",
            body=[
                {
                    "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                    "file_name": "image_name.png",
                }
            ],
            api_key="apiKey",
        )
        assert purchase_requisition is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_add_document(self, client: Testmcp) -> None:
        response = client.purchase_requisitions.with_raw_response.add_document(
            id="id",
            body=[
                {
                    "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                    "file_name": "image_name.png",
                }
            ],
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase_requisition = response.parse()
        assert purchase_requisition is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_add_document(self, client: Testmcp) -> None:
        with client.purchase_requisitions.with_streaming_response.add_document(
            id="id",
            body=[
                {
                    "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                    "file_name": "image_name.png",
                }
            ],
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase_requisition = response.parse()
            assert purchase_requisition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_add_document(self, client: Testmcp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.purchase_requisitions.with_raw_response.add_document(
                id="",
                body=[
                    {
                        "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                        "file_name": "image_name.png",
                    }
                ],
                api_key="apiKey",
            )


class TestAsyncPurchaseRequisitions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncTestmcp) -> None:
        purchase_requisition = await async_client.purchase_requisitions.create(
            purchase_requisition_date="2025-02-01T00:00:00.000Z",
            api_key="apiKey",
        )
        assert_matches_type(PurchaseRequisitionCreateResponse, purchase_requisition, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncTestmcp) -> None:
        purchase_requisition = await async_client.purchase_requisitions.create(
            purchase_requisition_date="2025-02-01T00:00:00.000Z",
            api_key="apiKey",
            add_products=[
                {
                    "product_id": "1234",
                    "description": "product description",
                    "product_code": "1234",
                    "product_qty": "1",
                    "spec_id": "1234",
                }
            ],
            customer_id="1234",
            date_format="yyyy-MM-dd",
            description="very important purchase requisition",
            documents=[
                {
                    "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                    "file_name": "image_name.png",
                    "description": "file description",
                }
            ],
        )
        assert_matches_type(PurchaseRequisitionCreateResponse, purchase_requisition, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.purchase_requisitions.with_raw_response.create(
            purchase_requisition_date="2025-02-01T00:00:00.000Z",
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase_requisition = await response.parse()
        assert_matches_type(PurchaseRequisitionCreateResponse, purchase_requisition, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTestmcp) -> None:
        async with async_client.purchase_requisitions.with_streaming_response.create(
            purchase_requisition_date="2025-02-01T00:00:00.000Z",
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase_requisition = await response.parse()
            assert_matches_type(PurchaseRequisitionCreateResponse, purchase_requisition, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_add_document(self, async_client: AsyncTestmcp) -> None:
        purchase_requisition = await async_client.purchase_requisitions.add_document(
            id="id",
            body=[
                {
                    "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                    "file_name": "image_name.png",
                }
            ],
            api_key="apiKey",
        )
        assert purchase_requisition is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_add_document(self, async_client: AsyncTestmcp) -> None:
        response = await async_client.purchase_requisitions.with_raw_response.add_document(
            id="id",
            body=[
                {
                    "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                    "file_name": "image_name.png",
                }
            ],
            api_key="apiKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purchase_requisition = await response.parse()
        assert purchase_requisition is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_add_document(self, async_client: AsyncTestmcp) -> None:
        async with async_client.purchase_requisitions.with_streaming_response.add_document(
            id="id",
            body=[
                {
                    "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                    "file_name": "image_name.png",
                }
            ],
            api_key="apiKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purchase_requisition = await response.parse()
            assert purchase_requisition is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_add_document(self, async_client: AsyncTestmcp) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.purchase_requisitions.with_raw_response.add_document(
                id="",
                body=[
                    {
                        "file_data_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAYAAACNMs+9AAAAFUlEQVR42mNk+M9Qz0AEYBxVSF+FAAhKDveksOjmAAAAAElFTkSuQmCC",
                        "file_name": "image_name.png",
                    }
                ],
                api_key="apiKey",
            )
