# CompanyCarrierAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**company_id** | **int** |  | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**carrier_id** | **int** |  | [optional] 
**carrier_account** | [**CarrierAccount**](CarrierAccount.md) |  | [optional] 
**carrier_account_id** | **int** |  | [optional] 
**markup** | **float** |  | [optional] 
**total_markup_type** | [**SellRateType**](SellRateType.md) |  | [optional] 
**minimum_markup** | **float** |  | [optional] 
**minimum_markup_type** | [**SellRateType**](SellRateType.md) |  | [optional] 
**basic_markup** | **float** |  | [optional] 
**basic_markup_type** | [**SellRateType**](SellRateType.md) |  | [optional] 
**break_markup** | **float** |  | [optional] 
**break_markup_type** | [**SellRateType**](SellRateType.md) |  | [optional] 
**name** | **str** |  | 
**abbreviation** | **str** |  | 
**total_rows** | **int** |  | [optional] 
**carrier_service_overrides** | [**list[CompanyCarrierAccountServiceOverride]**](CompanyCarrierAccountServiceOverride.md) |  | [optional] 
**sell_lane_rates** | [**list[CompanyCarrierAccountSellLaneRateWithBreakSets]**](CompanyCarrierAccountSellLaneRateWithBreakSets.md) |  | [optional] 
**cubic_conversion_rate** | **float** |  | [optional] 
**fuel_surcharge_id** | **int** |  | [optional] 
**enable_receiver_pays** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**valid_services** | **bool** |  | [optional] 
**company_carrier_account_services** | [**list[CompanyCarrierAccountService]**](CompanyCarrierAccountService.md) |  | [optional] 
**dg_enabled** | **bool** |  | [optional] 
**limit_to_ratecard_sell_rates** | **bool** | When set to true, prices will only price when there is a sell rate for that lane (and the breaks cover the consignment&#x27;s items) | [optional] 
**is_inheritable** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

