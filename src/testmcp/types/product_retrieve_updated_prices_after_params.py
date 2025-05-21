# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProductRetrieveUpdatedPricesAfterParams"]


class ProductRetrieveUpdatedPricesAfterParams(TypedDict, total=False):
    date: Required[str]
    """Date Of Products Prices Updates | Date Format : yyyy-MM-dd"""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]

    limit: int
    """the number of records per page | 250 by default | 500 maximum"""

    page: int
    """the page offset | page 1 by default"""
