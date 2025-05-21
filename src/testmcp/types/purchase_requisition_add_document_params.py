# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .documents_info_param import DocumentsInfoParam

__all__ = ["PurchaseRequisitionAddDocumentParams"]


class PurchaseRequisitionAddDocumentParams(TypedDict, total=False):
    body: Required[Iterable[DocumentsInfoParam]]

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]
