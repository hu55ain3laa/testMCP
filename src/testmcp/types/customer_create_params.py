# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .documents_info_param import DocumentsInfoParam

__all__ = ["CustomerCreateParams"]


class CustomerCreateParams(TypedDict, total=False):
    customer_type: Required[Annotated[str, PropertyInfo(alias="customerType")]]
    """always required, values ('company' 'individual' 'cash' 'potential')"""

    api_key: Required[Annotated[str, PropertyInfo(alias="apiKey")]]

    company_name: Annotated[str, PropertyInfo(alias="companyName")]
    """Customer company name , required for type company and potential"""

    customer_address: Annotated[str, PropertyInfo(alias="customerAddress")]
    """Customer Address"""

    customer_city: Annotated[str, PropertyInfo(alias="customerCity")]
    """Customer city , must exist in cities defintions"""

    customer_code: Annotated[int, PropertyInfo(alias="customerCode")]
    """Customer code"""

    customer_comm_reg_number: Annotated[str, PropertyInfo(alias="customerCommRegNumber")]
    """Customer Commercial Registration No."""

    customer_email: Annotated[str, PropertyInfo(alias="customerEmail")]
    """Customer Email"""

    customer_fax: Annotated[str, PropertyInfo(alias="customerFax")]
    """Customer Fax"""

    customer_first_name: Annotated[str, PropertyInfo(alias="customerFirstName")]
    """Customer first name , required for type individual and cash"""

    customer_last_name: Annotated[str, PropertyInfo(alias="customerLastName")]
    """Customer last Name , required for type individual and cash"""

    customer_middle_name: Annotated[str, PropertyInfo(alias="customerMiddleName")]
    """Customer middle Name"""

    customer_phone1: Annotated[str, PropertyInfo(alias="customerPhone1")]
    """Customer Phone 1 , required for type individual and cash"""

    customer_phone2: Annotated[str, PropertyInfo(alias="customerPhone2")]
    """Customer Phone 2"""

    customer_phone3: Annotated[str, PropertyInfo(alias="customerPhone3")]
    """Customer Phone 3"""

    customer_website: Annotated[str, PropertyInfo(alias="customerWebsite")]
    """Customer Website"""

    documents: Iterable[DocumentsInfoParam]
