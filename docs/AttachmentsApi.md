# swagger_client.AttachmentsApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_attachments_get_attachment_get**](AttachmentsApi.md#apiv2_attachments_get_attachment_get) | **GET** /apiv2/attachments/getAttachment | Downloads the raw Attachment file
[**apiv2_attachments_get_attachment_pod_report_get**](AttachmentsApi.md#apiv2_attachments_get_attachment_pod_report_get) | **GET** /apiv2/attachments/getAttachmentPodReport | Downloads the POD report which includes the attachment and details about the consignment
[**apiv2_attachments_get_attachments_by_consignment_ids_get**](AttachmentsApi.md#apiv2_attachments_get_attachments_by_consignment_ids_get) | **GET** /apiv2/attachments/getAttachmentsByConsignmentIds | Downloads attachments given a list of up to 40 consignments
[**apiv2_attachments_upload_attachments_post**](AttachmentsApi.md#apiv2_attachments_upload_attachments_post) | **POST** /apiv2/attachments/uploadAttachments | 

# **apiv2_attachments_get_attachment_get**
> apiv2_attachments_get_attachment_get(id=id)

Downloads the raw Attachment file

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
api_instance = swagger_client.AttachmentsApi(swagger_client.ApiClient(configuration))
id = 56 # int | The id of the attachment (optional)

try:
    # Downloads the raw Attachment file
    api_instance.apiv2_attachments_get_attachment_get(id=id)
except ApiException as e:
    print("Exception when calling AttachmentsApi->apiv2_attachments_get_attachment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the attachment | [optional] 

### Return type

void (empty response body)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_attachments_get_attachment_pod_report_get**
> apiv2_attachments_get_attachment_pod_report_get(id=id)

Downloads the POD report which includes the attachment and details about the consignment

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
api_instance = swagger_client.AttachmentsApi(swagger_client.ApiClient(configuration))
id = 56 # int | The id of the attachment (optional)

try:
    # Downloads the POD report which includes the attachment and details about the consignment
    api_instance.apiv2_attachments_get_attachment_pod_report_get(id=id)
except ApiException as e:
    print("Exception when calling AttachmentsApi->apiv2_attachments_get_attachment_pod_report_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the attachment | [optional] 

### Return type

void (empty response body)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_attachments_get_attachments_by_consignment_ids_get**
> apiv2_attachments_get_attachments_by_consignment_ids_get(ids=ids)

Downloads attachments given a list of up to 40 consignments

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
api_instance = swagger_client.AttachmentsApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | A list of Ids of the consignments. Note that the maximum number of consignments to query              at once is 40 and supplying any more than that will result in an error (optional)

try:
    # Downloads attachments given a list of up to 40 consignments
    api_instance.apiv2_attachments_get_attachments_by_consignment_ids_get(ids=ids)
except ApiException as e:
    print("Exception when calling AttachmentsApi->apiv2_attachments_get_attachments_by_consignment_ids_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| A list of Ids of the consignments. Note that the maximum number of consignments to query              at once is 40 and supplying any more than that will result in an error | [optional] 

### Return type

void (empty response body)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_attachments_upload_attachments_post**
> EmptyDomainEntityV2 apiv2_attachments_upload_attachments_post(body=body)



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
api_instance = swagger_client.AttachmentsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.Attachment()] # list[Attachment] |  (optional)

try:
    api_response = api_instance.apiv2_attachments_upload_attachments_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->apiv2_attachments_upload_attachments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Attachment]**](Attachment.md)|  | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

