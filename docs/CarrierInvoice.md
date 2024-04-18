# CarrierInvoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**carrier_id** | **int** |  | [optional] 
**carrier** | [**Carrier**](Carrier.md) |  | [optional] 
**broker_id** | **int** |  | [optional] 
**broker** | [**Company**](Company.md) |  | [optional] 
**filename** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**invoice_date** | **datetime** |  | [optional] 
**uploaded_date** | **datetime** |  | [optional] 
**extra_charges** | **float** |  | [optional] 
**extra_charges_tax** | **float** |  | [optional] 
**date_paid** | **datetime** |  | [optional] 
**paid** | **bool** |  | [optional] 
**has_file** | **bool** |  | [optional] 
**total_extra_charges** | **float** |  | [optional] 
**total_pending_before_tax** | **float** |  | [optional] 
**total_pending** | **float** |  | [optional] 
**total_external_before_tax** | **float** |  | [optional] 
**total_external** | **float** |  | [optional] 
**total_rejected_before_tax** | **float** |  | [optional] 
**total_rejected** | **float** |  | [optional] 
**total_accepted_before_tax** | **float** |  | [optional] 
**total_accepted** | **float** |  | [optional] 
**total_adjustments_before_tax** | **float** |  | [optional] 
**total_adjustments** | **float** |  | [optional] 
**total_due_before_tax** | **float** |  | [optional] 
**total_due** | **float** |  | [optional] 
**original_total_before_tax** | **float** |  | [optional] 
**original_total** | **float** |  | [optional] 
**contains_pending** | **bool** |  | [optional] 
**carrier_invoice_entries** | [**list[CarrierInvoiceEntry]**](CarrierInvoiceEntry.md) |  | [optional] 
**date_time_reconciled_utc** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

