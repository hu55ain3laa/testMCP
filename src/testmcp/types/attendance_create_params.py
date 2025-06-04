# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AttendanceCreateParams", "Body"]


class AttendanceCreateParams(TypedDict, total=False):
    body: Required[Iterable[Body]]

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]


class Body(TypedDict, total=False):
    employee_code: Required[Annotated[str, PropertyInfo(alias="employeeCode")]]

    machine_name: Required[Annotated[str, PropertyInfo(alias="machineName")]]

    status: Required[Literal["IN", "OUT", "BREAK_IN", "BREAK_OUT"]]
    """Either 'IN' , 'OUT' , 'BREAK_IN' , or 'BREAK_OUT'"""

    timestamp: Required[str]
    """
    ISO 8601 datetime with 'T' with or without seconds and milliseconds. Do not set
    a timezone or 'Z' field.
    """
