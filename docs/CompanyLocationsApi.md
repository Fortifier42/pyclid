# swagger_client.CompanyLocationsApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_company_locations_add_permanent_pickups_to_company_location_post**](CompanyLocationsApi.md#apiv2_company_locations_add_permanent_pickups_to_company_location_post) | **POST** /apiv2/companyLocations/addPermanentPickupsToCompanyLocation | 
[**apiv2_company_locations_create_post**](CompanyLocationsApi.md#apiv2_company_locations_create_post) | **POST** /apiv2/companyLocations/create | Create a new company location against a company
[**apiv2_company_locations_edit_post**](CompanyLocationsApi.md#apiv2_company_locations_edit_post) | **POST** /apiv2/companyLocations/edit | Edit a company location
[**apiv2_company_locations_get_all_get**](CompanyLocationsApi.md#apiv2_company_locations_get_all_get) | **GET** /apiv2/companyLocations/getAll | 
[**apiv2_company_locations_get_get**](CompanyLocationsApi.md#apiv2_company_locations_get_get) | **GET** /apiv2/companyLocations/get | 
[**apiv2_company_locations_get_permanent_pickups_for_company_location_get**](CompanyLocationsApi.md#apiv2_company_locations_get_permanent_pickups_for_company_location_get) | **GET** /apiv2/companyLocations/getPermanentPickupsForCompanyLocation | 

# **apiv2_company_locations_add_permanent_pickups_to_company_location_post**
> EmptyDomainEntityV2 apiv2_company_locations_add_permanent_pickups_to_company_location_post(body=body)



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
api_instance = swagger_client.CompanyLocationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyLocationV2PermanentPickups() # CompanyLocationV2PermanentPickups |  (optional)

try:
    api_response = api_instance.apiv2_company_locations_add_permanent_pickups_to_company_location_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLocationsApi->apiv2_company_locations_add_permanent_pickups_to_company_location_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyLocationV2PermanentPickups**](CompanyLocationV2PermanentPickups.md)|  | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_company_locations_create_post**
> Int32BaseDomainEntityV2 apiv2_company_locations_create_post(body=body)

Create a new company location against a company

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
api_instance = swagger_client.CompanyLocationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyLocationV2() # CompanyLocationV2 |  (optional)

try:
    # Create a new company location against a company
    api_response = api_instance.apiv2_company_locations_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLocationsApi->apiv2_company_locations_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyLocationV2**](CompanyLocationV2.md)|  | [optional] 

### Return type

[**Int32BaseDomainEntityV2**](Int32BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_company_locations_edit_post**
> EmptyDomainEntityV2 apiv2_company_locations_edit_post(body=body)

Edit a company location

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
api_instance = swagger_client.CompanyLocationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CompanyLocationV2() # CompanyLocationV2 |  (optional)

try:
    # Edit a company location
    api_response = api_instance.apiv2_company_locations_edit_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLocationsApi->apiv2_company_locations_edit_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CompanyLocationV2**](CompanyLocationV2.md)|  | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_company_locations_get_all_get**
> CompanyLocationV2GridDomainEntityV2 apiv2_company_locations_get_all_get(company_id=company_id)



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
api_instance = swagger_client.CompanyLocationsApi(swagger_client.ApiClient(configuration))
company_id = 56 # int |  (optional)

try:
    api_response = api_instance.apiv2_company_locations_get_all_get(company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLocationsApi->apiv2_company_locations_get_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**|  | [optional] 

### Return type

[**CompanyLocationV2GridDomainEntityV2**](CompanyLocationV2GridDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_company_locations_get_get**
> CompanyLocationV2BaseDomainEntityV2 apiv2_company_locations_get_get(id=id)



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
api_instance = swagger_client.CompanyLocationsApi(swagger_client.ApiClient(configuration))
id = 56 # int |  (optional)

try:
    api_response = api_instance.apiv2_company_locations_get_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLocationsApi->apiv2_company_locations_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 

### Return type

[**CompanyLocationV2BaseDomainEntityV2**](CompanyLocationV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_company_locations_get_permanent_pickups_for_company_location_get**
> CompanyLocationV2PermanentPickupsBaseDomainEntityV2 apiv2_company_locations_get_permanent_pickups_for_company_location_get(company_location_id=company_location_id)



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
api_instance = swagger_client.CompanyLocationsApi(swagger_client.ApiClient(configuration))
company_location_id = 56 # int |  (optional)

try:
    api_response = api_instance.apiv2_company_locations_get_permanent_pickups_for_company_location_get(company_location_id=company_location_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyLocationsApi->apiv2_company_locations_get_permanent_pickups_for_company_location_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_location_id** | **int**|  | [optional] 

### Return type

[**CompanyLocationV2PermanentPickupsBaseDomainEntityV2**](CompanyLocationV2PermanentPickupsBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

