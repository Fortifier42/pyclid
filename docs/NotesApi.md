# swagger_client.NotesApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_notes_get_notes_for_consignment_get**](NotesApi.md#apiv2_notes_get_notes_for_consignment_get) | **GET** /apiv2/notes/getNotesForConsignment | 

# **apiv2_notes_get_notes_for_consignment_get**
> NoteModelV2IEnumerableBaseDomainEntityV2 apiv2_notes_get_notes_for_consignment_get(id=id)



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
api_instance = swagger_client.NotesApi(swagger_client.ApiClient(configuration))
id = 56 # int |  (optional)

try:
    api_response = api_instance.apiv2_notes_get_notes_for_consignment_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->apiv2_notes_get_notes_for_consignment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 

### Return type

[**NoteModelV2IEnumerableBaseDomainEntityV2**](NoteModelV2IEnumerableBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

