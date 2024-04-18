# swagger_client.CompanyItemsApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_items_create_complex_post**](CompanyItemsApi.md#apiv2_items_create_complex_post) | **POST** /apiv2/items/createComplex | 
[**apiv2_items_delete_delete**](CompanyItemsApi.md#apiv2_items_delete_delete) | **DELETE** /apiv2/items/delete | 
[**apiv2_items_get_all_complex_get**](CompanyItemsApi.md#apiv2_items_get_all_complex_get) | **GET** /apiv2/items/getAllComplex | Returns a list of items for a given company. By default, it will return the top 200 items. If you have more than 200, you will need to enter a different startIndex. Eg. 201, 401, etc. Returns all items as complex items
[**apiv2_items_get_all_get**](CompanyItemsApi.md#apiv2_items_get_all_get) | **GET** /apiv2/items/getAll | Returns a list of items for a given company. By default, it will return the top 200 items. If you have more than 200, you will need to enter a different startIndex. Eg. 201, 401, etc. This only returns standard items
[**apiv2_items_get_by_sku_complex_get**](CompanyItemsApi.md#apiv2_items_get_by_sku_complex_get) | **GET** /apiv2/items/getBySkuComplex | Returns a saved item that has the matching Sku. Returns complex items
[**apiv2_items_get_by_sku_get**](CompanyItemsApi.md#apiv2_items_get_by_sku_get) | **GET** /apiv2/items/getBySku | Returns a saved item that has the matching Sku. This only returns simple items
[**apiv2_items_get_complex_get**](CompanyItemsApi.md#apiv2_items_get_complex_get) | **GET** /apiv2/items/getComplex | Returns a saved complex item with all its dimensions
[**apiv2_items_get_get**](CompanyItemsApi.md#apiv2_items_get_get) | **GET** /apiv2/items/get | Returns a saved item with all its dimensions

# **apiv2_items_create_complex_post**
> Int32BaseDomainEntityV2 apiv2_items_create_complex_post(body=body, company_id=company_id)



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
api_instance = swagger_client.CompanyItemsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyItemComplexV2() # CompanyItemComplexV2 |  (optional)
company_id = 56 # int |  (optional)

try:
    api_response = api_instance.apiv2_items_create_complex_post(body=body, company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyItemsApi->apiv2_items_create_complex_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyItemComplexV2**](CompanyItemComplexV2.md)|  | [optional] 
 **company_id** | **int**|  | [optional] 

### Return type

[**Int32BaseDomainEntityV2**](Int32BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_items_delete_delete**
> EmptyDomainEntityV2 apiv2_items_delete_delete(company_item_id=company_item_id)



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
api_instance = swagger_client.CompanyItemsApi(swagger_client.ApiClient(configuration))
company_item_id = 56 # int |  (optional)

try:
    api_response = api_instance.apiv2_items_delete_delete(company_item_id=company_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyItemsApi->apiv2_items_delete_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_item_id** | **int**|  | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_items_get_all_complex_get**
> CompanyItemComplexV2GridDomainEntityV2 apiv2_items_get_all_complex_get(company_id=company_id, start_index=start_index, retrieve_size=retrieve_size)

Returns a list of items for a given company. By default, it will return the top 200 items. If you have more than 200, you will need to enter a different startIndex. Eg. 201, 401, etc. Returns all items as complex items

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
api_instance = swagger_client.CompanyItemsApi(swagger_client.ApiClient(configuration))
company_id = 56 # int | The company whose items you want want to get (optional)
start_index = 1 # int | The start Index of the get (Optional. By default this is 1) (optional) (default to 1)
retrieve_size = 200 # int | The number of results to retrieve (Optional. Max number is 200) (optional) (default to 200)

try:
    # Returns a list of items for a given company. By default, it will return the top 200 items. If you have more than 200, you will need to enter a different startIndex. Eg. 201, 401, etc. Returns all items as complex items
    api_response = api_instance.apiv2_items_get_all_complex_get(company_id=company_id, start_index=start_index, retrieve_size=retrieve_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyItemsApi->apiv2_items_get_all_complex_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The company whose items you want want to get | [optional] 
 **start_index** | **int**| The start Index of the get (Optional. By default this is 1) | [optional] [default to 1]
 **retrieve_size** | **int**| The number of results to retrieve (Optional. Max number is 200) | [optional] [default to 200]

### Return type

[**CompanyItemComplexV2GridDomainEntityV2**](CompanyItemComplexV2GridDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_items_get_all_get**
> CompanyItemV2GridDomainEntityV2 apiv2_items_get_all_get(company_id=company_id, start_index=start_index, retrieve_size=retrieve_size)

Returns a list of items for a given company. By default, it will return the top 200 items. If you have more than 200, you will need to enter a different startIndex. Eg. 201, 401, etc. This only returns standard items

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
api_instance = swagger_client.CompanyItemsApi(swagger_client.ApiClient(configuration))
company_id = 56 # int | The company whose items you want want to get (optional)
start_index = 1 # int | The start Index of the get (Optional. By default this is 1) (optional) (default to 1)
retrieve_size = 200 # int | The number of results to retrieve (Optional. Max number is 200) (optional) (default to 200)

try:
    # Returns a list of items for a given company. By default, it will return the top 200 items. If you have more than 200, you will need to enter a different startIndex. Eg. 201, 401, etc. This only returns standard items
    api_response = api_instance.apiv2_items_get_all_get(company_id=company_id, start_index=start_index, retrieve_size=retrieve_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyItemsApi->apiv2_items_get_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The company whose items you want want to get | [optional] 
 **start_index** | **int**| The start Index of the get (Optional. By default this is 1) | [optional] [default to 1]
 **retrieve_size** | **int**| The number of results to retrieve (Optional. Max number is 200) | [optional] [default to 200]

### Return type

[**CompanyItemV2GridDomainEntityV2**](CompanyItemV2GridDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_items_get_by_sku_complex_get**
> CompanyItemComplexV2BaseDomainEntityV2 apiv2_items_get_by_sku_complex_get(company_id=company_id, sku=sku)

Returns a saved item that has the matching Sku. Returns complex items

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
api_instance = swagger_client.CompanyItemsApi(swagger_client.ApiClient(configuration))
company_id = 56 # int |  (optional)
sku = 'sku_example' # str |  (optional)

try:
    # Returns a saved item that has the matching Sku. Returns complex items
    api_response = api_instance.apiv2_items_get_by_sku_complex_get(company_id=company_id, sku=sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyItemsApi->apiv2_items_get_by_sku_complex_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**|  | [optional] 
 **sku** | **str**|  | [optional] 

### Return type

[**CompanyItemComplexV2BaseDomainEntityV2**](CompanyItemComplexV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_items_get_by_sku_get**
> CompanyItemV2BaseDomainEntityV2 apiv2_items_get_by_sku_get(company_id=company_id, sku=sku)

Returns a saved item that has the matching Sku. This only returns simple items

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
api_instance = swagger_client.CompanyItemsApi(swagger_client.ApiClient(configuration))
company_id = 56 # int |  (optional)
sku = 'sku_example' # str |  (optional)

try:
    # Returns a saved item that has the matching Sku. This only returns simple items
    api_response = api_instance.apiv2_items_get_by_sku_get(company_id=company_id, sku=sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyItemsApi->apiv2_items_get_by_sku_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**|  | [optional] 
 **sku** | **str**|  | [optional] 

### Return type

[**CompanyItemV2BaseDomainEntityV2**](CompanyItemV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_items_get_complex_get**
> CompanyItemComplexV2BaseDomainEntityV2 apiv2_items_get_complex_get(id=id)

Returns a saved complex item with all its dimensions

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
api_instance = swagger_client.CompanyItemsApi(swagger_client.ApiClient(configuration))
id = 56 # int | The Machship Id of the saved item (optional)

try:
    # Returns a saved complex item with all its dimensions
    api_response = api_instance.apiv2_items_get_complex_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyItemsApi->apiv2_items_get_complex_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Machship Id of the saved item | [optional] 

### Return type

[**CompanyItemComplexV2BaseDomainEntityV2**](CompanyItemComplexV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_items_get_get**
> CompanyItemV2BaseDomainEntityV2 apiv2_items_get_get(id=id)

Returns a saved item with all its dimensions

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
api_instance = swagger_client.CompanyItemsApi(swagger_client.ApiClient(configuration))
id = 56 # int | The Machship Id of the saved item (optional)

try:
    # Returns a saved item with all its dimensions
    api_response = api_instance.apiv2_items_get_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyItemsApi->apiv2_items_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The Machship Id of the saved item | [optional] 

### Return type

[**CompanyItemV2BaseDomainEntityV2**](CompanyItemV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

