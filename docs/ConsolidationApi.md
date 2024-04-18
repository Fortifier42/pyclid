# swagger_client.ConsolidationApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_consolidation_group_and_perform_consolidation_post**](ConsolidationApi.md#apiv2_consolidation_group_and_perform_consolidation_post) | **POST** /apiv2/consolidation/groupAndPerformConsolidation | Do both the grouping into auto consolidation as well as the routing and updating of consolidated consignments
[**apiv2_consolidation_group_consignments_for_consolidation_post**](ConsolidationApi.md#apiv2_consolidation_group_consignments_for_consolidation_post) | **POST** /apiv2/consolidation/groupConsignmentsForConsolidation | Perform automatic grouping on unmanifested and / or pending consignments/orders
[**apiv2_consolidation_perform_consolidation_post**](ConsolidationApi.md#apiv2_consolidation_perform_consolidation_post) | **POST** /apiv2/consolidation/performConsolidation | Consolidate consignments from other consignments / pending consignments/orders into a combined  unmanifested consignment

# **apiv2_consolidation_group_and_perform_consolidation_post**
> ConsolidationResultsBaseDomainEntityV2 apiv2_consolidation_group_and_perform_consolidation_post(body=body)

Do both the grouping into auto consolidation as well as the routing and updating of consolidated consignments

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
api_instance = swagger_client.ConsolidationApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConsolidationOptions() # ConsolidationOptions |  (optional)

try:
    # Do both the grouping into auto consolidation as well as the routing and updating of consolidated consignments
    api_response = api_instance.apiv2_consolidation_group_and_perform_consolidation_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsolidationApi->apiv2_consolidation_group_and_perform_consolidation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConsolidationOptions**](ConsolidationOptions.md)|  | [optional] 

### Return type

[**ConsolidationResultsBaseDomainEntityV2**](ConsolidationResultsBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consolidation_group_consignments_for_consolidation_post**
> ConsolidationResultsBaseDomainEntityV2 apiv2_consolidation_group_consignments_for_consolidation_post(body=body)

Perform automatic grouping on unmanifested and / or pending consignments/orders

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
api_instance = swagger_client.ConsolidationApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConsolidationOptions() # ConsolidationOptions |  (optional)

try:
    # Perform automatic grouping on unmanifested and / or pending consignments/orders
    api_response = api_instance.apiv2_consolidation_group_consignments_for_consolidation_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsolidationApi->apiv2_consolidation_group_consignments_for_consolidation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConsolidationOptions**](ConsolidationOptions.md)|  | [optional] 

### Return type

[**ConsolidationResultsBaseDomainEntityV2**](ConsolidationResultsBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_consolidation_perform_consolidation_post**
> ConsolidationResultsBaseDomainEntityV2 apiv2_consolidation_perform_consolidation_post(body=body)

Consolidate consignments from other consignments / pending consignments/orders into a combined  unmanifested consignment

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
api_instance = swagger_client.ConsolidationApi(swagger_client.ApiClient(configuration))
body = swagger_client.ConsolidationRequest() # ConsolidationRequest |  (optional)

try:
    # Consolidate consignments from other consignments / pending consignments/orders into a combined  unmanifested consignment
    api_response = api_instance.apiv2_consolidation_perform_consolidation_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsolidationApi->apiv2_consolidation_perform_consolidation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConsolidationRequest**](ConsolidationRequest.md)|  | [optional] 

### Return type

[**ConsolidationResultsBaseDomainEntityV2**](ConsolidationResultsBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

