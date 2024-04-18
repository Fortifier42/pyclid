# ReturnBookedManifestV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Machship&#x27;s Manifest Id | [optional] 
**consignment_ids** | **list[int]** | All the consignment Ids that should be manifested together | [optional] 
**company_id** | **int** | The company&#x27;s id in Machship which is manifesting these consignments | [optional] 
**carrier_reference** | **str** | Any reference information from the Carrier pertaining to the manifest | [optional] 
**booking_successful** | **bool** | Whether or not the manifest was booked successfully | [optional] 
**error_message** | **str** | The error message if the booking was not successful | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

