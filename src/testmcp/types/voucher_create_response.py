# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["VoucherCreateResponse"]


class VoucherCreateResponse(BaseModel):
    voucher_id: Optional[str] = FieldInfo(alias="voucherId", default=None)
    """Voucher ID"""
