# swagger_client.LabelsApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_labels_get_commercial_invoice_pdf_get**](LabelsApi.md#apiv2_labels_get_commercial_invoice_pdf_get) | **GET** /apiv2/labels/getCommercialInvoicePdf | 
[**apiv2_labels_get_consignment_pdf_file_info_get**](LabelsApi.md#apiv2_labels_get_consignment_pdf_file_info_get) | **GET** /apiv2/labels/getConsignmentPdfFileInfo | 
[**apiv2_labels_get_consignment_pdf_get**](LabelsApi.md#apiv2_labels_get_consignment_pdf_get) | **GET** /apiv2/labels/getConsignmentPdf | 
[**apiv2_labels_get_dangerous_goods_document_pdf_file_info_get**](LabelsApi.md#apiv2_labels_get_dangerous_goods_document_pdf_file_info_get) | **GET** /apiv2/labels/getDangerousGoodsDocumentPdfFileInfo | 
[**apiv2_labels_get_dangerous_goods_document_pdf_get**](LabelsApi.md#apiv2_labels_get_dangerous_goods_document_pdf_get) | **GET** /apiv2/labels/getDangerousGoodsDocumentPdf | 
[**apiv2_labels_get_item_pdf_file_info_get**](LabelsApi.md#apiv2_labels_get_item_pdf_file_info_get) | **GET** /apiv2/labels/getItemPdfFileInfo | 
[**apiv2_labels_get_item_pdf_get**](LabelsApi.md#apiv2_labels_get_item_pdf_get) | **GET** /apiv2/labels/getItemPdf | 
[**apiv2_labels_get_item_pdfs_for_consignments_get**](LabelsApi.md#apiv2_labels_get_item_pdfs_for_consignments_get) | **GET** /apiv2/labels/getItemPdfsForConsignments | Gets item labels as a zip for up to 40 consignments
[**apiv2_labels_get_manifest_pdf_by_consignment_id_get**](LabelsApi.md#apiv2_labels_get_manifest_pdf_by_consignment_id_get) | **GET** /apiv2/labels/getManifestPdfByConsignmentId | 
[**apiv2_labels_get_manifest_pdf_file_info_get**](LabelsApi.md#apiv2_labels_get_manifest_pdf_file_info_get) | **GET** /apiv2/labels/getManifestPdfFileInfo | 
[**apiv2_labels_get_manifest_pdf_get**](LabelsApi.md#apiv2_labels_get_manifest_pdf_get) | **GET** /apiv2/labels/getManifestPdf | 
[**apiv2_labels_get_mo41_document_pdf_file_info_get**](LabelsApi.md#apiv2_labels_get_mo41_document_pdf_file_info_get) | **GET** /apiv2/labels/getMO41DocumentPdfFileInfo | 
[**apiv2_labels_get_mo41_document_pdf_get**](LabelsApi.md#apiv2_labels_get_mo41_document_pdf_get) | **GET** /apiv2/labels/getMO41DocumentPdf | 
[**apiv2_labels_get_special_instructions_pdf_get**](LabelsApi.md#apiv2_labels_get_special_instructions_pdf_get) | **GET** /apiv2/labels/getSpecialInstructionsPdf | 
[**apiv2_labels_return_item_pdfs_for_consignments_post**](LabelsApi.md#apiv2_labels_return_item_pdfs_for_consignments_post) | **POST** /apiv2/labels/returnItemPdfsForConsignments | Returns item labels as a zip for up to 40 consignments
[**apiv2_labels_send_labels_to_printer_post**](LabelsApi.md#apiv2_labels_send_labels_to_printer_post) | **POST** /apiv2/labels/sendLabelsToPrinter | 

# **apiv2_labels_get_commercial_invoice_pdf_get**
> apiv2_labels_get_commercial_invoice_pdf_get(consignment_id=consignment_id)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
consignment_id = 56 # int |  (optional)

try:
    api_instance.apiv2_labels_get_commercial_invoice_pdf_get(consignment_id=consignment_id)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_commercial_invoice_pdf_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_get_consignment_pdf_file_info_get**
> FileInfoBaseDomainEntityV2 apiv2_labels_get_consignment_pdf_file_info_get(consignment_id=consignment_id)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
consignment_id = 56 # int |  (optional)

try:
    api_response = api_instance.apiv2_labels_get_consignment_pdf_file_info_get(consignment_id=consignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_consignment_pdf_file_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **int**|  | [optional] 

### Return type

[**FileInfoBaseDomainEntityV2**](FileInfoBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_get_consignment_pdf_get**
> apiv2_labels_get_consignment_pdf_get(consignment_id=consignment_id)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
consignment_id = 56 # int |  (optional)

try:
    api_instance.apiv2_labels_get_consignment_pdf_get(consignment_id=consignment_id)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_consignment_pdf_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_get_dangerous_goods_document_pdf_file_info_get**
> FileInfoBaseDomainEntityV2 apiv2_labels_get_dangerous_goods_document_pdf_file_info_get(consignment_id=consignment_id)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
consignment_id = 56 # int |  (optional)

try:
    api_response = api_instance.apiv2_labels_get_dangerous_goods_document_pdf_file_info_get(consignment_id=consignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_dangerous_goods_document_pdf_file_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **int**|  | [optional] 

### Return type

[**FileInfoBaseDomainEntityV2**](FileInfoBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_get_dangerous_goods_document_pdf_get**
> apiv2_labels_get_dangerous_goods_document_pdf_get(consignment_id=consignment_id)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
consignment_id = 56 # int |  (optional)

try:
    api_instance.apiv2_labels_get_dangerous_goods_document_pdf_get(consignment_id=consignment_id)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_dangerous_goods_document_pdf_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_get_item_pdf_file_info_get**
> FileInfoBaseDomainEntityV2 apiv2_labels_get_item_pdf_file_info_get(consignment_id=consignment_id, print_a4=print_a4)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
consignment_id = 56 # int |  (optional)
print_a4 = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.apiv2_labels_get_item_pdf_file_info_get(consignment_id=consignment_id, print_a4=print_a4)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_item_pdf_file_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **int**|  | [optional] 
 **print_a4** | **bool**|  | [optional] [default to false]

### Return type

[**FileInfoBaseDomainEntityV2**](FileInfoBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_get_item_pdf_get**
> apiv2_labels_get_item_pdf_get(consignment_id=consignment_id, print_a4=print_a4)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
consignment_id = 56 # int |  (optional)
print_a4 = false # bool |  (optional) (default to false)

try:
    api_instance.apiv2_labels_get_item_pdf_get(consignment_id=consignment_id, print_a4=print_a4)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_item_pdf_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **int**|  | [optional] 
 **print_a4** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_get_item_pdfs_for_consignments_get**
> apiv2_labels_get_item_pdfs_for_consignments_get(consignment_ids=consignment_ids, print_a4=print_a4, single_pdf=single_pdf)

Gets item labels as a zip for up to 40 consignments

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
consignment_ids = [56] # list[int] |  (optional)
print_a4 = true # bool |  (optional)
single_pdf = false # bool |  (optional) (default to false)

try:
    # Gets item labels as a zip for up to 40 consignments
    api_instance.apiv2_labels_get_item_pdfs_for_consignments_get(consignment_ids=consignment_ids, print_a4=print_a4, single_pdf=single_pdf)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_item_pdfs_for_consignments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_ids** | [**list[int]**](int.md)|  | [optional] 
 **print_a4** | **bool**|  | [optional] 
 **single_pdf** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_get_manifest_pdf_by_consignment_id_get**
> apiv2_labels_get_manifest_pdf_by_consignment_id_get(consignment_id=consignment_id)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
consignment_id = 56 # int |  (optional)

try:
    api_instance.apiv2_labels_get_manifest_pdf_by_consignment_id_get(consignment_id=consignment_id)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_manifest_pdf_by_consignment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_get_manifest_pdf_file_info_get**
> FileInfoBaseDomainEntityV2 apiv2_labels_get_manifest_pdf_file_info_get(manifest_id=manifest_id)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
manifest_id = 56 # int |  (optional)

try:
    api_response = api_instance.apiv2_labels_get_manifest_pdf_file_info_get(manifest_id=manifest_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_manifest_pdf_file_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_id** | **int**|  | [optional] 

### Return type

[**FileInfoBaseDomainEntityV2**](FileInfoBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_get_manifest_pdf_get**
> apiv2_labels_get_manifest_pdf_get(manifest_id=manifest_id)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
manifest_id = 56 # int |  (optional)

try:
    api_instance.apiv2_labels_get_manifest_pdf_get(manifest_id=manifest_id)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_manifest_pdf_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manifest_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_get_mo41_document_pdf_file_info_get**
> FileInfoBaseDomainEntityV2 apiv2_labels_get_mo41_document_pdf_file_info_get(consignment_id=consignment_id)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
consignment_id = 56 # int |  (optional)

try:
    api_response = api_instance.apiv2_labels_get_mo41_document_pdf_file_info_get(consignment_id=consignment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_mo41_document_pdf_file_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **int**|  | [optional] 

### Return type

[**FileInfoBaseDomainEntityV2**](FileInfoBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_get_mo41_document_pdf_get**
> apiv2_labels_get_mo41_document_pdf_get(consignment_id=consignment_id)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
consignment_id = 56 # int |  (optional)

try:
    api_instance.apiv2_labels_get_mo41_document_pdf_get(consignment_id=consignment_id)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_mo41_document_pdf_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_get_special_instructions_pdf_get**
> apiv2_labels_get_special_instructions_pdf_get(consignment_id=consignment_id, print_a4=print_a4)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
consignment_id = 56 # int |  (optional)
print_a4 = false # bool |  (optional) (default to false)

try:
    api_instance.apiv2_labels_get_special_instructions_pdf_get(consignment_id=consignment_id, print_a4=print_a4)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_get_special_instructions_pdf_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consignment_id** | **int**|  | [optional] 
 **print_a4** | **bool**|  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_return_item_pdfs_for_consignments_post**
> apiv2_labels_return_item_pdfs_for_consignments_post(body=body)

Returns item labels as a zip for up to 40 consignments

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ItemLabelRequest() # ItemLabelRequest |  (optional)

try:
    # Returns item labels as a zip for up to 40 consignments
    api_instance.apiv2_labels_return_item_pdfs_for_consignments_post(body=body)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_return_item_pdfs_for_consignments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemLabelRequest**](ItemLabelRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_labels_send_labels_to_printer_post**
> EmptyDomainEntityV2 apiv2_labels_send_labels_to_printer_post(body=body)



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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
body = [swagger_client.SendToPrinterRequest()] # list[SendToPrinterRequest] |  (optional)

try:
    api_response = api_instance.apiv2_labels_send_labels_to_printer_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->apiv2_labels_send_labels_to_printer_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[SendToPrinterRequest]**](SendToPrinterRequest.md)|  | [optional] 

### Return type

[**EmptyDomainEntityV2**](EmptyDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

