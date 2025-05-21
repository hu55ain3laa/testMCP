# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CurrencyGetRatesResponse"]


class CurrencyGetRatesResponse(BaseModel):
    lbp_usd: Optional[str] = FieldInfo(alias="LBP_USD", default=None)

    multiplier: Optional[str] = None
