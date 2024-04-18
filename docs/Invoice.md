# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**insertion_guid** | **str** |  | [optional] 
**transaction_status** | [**FinanceTransactionStatus**](FinanceTransactionStatus.md) |  | [optional] 
**document_number** | **str** |  | [optional] 
**broker_id** | **int** |  | [optional] 
**broker** | [**Company**](Company.md) |  | [optional] 
**company_id** | **int** |  | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**invoice_date** | **datetime** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**total_base_charge** | **float** |  | [optional] 
**total_tax** | **float** |  | [optional] 
**total_fuel_levy** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**amount_paid** | **float** |  | [optional] 
**invoice_items** | [**list[InvoiceItem]**](InvoiceItem.md) |  | [optional] 
**manual_invoice_items** | [**list[InvoiceItem]**](InvoiceItem.md) | Used by the UI. This is all the invoice items that are not linked to any consignments. Ie. can be edited | [optional] 
**invoice_pdf** | **str** |  | [optional] 
**invoice_csv** | **str** |  | [optional] 
**invoice_csv_extension** | **str** |  | [optional] 
**total_oweing** | **float** |  | [optional] 
**terms_description** | **str** |  | [optional] 
**custom_email_subject_prefix** | **str** |  | [optional] 
**validation_results** | [**list[MachshipValidationResult]**](MachshipValidationResult.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

