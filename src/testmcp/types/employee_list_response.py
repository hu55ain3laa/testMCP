# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmployeeListResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    code: Optional[str] = None
    """numeric string"""

    full_name: Optional[str] = FieldInfo(alias="fullName", default=None)


class EmployeeListResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
