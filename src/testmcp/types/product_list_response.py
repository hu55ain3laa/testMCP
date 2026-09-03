# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ProductListResponse",
    "Data",
    "DataProductAssignedSpec",
    "DataProductAssignedSpecSpecDetails",
    "DataProductAssignedSpecSpecDetailsColor",
    "DataProductAssignedSpecSpecDetailsCustom",
    "DataProductAssignedSpecSpecDetailsMaterial",
    "DataProductAssignedSpecSpecDetailsSize",
]


class DataProductAssignedSpecSpecDetailsColor(BaseModel):
    detail_code: Optional[str] = FieldInfo(alias="detailCode", default=None)

    detail_id: Optional[str] = FieldInfo(alias="detailId", default=None)

    detail_name: Optional[str] = FieldInfo(alias="detailName", default=None)

    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)

    group_name: Optional[str] = FieldInfo(alias="groupName", default=None)


class DataProductAssignedSpecSpecDetailsCustom(BaseModel):
    detail_code: Optional[str] = FieldInfo(alias="detailCode", default=None)

    detail_id: Optional[str] = FieldInfo(alias="detailId", default=None)

    detail_name: Optional[str] = FieldInfo(alias="detailName", default=None)

    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)

    group_name: Optional[str] = FieldInfo(alias="groupName", default=None)


class DataProductAssignedSpecSpecDetailsMaterial(BaseModel):
    detail_code: Optional[str] = FieldInfo(alias="detailCode", default=None)

    detail_id: Optional[str] = FieldInfo(alias="detailId", default=None)

    detail_name: Optional[str] = FieldInfo(alias="detailName", default=None)

    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)

    group_name: Optional[str] = FieldInfo(alias="groupName", default=None)


class DataProductAssignedSpecSpecDetailsSize(BaseModel):
    detail_code: Optional[str] = FieldInfo(alias="detailCode", default=None)

    detail_id: Optional[str] = FieldInfo(alias="detailId", default=None)

    detail_name: Optional[str] = FieldInfo(alias="detailName", default=None)

    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)

    group_name: Optional[str] = FieldInfo(alias="groupName", default=None)


class DataProductAssignedSpecSpecDetails(BaseModel):
    color: Optional[DataProductAssignedSpecSpecDetailsColor] = None

    custom: Optional[DataProductAssignedSpecSpecDetailsCustom] = None

    material: Optional[DataProductAssignedSpecSpecDetailsMaterial] = None

    size: Optional[DataProductAssignedSpecSpecDetailsSize] = None


class DataProductAssignedSpec(BaseModel):
    id: Optional[str] = None

    barcode: Optional[str] = None

    code: Optional[str] = None

    name: Optional[str] = None

    spec_details: Optional[DataProductAssignedSpecSpecDetails] = FieldInfo(alias="specDetails", default=None)


class Data(BaseModel):
    id: Optional[str] = None

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
