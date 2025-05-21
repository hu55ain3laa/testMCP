# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Customer"]


class Customer(BaseModel):
    customer_account_number: Optional[str] = FieldInfo(alias="customerAccountNumber", default=None)
    """Customer Account Number"""

    customer_address: Optional[str] = FieldInfo(alias="customerAddress", default=None)
    """Customer Address"""

    customer_city: Optional[str] = FieldInfo(alias="customerCity", default=None)
    """Customer City"""

    customer_code: Optional[int] = FieldInfo(alias="customerCode", default=None)
    """Customer Code"""

    customer_comm_reg_number: Optional[str] = FieldInfo(alias="customerCommRegNumber", default=None)
    """Customer Commercial Registration No."""

    customer_email: Optional[str] = FieldInfo(alias="customerEmail", default=None)
    """Customer Email"""

    customer_fax: Optional[str] = FieldInfo(alias="customerFax", default=None)
    """Customer Fax"""

    customer_id: Optional[str] = FieldInfo(alias="customerId", default=None)
    """Customer ID"""

    customer_name: Optional[str] = FieldInfo(alias="customerName", default=None)
    """Customer Name (Company or Full Name)"""

    customer_phone1: Optional[str] = FieldInfo(alias="customerPhone1", default=None)
    """Customer Phone 1"""

    customer_phone2: Optional[str] = FieldInfo(alias="customerPhone2", default=None)
    """Customer Phone 2"""

    customer_phone3: Optional[str] = FieldInfo(alias="customerPhone3", default=None)
    """Customer Phone 3"""

    customer_vat_account_number: Optional[str] = FieldInfo(alias="customerVatAccountNumber", default=None)
    """Customer VAT Account Number"""

    customer_website: Optional[str] = FieldInfo(alias="customerWebsite", default=None)
    """Customer Website"""
