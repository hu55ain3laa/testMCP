# Product

Types:

```python
from testmcp.types import (
    ProductListResponse,
    ProductRetrieveCreatedAfterResponse,
    ProductRetrieveDetailsResponse,
    ProductRetrievePromotedAfterResponse,
    ProductRetrieveUpdatedAvailabilityAfterResponse,
    ProductRetrieveUpdatedPricesAfterResponse,
)
```

Methods:

- <code title="get /product/">client.product.<a href="./src/testmcp/resources/product.py">list</a>(\*\*<a href="src/testmcp/types/product_list_params.py">params</a>) -> <a href="./src/testmcp/types/product_list_response.py">ProductListResponse</a></code>
- <code title="get /product/createdProduct">client.product.<a href="./src/testmcp/resources/product.py">retrieve_created_after</a>(\*\*<a href="src/testmcp/types/product_retrieve_created_after_params.py">params</a>) -> <a href="./src/testmcp/types/product_retrieve_created_after_response.py">ProductRetrieveCreatedAfterResponse</a></code>
- <code title="get /product/details">client.product.<a href="./src/testmcp/resources/product.py">retrieve_details</a>(\*\*<a href="src/testmcp/types/product_retrieve_details_params.py">params</a>) -> <a href="./src/testmcp/types/product_retrieve_details_response.py">ProductRetrieveDetailsResponse</a></code>
- <code title="get /product/promotionPrices">client.product.<a href="./src/testmcp/resources/product.py">retrieve_promoted_after</a>(\*\*<a href="src/testmcp/types/product_retrieve_promoted_after_params.py">params</a>) -> <a href="./src/testmcp/types/product_retrieve_promoted_after_response.py">ProductRetrievePromotedAfterResponse</a></code>
- <code title="get /product/updatedAvailability">client.product.<a href="./src/testmcp/resources/product.py">retrieve_updated_availability_after</a>(\*\*<a href="src/testmcp/types/product_retrieve_updated_availability_after_params.py">params</a>) -> <a href="./src/testmcp/types/product_retrieve_updated_availability_after_response.py">ProductRetrieveUpdatedAvailabilityAfterResponse</a></code>
- <code title="get /product/updatedPrice">client.product.<a href="./src/testmcp/resources/product.py">retrieve_updated_prices_after</a>(\*\*<a href="src/testmcp/types/product_retrieve_updated_prices_after_params.py">params</a>) -> <a href="./src/testmcp/types/product_retrieve_updated_prices_after_response.py">ProductRetrieveUpdatedPricesAfterResponse</a></code>

# Categories

Types:

```python
from testmcp.types import CategoryRetrieveTreeResponse
```

Methods:

- <code title="get /categories/tree">client.categories.<a href="./src/testmcp/resources/categories.py">retrieve_tree</a>() -> <a href="./src/testmcp/types/category_retrieve_tree_response.py">CategoryRetrieveTreeResponse</a></code>

# Currency

Types:

```python
from testmcp.types import CurrencyGetRatesResponse
```

Methods:

- <code title="get /currency/rates">client.currency.<a href="./src/testmcp/resources/currency.py">get_rates</a>(\*\*<a href="src/testmcp/types/currency_get_rates_params.py">params</a>) -> <a href="./src/testmcp/types/currency_get_rates_response.py">CurrencyGetRatesResponse</a></code>

# Vouchers

Types:

```python
from testmcp.types import VoucherCreateResponse
```

Methods:

- <code title="post /vouchers/">client.vouchers.<a href="./src/testmcp/resources/vouchers.py">create</a>(\*\*<a href="src/testmcp/types/voucher_create_params.py">params</a>) -> <a href="./src/testmcp/types/voucher_create_response.py">VoucherCreateResponse</a></code>

# Customers

Types:

```python
from testmcp.types import (
    Customer,
    CustomerCreateResponse,
    CustomerUpdateResponse,
    CustomerListResponse,
)
```

Methods:

- <code title="post /customers/">client.customers.<a href="./src/testmcp/resources/customers.py">create</a>(\*\*<a href="src/testmcp/types/customer_create_params.py">params</a>) -> <a href="./src/testmcp/types/customer_create_response.py">CustomerCreateResponse</a></code>
- <code title="get /customers/{id}">client.customers.<a href="./src/testmcp/resources/customers.py">retrieve</a>(id) -> <a href="./src/testmcp/types/customer.py">Customer</a></code>
- <code title="put /customers/{id}">client.customers.<a href="./src/testmcp/resources/customers.py">update</a>(id, \*\*<a href="src/testmcp/types/customer_update_params.py">params</a>) -> <a href="./src/testmcp/types/customer_update_response.py">CustomerUpdateResponse</a></code>
- <code title="get /customers/">client.customers.<a href="./src/testmcp/resources/customers.py">list</a>(\*\*<a href="src/testmcp/types/customer_list_params.py">params</a>) -> <a href="./src/testmcp/types/customer_list_response.py">CustomerListResponse</a></code>

# Suppliers

Types:

```python
from testmcp.types import SupplierCreateResponse, SupplierUpdateResponse
```

Methods:

