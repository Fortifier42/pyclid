# SimpleRouteV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | The GUID which can be used to match a response back to the request made for it | [optional] 
**carrier** | [**CarrierLiteWithCustomFieldSets**](CarrierLiteWithCustomFieldSets.md) |  | [optional] 
**carrier_service** | [**CarrierServiceLite**](CarrierServiceLite.md) |  | [optional] 
**carrier_account** | [**CarrierAccountLite**](CarrierAccountLite.md) |  | [optional] 
**company_carrier_account_id** | **int** | The Company Carrier Account for the route | [optional] 
**company_id** | **int** | The Machship ID of the Company the route is connected to | [optional] 
**consignment_total** | [**ConsignmentTotal**](ConsignmentTotal.md) |  | [optional] 
**from_company_location_id** | **int** | The Machship ID of the From Company Location | [optional] 
**from_address** | [**Address**](Address.md) |  | [optional] 
**from_location** | [**LocationV2**](LocationV2.md) |  | [optional] 
**from_zone** | [**CarrierZoneLite**](CarrierZoneLite.md) |  | [optional] 
**to_company_location_id** | **int** | The Machship ID of the To Company Location | [optional] 
**to_address** | [**Address**](Address.md) |  | [optional] 
**to_location** | [**LocationV2**](LocationV2.md) |  | [optional] 
**to_zone** | [**CarrierZoneLite**](CarrierZoneLite.md) |  | [optional] 
**despatch_options** | [**list[RouteDespatchOptionLite]**](RouteDespatchOptionLite.md) | The despatch options for this route | [optional] 
**fuel_levy_percentage** | **float** |  | [optional] 
**sell_fuel_levy_percentage** | **float** |  | [optional] 
**tax_percentage** | **float** |  | [optional] 
**elective_surcharges** | [**list[ConsignmentSurchargeV2]**](ConsignmentSurchargeV2.md) | Contains all Elective surcharges | [optional] 
**automatic_surcharges** | [**list[ConsignmentSurchargeV2]**](ConsignmentSurchargeV2.md) | Contains all Automatic Surchanges | [optional] 
**total_weight** | **float** | The total weight of all items in the current consignment | [optional] 
**total_cubic** | **float** | The total cubic weight of all items in the current consignment | [optional] 
**total_volume** | **float** | The total volume of all items in the current consignment | [optional] 
**carrier_logo_file_name** | **str** | the carrier&#x27;s image filename. This file can be found at {machshipenvironment}/app/css/img/carrierLogos/{carrierLogoFileName} | [optional] 
**price_display** | **float** |  | [optional] 
**price_display_type** | [**QuoteTotalDisplayType**](QuoteTotalDisplayType.md) |  | [optional] 
**is_hourly** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

