# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomerListParams"]


class CustomerListParams(TypedDict, total=False):
    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]

    code: str
    """Filter by customer code"""

    conversion_date: Annotated[str, PropertyInfo(alias="conversionDate")]
    """
    Get customers that were created or converted after the sent date | Date format :
    yyyy-MM-dd
    """

    limit: int
    """the number of records per page | 250 by default | 500 maximum"""

    name: str
    """Filter by customer name"""

    page: int
    """the page offset | page 1 by default"""

    phone: str
    """Filter by customer phone"""

    search_filter: Annotated[str, PropertyInfo(alias="searchFilter")]
    """general search filter"""
