# CarrierLaneRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**carrier_service_id** | **int** |  | [optional] 
**carrier_service** | [**CarrierServiceModel**](CarrierServiceModel.md) |  | [optional] 
**ratecard_version_id** | **int** |  | [optional] 
**ratecard_version** | [**RatecardVersion**](RatecardVersion.md) |  | [optional] 
**from_zone_id** | **int** |  | [optional] 
**from_zone** | [**CarrierZone**](CarrierZone.md) |  | [optional] 
**to_zone_id** | **int** |  | [optional] 
**to_zone** | [**CarrierZone**](CarrierZone.md) |  | [optional] 
**minimum_charge** | **float** |  | [optional] 
**basic_charge** | **float** |  | [optional] 
**cubic_conversion_rate** | **float** |  | [optional] 
**reciprocal** | **bool** |  | [optional] 
**carrier_lane_rate_breaks** | [**list[CarrierLaneRateBreak]**](CarrierLaneRateBreak.md) |  | [optional] 
**consignments** | [**list[Consignment]**](Consignment.md) |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**date_deleted** | **datetime** |  | [optional] 
**insertion_guid** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

