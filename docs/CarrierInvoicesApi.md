# swagger_client.CarrierInvoicesApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_carrier_invoices_attempt_auto_reconciliation_post**](CarrierInvoicesApi.md#apiv2_carrier_invoices_attempt_auto_reconciliation_post) | **POST** /apiv2/carrierInvoices/attemptAutoReconciliation | Attempt to auto reconcile consignments based on the thresholds defined in the carrier account associated with the consignment.  Note that a successful response from this function will not indicate whether the consignments did or did not auto-reconcile - you  will need to establish that from the consignments and their notes instead.
[**apiv2_carrier_invoices_get_all_get**](CarrierInvoicesApi.md#apiv2_carrier_invoices_get_all_get) | **GET** /apiv2/carrierInvoices/getAll | Return the basic information about carrier invoices that have been imported into Machship. It will return at most 100 records,  in the order of most recently imported to oldest.
[**apiv2_carrier_invoices_get_entries_for_invoice_get**](CarrierInvoicesApi.md#apiv2_carrier_invoices_get_entries_for_invoice_get) | **GET** /apiv2/carrierInvoices/getEntriesForInvoice | Get a listing of carrier invoice entries for a particular carrier invoice, with the option to filter by the status of the entries.
[**apiv2_carrier_invoices_update_and_reprice_consignment_post**](CarrierInvoicesApi.md#apiv2_carrier_invoices_update_and_reprice_consignment_post) | **POST** /apiv2/carrierInvoices/updateAndRepriceConsignment | Update a consignment&#x27;s items and trigger Machship to reprice it using the new item weights / dimensions.

# **apiv2_carrier_invoices_attempt_auto_reconciliation_post**
> EmptyDomainEntityV2 apiv2_carrier_invoices_attempt_auto_reconciliation_post(body=body)

Attempt to auto reconcile consignments based on the thresholds defined in the carrier account associated with the consignment.  Note that a successful response from this function will not indicate whether the consignments did or did not auto-reconcile - you  will need to establish that from the consignments and their notes instead.

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
api_instance = swagger_client.CarrierInvoicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.AutoReconcileRequest() # AutoReconcileRequest |  (optional)

try:
    # Attempt to auto reconcile consignments based on the thresholds defined in the carrier account associated with the consignment.  Note that a successful response from this function will not indicate whether the consignments did or did not auto-reconcile - you  will need to establish that from the consignments and their notes instead.
    api_response = api_instance.apiv2_carrier_invoices_attempt_auto_reconciliation_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarrierInvoicesApi->apiv2_carrier_invoices_attempt_auto_reconciliation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AutoReconcileRequest**](AutoReconcileRequest.md)|  | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_carrier_invoices_get_all_get**
> CarrierInvoiceInformationICollectionBaseDomainEntityV2 apiv2_carrier_invoices_get_all_get(company_id=company_id, carrier_id=carrier_id, file_name=file_name, invoice_id=invoice_id)

Return the basic information about carrier invoices that have been imported into Machship. It will return at most 100 records,  in the order of most recently imported to oldest.

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
api_instance = swagger_client.CarrierInvoicesApi(swagger_client.ApiClient(configuration))
company_id = 56 # int | Optional parameter to limit invoices to those imported against a certain MachShip company ID (optional)
carrier_id = 56 # int | Optional parameter to limit invoices to those imported against a certain MachShip carrier ID (optional)
file_name = 'file_name_example' # str | Optional parameter - when supplied it will filter the results to invoices which match the supplied file name (optional)
invoice_id = 'invoice_id_example' # str | Optional parameter - when supplied it will filter the results to invoices which match the supplied invoice ID (optional)

try:
    # Return the basic information about carrier invoices that have been imported into Machship. It will return at most 100 records,  in the order of most recently imported to oldest.
    api_response = api_instance.apiv2_carrier_invoices_get_all_get(company_id=company_id, carrier_id=carrier_id, file_name=file_name, invoice_id=invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarrierInvoicesApi->apiv2_carrier_invoices_get_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Optional parameter to limit invoices to those imported against a certain MachShip company ID | [optional] 
 **carrier_id** | **int**| Optional parameter to limit invoices to those imported against a certain MachShip carrier ID | [optional] 
 **file_name** | **str**| Optional parameter - when supplied it will filter the results to invoices which match the supplied file name | [optional] 
 **invoice_id** | **str**| Optional parameter - when supplied it will filter the results to invoices which match the supplied invoice ID | [optional] 

### Return type

[**CarrierInvoiceInformationICollectionBaseDomainEntityV2**](CarrierInvoiceInformationICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_carrier_invoices_get_entries_for_invoice_get**
> CarrierInvoiceEntryV2ForGetEntriesEndpointICollectionBaseDomainEntityV2 apiv2_carrier_invoices_get_entries_for_invoice_get(carrier_invoice_id=carrier_invoice_id, status=status)

Get a listing of carrier invoice entries for a particular carrier invoice, with the option to filter by the status of the entries.

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
api_instance = swagger_client.CarrierInvoicesApi(swagger_client.ApiClient(configuration))
carrier_invoice_id = 56 # int | The Machship ID of an imported carrier invoice (optional)
status = swagger_client.CarrierInvoiceEntryStatus() # CarrierInvoiceEntryStatus | An optional status filter for the entries (optional)

try:
    # Get a listing of carrier invoice entries for a particular carrier invoice, with the option to filter by the status of the entries.
    api_response = api_instance.apiv2_carrier_invoices_get_entries_for_invoice_get(carrier_invoice_id=carrier_invoice_id, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarrierInvoicesApi->apiv2_carrier_invoices_get_entries_for_invoice_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carrier_invoice_id** | **int**| The Machship ID of an imported carrier invoice | [optional] 
 **status** | [**CarrierInvoiceEntryStatus**](.md)| An optional status filter for the entries | [optional] 

### Return type

[**CarrierInvoiceEntryV2ForGetEntriesEndpointICollectionBaseDomainEntityV2**](CarrierInvoiceEntryV2ForGetEntriesEndpointICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_carrier_invoices_update_and_reprice_consignment_post**
> EmptyDomainEntityV2 apiv2_carrier_invoices_update_and_reprice_consignment_post(body=body)

Update a consignment's items and trigger Machship to reprice it using the new item weights / dimensions.

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
api_instance = swagger_client.CarrierInvoicesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RepriceConsignmentV2Model() # RepriceConsignmentV2Model |  (optional)

try:
    # Update a consignment's items and trigger Machship to reprice it using the new item weights / dimensions.
    api_response = api_instance.apiv2_carrier_invoices_update_and_reprice_consignment_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CarrierInvoicesApi->apiv2_carrier_invoices_update_and_reprice_consignment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RepriceConsignmentV2Model**](RepriceConsignmentV2Model.md)|  | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

