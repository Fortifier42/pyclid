# swagger_client.LabelsV2Api

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_labels_group_consignments_for_printing_post**](LabelsV2Api.md#apiv2_labels_group_consignments_for_printing_post) | **POST** /apiv2/labels/groupConsignmentsForPrinting | 

# **apiv2_labels_group_consignments_for_printing_post**
> SendToPrinterModelBaseDomainEntityV2 apiv2_labels_group_consignments_for_printing_post(body=body)



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
api_instance = swagger_client.LabelsV2Api(swagger_client.ApiClient(configuration))
body = [56] # list[int] |  (optional)

try:
    api_response = api_instance.apiv2_labels_group_consignments_for_printing_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsV2Api->apiv2_labels_group_consignments_for_printing_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[int]**](int.md)|  | [optional] 

### Return type

[**SendToPrinterModelBaseDomainEntityV2**](SendToPrinterModelBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

