# ManualTrackingStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consignment_id** | **int** | The ID of the consignment in MachShip | [optional] 
**status** | [**TrackingStatus**](TrackingStatus.md) |  | [optional] 
**status_date_time_local** | **datetime** | Optional. | [optional] 
**item_reference** | **str** | When present this tracking status relates to an item on the consignment. When absent it relates  to the consignment as a whole. | [optional] 
**extra_information** | **str** | Any extra information about this status - this will be shown in MachShip when viewing the tracking history | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

