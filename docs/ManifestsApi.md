# swagger_client.ManifestsApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_manifests_get_all_get**](ManifestsApi.md#apiv2_manifests_get_all_get) | **GET** /apiv2/manifests/getAll | Get a list of (up to 200) manifests for a company.
[**apiv2_manifests_group_all_unmanifested_consignments_for_manifest_post**](ManifestsApi.md#apiv2_manifests_group_all_unmanifested_consignments_for_manifest_post) | **POST** /apiv2/manifests/groupAllUnmanifestedConsignmentsForManifest | Groups all unmanifested consignments for a company into manifests.
[**apiv2_manifests_group_consignments_for_manifest_post**](ManifestsApi.md#apiv2_manifests_group_consignments_for_manifest_post) | **POST** /apiv2/manifests/groupConsignmentsForManifest | Groups a set of consignments into manifests.
[**apiv2_manifests_manifest_post**](ManifestsApi.md#apiv2_manifests_manifest_post) | **POST** /apiv2/manifests/manifest | 

# **apiv2_manifests_get_all_get**
> ManifestForListWithConsignmentsGridDomainEntityV2 apiv2_manifests_get_all_get(company_id=company_id, start_index=start_index, retrieve_size=retrieve_size, carrier_id=carrier_id, include_child_companies=include_child_companies, start_date=start_date, end_date=end_date)

Get a list of (up to 200) manifests for a company.

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
api_instance = swagger_client.ManifestsApi(swagger_client.ApiClient(configuration))
company_id = 56 # int | Optional - defaults to your company. Must be a valid company ID in MachShip (optional)
start_index = 1 # int | Defaults to 1. Can be used to \"page\" through subsequent requests (optional) (default to 1)
retrieve_size = 40 # int | The number of manifests to return. Defaults to 40, will return a maximum of 200 rows (optional) (default to 40)
carrier_id = 56 # int | Optional to limit the results to manifests for that carrier (optional)
include_child_companies = false # bool | Whether to include companies that are \"children\" below companyId (optional) (default to false)
start_date = '2013-10-20T19:20:30+01:00' # datetime | Start Date which is compared against the manifest's creation date (all date times are local to the pickup location) (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | End Date which is compared against the manifest's creation date (all date times are local to the pickup location) (optional)

try:
    # Get a list of (up to 200) manifests for a company.
    api_response = api_instance.apiv2_manifests_get_all_get(company_id=company_id, start_index=start_index, retrieve_size=retrieve_size, carrier_id=carrier_id, include_child_companies=include_child_companies, start_date=start_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestsApi->apiv2_manifests_get_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| Optional - defaults to your company. Must be a valid company ID in MachShip | [optional] 
 **start_index** | **int**| Defaults to 1. Can be used to \&quot;page\&quot; through subsequent requests | [optional] [default to 1]
 **retrieve_size** | **int**| The number of manifests to return. Defaults to 40, will return a maximum of 200 rows | [optional] [default to 40]
 **carrier_id** | **int**| Optional to limit the results to manifests for that carrier | [optional] 
 **include_child_companies** | **bool**| Whether to include companies that are \&quot;children\&quot; below companyId | [optional] [default to false]
 **start_date** | **datetime**| Start Date which is compared against the manifest&#x27;s creation date (all date times are local to the pickup location) | [optional] 
 **end_date** | **datetime**| End Date which is compared against the manifest&#x27;s creation date (all date times are local to the pickup location) | [optional] 

### Return type

[**ManifestForListWithConsignmentsGridDomainEntityV2**](ManifestForListWithConsignmentsGridDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_manifests_group_all_unmanifested_consignments_for_manifest_post**
> BookedManifestV2ICollectionBaseDomainEntityV2 apiv2_manifests_group_all_unmanifested_consignments_for_manifest_post(body=body)

Groups all unmanifested consignments for a company into manifests.

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
api_instance = swagger_client.ManifestsApi(swagger_client.ApiClient(configuration))
body = 56 # int | Machship's company Id (optional)

try:
    # Groups all unmanifested consignments for a company into manifests.
    api_response = api_instance.apiv2_manifests_group_all_unmanifested_consignments_for_manifest_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestsApi->apiv2_manifests_group_all_unmanifested_consignments_for_manifest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**int**](int.md)| Machship&#x27;s company Id | [optional] 

### Return type

[**BookedManifestV2ICollectionBaseDomainEntityV2**](BookedManifestV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_manifests_group_consignments_for_manifest_post**
> BookedManifestV2ICollectionBaseDomainEntityV2 apiv2_manifests_group_consignments_for_manifest_post(body=body)

Groups a set of consignments into manifests.

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
api_instance = swagger_client.ManifestsApi(swagger_client.ApiClient(configuration))
body = [56] # list[int] |  (optional)

try:
    # Groups a set of consignments into manifests.
    api_response = api_instance.apiv2_manifests_group_consignments_for_manifest_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestsApi->apiv2_manifests_group_consignments_for_manifest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | [optional] 

### Return type

[**BookedManifestV2ICollectionBaseDomainEntityV2**](BookedManifestV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_manifests_manifest_post**
> ReturnBookedManifestV2ICollectionBaseDomainEntityV2 apiv2_manifests_manifest_post(body=body)



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
api_instance = swagger_client.ManifestsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.BookedManifestV2()] # list[BookedManifestV2] |  (optional)

try:
    api_response = api_instance.apiv2_manifests_manifest_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ManifestsApi->apiv2_manifests_manifest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[BookedManifestV2]**](BookedManifestV2.md)|  | [optional] 

### Return type

[**ReturnBookedManifestV2ICollectionBaseDomainEntityV2**](ReturnBookedManifestV2ICollectionBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

