# PendingConsignmentItemV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_item_id** | **int** | Links this item back up to a saved item in Machship | [optional] 
**item_type** | [**ItemType**](ItemType.md) |  | [optional] 
**name** | **str** | Name or description of the goods you are sending | [optional] 
**sku** | **str** | the SKU or code of the item you are sending | [optional] 
**quantity** | **int** | Number of items | [optional] 
**volume** | **float** | Volume of the item | [optional] 
**height** | **float** | Height of the item in cm | [optional] 
**weight** | **float** | Weight of the item in kg | [optional] 
**length** | **float** | Length of the item in cm | [optional] 
**width** | **float** | Width of the item in cm | [optional] 
**carrier_reference** | **str** | The carrier reference of the item | [optional] 
**pallet_spaces** | **float** |  | [optional] 
**pending_consignment_item_dg_items** | [**list[PendingConsignmentItemDgItemV2]**](PendingConsignmentItemDgItemV2.md) |  | [optional] 
**pending_consignment_item_references** | [**list[PendingConsignmentItemReference]**](PendingConsignmentItemReference.md) |  | [optional] 
**pending_consignment_item_contents** | [**list[PendingConsignmentItemContentV2]**](PendingConsignmentItemContentV2.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

