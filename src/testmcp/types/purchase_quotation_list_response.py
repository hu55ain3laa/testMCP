# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PurchaseQuotationListResponse", "Data", "DataProduct", "DataSupplier"]


class DataProduct(BaseModel):
    id: Optional[str] = None
    """ID of the Purchase Quotation Product"""

    product_code: Optional[str] = FieldInfo(alias="productCode", default=None)
    """Product Code"""

    product_id: Optional[str] = FieldInfo(alias="productId", default=None)
    """Product ID"""

    product_qty: Optional[float] = FieldInfo(alias="productQty", default=None)

    spec_id: Optional[str] = FieldInfo(alias="specId", default=None)
    """Product Spec ID"""

    unit_price: Optional[float] = FieldInfo(alias="unitPrice", default=None)


class DataSupplier(BaseModel):
    id: Optional[str] = None

    code: Optional[str] = None

    name: Optional[str] = None


class Data(BaseModel):
    id: Optional[str] = None

    code: Optional[str] = None

    currency: Optional[str] = None

    date: Optional[datetime.date] = None

    description: Optional[str] = None

    products: Optional[List[DataProduct]] = None

    supplier: Optional[DataSupplier] = None


class PurchaseQuotationListResponse(BaseModel):
    data: Optional[List[Data]] = None

    limit: Optional[int] = None

    page: Optional[int] = None

    total_pages: Optional[int] = FieldInfo(alias="totalPages", default=None)
