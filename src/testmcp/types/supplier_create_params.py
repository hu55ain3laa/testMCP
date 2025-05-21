# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SupplierCreateParams"]


class SupplierCreateParams(TypedDict, total=False):
    name: Required[str]
    """Supplier Name"""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]

    city: str
    """Supplier City"""

    code: str
    """Numeric Supplier Code"""

    comm_reg_number: Annotated[str, PropertyInfo(alias="commRegNumber")]
    """Supplier Commercial Registration Number"""

    email: str
    """Supplier Email"""

    phone1: str
    """Supplier Phone 1"""
