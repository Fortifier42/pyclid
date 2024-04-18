# swagger_client.RolesApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_identities_get_available_roles_get**](RolesApi.md#apiv2_identities_get_available_roles_get) | **GET** /apiv2/identities/getAvailableRoles | Get all roles that are available to assign users of a certain company

# **apiv2_identities_get_available_roles_get**
> RoleV2ICollectionBaseDomainEntityV2 apiv2_identities_get_available_roles_get(company_id=company_id)

Get all roles that are available to assign users of a certain company

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
company_id = 56 # int | The ID of a company in MachShip (optional)

try:
    # Get all roles that are available to assign users of a certain company
    api_response = api_instance.apiv2_identities_get_available_roles_get(company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->apiv2_identities_get_available_roles_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The ID of a company in MachShip | [optional] 

### Return type

[**RoleV2ICollectionBaseDomainEntityV2**](RoleV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

