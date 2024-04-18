# CompanyCarrierAccountSellLaneRateBreak

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**company_carrier_account_sell_lane_rate_id** | **int** |  | [optional] 
**carrier_item_type_id** | **int** | if a carrier item type is not provided then this is the default breaks | [optional] 
**carrier_item_type** | [**CarrierItemTypeLite**](CarrierItemTypeLite.md) |  | [optional] 
**calculation_type** | [**CalculationType**](CalculationType.md) |  | [optional] 
**break_from** | **int** |  | [optional] 
**break_to** | **int** | the maximum for this current break. If this is null, it is infinite | [optional] 
**price** | **float** |  | [optional] 
**price_type** | [**SellRateType**](SellRateType.md) |  | [optional] 
**rate_insertion_guid** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

