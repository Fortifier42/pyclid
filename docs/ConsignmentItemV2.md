# ConsignmentItemV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_item_id** | **int** | Optional: Links this item back up to a saved item in Machship | [optional] 
**item_type** | [**ItemType**](ItemType.md) |  | 
**name** | **str** | Name or description of the goods you are sending | 
**sku** | **str** | Optional: the SKU or code of the item you are sending | [optional] 
**quantity** | **int** | Number of items | 
**height** | **float** | Height of the item in cm | 
**weight** | **float** | Weight of the item in kg | 
**length** | **float** | Length of the item in cm | 
**width** | **float** | Width of the item in cm | 
**references** | **list[str]** |  | [optional] 
**consignment_item_dg_items** | [**list[ConsignmentItemDgItemV2]**](ConsignmentItemDgItemV2.md) |  | [optional] 
**consignment_item_contents** | [**list[ConsignmentItemContent]**](ConsignmentItemContent.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

