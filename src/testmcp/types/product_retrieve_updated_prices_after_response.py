# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProductRetrieveUpdatedPricesAfterResponse", "Data"]


class Data(BaseModel):
    barcode: Optional[str] = None

    currency: Optional[str] = None

    default_price: Optional[str] = FieldInfo(alias="defaultPrice", default=None)

    name: Optional[str] = None

    reduced_price: Optional[str] = FieldInfo(alias="reducedPrice", default=None)


class ProductRetrieveUpdatedPricesAfterResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
