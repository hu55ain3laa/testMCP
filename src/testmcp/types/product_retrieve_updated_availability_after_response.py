# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProductRetrieveUpdatedAvailabilityAfterResponse", "Data"]


class Data(BaseModel):
    available_qty: Optional[str] = FieldInfo(alias="availableQty", default=None)

    barcode: Optional[str] = None

    name: Optional[str] = None


class ProductRetrieveUpdatedAvailabilityAfterResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
