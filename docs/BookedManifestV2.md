# BookedManifestV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consignment_ids** | **list[int]** | All the consignment Ids that should be manifested together | 
**company_id** | **int** | The company&#x27;s id in MachShip which is manifesting these consignments | 
**pickup_date_time** | **datetime** | Pickup Date of this manifest. Should be in the format &#x27;YYYY-MM-DD HH:SS&#x27; | [optional] 
**pallet_spaces** | **int** | How many pallet spaces are required for this manifest? | [optional] 
**pickup_closing_time** | **datetime** | What is the closing time for this pickup location? | [optional] 
**pickup_special_instructions** | **str** | Pickup special instructions for the driver (Optional) | [optional] 
**pickup_already_booked** | **bool** | Has a pickup already been booked? If a pickup has not been booked, MachShip will book it for you | [optional] 
**carrier_name** | **str** | The carrier that the manifest is for | [optional] 
**dgs_declaration** | **bool** | Must be true if manifesting DG consignments. Setting this to true means you Agree this Manifest is Compatible and in accordance with the Australian Dangerous Goods (ADG) Code Edition 7.8 | [optional] 
**custom_values** | [**list[CustomValue]**](CustomValue.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

