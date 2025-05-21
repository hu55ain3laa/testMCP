# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PurchaseQuotationUpdateParams",
    "AddProduct",
    "AddProductUnionMember0",
    "AddProductUnionMember1",
    "AddProductUnionMember2",
    "DelProduct",
    "ModProduct",
]


class PurchaseQuotationUpdateParams(TypedDict, total=False):
    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]

    add_products: Annotated[Iterable[AddProduct], PropertyInfo(alias="addProducts")]
    """Products to be deleted"""

    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """Date of The Purchase Quotation in `yyyy-MM-dd`"""

    del_products: Annotated[Iterable[DelProduct], PropertyInfo(alias="delProducts")]
    """Products to be deleted"""

    description: str

    mod_products: Annotated[Iterable[ModProduct], PropertyInfo(alias="modProducts")]
    """Products to be modified"""

    supplier_id: Annotated[str, PropertyInfo(alias="supplierId")]
    """Supplier ID"""


class AddProductUnionMember0(TypedDict, total=False):
    product_id: Required[Annotated[str, PropertyInfo(alias="productId")]]

    description: str

    product_qty: Annotated[float, PropertyInfo(alias="productQty")]

    unit_price: Annotated[float, PropertyInfo(alias="unitPrice")]
    """Unit Price of the product"""


class AddProductUnionMember1(TypedDict, total=False):
    spec_id: Required[Annotated[str, PropertyInfo(alias="specId")]]

    description: str

    product_qty: Annotated[float, PropertyInfo(alias="productQty")]

    unit_price: Annotated[float, PropertyInfo(alias="unitPrice")]
    """Unit Price of the product"""


class AddProductUnionMember2(TypedDict, total=False):
    product_code: Required[Annotated[str, PropertyInfo(alias="productCode")]]

    description: str

    product_qty: Annotated[float, PropertyInfo(alias="productQty")]

    unit_price: Annotated[float, PropertyInfo(alias="unitPrice")]
    """Unit Price of the product"""


AddProduct: TypeAlias = Union[AddProductUnionMember0, AddProductUnionMember1, AddProductUnionMember2]


class DelProduct(TypedDict, total=False):
    id: Required[str]


class ModProduct(TypedDict, total=False):
    id: Required[str]

    description: str

    product_code: Annotated[str, PropertyInfo(alias="productCode")]
    """Product Code"""

    product_id: Annotated[str, PropertyInfo(alias="productId")]

    product_qty: Annotated[float, PropertyInfo(alias="productQty")]

    spec_id: Annotated[str, PropertyInfo(alias="specId")]

    unit_price: Annotated[float, PropertyInfo(alias="unitPrice")]
    """Unit Price of the product"""
