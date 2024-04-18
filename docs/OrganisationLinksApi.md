# swagger_client.OrganisationLinksApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_organisation_links_add_post**](OrganisationLinksApi.md#apiv2_organisation_links_add_post) | **POST** /apiv2/organisationLinks/add | Take the public key of an organisation and \&quot;link it into\&quot; an organisation you  are an administrator of. Doing this allows you to assign users from the other  organisation into companies in your organisation.
[**apiv2_organisation_links_get_for_organisation_get**](OrganisationLinksApi.md#apiv2_organisation_links_get_for_organisation_get) | **GET** /apiv2/organisationLinks/getForOrganisation | Returns all the links that exist for the organisation
[**apiv2_organisation_links_get_linked_from_organisations_get**](OrganisationLinksApi.md#apiv2_organisation_links_get_linked_from_organisations_get) | **GET** /apiv2/organisationLinks/getLinkedFromOrganisations | Returns all the from linked organisations that exist for the organisation
[**apiv2_organisation_links_get_linked_to_organisations_get**](OrganisationLinksApi.md#apiv2_organisation_links_get_linked_to_organisations_get) | **GET** /apiv2/organisationLinks/getLinkedToOrganisations | Returns all the to linked organisations that exist for the organisation
[**apiv2_organisation_links_get_organisation_details_by_public_key_get**](OrganisationLinksApi.md#apiv2_organisation_links_get_organisation_details_by_public_key_get) | **GET** /apiv2/organisationLinks/getOrganisationDetailsByPublicKey | Test a public key and, if it is correct, return details on which organisation it corresponds to
[**apiv2_organisation_links_get_public_key_for_organisation_get**](OrganisationLinksApi.md#apiv2_organisation_links_get_public_key_for_organisation_get) | **GET** /apiv2/organisationLinks/getPublicKeyForOrganisation | Return this organisation&#x27;s \&quot;public key\&quot; - which can be given to other organisations to link  the organisation \&quot;into\&quot; the other - meaning that users can be invited into the other organisation  to access their data.
[**apiv2_organisation_links_remove_post**](OrganisationLinksApi.md#apiv2_organisation_links_remove_post) | **POST** /apiv2/organisationLinks/remove | Remove an existing link between organisations. Note that doing this will remove access to the  \&quot;to\&quot; organisation from any users of the \&quot;from\&quot; organisation, and that this is irreversable.
[**apiv2_organisation_links_reset_public_key_for_organisation_get**](OrganisationLinksApi.md#apiv2_organisation_links_reset_public_key_for_organisation_get) | **GET** /apiv2/organisationLinks/resetPublicKeyForOrganisation | Resets the organisation&#x27;s public key. Note that this will not reset any organisation links set up  via the old public key.

# **apiv2_organisation_links_add_post**
> EmptyDomainEntityV2 apiv2_organisation_links_add_post(body=body)

Take the public key of an organisation and \"link it into\" an organisation you  are an administrator of. Doing this allows you to assign users from the other  organisation into companies in your organisation.

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
api_instance = swagger_client.OrganisationLinksApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrganisationLinkRequest() # OrganisationLinkRequest |  (optional)

try:
    # Take the public key of an organisation and \"link it into\" an organisation you  are an administrator of. Doing this allows you to assign users from the other  organisation into companies in your organisation.
    api_response = api_instance.apiv2_organisation_links_add_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationLinksApi->apiv2_organisation_links_add_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganisationLinkRequest**](OrganisationLinkRequest.md)|  | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_organisation_links_get_for_organisation_get**
> OrganisationLinkDetailICollectionBaseDomainEntityV2 apiv2_organisation_links_get_for_organisation_get(id=id)

Returns all the links that exist for the organisation

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
api_instance = swagger_client.OrganisationLinksApi(swagger_client.ApiClient(configuration))
id = 56 # int | Organisation Id. Leave blank to use your current organisation (optional)

try:
    # Returns all the links that exist for the organisation
    api_response = api_instance.apiv2_organisation_links_get_for_organisation_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationLinksApi->apiv2_organisation_links_get_for_organisation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Organisation Id. Leave blank to use your current organisation | [optional] 

### Return type

[**OrganisationLinkDetailICollectionBaseDomainEntityV2**](OrganisationLinkDetailICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_organisation_links_get_linked_from_organisations_get**
> OrganisationDetailsForGridGridDomainEntityV2 apiv2_organisation_links_get_linked_from_organisations_get(start_index=start_index, retrieve_size=retrieve_size, sort=sort, search_text=search_text)

Returns all the from linked organisations that exist for the organisation

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
api_instance = swagger_client.OrganisationLinksApi(swagger_client.ApiClient(configuration))
start_index = 56 # int |  (optional)
retrieve_size = 40 # int |  (optional) (default to 40)
sort = '' # str |  (optional)
search_text = '' # str |  (optional)

try:
    # Returns all the from linked organisations that exist for the organisation
    api_response = api_instance.apiv2_organisation_links_get_linked_from_organisations_get(start_index=start_index, retrieve_size=retrieve_size, sort=sort, search_text=search_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationLinksApi->apiv2_organisation_links_get_linked_from_organisations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**|  | [optional] 
 **retrieve_size** | **int**|  | [optional] [default to 40]
 **sort** | **str**|  | [optional] 
 **search_text** | **str**|  | [optional] 

### Return type

[**OrganisationDetailsForGridGridDomainEntityV2**](OrganisationDetailsForGridGridDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_organisation_links_get_linked_to_organisations_get**
> OrganisationDetailsForGridGridDomainEntityV2 apiv2_organisation_links_get_linked_to_organisations_get(start_index=start_index, retrieve_size=retrieve_size, sort=sort, search_text=search_text)

Returns all the to linked organisations that exist for the organisation

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
api_instance = swagger_client.OrganisationLinksApi(swagger_client.ApiClient(configuration))
start_index = 56 # int |  (optional)
retrieve_size = 40 # int |  (optional) (default to 40)
sort = '' # str |  (optional)
search_text = '' # str |  (optional)

try:
    # Returns all the to linked organisations that exist for the organisation
    api_response = api_instance.apiv2_organisation_links_get_linked_to_organisations_get(start_index=start_index, retrieve_size=retrieve_size, sort=sort, search_text=search_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationLinksApi->apiv2_organisation_links_get_linked_to_organisations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_index** | **int**|  | [optional] 
 **retrieve_size** | **int**|  | [optional] [default to 40]
 **sort** | **str**|  | [optional] 
 **search_text** | **str**|  | [optional] 

### Return type

[**OrganisationDetailsForGridGridDomainEntityV2**](OrganisationDetailsForGridGridDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_organisation_links_get_organisation_details_by_public_key_get**
> OrganisationDetailBaseDomainEntityV2 apiv2_organisation_links_get_organisation_details_by_public_key_get(public_key=public_key)

Test a public key and, if it is correct, return details on which organisation it corresponds to

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
api_instance = swagger_client.OrganisationLinksApi(swagger_client.ApiClient(configuration))
public_key = 'public_key_example' # str |  (optional)

try:
    # Test a public key and, if it is correct, return details on which organisation it corresponds to
    api_response = api_instance.apiv2_organisation_links_get_organisation_details_by_public_key_get(public_key=public_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationLinksApi->apiv2_organisation_links_get_organisation_details_by_public_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_key** | **str**|  | [optional] 

### Return type

[**OrganisationDetailBaseDomainEntityV2**](OrganisationDetailBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_organisation_links_get_public_key_for_organisation_get**
> StringBaseDomainEntityV2 apiv2_organisation_links_get_public_key_for_organisation_get(id=id)

Return this organisation's \"public key\" - which can be given to other organisations to link  the organisation \"into\" the other - meaning that users can be invited into the other organisation  to access their data.

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
api_instance = swagger_client.OrganisationLinksApi(swagger_client.ApiClient(configuration))
id = 56 # int | Id of the Organisation that you are requesting the public key for. Leave blank to use the organisation linked to the current user (optional)

try:
    # Return this organisation's \"public key\" - which can be given to other organisations to link  the organisation \"into\" the other - meaning that users can be invited into the other organisation  to access their data.
    api_response = api_instance.apiv2_organisation_links_get_public_key_for_organisation_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationLinksApi->apiv2_organisation_links_get_public_key_for_organisation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the Organisation that you are requesting the public key for. Leave blank to use the organisation linked to the current user | [optional] 

### Return type

[**StringBaseDomainEntityV2**](StringBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_organisation_links_remove_post**
> EmptyDomainEntityV2 apiv2_organisation_links_remove_post(body=body)

Remove an existing link between organisations. Note that doing this will remove access to the  \"to\" organisation from any users of the \"from\" organisation, and that this is irreversable.

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
api_instance = swagger_client.OrganisationLinksApi(swagger_client.ApiClient(configuration))
body = swagger_client.OrganisationUnlinkRequest() # OrganisationUnlinkRequest |  (optional)

try:
    # Remove an existing link between organisations. Note that doing this will remove access to the  \"to\" organisation from any users of the \"from\" organisation, and that this is irreversable.
    api_response = api_instance.apiv2_organisation_links_remove_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationLinksApi->apiv2_organisation_links_remove_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrganisationUnlinkRequest**](OrganisationUnlinkRequest.md)|  | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_organisation_links_reset_public_key_for_organisation_get**
> EmptyDomainEntityV2 apiv2_organisation_links_reset_public_key_for_organisation_get(id=id)

Resets the organisation's public key. Note that this will not reset any organisation links set up  via the old public key.

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
api_instance = swagger_client.OrganisationLinksApi(swagger_client.ApiClient(configuration))
id = 56 # int | Id of the Organisation that you are requesting to reset the public key for. Leave blank to use the organisation linked to the current user (optional)

try:
    # Resets the organisation's public key. Note that this will not reset any organisation links set up  via the old public key.
    api_response = api_instance.apiv2_organisation_links_reset_public_key_for_organisation_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganisationLinksApi->apiv2_organisation_links_reset_public_key_for_organisation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Id of the Organisation that you are requesting to reset the public key for. Leave blank to use the organisation linked to the current user | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

