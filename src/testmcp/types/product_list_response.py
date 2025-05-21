# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProductListResponse", "Data", "DataAllSpecDetail", "DataProductAssignedSpec"]


class DataAllSpecDetail(BaseModel):
    id: Optional[int] = None
    """Spec details ID"""

    name: Optional[str] = None
    """Spec Details Name"""


class DataProductAssignedSpec(BaseModel):
    id: Optional[str] = None

    barcode: Optional[str] = None

    code: Optional[str] = None

    name: Optional[str] = None

    spec_details: Optional[Dict[str, int]] = FieldInfo(alias="specDetails", default=None)


class Data(BaseModel):
    id: Optional[str] = None

    all_spec_details: Optional[Dict[str, List[DataAllSpecDetail]]] = FieldInfo(alias="allSpecDetails", default=None)

    barcode: Optional[str] = None

    category: Optional[str] = None
    """The category of the product."""

    code: Optional[str] = None

    description: Optional[str] = None

    family: Optional[str] = None

    gender: Optional[str] = None

    image_path: Optional[str] = FieldInfo(alias="imagePath", default=None)

    main_category: Optional[str] = FieldInfo(alias="mainCategory", default=None)
    """The main category of the product."""

    name: Optional[str] = None

    product_assigned_specs: Optional[List[DataProductAssignedSpec]] = FieldInfo(
        alias="productAssignedSpecs", default=None
    )

    season: Optional[str] = None

    selling_um_code: Optional[str] = FieldInfo(alias="sellingUmCode", default=None)
    """Stock Unit of Measurement Code"""


class ProductListResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
