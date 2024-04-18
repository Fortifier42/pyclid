# swagger_client.RoutesApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_routes_returnmultipleroutes_post**](RoutesApi.md#apiv2_routes_returnmultipleroutes_post) | **POST** /apiv2/routes/returnmultipleroutes | Returns a list of available routes corresponding to supplied the route requests
[**apiv2_routes_returnroutes_post**](RoutesApi.md#apiv2_routes_returnroutes_post) | **POST** /apiv2/routes/returnroutes | Returns a list of available routes corresponding to supplied the route request
[**apiv2_routes_returnrouteswithcomplexitems_post**](RoutesApi.md#apiv2_routes_returnrouteswithcomplexitems_post) | **POST** /apiv2/routes/returnrouteswithcomplexitems | Returns a list of available routes corresponding to supplied the route request

# **apiv2_routes_returnmultipleroutes_post**
> RoutesResponseV2ArrayBaseDomainEntityV2 apiv2_routes_returnmultipleroutes_post(body=body)

Returns a list of available routes corresponding to supplied the route requests

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
api_instance = swagger_client.RoutesApi(swagger_client.ApiClient(configuration))
body = [swagger_client.RouteRequestV2()] # list[RouteRequestV2] | Detailed information for the request, including the items and from and to locations (optional)

try:
    # Returns a list of available routes corresponding to supplied the route requests
    api_response = api_instance.apiv2_routes_returnmultipleroutes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->apiv2_routes_returnmultipleroutes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[RouteRequestV2]**](RouteRequestV2.md)| Detailed information for the request, including the items and from and to locations | [optional] 

### Return type

[**RoutesResponseV2ArrayBaseDomainEntityV2**](RoutesResponseV2ArrayBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_routes_returnroutes_post**
> RoutesResponseV2BaseDomainEntityV2 apiv2_routes_returnroutes_post(body=body)

Returns a list of available routes corresponding to supplied the route request

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
api_instance = swagger_client.RoutesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RouteRequestV2() # RouteRequestV2 | Detailed information for the request, including the items and from and to locations (optional)

try:
    # Returns a list of available routes corresponding to supplied the route request
    api_response = api_instance.apiv2_routes_returnroutes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->apiv2_routes_returnroutes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RouteRequestV2**](RouteRequestV2.md)| Detailed information for the request, including the items and from and to locations | [optional] 

### Return type

[**RoutesResponseV2BaseDomainEntityV2**](RoutesResponseV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_routes_returnrouteswithcomplexitems_post**
> RoutesResponseV2BaseDomainEntityV2 apiv2_routes_returnrouteswithcomplexitems_post(body=body)

Returns a list of available routes corresponding to supplied the route request

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
api_instance = swagger_client.RoutesApi(swagger_client.ApiClient(configuration))
body = swagger_client.RouteRequestComplexItemsV2() # RouteRequestComplexItemsV2 | Detailed information for the request, including the items and from and to locations (optional)

try:
    # Returns a list of available routes corresponding to supplied the route request
    api_response = api_instance.apiv2_routes_returnrouteswithcomplexitems_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutesApi->apiv2_routes_returnrouteswithcomplexitems_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RouteRequestComplexItemsV2**](RouteRequestComplexItemsV2.md)| Detailed information for the request, including the items and from and to locations | [optional] 

### Return type

[**RoutesResponseV2BaseDomainEntityV2**](RoutesResponseV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

