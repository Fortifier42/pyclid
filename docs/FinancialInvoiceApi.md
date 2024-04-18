# swagger_client.FinancialInvoiceApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_financial_invoice_get_all_posted_get**](FinancialInvoiceApi.md#apiv2_financial_invoice_get_all_posted_get) | **GET** /apiv2/financialInvoice/getAllPosted | Return the basic information about invoices that are in a posted state. It will return at most 100 records,  in the order of most recently imported to oldest.
[**apiv2_financial_invoice_get_posted_invoice_by_document_number_get**](FinancialInvoiceApi.md#apiv2_financial_invoice_get_posted_invoice_by_document_number_get) | **GET** /apiv2/financialInvoice/getPostedInvoiceByDocumentNumber | Returns invoice details with the invoice pdf as a byte array

# **apiv2_financial_invoice_get_all_posted_get**
> InvoiceV2LiteICollectionBaseDomainEntityV2 apiv2_financial_invoice_get_all_posted_get(start_date=start_date, end_date=end_date, start_index=start_index, retrieve_size=retrieve_size)

Return the basic information about invoices that are in a posted state. It will return at most 100 records,  in the order of most recently imported to oldest.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: User API Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FinancialInvoiceApi(swagger_client.ApiClient(configuration))
start_date = '2013-10-20T19:20:30+01:00' # datetime | Optional parameter - when supplied it will filter the results to invoices which have an invoice date which is greater or equal to the supplied date (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | Optional parameter - when supplied it will filter the results to invoices which have an invoice date which is earlier or equal to the supplied date (optional)
start_index = 1 # int |  (optional) (default to 1)
retrieve_size = 100 # int |  (optional) (default to 100)

try:
    # Return the basic information about invoices that are in a posted state. It will return at most 100 records,  in the order of most recently imported to oldest.
    api_response = api_instance.apiv2_financial_invoice_get_all_posted_get(start_date=start_date, end_date=end_date, start_index=start_index, retrieve_size=retrieve_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialInvoiceApi->apiv2_financial_invoice_get_all_posted_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| Optional parameter - when supplied it will filter the results to invoices which have an invoice date which is greater or equal to the supplied date | [optional] 
 **end_date** | **datetime**| Optional parameter - when supplied it will filter the results to invoices which have an invoice date which is earlier or equal to the supplied date | [optional] 
 **start_index** | **int**|  | [optional] [default to 1]
 **retrieve_size** | **int**|  | [optional] [default to 100]

### Return type

[**InvoiceV2LiteICollectionBaseDomainEntityV2**](InvoiceV2LiteICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_financial_invoice_get_posted_invoice_by_document_number_get**
> InvoiceV2BaseDomainEntityV2 apiv2_financial_invoice_get_posted_invoice_by_document_number_get(document_number=document_number, return_pdf_file_bytes=return_pdf_file_bytes)

Returns invoice details with the invoice pdf as a byte array

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: User API Token
configuration = swagger_client.Configuration()
configuration.api_key['token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.FinancialInvoiceApi(swagger_client.ApiClient(configuration))
document_number = 'document_number_example' # str | Machship Invoice Document Number (optional)
return_pdf_file_bytes = false # bool | Optional parameter - When supplied and true, the invoice pdf as a byte array will be returned as the Pdf property (optional) (default to false)

try:
    # Returns invoice details with the invoice pdf as a byte array
    api_response = api_instance.apiv2_financial_invoice_get_posted_invoice_by_document_number_get(document_number=document_number, return_pdf_file_bytes=return_pdf_file_bytes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialInvoiceApi->apiv2_financial_invoice_get_posted_invoice_by_document_number_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_number** | **str**| Machship Invoice Document Number | [optional] 
 **return_pdf_file_bytes** | **bool**| Optional parameter - When supplied and true, the invoice pdf as a byte array will be returned as the Pdf property | [optional] [default to false]

### Return type

[**InvoiceV2BaseDomainEntityV2**](InvoiceV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

