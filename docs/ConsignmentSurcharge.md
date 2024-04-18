# ConsignmentSurcharge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**surcharge** | [**Surcharge**](Surcharge.md) |  | [optional] 
**invoice_item_id** | **int** |  | [optional] 
**invoice_item** | [**InvoiceItem**](InvoiceItem.md) |  | [optional] 
**surcharge_id** | **int** |  | [optional] 
**selected** | **bool** | used when the user selects elective surcharges | [optional] 
**cost_price** | **float** |  | [optional] 
**sell_price** | **float** |  | [optional] 
**markup_percentage** | **float** | This is used by the routing engine when this surcharge is based on a percentage rather than a price | [optional] 
**original_price** | **float** | This is the &#x27;price&#x27; field from the surcharge. This is needed for the front end so it can figure out price changes on the fly | [optional] 
**price_type** | [**SurchargePriceType**](SurchargePriceType.md) |  | [optional] 
**quantity** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**abbreviation** | **str** |  | [optional] 
**consignment_item_consignment_surcharges** | [**list[ConsignmentItemConsignmentSurcharge]**](ConsignmentItemConsignmentSurcharge.md) |  | [optional] 
**percentage_of_sell_price** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

