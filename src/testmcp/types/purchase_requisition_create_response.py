# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PurchaseRequisitionCreateResponse"]


class PurchaseRequisitionCreateResponse(BaseModel):
    purchase_requisition_id: Optional[str] = FieldInfo(alias="purchaseRequisitionId", default=None)
    """Purchase Requisition ID"""
