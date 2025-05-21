# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CurrencyGetRatesParams"]


class CurrencyGetRatesParams(TypedDict, total=False):
    date: Required[str]
    """Date Of Conversion | Date Format : yyyy-MM-dd"""

    from_currency_code: Required[Annotated[str, PropertyInfo(alias="fromCurrencyCode")]]
    """Currency You Want To Convert From"""

    to_currency_code: Required[Annotated[str, PropertyInfo(alias="toCurrencyCode")]]
    """Currency You Want To Convert To"""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
