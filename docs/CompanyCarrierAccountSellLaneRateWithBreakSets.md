# CompanyCarrierAccountSellLaneRateWithBreakSets

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**carrier_service_id** | **int** |  | [optional] 
**carrier_service** | [**CarrierServiceLite**](CarrierServiceLite.md) |  | [optional] 
**company_carrier_account_id** | **int** |  | [optional] 
**from_zone_id** | **int** |  | [optional] 
**from_zone** | [**CarrierZoneLite**](CarrierZoneLite.md) |  | [optional] 
**to_zone_id** | **int** |  | [optional] 
**to_zone** | [**CarrierZoneLite**](CarrierZoneLite.md) |  | [optional] 
**reciprocal** | **bool** |  | [optional] 
**total_markup** | **float** | Markup for the entire leg. | [optional] 
**total_markup_type** | [**SellRateType**](SellRateType.md) |  | [optional] 
**minimum_charge** | **float** | Markup for the minimum | [optional] 
**minimum_charge_type** | [**SellRateType**](SellRateType.md) |  | [optional] 
**basic_charge** | **float** | Markup for the basic | [optional] 
**basic_charge_type** | [**SellRateType**](SellRateType.md) |  | [optional] 
**break_charge** | **float** |  | [optional] 
**break_charge_type** | [**SellRateType**](SellRateType.md) |  | [optional] 
**sell_lane_rate_breaks** | [**list[CompanyCarrierAccountSellLaneRateBreak]**](CompanyCarrierAccountSellLaneRateBreak.md) |  | [optional] 
**cubic_conversion_rate** | **float** |  | [optional] 
**total_rows** | **int** |  | [optional] 
**grouped_break_sets** | [**list[CompanyCarrierAccountSellLaneRateGroupedBreakSet]**](CompanyCarrierAccountSellLaneRateGroupedBreakSet.md) |  | [optional] 
**company_carrier_account** | [**CompanyCarrierAccountLite**](CompanyCarrierAccountLite.md) |  | [optional] 
**carrier_id** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

