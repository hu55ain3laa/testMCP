# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProductRetrieveDetailsResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    available_qty: Optional[str] = FieldInfo(alias="availableQty", default=None)

    barcode: Optional[str] = None

    default_price_fbc: Optional[str] = FieldInfo(alias="defaultPriceFbc", default=None)

    default_price_sbc: Optional[str] = FieldInfo(alias="defaultPriceSbc", default=None)

    name: Optional[str] = None

    reduced_price_fbc: Optional[str] = FieldInfo(alias="reducedPriceFbc", default=None)

    reduced_price_sbc: Optional[str] = FieldInfo(alias="reducedPriceSbc", default=None)

    spec_id: Optional[str] = FieldInfo(alias="specId", default=None)


class ProductRetrieveDetailsResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
