# CreateConsignmentResponseV2

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
**carrier_consignment_id** | **str** | The carrier&#x27;s reference for this consignment | [optional] 
**status** | [**ConsignmentTrackingStatusV2**](ConsignmentTrackingStatusV2.md) |  | [optional] 
**tracking_page_access_token** | **str** | Access Token for this consignment&#x27;s tracking page.  This can be used by your customer to track their consignment using the url:  https://live.machship.com/public/#/consignments/{TrackingPageAccessToken} | [optional] 
**consignment_total** | [**ConsignmentTotal**](ConsignmentTotal.md) |  | [optional] 
**consignment_hourly_pricing** | [**ConsignmentHourlyPricing**](ConsignmentHourlyPricing.md) |  | [optional] 
**consignment_carrier_surcharges** | [**list[CreateConsignmentResponseConsignmentSurchargeV2]**](CreateConsignmentResponseConsignmentSurchargeV2.md) |  | [optional] 
**print_settings** | [**CarrierPrintSettings**](CarrierPrintSettings.md) |  | [optional] 
**items** | [**list[ConsignmentItemV2]**](ConsignmentItemV2.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

