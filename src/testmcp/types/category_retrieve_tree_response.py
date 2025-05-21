# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CategoryRetrieveTreeResponse", "Data", "DataCategory", "DataCategorySubCategory"]


class DataCategorySubCategory(BaseModel):
    id: Optional[str] = None
    """Category ID"""

    code: Optional[str] = None
    """Category Code"""

    name: Optional[str] = None
    """Category Name"""


class DataCategory(BaseModel):
    id: Optional[str] = None
    """Category ID"""

    code: Optional[str] = None
    """Category Code"""

    name: Optional[str] = None
    """Category Name"""

    sub_categories: Optional[List[DataCategorySubCategory]] = FieldInfo(alias="subCategories", default=None)


class Data(BaseModel):
    id: Optional[str] = None
    """Category ID"""

    categories: Optional[List[DataCategory]] = None

    code: Optional[str] = None
    """Category Code"""

    name: Optional[str] = None
    """Category Name"""


class CategoryRetrieveTreeResponse(BaseModel):
    data: Optional[List[Data]] = None
