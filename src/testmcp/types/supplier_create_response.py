# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SupplierCreateResponse"]


class SupplierCreateResponse(BaseModel):
    supplier_id: Optional[str] = FieldInfo(alias="supplierId", default=None)
    """Supplier ID"""
