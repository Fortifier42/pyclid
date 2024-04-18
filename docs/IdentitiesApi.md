# swagger_client.IdentitiesApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_identities_create_identities_post**](IdentitiesApi.md#apiv2_identities_create_identities_post) | **POST** /apiv2/identities/createIdentities | Create Identities in MachShip and assign companies and roles to identities to give them access to the system. Note that all identities provided must belong to the same identityProvider and organisation    You must be an administrator of the organisation in question to be able to access  this endpoint.
[**apiv2_identities_disable_identities_post**](IdentitiesApi.md#apiv2_identities_disable_identities_post) | **POST** /apiv2/identities/disableIdentities | 
[**apiv2_identities_get_identities_get**](IdentitiesApi.md#apiv2_identities_get_identities_get) | **GET** /apiv2/identities/getIdentities | Get all identities owned by an organisation, along with details on which company they are  linked to. You must be an administrator of the organisation in question to be able to access  this endpoint.
[**apiv2_identities_link_identities_to_companies_post**](IdentitiesApi.md#apiv2_identities_link_identities_to_companies_post) | **POST** /apiv2/identities/linkIdentitiesToCompanies | Assign companies and roles to identities to give them access to the system.    You must be an administrator of the organisation in question to be able to access  this endpoint.
[**apiv2_identities_reenable_identities_post**](IdentitiesApi.md#apiv2_identities_reenable_identities_post) | **POST** /apiv2/identities/reenableIdentities | 
[**apiv2_identities_return_identity_public_keys_post**](IdentitiesApi.md#apiv2_identities_return_identity_public_keys_post) | **POST** /apiv2/identities/returnIdentityPublicKeys | Get the \&quot;public keys\&quot; of the supplied identities that can be used by another organisation  (that has been linked to the organisation owning the identity) to give that identity  access to a company in their organisation.    You must be an administrator of the organisation in question to be able to access  this endpoint.
[**apiv2_identities_unlink_identities_from_companies_post**](IdentitiesApi.md#apiv2_identities_unlink_identities_from_companies_post) | **POST** /apiv2/identities/unlinkIdentitiesFromCompanies | 

# **apiv2_identities_create_identities_post**
> EmptyDomainEntityV2 apiv2_identities_create_identities_post(body=body)

Create Identities in MachShip and assign companies and roles to identities to give them access to the system. Note that all identities provided must belong to the same identityProvider and organisation    You must be an administrator of the organisation in question to be able to access  this endpoint.

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
api_instance = swagger_client.IdentitiesApi(swagger_client.ApiClient(configuration))
body = [swagger_client.CreateIdentityV2()] # list[CreateIdentityV2] | The identities to create (optional)

try:
    # Create Identities in MachShip and assign companies and roles to identities to give them access to the system. Note that all identities provided must belong to the same identityProvider and organisation    You must be an administrator of the organisation in question to be able to access  this endpoint.
    api_response = api_instance.apiv2_identities_create_identities_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentitiesApi->apiv2_identities_create_identities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[CreateIdentityV2]**](CreateIdentityV2.md)| The identities to create | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_identities_disable_identities_post**
> EmptyDomainEntityV2 apiv2_identities_disable_identities_post(body=body)



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
api_instance = swagger_client.IdentitiesApi(swagger_client.ApiClient(configuration))
body = [56] # list[int] |  (optional)

try:
    api_response = api_instance.apiv2_identities_disable_identities_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentitiesApi->apiv2_identities_disable_identities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_identities_get_identities_get**
> IdentityV2ICollectionBaseDomainEntityV2 apiv2_identities_get_identities_get(organisation_id=organisation_id, only_unlinked_identities=only_unlinked_identities, identity_provider_id=identity_provider_id)

Get all identities owned by an organisation, along with details on which company they are  linked to. You must be an administrator of the organisation in question to be able to access  this endpoint.

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
api_instance = swagger_client.IdentitiesApi(swagger_client.ApiClient(configuration))
organisation_id = 56 # int | Optional. The ID in MachShip of the organisation.  Only relevant if you are an administrator of more than one organisation in MachShip. If omitted, your current organisation will be returned (optional)
only_unlinked_identities = false # bool | Optional - whether or not to filter the results to identities that have not been linked to  any companies in the system (optional) (default to false)
identity_provider_id = 56 # int | Optional - whether or not to filter by identities who are authenticated by a certain identity. If not provided, all identities will be returned  provider (optional)

try:
    # Get all identities owned by an organisation, along with details on which company they are  linked to. You must be an administrator of the organisation in question to be able to access  this endpoint.
    api_response = api_instance.apiv2_identities_get_identities_get(organisation_id=organisation_id, only_unlinked_identities=only_unlinked_identities, identity_provider_id=identity_provider_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentitiesApi->apiv2_identities_get_identities_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **int**| Optional. The ID in MachShip of the organisation.  Only relevant if you are an administrator of more than one organisation in MachShip. If omitted, your current organisation will be returned | [optional] 
 **only_unlinked_identities** | **bool**| Optional - whether or not to filter the results to identities that have not been linked to  any companies in the system | [optional] [default to false]
 **identity_provider_id** | **int**| Optional - whether or not to filter by identities who are authenticated by a certain identity. If not provided, all identities will be returned  provider | [optional] 

### Return type

[**IdentityV2ICollectionBaseDomainEntityV2**](IdentityV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_identities_link_identities_to_companies_post**
> EmptyDomainEntityV2 apiv2_identities_link_identities_to_companies_post(body=body)

Assign companies and roles to identities to give them access to the system.    You must be an administrator of the organisation in question to be able to access  this endpoint.

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
api_instance = swagger_client.IdentitiesApi(swagger_client.ApiClient(configuration))
body = swagger_client.IdentityCompanyLinkSetterRequestObject() # IdentityCompanyLinkSetterRequestObject | One or more identities to provision access for (optional)

try:
    # Assign companies and roles to identities to give them access to the system.    You must be an administrator of the organisation in question to be able to access  this endpoint.
    api_response = api_instance.apiv2_identities_link_identities_to_companies_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentitiesApi->apiv2_identities_link_identities_to_companies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdentityCompanyLinkSetterRequestObject**](IdentityCompanyLinkSetterRequestObject.md)| One or more identities to provision access for | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_identities_reenable_identities_post**
> EmptyDomainEntityV2 apiv2_identities_reenable_identities_post(body=body)



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
api_instance = swagger_client.IdentitiesApi(swagger_client.ApiClient(configuration))
body = [56] # list[int] |  (optional)

try:
    api_response = api_instance.apiv2_identities_reenable_identities_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentitiesApi->apiv2_identities_reenable_identities_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_identities_return_identity_public_keys_post**
> IdentityPublicKeyV2ICollectionBaseDomainEntityV2 apiv2_identities_return_identity_public_keys_post(body=body)

Get the \"public keys\" of the supplied identities that can be used by another organisation  (that has been linked to the organisation owning the identity) to give that identity  access to a company in their organisation.    You must be an administrator of the organisation in question to be able to access  this endpoint.

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
api_instance = swagger_client.IdentitiesApi(swagger_client.ApiClient(configuration))
body = [56] # list[int] | The IDs in MachShip of the identities (optional)

try:
    # Get the \"public keys\" of the supplied identities that can be used by another organisation  (that has been linked to the organisation owning the identity) to give that identity  access to a company in their organisation.    You must be an administrator of the organisation in question to be able to access  this endpoint.
    api_response = api_instance.apiv2_identities_return_identity_public_keys_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentitiesApi->apiv2_identities_return_identity_public_keys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)| The IDs in MachShip of the identities | [optional] 

### Return type

[**IdentityPublicKeyV2ICollectionBaseDomainEntityV2**](IdentityPublicKeyV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_identities_unlink_identities_from_companies_post**
> EmptyDomainEntityV2 apiv2_identities_unlink_identities_from_companies_post(body=body)



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
api_instance = swagger_client.IdentitiesApi(swagger_client.ApiClient(configuration))
body = [swagger_client.IdentityCompanyUnsetter()] # list[IdentityCompanyUnsetter] |  (optional)

try:
    api_response = api_instance.apiv2_identities_unlink_identities_from_companies_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdentitiesApi->apiv2_identities_unlink_identities_from_companies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[IdentityCompanyUnsetter]**](IdentityCompanyUnsetter.md)|  | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

