# CarrierSurcharge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**company_id** | **int** |  | 
**company** | [**CompanyLite**](CompanyLite.md) |  | [optional] 
**surcharge_id** | **int** |  | [optional] 
**surcharge** | [**Surcharge**](Surcharge.md) |  | [optional] 
**carrier_id** | **int** |  | [optional] 
**carrier** | [**CarrierLite**](CarrierLite.md) |  | [optional] 
**carrier_service_id** | **int** |  | [optional] 
**carrier_service** | [**CarrierServiceLite**](CarrierServiceLite.md) |  | [optional] 
**carrier_account_id** | **int** |  | [optional] 
**carrier_account** | [**BaseCarrierAccount**](BaseCarrierAccount.md) |  | [optional] 
**carrier_services** | [**list[CarrierSurchargeService]**](CarrierSurchargeService.md) | List of all the carrier services that point to the surcharge for a given carrier | [optional] 
**carrier_accounts** | [**list[CarrierSurchargeAccount]**](CarrierSurchargeAccount.md) | List of all the carrier accounts that point to the surcharge for a given account | [optional] 
**exclude** | **bool** |  | [optional] 
**price** | **float** |  | [optional] 
**hard_set_sell_price** | **float** |  | [optional] 
**percentage_of_sell_price** | **float** |  | [optional] 
**markup** | **float** |  | [optional] 
**price_type** | [**SurchargePriceType**](SurchargePriceType.md) |  | [optional] 
**override_pricing** | **bool** |  | [optional] 
**cost_minimum** | **float** |  | [optional] 
**sell_minimum** | **float** |  | [optional] 
**sell_ratecard_id** | **int** |  | [optional] 
**sell_ratecard** | [**RatecardLite**](RatecardLite.md) |  | [optional] 
**cost_ratecard_id** | **int** |  | [optional] 
**cost_ratecard** | [**RatecardLite**](RatecardLite.md) |  | [optional] 
**markup_type** | [**MarkupType**](MarkupType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

