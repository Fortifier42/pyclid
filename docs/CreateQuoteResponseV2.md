# CreateQuoteResponseV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Machship&#x27;s Id reference for this consignment. Use this id when interacting via the API | [optional] 
**consignment_number** | **str** | Machship&#x27;s MS Number. This is the human friendly Machship consignment number that is sent to the carrier | [optional] 
**despatch_date_local** | **datetime** |  | [optional] 
**despatch_date_utc** | **datetime** |  | [optional] 
**eta_local** | **datetime** |  | [optional] 
**eta_utc** | **datetime** |  | [optional] 
**carrier** | [**CarrierLite**](CarrierLite.md) |  | [optional] 
**carrier_service** | [**CarrierServiceLite**](CarrierServiceLite.md) |  | [optional] 
**company_carrier_account** | [**CompanyCarrierAccountLite**](CompanyCarrierAccountLite.md) |  | [optional] 
**is_test** | **bool** |  | [optional] 
**is_international** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

