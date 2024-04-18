# Surcharge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**company_id** | **int** |  | 
**company** | [**CompanyLite**](CompanyLite.md) |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**abbreviation** | **str** |  | [optional] 
**price** | **float** | This is the base price of the surcharge before markups have been applied | 
**sell_price** | **float** |  | [optional] 
**hard_set_sell_price** | **float** |  | [optional] 
**percentage_of_sell_price** | **float** |  | [optional] 
**cost_minimum** | **float** |  | [optional] 
**sell_minimum** | **float** |  | [optional] 
**markup** | **float** |  | [optional] 
**automatic** | **bool** | Indicates this surcharge is mandatory | [optional] 
**is_fuel_levy_exempt** | **bool** | True if the fuel levy should not be applied to this surcharge | [optional] 
**only_apply_surcharge_to_dg** | **bool** | True if the Surcharge should only apply to DGs | [optional] 
**query** | **str** |  | [optional] 
**query_json** | **str** |  | [optional] 
**is_conditional** | **bool** |  | [optional] 
**per_lane_rate** | **bool** |  | [optional] 
**per_matching_item** | **bool** |  | [optional] 
**price_type** | [**SurchargePriceType**](SurchargePriceType.md) |  | [optional] 
**special_instructions** | **str** |  | [optional] 
**surcharge_evaluator_class_id** | **int** |  | [optional] 
**surcharge_evaluator_class_serialised_settings** | **str** |  | [optional] 
**sell_ratecard_id** | **int** |  | [optional] 
**sell_ratecard** | [**RatecardLite**](RatecardLite.md) |  | [optional] 
**cost_ratecard_id** | **int** |  | [optional] 
**cost_ratecard** | [**RatecardLite**](RatecardLite.md) |  | [optional] 
**carrier_surcharges** | [**list[CarrierSurcharge]**](CarrierSurcharge.md) |  | [optional] 
**referenced_query_ids** | **list[int]** | a list of query ids that are referenced in this surcharge | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

