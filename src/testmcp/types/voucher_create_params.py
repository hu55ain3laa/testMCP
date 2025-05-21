# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VoucherCreateParams", "VoucherDetail"]


class VoucherCreateParams(TypedDict, total=False):
    voucher_date: Required[Annotated[str, PropertyInfo(alias="voucherDate")]]
    """
    Date of The Voucher | Date Format is the sent `dateFormat` or default
    `yyyy-MM-dd`
    """

    voucher_reference: Required[Annotated[str, PropertyInfo(alias="voucherReference")]]
    """Voucher Reference"""

    voucher_type: Required[Annotated[str, PropertyInfo(alias="voucherType")]]
    """Voucher Type Code of existing voucher types | example 'JV' or 'SI'"""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]

    date_format: Annotated[str, PropertyInfo(alias="dateFormat")]

    delete_voucher_id: Annotated[str, PropertyInfo(alias="deleteVoucherId")]
    """ID of voucher to be replaced"""

    voucher_description: Annotated[str, PropertyInfo(alias="voucherDescription")]
    """any voucher description"""

    voucher_details: Annotated[Iterable[VoucherDetail], PropertyInfo(alias="voucherDetails")]


class VoucherDetail(TypedDict, total=False):
    account_number: Required[Annotated[str, PropertyInfo(alias="accountNumber")]]

    currency_code: Required[Annotated[str, PropertyInfo(alias="currencyCode")]]

    type: Required[str]
    """Debit or Credit type | values ('d' or 'c')"""

    amount: float

    amount_fbc: Annotated[float, PropertyInfo(alias="amountFbc")]

    amount_sbc: Annotated[float, PropertyInfo(alias="amountSbc")]
