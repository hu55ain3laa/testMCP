# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PurchaseQuotationUpdateResponse"]


class PurchaseQuotationUpdateResponse(BaseModel):
    purchase_quotation_id: Optional[str] = FieldInfo(alias="purchaseQuotationId", default=None)
    """Purchase Quotation ID"""