- <code title="post /suppliers/">client.suppliers.<a href="./src/testmcp/resources/suppliers.py">create</a>(\*\*<a href="src/testmcp/types/supplier_create_params.py">params</a>) -> <a href="./src/testmcp/types/supplier_create_response.py">SupplierCreateResponse</a></code>
- <code title="put /suppliers/{id}">client.suppliers.<a href="./src/testmcp/resources/suppliers.py">update</a>(id, \*\*<a href="src/testmcp/types/supplier_update_params.py">params</a>) -> <a href="./src/testmcp/types/supplier_update_response.py">SupplierUpdateResponse</a></code>

# PurchaseRequisitions

Types:

```python
from testmcp.types import DocumentsInfo, PurchaseRequisitionCreateResponse
```

Methods:

- <code title="post /purchaseRequisitions/">client.purchase_requisitions.<a href="./src/testmcp/resources/purchase_requisitions.py">create</a>(\*\*<a href="src/testmcp/types/purchase_requisition_create_params.py">params</a>) -> <a href="./src/testmcp/types/purchase_requisition_create_response.py">PurchaseRequisitionCreateResponse</a></code>
- <code title="post /purchaseRequisitions/{id}/documents">client.purchase_requisitions.<a href="./src/testmcp/resources/purchase_requisitions.py">add_document</a>(id, \*\*<a href="src/testmcp/types/purchase_requisition_add_document_params.py">params</a>) -> None</code>

# PurchaseQuotations

Types:

```python
from testmcp.types import (
    PurchaseQuotationCreateResponse,
    PurchaseQuotationUpdateResponse,
    PurchaseQuotationListResponse,
)
```

Methods:

- <code title="post /purchaseQuotations/">client.purchase_quotations.<a href="./src/testmcp/resources/purchase_quotations.py">create</a>(\*\*<a href="src/testmcp/types/purchase_quotation_create_params.py">params</a>) -> <a href="./src/testmcp/types/purchase_quotation_create_response.py">PurchaseQuotationCreateResponse</a></code>
- <code title="put /purchaseQuotations/{id}">client.purchase_quotations.<a href="./src/testmcp/resources/purchase_quotations.py">update</a>(id, \*\*<a href="src/testmcp/types/purchase_quotation_update_params.py">params</a>) -> <a href="./src/testmcp/types/purchase_quotation_update_response.py">PurchaseQuotationUpdateResponse</a></code>
- <code title="get /purchaseQuotations/">client.purchase_quotations.<a href="./src/testmcp/resources/purchase_quotations.py">list</a>(\*\*<a href="src/testmcp/types/purchase_quotation_list_params.py">params</a>) -> <a href="./src/testmcp/types/purchase_quotation_list_response.py">PurchaseQuotationListResponse</a></code>

# SalesQuotations

## ByPurchaseRequisition

Types:

```python
from testmcp.types.sales_quotations import ByPurchaseRequisitionPrintHTMLResponse
```

Methods:

- <code title="get /salesQuotations/byPurchaseRequisition/{id}/printHtml">client.sales_quotations.by_purchase_requisition.<a href="./src/testmcp/resources/sales_quotations/by_purchase_requisition.py">print_html</a>(id) -> str</code>

# SalesInvoices

Types:

```python
from testmcp.types import SalesInvoicePrintHTMLResponse
```

Methods:

- <code title="get /salesInvoices/{id}/printHtml">client.sales_invoices.<a href="./src/testmcp/resources/sales_invoices/sales_invoices.py">print_html</a>(id) -> str</code>

## ByPurchaseRequisition

Types:

```python
from testmcp.types.sales_invoices import ByPurchaseRequisitionGenerateResponse
```

Methods:

- <code title="post /salesInvoices/byPurchaseRequisition/{id}/generate">client.sales_invoices.by_purchase_requisition.<a href="./src/testmcp/resources/sales_invoices/by_purchase_requisition.py">generate</a>(id) -> <a href="./src/testmcp/types/sales_invoices/by_purchase_requisition_generate_response.py">ByPurchaseRequisitionGenerateResponse</a></code>

# Employees

Types:

```python
from testmcp.types import EmployeeListResponse
```

Methods:

- <code title="get /employees/">client.employees.<a href="./src/testmcp/resources/employees.py">list</a>(\*\*<a href="src/testmcp/types/employee_list_params.py">params</a>) -> <a href="./src/testmcp/types/employee_list_response.py">EmployeeListResponse</a></code>

# Attendance

Types:

```python
from testmcp.types import AttendanceCreateResponse, AttendanceDeleteResponse
```

Methods:

- <code title="post /attendance/">client.attendance.<a href="./src/testmcp/resources/attendance.py">create</a>(\*\*<a href="src/testmcp/types/attendance_create_params.py">params</a>) -> <a href="./src/testmcp/types/attendance_create_response.py">AttendanceCreateResponse</a></code>
- <code title="delete /attendance/">client.attendance.<a href="./src/testmcp/resources/attendance.py">delete</a>(\*\*<a href="src/testmcp/types/attendance_delete_params.py">params</a>) -> <a href="./src/testmcp/types/attendance_delete_response.py">AttendanceDeleteResponse</a></code>
