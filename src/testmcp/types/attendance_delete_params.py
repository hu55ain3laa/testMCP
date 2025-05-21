# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AttendanceDeleteParams"]


class AttendanceDeleteParams(TypedDict, total=False):
    employee_codes: Required[Annotated[str, PropertyInfo(alias="employeeCodes")]]
    """Commpa seperated employee codes"""

    from_date: Required[Annotated[str, PropertyInfo(alias="fromDate")]]
    """starting date in format yyyy-MM-dd"""

    to_date: Required[Annotated[str, PropertyInfo(alias="toDate")]]
    """ending date in format yyyy-MM-dd"""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
