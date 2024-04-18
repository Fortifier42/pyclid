# InvoiceItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **int** |  | [optional] 
**invoice** | [**Invoice**](Invoice.md) |  | [optional] 
**insertion_guid** | **str** |  | [optional] 
**crc_insertion_guid** | **str** |  | [optional] 
**billing_charge_insertion_guid** | **str** | This is used to link the invoice item to the billing charge when generating invoices | [optional] 
**invoice_document_number** | **str** |  | [optional] 
**consignment** | [**Consignment**](Consignment.md) |  | [optional] 
**has_consignment** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**quantity** | **float** |  | 
**base_charge_each** | **float** |  | [optional] 
**fuel_levy_each** | **float** |  | [optional] 
**tax_amount_each** | **float** |  | [optional] 
**tax_percentage** | **float** |  | [optional] 
**total_base_charge** | **float** |  | [optional] 
**total_fuel_levy** | **float** |  | [optional] 
**total_tax** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**item_type_abbreviation** | **str** | This information is not persisted and is only used when generating the csv invoices.  This helps determine which type of line item we are currently using | [optional] 
**item_type_name** | **str** |  | [optional] 
**machship_item_type** | **str** |  | [optional] 
**consignment_number** | **str** | This is only used when generating the invoices for csv and pdf. | [optional] 
**is_manual_entry** | **bool** |  | [optional] 
**consignment_id** | **int** |  | [optional] 
**consignment_reconciliation_charges** | [**list[ConsignmentReconciliationCharge]**](ConsignmentReconciliationCharge.md) |  | [optional] 
**company_billing_charge** | [**CompanyBillingCharge**](CompanyBillingCharge.md) |  | [optional] 
**is_international** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

