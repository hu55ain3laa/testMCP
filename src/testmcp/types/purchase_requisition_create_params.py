# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .documents_info_param import DocumentsInfoParam

__all__ = ["PurchaseRequisitionCreateParams", "AddProduct"]


class PurchaseRequisitionCreateParams(TypedDict, total=False):
    purchase_requisition_date: Required[Annotated[str, PropertyInfo(alias="purchaseRequisitionDate")]]
    """
    Date of The Purchase Requisition | Date Format is the sent `dateFormat` or
    default `yyyy-MM-dd`
    """

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]

    add_products: Annotated[Iterable[AddProduct], PropertyInfo(alias="addProducts")]

    customer_id: Annotated[str, PropertyInfo(alias="customerId")]
    """Customer ID"""

    date_format: Annotated[str, PropertyInfo(alias="dateFormat")]
    """Date format to be used"""

    description: str
    """any purchase requisition description"""

    documents: Iterable[DocumentsInfoParam]


class AddProduct(TypedDict, total=False):
    product_id: Required[Annotated[str, PropertyInfo(alias="productId")]]
    """Product ID"""

    description: str

    product_code: Annotated[str, PropertyInfo(alias="productCode")]

    product_qty: Annotated[str, PropertyInfo(alias="productQty")]
    """Product Quantity"""

    spec_id: Annotated[str, PropertyInfo(alias="specId")]
