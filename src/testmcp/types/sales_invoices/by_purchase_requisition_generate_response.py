# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ByPurchaseRequisitionGenerateResponse"]


class ByPurchaseRequisitionGenerateResponse(BaseModel):
    sales_invoice_id: Optional[str] = FieldInfo(alias="salesInvoiceId", default=None)
    """Sales Invoice Id"""
