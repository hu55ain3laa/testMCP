# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentsInfoParam"]


class DocumentsInfoParam(TypedDict, total=False):
    file_data_base64: Required[Annotated[str, PropertyInfo(alias="fileDataBase64")]]
    """Base 64 encoded file data, can be sent with or without data:...;base64, prefix"""

    file_name: Required[Annotated[str, PropertyInfo(alias="fileName")]]
    """File name, will be checked if it is safe to use in the system"""

    description: str
    """file description"""
