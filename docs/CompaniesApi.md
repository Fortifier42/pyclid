# swagger_client.CompaniesApi

All URIs are relative to *https://live.machship.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiv2_companies_get_all_get**](CompaniesApi.md#apiv2_companies_get_all_get) | **GET** /apiv2/companies/getAll | Get all companies that the current user can access
[**apiv2_companies_get_available_carriers_accounts_and_services_get**](CompaniesApi.md#apiv2_companies_get_available_carriers_accounts_and_services_get) | **GET** /apiv2/companies/getAvailableCarriersAccountsAndServices | Get all available carriers with accounts and services

# **apiv2_companies_get_all_get**
> CompanyV2WithParentIdIEnumerableBaseDomainEntityV2 apiv2_companies_get_all_get(at_or_below_company_id=at_or_below_company_id)

Get all companies that the current user can access

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
api_instance = swagger_client.CompaniesApi(swagger_client.ApiClient(configuration))
at_or_below_company_id = 56 # int | When supplied the results will be limited to the company with that ID and any descendants  below it. Leave blank to return all companies. (optional)

try:
    # Get all companies that the current user can access
    api_response = api_instance.apiv2_companies_get_all_get(at_or_below_company_id=at_or_below_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->apiv2_companies_get_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **at_or_below_company_id** | **int**| When supplied the results will be limited to the company with that ID and any descendants  below it. Leave blank to return all companies. | [optional] 

### Return type

[**CompanyV2WithParentIdIEnumerableBaseDomainEntityV2**](CompanyV2WithParentIdIEnumerableBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apiv2_companies_get_available_carriers_accounts_and_services_get**
> CarrierWithAccountsAndServicesLiteIEnumerableBaseDomainEntityV2 apiv2_companies_get_available_carriers_accounts_and_services_get(company_id=company_id)

Get all available carriers with accounts and services

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
api_instance = swagger_client.CompaniesApi(swagger_client.ApiClient(configuration))
company_id = 56 # int | The id of the company to get the carriers, accounts and services for (optional)

try:
    # Get all available carriers with accounts and services
    api_response = api_instance.apiv2_companies_get_available_carriers_accounts_and_services_get(company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->apiv2_companies_get_available_carriers_accounts_and_services_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **int**| The id of the company to get the carriers, accounts and services for | [optional] 

### Return type

[**CarrierWithAccountsAndServicesLiteIEnumerableBaseDomainEntityV2**](CarrierWithAccountsAndServicesLiteIEnumerableBaseDomainEntityV2.md)

### Authorization

[User API Token](../README.md#User API Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

