# swagger_client.IdentityProvidersApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_identityproviders_get**](IdentityProvidersApi.md#apiv2_identityproviders_get) | **GET** /apiv2/identityproviders | 
[**apiv2_identityproviders_get_identity_providers_for_company_get**](IdentityProvidersApi.md#apiv2_identityproviders_get_identity_providers_for_company_get) | **GET** /apiv2/identityproviders/GetIdentityProvidersForCompany | 
[**apiv2_identityproviders_get_identity_providers_for_logged_user_get**](IdentityProvidersApi.md#apiv2_identityproviders_get_identity_providers_for_logged_user_get) | **GET** /apiv2/identityproviders/GetIdentityProvidersForLoggedUser | Returns all the identity providers for your current organisation
[**apiv2_identityproviders_get_identity_providers_for_organisation_get**](IdentityProvidersApi.md#apiv2_identityproviders_get_identity_providers_for_organisation_get) | **GET** /apiv2/identityproviders/GetIdentityProvidersForOrganisation | Returns all the identity providers for the specified organisation

# **apiv2_identityproviders_get**
> IdentityProviderV2BaseDomainEntityV2 apiv2_identityproviders_get(identity_provider_id=identity_provider_id)



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
api_instance = swagger_client.IdentityProvidersApi(swagger_client.ApiClient(configuration))
identity_provider_id = 56 # int |  (optional)

try:
    api_response = api_instance.apiv2_identityproviders_get(identity_provider_id=identity_provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProvidersApi->apiv2_identityproviders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identity_provider_id** | **int**|  | [optional] 

### Return type

[**IdentityProviderV2BaseDomainEntityV2**](IdentityProviderV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_identityproviders_get_identity_providers_for_company_get**
> IdentityProviderV2ICollectionBaseDomainEntityV2 apiv2_identityproviders_get_identity_providers_for_company_get(company_id=company_id)



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
api_instance = swagger_client.IdentityProvidersApi(swagger_client.ApiClient(configuration))
company_id = 56 # int |  (optional)

try:
    api_response = api_instance.apiv2_identityproviders_get_identity_providers_for_company_get(company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProvidersApi->apiv2_identityproviders_get_identity_providers_for_company_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**|  | [optional] 

### Return type

[**IdentityProviderV2ICollectionBaseDomainEntityV2**](IdentityProviderV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_identityproviders_get_identity_providers_for_logged_user_get**
> IdentityProviderV2ICollectionBaseDomainEntityV2 apiv2_identityproviders_get_identity_providers_for_logged_user_get()

Returns all the identity providers for your current organisation

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
api_instance = swagger_client.IdentityProvidersApi(swagger_client.ApiClient(configuration))

try:
    # Returns all the identity providers for your current organisation
    api_response = api_instance.apiv2_identityproviders_get_identity_providers_for_logged_user_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProvidersApi->apiv2_identityproviders_get_identity_providers_for_logged_user_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdentityProviderV2ICollectionBaseDomainEntityV2**](IdentityProviderV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_identityproviders_get_identity_providers_for_organisation_get**
> IdentityProviderV2ICollectionBaseDomainEntityV2 apiv2_identityproviders_get_identity_providers_for_organisation_get(organisation_id=organisation_id)

Returns all the identity providers for the specified organisation

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
api_instance = swagger_client.IdentityProvidersApi(swagger_client.ApiClient(configuration))
organisation_id = 56 # int | Id of the Organisation that you are requesting. Leave blank to use the organisation linked to the current user (optional)

try:
    # Returns all the identity providers for the specified organisation
    api_response = api_instance.apiv2_identityproviders_get_identity_providers_for_organisation_get(organisation_id=organisation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentityProvidersApi->apiv2_identityproviders_get_identity_providers_for_organisation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **int**| Id of the Organisation that you are requesting. Leave blank to use the organisation linked to the current user | [optional] 

### Return type

[**IdentityProviderV2ICollectionBaseDomainEntityV2**](IdentityProviderV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

