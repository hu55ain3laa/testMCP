# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProductRetrieveCreatedAfterResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    attributes: Optional[List[str]] = None

    barcode: Optional[str] = None

    brand: Optional[str] = FieldInfo(alias="Brand", default=None)

    category: Optional[str] = None
    """The category of the product."""

    code: Optional[str] = None

    description: Optional[str] = None

    family: Optional[str] = None

    gender: Optional[str] = None

    image: Optional[str] = None

    name: Optional[str] = None

    season: Optional[str] = None

    spec_id: Optional[str] = FieldInfo(alias="specId", default=None)


class ProductRetrieveCreatedAfterResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
