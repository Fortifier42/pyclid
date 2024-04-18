# swagger_client.LocationsApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_locations_get_locations_with_search_options_get**](LocationsApi.md#apiv2_locations_get_locations_with_search_options_get) | **GET** /apiv2/locations/getLocationsWithSearchOptions | Returns the top 10 locations where the suburb or postcode match the search string
[**apiv2_locations_return_locations_post**](LocationsApi.md#apiv2_locations_return_locations_post) | **POST** /apiv2/locations/returnLocations | Returns all locations that exactly match the supplied suburb and postcode combination. Multiple locations can be provided
[**apiv2_locations_return_locations_with_search_options_post**](LocationsApi.md#apiv2_locations_return_locations_with_search_options_post) | **POST** /apiv2/locations/returnLocationsWithSearchOptions | 

# **apiv2_locations_get_locations_with_search_options_get**
> LocationV2IEnumerableBaseDomainEntityV2 apiv2_locations_get_locations_with_search_options_get(body=body, s=s)

Returns the top 10 locations where the suburb or postcode match the search string

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
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LocationSearchOptionsV2() # LocationSearchOptionsV2 | The options for getting locations (optional)
s = 's_example' # str | Search string with space separated search terms. Eg. \"Mel 3000\" will return any locations that match \"Mel\" AND \"3000\" (optional)

try:
    # Returns the top 10 locations where the suburb or postcode match the search string
    api_response = api_instance.apiv2_locations_get_locations_with_search_options_get(body=body, s=s)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->apiv2_locations_get_locations_with_search_options_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationSearchOptionsV2**](LocationSearchOptionsV2.md)| The options for getting locations | [optional] 
 **s** | **str**| Search string with space separated search terms. Eg. \&quot;Mel 3000\&quot; will return any locations that match \&quot;Mel\&quot; AND \&quot;3000\&quot; | [optional] 

### Return type

[**LocationV2IEnumerableBaseDomainEntityV2**](LocationV2IEnumerableBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_locations_return_locations_post**
> LocationV2ICollectionBaseDomainEntityV2 apiv2_locations_return_locations_post(body=body)

Returns all locations that exactly match the supplied suburb and postcode combination. Multiple locations can be provided

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
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.RawLocationsWithLocationSearchOptions() # RawLocationsWithLocationSearchOptions | A list of suburb and postcode combinations accompanied by the options to consider when searching locations (optional)

try:
    # Returns all locations that exactly match the supplied suburb and postcode combination. Multiple locations can be provided
    api_response = api_instance.apiv2_locations_return_locations_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->apiv2_locations_return_locations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RawLocationsWithLocationSearchOptions**](RawLocationsWithLocationSearchOptions.md)| A list of suburb and postcode combinations accompanied by the options to consider when searching locations | [optional] 

### Return type

[**LocationV2ICollectionBaseDomainEntityV2**](LocationV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_locations_return_locations_with_search_options_post**
> LocationV2IEnumerableBaseDomainEntityV2 apiv2_locations_return_locations_with_search_options_post(body=body, s=s)



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
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LocationSearchOptionsV2() # LocationSearchOptionsV2 |  (optional)
s = 's_example' # str |  (optional)

try:
    api_response = api_instance.apiv2_locations_return_locations_with_search_options_post(body=body, s=s)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->apiv2_locations_return_locations_with_search_options_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationSearchOptionsV2**](LocationSearchOptionsV2.md)|  | [optional] 
 **s** | **str**|  | [optional] 

### Return type

[**LocationV2IEnumerableBaseDomainEntityV2**](LocationV2IEnumerableBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

