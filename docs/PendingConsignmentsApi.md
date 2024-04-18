# swagger_client.PendingConsignmentsApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_pending_consignments_create_pending_consignment_post**](PendingConsignmentsApi.md#apiv2_pending_consignments_create_pending_consignment_post) | **POST** /apiv2/pendingConsignments/createPendingConsignment | Creates a pending consignment in Machship
[**apiv2_pending_consignments_delete_pending_consignments_post**](PendingConsignmentsApi.md#apiv2_pending_consignments_delete_pending_consignments_post) | **POST** /apiv2/pendingConsignments/deletePendingConsignments | Deletes the specified Pending Consignments in Machship
[**apiv2_pending_consignments_get_pending_consignment_get**](PendingConsignmentsApi.md#apiv2_pending_consignments_get_pending_consignment_get) | **GET** /apiv2/pendingConsignments/getPendingConsignment | Get Pending Consignment Details for a single pending consignment
[**apiv2_pending_consignments_get_recently_created_or_updated_pending_consignments_get**](PendingConsignmentsApi.md#apiv2_pending_consignments_get_recently_created_or_updated_pending_consignments_get) | **GET** /apiv2/pendingConsignments/getRecentlyCreatedOrUpdatedPendingConsignments | 
[**apiv2_pending_consignments_return_pending_consignments_by_reference1_post**](PendingConsignmentsApi.md#apiv2_pending_consignments_return_pending_consignments_by_reference1_post) | **POST** /apiv2/pendingConsignments/returnPendingConsignmentsByReference1 | Get Pending Consignment Details for multiple pending consignments using Reference 1 as the lookup. Maximum of 10 per request
[**apiv2_pending_consignments_return_pending_consignments_by_reference2_post**](PendingConsignmentsApi.md#apiv2_pending_consignments_return_pending_consignments_by_reference2_post) | **POST** /apiv2/pendingConsignments/returnPendingConsignmentsByReference2 | Get Pending Consignment Details for multiple pending consignments using Reference 2 as the lookup. Maximum of 10 per request
[**apiv2_pending_consignments_return_pending_consignments_post**](PendingConsignmentsApi.md#apiv2_pending_consignments_return_pending_consignments_post) | **POST** /apiv2/pendingConsignments/returnPendingConsignments | Get Pending Consignment Details for multiple pending consignments. Maximum of 10 per request

# **apiv2_pending_consignments_create_pending_consignment_post**
> CreatePendingConsignmentResponseBaseDomainEntityV2 apiv2_pending_consignments_create_pending_consignment_post(body=body)

Creates a pending consignment in Machship

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
api_instance = swagger_client.PendingConsignmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreatePendingConsignmentV2() # CreatePendingConsignmentV2 | Details of the pending consignment to create (optional)

try:
    # Creates a pending consignment in Machship
    api_response = api_instance.apiv2_pending_consignments_create_pending_consignment_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PendingConsignmentsApi->apiv2_pending_consignments_create_pending_consignment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePendingConsignmentV2**](CreatePendingConsignmentV2.md)| Details of the pending consignment to create | [optional] 

### Return type

[**CreatePendingConsignmentResponseBaseDomainEntityV2**](CreatePendingConsignmentResponseBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_pending_consignments_delete_pending_consignments_post**
> EmptyDomainEntityV2 apiv2_pending_consignments_delete_pending_consignments_post(body=body)

Deletes the specified Pending Consignments in Machship

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
api_instance = swagger_client.PendingConsignmentsApi(swagger_client.ApiClient(configuration))
body = [56] # list[int] | Ids of the pending consignments to be deleted (optional)

try:
    # Deletes the specified Pending Consignments in Machship
    api_response = api_instance.apiv2_pending_consignments_delete_pending_consignments_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PendingConsignmentsApi->apiv2_pending_consignments_delete_pending_consignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)| Ids of the pending consignments to be deleted | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_pending_consignments_get_pending_consignment_get**
> PendingConsignmentV2BaseDomainEntityV2 apiv2_pending_consignments_get_pending_consignment_get(id=id)

Get Pending Consignment Details for a single pending consignment

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
api_instance = swagger_client.PendingConsignmentsApi(swagger_client.ApiClient(configuration))
id = 56 # int |  (optional)

try:
    # Get Pending Consignment Details for a single pending consignment
    api_response = api_instance.apiv2_pending_consignments_get_pending_consignment_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PendingConsignmentsApi->apiv2_pending_consignments_get_pending_consignment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 

### Return type

[**PendingConsignmentV2BaseDomainEntityV2**](PendingConsignmentV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_pending_consignments_get_recently_created_or_updated_pending_consignments_get**
> PendingConsignmentV2ForListGridDomainEntityV2 apiv2_pending_consignments_get_recently_created_or_updated_pending_consignments_get(company_id=company_id, from_date_utc=from_date_utc, to_date_utc=to_date_utc, start_index=start_index, retrieve_size=retrieve_size, carrier_id=carrier_id, include_child_companies=include_child_companies, get_deleted=get_deleted)



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
api_instance = swagger_client.PendingConsignmentsApi(swagger_client.ApiClient(configuration))
company_id = 56 # int |  (optional)
from_date_utc = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to_date_utc = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
start_index = 1 # int |  (optional) (default to 1)
retrieve_size = 40 # int |  (optional) (default to 40)
carrier_id = 56 # int |  (optional)
include_child_companies = false # bool |  (optional) (default to false)
get_deleted = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.apiv2_pending_consignments_get_recently_created_or_updated_pending_consignments_get(company_id=company_id, from_date_utc=from_date_utc, to_date_utc=to_date_utc, start_index=start_index, retrieve_size=retrieve_size, carrier_id=carrier_id, include_child_companies=include_child_companies, get_deleted=get_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PendingConsignmentsApi->apiv2_pending_consignments_get_recently_created_or_updated_pending_consignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**|  | [optional] 
 **from_date_utc** | **datetime**|  | [optional] 
 **to_date_utc** | **datetime**|  | [optional] 
 **start_index** | **int**|  | [optional] [default to 1]
 **retrieve_size** | **int**|  | [optional] [default to 40]
 **carrier_id** | **int**|  | [optional] 
 **include_child_companies** | **bool**|  | [optional] [default to false]
 **get_deleted** | **bool**|  | [optional] [default to false]

### Return type

[**PendingConsignmentV2ForListGridDomainEntityV2**](PendingConsignmentV2ForListGridDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_pending_consignments_return_pending_consignments_by_reference1_post**
> PendingConsignmentV2ICollectionBaseDomainEntityV2 apiv2_pending_consignments_return_pending_consignments_by_reference1_post(body=body)

Get Pending Consignment Details for multiple pending consignments using Reference 1 as the lookup. Maximum of 10 per request

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
api_instance = swagger_client.PendingConsignmentsApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | The Reference 1's of the pending consignments. Maximum of 10 consignments per request (optional)

try:
    # Get Pending Consignment Details for multiple pending consignments using Reference 1 as the lookup. Maximum of 10 per request
    api_response = api_instance.apiv2_pending_consignments_return_pending_consignments_by_reference1_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PendingConsignmentsApi->apiv2_pending_consignments_return_pending_consignments_by_reference1_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The Reference 1&#x27;s of the pending consignments. Maximum of 10 consignments per request | [optional] 

### Return type

[**PendingConsignmentV2ICollectionBaseDomainEntityV2**](PendingConsignmentV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_pending_consignments_return_pending_consignments_by_reference2_post**
> PendingConsignmentV2ICollectionBaseDomainEntityV2 apiv2_pending_consignments_return_pending_consignments_by_reference2_post(body=body)

Get Pending Consignment Details for multiple pending consignments using Reference 2 as the lookup. Maximum of 10 per request

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
api_instance = swagger_client.PendingConsignmentsApi(swagger_client.ApiClient(configuration))
body = ['body_example'] # list[str] | The Reference 2's of the pending consignments. Maximum of 10 consignments per request (optional)

try:
    # Get Pending Consignment Details for multiple pending consignments using Reference 2 as the lookup. Maximum of 10 per request
    api_response = api_instance.apiv2_pending_consignments_return_pending_consignments_by_reference2_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PendingConsignmentsApi->apiv2_pending_consignments_return_pending_consignments_by_reference2_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)| The Reference 2&#x27;s of the pending consignments. Maximum of 10 consignments per request | [optional] 

### Return type

[**PendingConsignmentV2ICollectionBaseDomainEntityV2**](PendingConsignmentV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_pending_consignments_return_pending_consignments_post**
> PendingConsignmentV2ICollectionBaseDomainEntityV2 apiv2_pending_consignments_return_pending_consignments_post(body=body)

Get Pending Consignment Details for multiple pending consignments. Maximum of 10 per request

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
api_instance = swagger_client.PendingConsignmentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IdsContainer() # IdsContainer | The Machship ids of the pending consignments. Maximum of 10 per request (optional)

try:
    # Get Pending Consignment Details for multiple pending consignments. Maximum of 10 per request
    api_response = api_instance.apiv2_pending_consignments_return_pending_consignments_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PendingConsignmentsApi->apiv2_pending_consignments_return_pending_consignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdsContainer**](IdsContainer.md)| The Machship ids of the pending consignments. Maximum of 10 per request | [optional] 

### Return type

[**PendingConsignmentV2ICollectionBaseDomainEntityV2**](PendingConsignmentV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

