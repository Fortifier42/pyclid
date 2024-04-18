# swagger_client.QuotesApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_quotes_create_quote_post**](QuotesApi.md#apiv2_quotes_create_quote_post) | **POST** /apiv2/quotes/createQuote | Creates a quote in Machship
[**apiv2_quotes_create_quote_with_complex_items_post**](QuotesApi.md#apiv2_quotes_create_quote_with_complex_items_post) | **POST** /apiv2/quotes/createQuoteWithComplexItems | Creates a quote in Machship
[**apiv2_quotes_get_all_get**](QuotesApi.md#apiv2_quotes_get_all_get) | **GET** /apiv2/quotes/getAll | Get All quotes for the given company
[**apiv2_quotes_get_quote_get**](QuotesApi.md#apiv2_quotes_get_quote_get) | **GET** /apiv2/quotes/getQuote | Get Quote Details for a single quote

# **apiv2_quotes_create_quote_post**
> CreateQuoteResponseV2BaseDomainEntityV2 apiv2_quotes_create_quote_post(body=body)

Creates a quote in Machship

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateQuoteV2() # CreateQuoteV2 | Details of the quote to create (optional)

try:
    # Creates a quote in Machship
    api_response = api_instance.apiv2_quotes_create_quote_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->apiv2_quotes_create_quote_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateQuoteV2**](CreateQuoteV2.md)| Details of the quote to create | [optional] 

### Return type

[**CreateQuoteResponseV2BaseDomainEntityV2**](CreateQuoteResponseV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_quotes_create_quote_with_complex_items_post**
> CreateQuoteResponseV2BaseDomainEntityV2 apiv2_quotes_create_quote_with_complex_items_post(body=body)

Creates a quote in Machship

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateQuoteComplexItemsV2() # CreateQuoteComplexItemsV2 | Details of the quote to create (optional)

try:
    # Creates a quote in Machship
    api_response = api_instance.apiv2_quotes_create_quote_with_complex_items_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->apiv2_quotes_create_quote_with_complex_items_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateQuoteComplexItemsV2**](CreateQuoteComplexItemsV2.md)| Details of the quote to create | [optional] 

### Return type

[**CreateQuoteResponseV2BaseDomainEntityV2**](CreateQuoteResponseV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_quotes_get_all_get**
> QuoteForListGridDomainEntityV2 apiv2_quotes_get_all_get(company_id=company_id)

Get All quotes for the given company

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
company_id = 56 # int | The selected company's id (optional)

try:
    # Get All quotes for the given company
    api_response = api_instance.apiv2_quotes_get_all_get(company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->apiv2_quotes_get_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The selected company&#x27;s id | [optional] 

### Return type

[**QuoteForListGridDomainEntityV2**](QuoteForListGridDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_quotes_get_quote_get**
> QuoteV2BaseDomainEntityV2 apiv2_quotes_get_quote_get(id=id)

Get Quote Details for a single quote

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
api_instance = swagger_client.QuotesApi(swagger_client.ApiClient(configuration))
id = 56 # int |  (optional)

try:
    # Get Quote Details for a single quote
    api_response = api_instance.apiv2_quotes_get_quote_get(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotesApi->apiv2_quotes_get_quote_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 

### Return type

[**QuoteV2BaseDomainEntityV2**](QuoteV2BaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

