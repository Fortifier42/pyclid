# swagger_client.AuthenticateApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_authenticate_ping_post**](AuthenticateApi.md#apiv2_authenticate_ping_post) | **POST** /apiv2/authenticate/ping | Determine whether a user is logged in and get any session properties required by the front end

# **apiv2_authenticate_ping_post**
> BooleanBaseDomainEntityV2 apiv2_authenticate_ping_post()

Determine whether a user is logged in and get any session properties required by the front end

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
api_instance = swagger_client.AuthenticateApi(swagger_client.ApiClient(configuration))

try:
    # Determine whether a user is logged in and get any session properties required by the front end
    api_response = api_instance.apiv2_authenticate_ping_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticateApi->apiv2_authenticate_ping_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BooleanBaseDomainEntityV2**](BooleanBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

