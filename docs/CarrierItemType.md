# CarrierItemType

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**carrier_id** | **int** |  | [optional] 
**carrier** | [**Carrier**](Carrier.md) |  | [optional] 
**name** | **str** |  | 
**abbreviation** | **str** |  | 
**display_name** | **str** |  | [optional] 
**order** | **int** | This is the order that the these items are assigned for a given carrier.  The lower the number, the \&quot;smaller\&quot; the item is.  This is used to determine which item type is used when converting consingment items to carrier items.  ie. if an item can be a carton or a large carton, the carton order is lower so the carton is selected.    Pro rataing is only considered if an item is bigger then the largest carrier item (ie. item with the largest order) | [optional] 
**min_length** | **float** |  | [optional] 
**max_length** | **float** |  | [optional] 
**min_width** | **float** |  | [optional] 
**max_width** | **float** |  | [optional] 
**min_height** | **float** |  | [optional] 
**max_height** | **float** |  | [optional] 
**min_weight** | **float** |  | [optional] 
**max_weight** | **float** |  | [optional] 
**min_volume** | **float** |  | [optional] 
**max_volume** | **float** |  | [optional] 
**min_cubic_weight** | **float** |  | [optional] 
**max_cubic_weight** | **float** |  | [optional] 
**can_exceed_weight** | **bool** |  | [optional] 
**can_exceed_height** | **bool** |  | [optional] 
**can_exceed_length** | **bool** |  | [optional] 
**can_exceed_width** | **bool** |  | [optional] 
**can_exceed_volume** | **bool** |  | [optional] 
**can_exceed_cubic_weight** | **bool** |  | [optional] 
**total** | **int** |  | [optional] 
**carrier_item_type_linked_item_types** | [**list[CarrierItemTypeLinkedItemType]**](CarrierItemTypeLinkedItemType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

