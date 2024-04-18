# swagger_client.ConsignmentsApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_consignments_create_consignment_post**](ConsignmentsApi.md#apiv2_consignments_create_consignment_post) | **POST** /apiv2/consignments/createConsignment | Creates an unmanifested consignment in Machship
[**apiv2_consignments_create_consignmentwith_complex_items_post**](ConsignmentsApi.md#apiv2_consignments_create_consignmentwith_complex_items_post) | **POST** /apiv2/consignments/createConsignmentwithComplexItems | Creates an unmanifested consignment in Machship
[**apiv2_consignments_create_existing_consignment_post**](ConsignmentsApi.md#apiv2_consignments_create_existing_consignment_post) | **POST** /apiv2/consignments/createExistingConsignment | Creates an unmanifested consignment in Machship
[**apiv2_consignments_delete_unmanifested_consignments_post**](ConsignmentsApi.md#apiv2_consignments_delete_unmanifested_consignments_post) | **POST** /apiv2/consignments/deleteUnmanifestedConsignments | Deletes the specified Unmanifested Consignments in Machship
[**apiv2_consignments_edit_unmanifested_consignment_post**](ConsignmentsApi.md#apiv2_consignments_edit_unmanifested_consignment_post) | **POST** /apiv2/consignments/editUnmanifestedConsignment | Edit a consignment - note that it must be in an \&quot;unmanifested\&quot; state for this to be a valid operation
[**apiv2_consignments_get_active_get**](ConsignmentsApi.md#apiv2_consignments_get_active_get) | **GET** /apiv2/consignments/getActive | Return all consignments for a company, regardless of status
[**apiv2_consignments_get_all_get**](ConsignmentsApi.md#apiv2_consignments_get_all_get) | **GET** /apiv2/consignments/getAll | Return all consignments for a company, regardless of status
[**apiv2_consignments_get_attachments_post**](ConsignmentsApi.md#apiv2_consignments_get_attachments_post) | **POST** /apiv2/consignments/getAttachments | Gets attachment information for a given consignment
[**apiv2_consignments_get_completed_get**](ConsignmentsApi.md#apiv2_consignments_get_completed_get) | **GET** /apiv2/consignments/getCompleted | Returns consignments for the given company that were completed within the provided start and end date range. Limited to 2000 consignments at a time.
[**apiv2_consignments_get_consignment_by_pending_consignment_id_get**](ConsignmentsApi.md#apiv2_consignments_get_consignment_by_pending_consignment_id_get) | **GET** /apiv2/consignments/getConsignmentByPendingConsignmentId | Get a Consignment Details (if it exists) for a single consignment, using a pending consignment ID that  has been transformed (linked) into a consignment
[**apiv2_consignments_get_consignment_for_clone_get**](ConsignmentsApi.md#apiv2_consignments_get_consignment_for_clone_get) | **GET** /apiv2/consignments/getConsignmentForClone | Get the details of an existing consignment in a format that can be passed to the createConsignmentWithComplexItems endpoint
[**apiv2_consignments_get_consignment_get**](ConsignmentsApi.md#apiv2_consignments_get_consignment_get) | **GET** /apiv2/consignments/getConsignment | Get Consignment Details for a single consignment
[**apiv2_consignments_get_recently_created_or_updated_consignments_get**](ConsignmentsApi.md#apiv2_consignments_get_recently_created_or_updated_consignments_get) | **GET** /apiv2/consignments/getRecentlyCreatedOrUpdatedConsignments | Return consignments for a company that have been created or updated within the timeframe specified
[**apiv2_consignments_get_unmanifested_consignment_for_edit_get**](ConsignmentsApi.md#apiv2_consignments_get_unmanifested_consignment_for_edit_get) | **GET** /apiv2/consignments/getUnmanifestedConsignmentForEdit | Get an unmanifested consignment in the same format required to perform an update in the edit endpoint
[**apiv2_consignments_get_unmanifested_get**](ConsignmentsApi.md#apiv2_consignments_get_unmanifested_get) | **GET** /apiv2/consignments/getUnmanifested | Get all consignments for a company that are in an \&quot;unmanifested\&quot; state
[**apiv2_consignments_return_consignment_statuses_post**](ConsignmentsApi.md#apiv2_consignments_return_consignment_statuses_post) | **POST** /apiv2/consignments/returnConsignmentStatuses | Return all statuses recorded in the system with an option to specify a cutoff date to limit the statuses returned to ones saved in Machship  after a certain date. Maximum of 100 consignments
[**apiv2_consignments_return_consignments_by_carrier_consignment_id_post**](ConsignmentsApi.md#apiv2_consignments_return_consignments_by_carrier_consignment_id_post) | **POST** /apiv2/consignments/returnConsignmentsByCarrierConsignmentId | Get Consignment Details for a multiple consignments using the Carrier Consignment ID as the lookup. Maximum of 10 consignments per request
[**apiv2_consignments_return_consignments_by_pending_consignment_ids_post**](ConsignmentsApi.md#apiv2_consignments_return_consignments_by_pending_consignment_ids_post) | **POST** /apiv2/consignments/returnConsignmentsByPendingConsignmentIds | Get Consignment Details for multiple consignments using the Pending Consignment Id as the lookup. Maximum of 100 consignments.
[**apiv2_consignments_return_consignments_by_reference1_post**](ConsignmentsApi.md#apiv2_consignments_return_consignments_by_reference1_post) | **POST** /apiv2/consignments/returnConsignmentsByReference1 | Get Consignment Details for a multiple consignments using Reference 1 as the lookup. Maximum of 10 consignments per request
[**apiv2_consignments_return_consignments_by_reference2_post**](ConsignmentsApi.md#apiv2_consignments_return_consignments_by_reference2_post) | **POST** /apiv2/consignments/returnConsignmentsByReference2 | Get Consignment Details for a multiple consignments using Reference 2 as the lookup. Maximum of 10 consignments per request
[**apiv2_consignments_return_consignments_post**](ConsignmentsApi.md#apiv2_consignments_return_consignments_post) | **POST** /apiv2/consignments/returnConsignments | Get Consignment Details for a multiple consignments. Maximum of 100 consignments per request
[**apiv2_consignments_search_consignments_post**](ConsignmentsApi.md#apiv2_consignments_search_consignments_post) | **POST** /apiv2/consignments/searchConsignments | Get the details of related consignments based on the provided list of consignment or item references
[**apiv2_consignments_update_consignment_statuses_post**](ConsignmentsApi.md#apiv2_consignments_update_consignment_statuses_post) | **POST** /apiv2/consignments/updateConsignmentStatuses | 

# **apiv2_consignments_create_consignment_post**
> CreateConsignmentResponseV2BaseDomainEntityV2 apiv2_consignments_create_consignment_post(body=body)

Creates an unmanifested consignment in Machship

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateConsignmentV2() # CreateConsignmentV2 | Details of the consignment to create (optional)

try:
    # Creates an unmanifested consignment in Machship
    api_response = api_instance.apiv2_consignments_create_consignment_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_create_consignment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateConsignmentV2**](CreateConsignmentV2.md)| Details of the consignment to create | [optional] 

### Return type

[**CreateConsignmentResponseV2BaseDomainEntityV2**](CreateConsignmentResponseV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_create_consignmentwith_complex_items_post**
> CreateConsignmentResponseV2BaseDomainEntityV2 apiv2_consignments_create_consignmentwith_complex_items_post(body=body)

Creates an unmanifested consignment in Machship

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateConsignmentComplexItemsV2() # CreateConsignmentComplexItemsV2 | Details of the consignment to create (optional)

try:
    # Creates an unmanifested consignment in Machship
    api_response = api_instance.apiv2_consignments_create_consignmentwith_complex_items_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_create_consignmentwith_complex_items_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateConsignmentComplexItemsV2**](CreateConsignmentComplexItemsV2.md)| Details of the consignment to create | [optional] 

### Return type

[**CreateConsignmentResponseV2BaseDomainEntityV2**](CreateConsignmentResponseV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_create_existing_consignment_post**
> Int32BaseDomainEntityV2 apiv2_consignments_create_existing_consignment_post(body=body)

Creates an unmanifested consignment in Machship

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateConsignmentExistingV2() # CreateConsignmentExistingV2 | Details of the consignment to create (optional)

try:
    # Creates an unmanifested consignment in Machship
    api_response = api_instance.apiv2_consignments_create_existing_consignment_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_create_existing_consignment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateConsignmentExistingV2**](CreateConsignmentExistingV2.md)| Details of the consignment to create | [optional] 

### Return type

[**Int32BaseDomainEntityV2**](Int32BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_delete_unmanifested_consignments_post**
> EmptyDomainEntityV2 apiv2_consignments_delete_unmanifested_consignments_post(body=body)

Deletes the specified Unmanifested Consignments in Machship

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
body = [56] # list[int] | Ids of the consignments to be deleted (optional)

try:
    # Deletes the specified Unmanifested Consignments in Machship
    api_response = api_instance.apiv2_consignments_delete_unmanifested_consignments_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_delete_unmanifested_consignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)| Ids of the consignments to be deleted | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_edit_unmanifested_consignment_post**
> CreateConsignmentResponseV2BaseDomainEntityV2 apiv2_consignments_edit_unmanifested_consignment_post(body=body)

Edit a consignment - note that it must be in an \"unmanifested\" state for this to be a valid operation

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.EditConsignmentV2() # EditConsignmentV2 | Details of the consignment to edit (optional)

try:
    # Edit a consignment - note that it must be in an \"unmanifested\" state for this to be a valid operation
    api_response = api_instance.apiv2_consignments_edit_unmanifested_consignment_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_edit_unmanifested_consignment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditConsignmentV2**](EditConsignmentV2.md)| Details of the consignment to edit | [optional] 

### Return type

[**CreateConsignmentResponseV2BaseDomainEntityV2**](CreateConsignmentResponseV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_get_active_get**
> ConsignmentsForListGridDomainEntityV2 apiv2_consignments_get_active_get(company_id=company_id, start_index=start_index, retrieve_size=retrieve_size, carrier_id=carrier_id, include_child_companies=include_child_companies)

Return all consignments for a company, regardless of status

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
company_id = 56 # int | Optional - defaults to your company. Must be a valid company ID in MachShip (optional)
start_index = 1 # int | Defaults to 1. Can be used to \"page\" through subsequent requests (optional) (default to 1)
retrieve_size = 999999 # int | The number of consignments to return at one time. (optional) (default to 999999)
carrier_id = 56 # int | Optional carrier ID to restrict consignments to those of this carrier (optional)
include_child_companies = false # bool | Whether to include companies that are \"children\" below companyId (optional) (default to false)

try:
    # Return all consignments for a company, regardless of status
    api_response = api_instance.apiv2_consignments_get_active_get(company_id=company_id, start_index=start_index, retrieve_size=retrieve_size, carrier_id=carrier_id, include_child_companies=include_child_companies)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_get_active_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Optional - defaults to your company. Must be a valid company ID in MachShip | [optional] 
 **start_index** | **int**| Defaults to 1. Can be used to \&quot;page\&quot; through subsequent requests | [optional] [default to 1]
 **retrieve_size** | **int**| The number of consignments to return at one time. | [optional] [default to 999999]
 **carrier_id** | **int**| Optional carrier ID to restrict consignments to those of this carrier | [optional] 
 **include_child_companies** | **bool**| Whether to include companies that are \&quot;children\&quot; below companyId | [optional] [default to false]

### Return type

[**ConsignmentsForListGridDomainEntityV2**](ConsignmentsForListGridDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_get_all_get**
> ConsignmentsForListGridDomainEntityV2 apiv2_consignments_get_all_get(company_id=company_id, start_index=start_index, retrieve_size=retrieve_size, carrier_id=carrier_id, include_child_companies=include_child_companies, include_deleted_consignments=include_deleted_consignments, from_date_time_local=from_date_time_local, to_date_time_local=to_date_time_local, filter_by_eta_completed_or_despatch=filter_by_eta_completed_or_despatch)

Return all consignments for a company, regardless of status

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
company_id = 56 # int | Optional - defaults to your company. Must be a valid company ID in MachShip (optional)
start_index = 1 # int | Defaults to 1. Can be used to \"page\" through subsequent requests (optional) (default to 1)
retrieve_size = 40 # int | The number of consignments to return. Defaults to 40, will return a maximum of 200 rows (optional) (default to 40)
carrier_id = 56 # int | Optional carrier ID to restrict consignments to those of this carrier (optional)
include_child_companies = false # bool | Whether to include companies that are \"children\" below companyId (optional) (default to false)
include_deleted_consignments = false # bool | Optional - when set to true consignments that have been deleted will return (optional) (default to false)
from_date_time_local = '2013-10-20T19:20:30+01:00' # datetime | Optional - Local time to filter consignments on. Set filterByEtaCompletedOrDespatch to switch between despatch date and ETA/Completed date (optional)
to_date_time_local = '2013-10-20T19:20:30+01:00' # datetime | Optional - Local time to filter consignments on. Set filterByEtaCompletedOrDespatch to switch between despatch date and ETA/Completed date (optional)
filter_by_eta_completed_or_despatch = true # bool | Optional - if times are provided, false = Despatch Date, true = ETA/Completed Date. Defaults to despatch date if omitted (optional)

try:
    # Return all consignments for a company, regardless of status
    api_response = api_instance.apiv2_consignments_get_all_get(company_id=company_id, start_index=start_index, retrieve_size=retrieve_size, carrier_id=carrier_id, include_child_companies=include_child_companies, include_deleted_consignments=include_deleted_consignments, from_date_time_local=from_date_time_local, to_date_time_local=to_date_time_local, filter_by_eta_completed_or_despatch=filter_by_eta_completed_or_despatch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_get_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Optional - defaults to your company. Must be a valid company ID in MachShip | [optional] 
 **start_index** | **int**| Defaults to 1. Can be used to \&quot;page\&quot; through subsequent requests | [optional] [default to 1]
 **retrieve_size** | **int**| The number of consignments to return. Defaults to 40, will return a maximum of 200 rows | [optional] [default to 40]
 **carrier_id** | **int**| Optional carrier ID to restrict consignments to those of this carrier | [optional] 
 **include_child_companies** | **bool**| Whether to include companies that are \&quot;children\&quot; below companyId | [optional] [default to false]
 **include_deleted_consignments** | **bool**| Optional - when set to true consignments that have been deleted will return | [optional] [default to false]
 **from_date_time_local** | **datetime**| Optional - Local time to filter consignments on. Set filterByEtaCompletedOrDespatch to switch between despatch date and ETA/Completed date | [optional] 
 **to_date_time_local** | **datetime**| Optional - Local time to filter consignments on. Set filterByEtaCompletedOrDespatch to switch between despatch date and ETA/Completed date | [optional] 
 **filter_by_eta_completed_or_despatch** | **bool**| Optional - if times are provided, false &#x3D; Despatch Date, true &#x3D; ETA/Completed Date. Defaults to despatch date if omitted | [optional] 

### Return type

[**ConsignmentsForListGridDomainEntityV2**](ConsignmentsForListGridDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_get_attachments_post**
> ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2 apiv2_consignments_get_attachments_post(consignment_id=consignment_id)

Gets attachment information for a given consignment

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
consignment_id = 56 # int | id of the consignment (optional)

try:
    # Gets attachment information for a given consignment
    api_response = api_instance.apiv2_consignments_get_attachments_post(consignment_id=consignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_get_attachments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **int**| id of the consignment | [optional] 

### Return type

[**ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2**](ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_get_completed_get**
> ConsignmentsForListGridDomainEntityV2 apiv2_consignments_get_completed_get(company_id=company_id, start_date=start_date, end_date=end_date, include_child_companies=include_child_companies)

Returns consignments for the given company that were completed within the provided start and end date range. Limited to 2000 consignments at a time.

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
company_id = 56 # int | Optional - defaults to your company. Must be a valid company ID in MachShip (optional)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start Date which is compared against the consignment's Completed Date (all date times are local to the delivery location) (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | End Date which is compared against the consignment's Completed Date (all date times are local to the delivery location) (optional)
include_child_companies = false # bool | Whether to include companies that are \"children\" below companyId (optional) (default to false)

try:
    # Returns consignments for the given company that were completed within the provided start and end date range. Limited to 2000 consignments at a time.
    api_response = api_instance.apiv2_consignments_get_completed_get(company_id=company_id, start_date=start_date, end_date=end_date, include_child_companies=include_child_companies)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_get_completed_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Optional - defaults to your company. Must be a valid company ID in MachShip | [optional] 
 **start_date** | **datetime**| Start Date which is compared against the consignment&#x27;s Completed Date (all date times are local to the delivery location) | [optional] 
 **end_date** | **datetime**| End Date which is compared against the consignment&#x27;s Completed Date (all date times are local to the delivery location) | [optional] 
 **include_child_companies** | **bool**| Whether to include companies that are \&quot;children\&quot; below companyId | [optional] [default to false]

### Return type

[**ConsignmentsForListGridDomainEntityV2**](ConsignmentsForListGridDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_get_consignment_by_pending_consignment_id_get**
> ConsignmentV2BaseDomainEntityV2 apiv2_consignments_get_consignment_by_pending_consignment_id_get(id=id)

Get a Consignment Details (if it exists) for a single consignment, using a pending consignment ID that  has been transformed (linked) into a consignment

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
id = 56 # int |  (optional)

try:
    # Get a Consignment Details (if it exists) for a single consignment, using a pending consignment ID that  has been transformed (linked) into a consignment
    api_response = api_instance.apiv2_consignments_get_consignment_by_pending_consignment_id_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_get_consignment_by_pending_consignment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 

### Return type

[**ConsignmentV2BaseDomainEntityV2**](ConsignmentV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_get_consignment_for_clone_get**
> CreateConsignmentComplexItemsV2BaseDomainEntityV2 apiv2_consignments_get_consignment_for_clone_get(id=id)

Get the details of an existing consignment in a format that can be passed to the createConsignmentWithComplexItems endpoint

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
id = 56 # int | The MachShip ID of a consignment (optional)

try:
    # Get the details of an existing consignment in a format that can be passed to the createConsignmentWithComplexItems endpoint
    api_response = api_instance.apiv2_consignments_get_consignment_for_clone_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_get_consignment_for_clone_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The MachShip ID of a consignment | [optional] 

### Return type

[**CreateConsignmentComplexItemsV2BaseDomainEntityV2**](CreateConsignmentComplexItemsV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_get_consignment_get**
> ConsignmentV2BaseDomainEntityV2 apiv2_consignments_get_consignment_get(id=id, include_deleted=include_deleted)

Get Consignment Details for a single consignment

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
id = 56 # int |  (optional)
include_deleted = false # bool | If true, will also return details for deleted consignments (optional) (default to false)

try:
    # Get Consignment Details for a single consignment
    api_response = api_instance.apiv2_consignments_get_consignment_get(id=id, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_get_consignment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 
 **include_deleted** | **bool**| If true, will also return details for deleted consignments | [optional] [default to false]

### Return type

[**ConsignmentV2BaseDomainEntityV2**](ConsignmentV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_get_recently_created_or_updated_consignments_get**
> ConsignmentsForListWithPendingConsignmentIdsGridDomainEntityV2 apiv2_consignments_get_recently_created_or_updated_consignments_get(company_id=company_id, from_date_utc=from_date_utc, to_date_utc=to_date_utc, start_index=start_index, retrieve_size=retrieve_size, carrier_id=carrier_id, include_child_companies=include_child_companies, get_notes=get_notes, get_reconciliation_data=get_reconciliation_data)

Return consignments for a company that have been created or updated within the timeframe specified

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
company_id = 56 # int | Optional - The company id for the consignments that are being queried (optional)
from_date_utc = '2013-10-20T19:20:30+01:00' # datetime | Required - This time period from which the consignment updates are to be queried from (optional)
to_date_utc = '2013-10-20T19:20:30+01:00' # datetime | Optional - This max time period which the consignment updates are to be queried from (optional)
start_index = 1 # int | Defaults to 1 - MachShip will return a maximum of 200 entries per request. Should there be more than 200 updated or created consignments  during the requested time period then you can utilise this index to obtain the next 200 entries by setting this to be 201. This can be  repeated until all updates have been obtained. (optional) (default to 1)
retrieve_size = 40 # int | This will be between 40 and 200 and will be the number of consignments returned in the request. If not provided the default returned will be 40. (optional) (default to 40)
carrier_id = 56 # int | Optional - If you wish to restrict the updates to a set carrier then you can set the id of that carrier in the request (optional)
include_child_companies = false # bool | if the query is desired to be made for an organisation that has multiple companies you can set this field to be true (optional) (default to false)
get_notes = false # bool | whether the query should return notes for the consignments or not (optional) (default to false)
get_reconciliation_data = false # bool | whether the query should return reconciliation data for the consignments or not (optional) (default to false)

try:
    # Return consignments for a company that have been created or updated within the timeframe specified
    api_response = api_instance.apiv2_consignments_get_recently_created_or_updated_consignments_get(company_id=company_id, from_date_utc=from_date_utc, to_date_utc=to_date_utc, start_index=start_index, retrieve_size=retrieve_size, carrier_id=carrier_id, include_child_companies=include_child_companies, get_notes=get_notes, get_reconciliation_data=get_reconciliation_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_get_recently_created_or_updated_consignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Optional - The company id for the consignments that are being queried | [optional] 
 **from_date_utc** | **datetime**| Required - This time period from which the consignment updates are to be queried from | [optional] 
 **to_date_utc** | **datetime**| Optional - This max time period which the consignment updates are to be queried from | [optional] 
 **start_index** | **int**| Defaults to 1 - MachShip will return a maximum of 200 entries per request. Should there be more than 200 updated or created consignments  during the requested time period then you can utilise this index to obtain the next 200 entries by setting this to be 201. This can be  repeated until all updates have been obtained. | [optional] [default to 1]
 **retrieve_size** | **int**| This will be between 40 and 200 and will be the number of consignments returned in the request. If not provided the default returned will be 40. | [optional] [default to 40]
 **carrier_id** | **int**| Optional - If you wish to restrict the updates to a set carrier then you can set the id of that carrier in the request | [optional] 
 **include_child_companies** | **bool**| if the query is desired to be made for an organisation that has multiple companies you can set this field to be true | [optional] [default to false]
 **get_notes** | **bool**| whether the query should return notes for the consignments or not | [optional] [default to false]
 **get_reconciliation_data** | **bool**| whether the query should return reconciliation data for the consignments or not | [optional] [default to false]

### Return type

[**ConsignmentsForListWithPendingConsignmentIdsGridDomainEntityV2**](ConsignmentsForListWithPendingConsignmentIdsGridDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_get_unmanifested_consignment_for_edit_get**
> EditConsignmentV2BaseDomainEntityV2 apiv2_consignments_get_unmanifested_consignment_for_edit_get(id=id)

Get an unmanifested consignment in the same format required to perform an update in the edit endpoint

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
id = 56 # int | The ID of the consignment in MachShip (optional)

try:
    # Get an unmanifested consignment in the same format required to perform an update in the edit endpoint
    api_response = api_instance.apiv2_consignments_get_unmanifested_consignment_for_edit_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_get_unmanifested_consignment_for_edit_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the consignment in MachShip | [optional] 

### Return type

[**EditConsignmentV2BaseDomainEntityV2**](EditConsignmentV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_get_unmanifested_get**
> UnmanifestedConsignmentForListGridDomainEntityV2 apiv2_consignments_get_unmanifested_get(company_id=company_id, start_index=start_index, retrieve_size=retrieve_size, carrier_id=carrier_id, include_child_companies=include_child_companies)

Get all consignments for a company that are in an \"unmanifested\" state

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
company_id = 56 # int | Optional - defaults to your company. Must be a valid company ID in MachShip (optional)
start_index = 1 # int | Defaults to 1. Can be used to \"page\" through subsequent requests (optional) (default to 1)
retrieve_size = 200 # int | The number of consignments to return. Defaults to 40, will return a maximum of 200 rows (optional) (default to 200)
carrier_id = 56 # int | Optional carrier ID to restrict consignments to those of this carrier (optional)
include_child_companies = false # bool | Whether to include companies that are \"children\" below companyId (optional) (default to false)

try:
    # Get all consignments for a company that are in an \"unmanifested\" state
    api_response = api_instance.apiv2_consignments_get_unmanifested_get(company_id=company_id, start_index=start_index, retrieve_size=retrieve_size, carrier_id=carrier_id, include_child_companies=include_child_companies)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_get_unmanifested_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Optional - defaults to your company. Must be a valid company ID in MachShip | [optional] 
 **start_index** | **int**| Defaults to 1. Can be used to \&quot;page\&quot; through subsequent requests | [optional] [default to 1]
 **retrieve_size** | **int**| The number of consignments to return. Defaults to 40, will return a maximum of 200 rows | [optional] [default to 200]
 **carrier_id** | **int**| Optional carrier ID to restrict consignments to those of this carrier | [optional] 
 **include_child_companies** | **bool**| Whether to include companies that are \&quot;children\&quot; below companyId | [optional] [default to false]

### Return type

[**UnmanifestedConsignmentForListGridDomainEntityV2**](UnmanifestedConsignmentForListGridDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_return_consignment_statuses_post**
> ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity apiv2_consignments_return_consignment_statuses_post(body=body, since_date_created_utc=since_date_created_utc)

Return all statuses recorded in the system with an option to specify a cutoff date to limit the statuses returned to ones saved in Machship  after a certain date. Maximum of 100 consignments

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IdsContainer() # IdsContainer | The list of Machship consignment IDs to return statuses for (optional)
since_date_created_utc = '2013-10-20T19:20:30+01:00' # datetime | The (optional) date/time in UTC to limit statuses by. If supplied only statuses recorded that are newer or equal to the date will be returned.             When not suplied all statuses for each consignment are returned (optional)

try:
    # Return all statuses recorded in the system with an option to specify a cutoff date to limit the statuses returned to ones saved in Machship  after a certain date. Maximum of 100 consignments
    api_response = api_instance.apiv2_consignments_return_consignment_statuses_post(body=body, since_date_created_utc=since_date_created_utc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_return_consignment_statuses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdsContainer**](IdsContainer.md)| The list of Machship consignment IDs to return statuses for | [optional] 
 **since_date_created_utc** | **datetime**| The (optional) date/time in UTC to limit statuses by. If supplied only statuses recorded that are newer or equal to the date will be returned.             When not suplied all statuses for each consignment are returned | [optional] 

### Return type

[**ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity**](ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_return_consignments_by_carrier_consignment_id_post**
> ConsignmentV2ICollectionBaseDomainEntityV2 apiv2_consignments_return_consignments_by_carrier_consignment_id_post(body=body)

Get Consignment Details for a multiple consignments using the Carrier Consignment ID as the lookup. Maximum of 10 consignments per request

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | The Carrier Consignment ids of the consignments. Maximum of 10 consignments per request (optional)

try:
    # Get Consignment Details for a multiple consignments using the Carrier Consignment ID as the lookup. Maximum of 10 consignments per request
    api_response = api_instance.apiv2_consignments_return_consignments_by_carrier_consignment_id_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_return_consignments_by_carrier_consignment_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The Carrier Consignment ids of the consignments. Maximum of 10 consignments per request | [optional] 

### Return type

[**ConsignmentV2ICollectionBaseDomainEntityV2**](ConsignmentV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_return_consignments_by_pending_consignment_ids_post**
> ConsignmentResponseV2ICollectionBaseDomainEntityV2 apiv2_consignments_return_consignments_by_pending_consignment_ids_post(body=body)

Get Consignment Details for multiple consignments using the Pending Consignment Id as the lookup. Maximum of 100 consignments.

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IdsContainer() # IdsContainer | List of Pending Consignment Ids from Pending Consignment. Maximum of 100 consignments per request. (optional)

try:
    # Get Consignment Details for multiple consignments using the Pending Consignment Id as the lookup. Maximum of 100 consignments.
    api_response = api_instance.apiv2_consignments_return_consignments_by_pending_consignment_ids_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_return_consignments_by_pending_consignment_ids_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdsContainer**](IdsContainer.md)| List of Pending Consignment Ids from Pending Consignment. Maximum of 100 consignments per request. | [optional] 

### Return type

[**ConsignmentResponseV2ICollectionBaseDomainEntityV2**](ConsignmentResponseV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_return_consignments_by_reference1_post**
> ConsignmentV2ICollectionBaseDomainEntityV2 apiv2_consignments_return_consignments_by_reference1_post(body=body)

Get Consignment Details for a multiple consignments using Reference 1 as the lookup. Maximum of 10 consignments per request

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | The Reference 1's of the consignments. Maximum of 10 consignments per request (optional)

try:
    # Get Consignment Details for a multiple consignments using Reference 1 as the lookup. Maximum of 10 consignments per request
    api_response = api_instance.apiv2_consignments_return_consignments_by_reference1_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_return_consignments_by_reference1_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The Reference 1&#x27;s of the consignments. Maximum of 10 consignments per request | [optional] 

### Return type

[**ConsignmentV2ICollectionBaseDomainEntityV2**](ConsignmentV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_return_consignments_by_reference2_post**
> ConsignmentV2ICollectionBaseDomainEntityV2 apiv2_consignments_return_consignments_by_reference2_post(body=body)

Get Consignment Details for a multiple consignments using Reference 2 as the lookup. Maximum of 10 consignments per request

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | The Reference 2's of the consignments. Maximum of 10 consignments per request (optional)

try:
    # Get Consignment Details for a multiple consignments using Reference 2 as the lookup. Maximum of 10 consignments per request
    api_response = api_instance.apiv2_consignments_return_consignments_by_reference2_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_return_consignments_by_reference2_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The Reference 2&#x27;s of the consignments. Maximum of 10 consignments per request | [optional] 

### Return type

[**ConsignmentV2ICollectionBaseDomainEntityV2**](ConsignmentV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_return_consignments_post**
> ConsignmentV2ICollectionBaseDomainEntityV2 apiv2_consignments_return_consignments_post(body=body)

Get Consignment Details for a multiple consignments. Maximum of 100 consignments per request

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IdsContainer() # IdsContainer | The Machship ids of the consignments. Maximum of 100 consignments per request (optional)

try:
    # Get Consignment Details for a multiple consignments. Maximum of 100 consignments per request
    api_response = api_instance.apiv2_consignments_return_consignments_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_return_consignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdsContainer**](IdsContainer.md)| The Machship ids of the consignments. Maximum of 100 consignments per request | [optional] 

### Return type

[**ConsignmentV2ICollectionBaseDomainEntityV2**](ConsignmentV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_search_consignments_post**
> ConsignmentV2ICollectionBaseDomainEntityV2 apiv2_consignments_search_consignments_post(body=body)

Get the details of related consignments based on the provided list of consignment or item references

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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | The list of references to use to search for the related consignments (optional)

try:
    # Get the details of related consignments based on the provided list of consignment or item references
    api_response = api_instance.apiv2_consignments_search_consignments_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_search_consignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The list of references to use to search for the related consignments | [optional] 

### Return type

[**ConsignmentV2ICollectionBaseDomainEntityV2**](ConsignmentV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consignments_update_consignment_statuses_post**
> EmptyDomainEntityV2 apiv2_consignments_update_consignment_statuses_post(body=body)



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
api_instance = swagger_client.ConsignmentsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.ManualTrackingStatus()] # list[ManualTrackingStatus] |  (optional)

try:
    api_response = api_instance.apiv2_consignments_update_consignment_statuses_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsignmentsApi->apiv2_consignments_update_consignment_statuses_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ManualTrackingStatus]**](ManualTrackingStatus.md)|  | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

