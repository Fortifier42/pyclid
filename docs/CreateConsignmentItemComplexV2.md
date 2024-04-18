# CreateConsignmentItemComplexV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | This is populated IF it is an existing unmanifested consignment&#x27;s consignment item ID | [optional] 
**company_item_id** | **int** | Optional: Links this item back up to a saved item in Machship | [optional] 
**item_type** | [**ItemType**](ItemType.md) |  | [optional] 
**name** | **str** | Name or description of the goods you are sending | [optional] 
**sku** | **str** | Optional: the SKU or code of the item you are sending | [optional] 
**quantity** | **int** | Number of items | [optional] 
**pallet_spaces** | **float** |  | [optional] 
**standard_item** | [**CreateConsignmentStandardItemV2**](CreateConsignmentStandardItemV2.md) |  | [optional] 
**combined_item** | [**CreateConsignmentCombinedItemV2**](CreateConsignmentCombinedItemV2.md) |  | [optional] 
**combined_load_size** | [**CreateConsignmentCombinedLoadSizeItemV2**](CreateConsignmentCombinedLoadSizeItemV2.md) |  | [optional] 
**consignment_item_dg_items** | [**list[CreateConsignmentItemDgItemV2]**](CreateConsignmentItemDgItemV2.md) |  | [optional] 
**consignment_item_references** | [**list[CreateConsignmentItemReferenceV2]**](CreateConsignmentItemReferenceV2.md) |  | [optional] 
**consignment_item_contents** | [**list[CreateConsignmentItemContentV2]**](CreateConsignmentItemContentV2.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

