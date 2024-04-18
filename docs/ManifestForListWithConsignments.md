# ManifestForListWithConsignments

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**pickup_name_and_location** | **str** |  | [optional] 
**despatch_date_local** | **datetime** |  | [optional] 
**total** | **float** |  | [optional] 
**carrier_name** | **str** |  | [optional] 
**service_names** | **str** |  | [optional] 
**carrier_and_service_name** | **str** |  | [optional] 
**consignment_count** | **int** |  | [optional] 
**pickup_location_description** | **str** |  | [optional] 
**pickup_location** | [**Location**](Location.md) |  | [optional] 
**pickup_name** | **str** |  | [optional] 
**is_dg_manifest** | **bool** |  | [optional] 
**is_test** | **bool** |  | [optional] 
**consignment_sub_dg_class_types** | [**list[ConsignmentSubDgClassTypes]**](ConsignmentSubDgClassTypes.md) |  | [optional] 
**dg_class_type_and_sub_class_type_for_consignment** | **str** |  | [optional] 
**total_rows** | **int** |  | [optional] 
**can_remanifest** | **bool** |  | [optional] 
**carrier_can_remanifest** | **bool** |  | [optional] 
**carrier_account_id** | **int** |  | [optional] 
**carrier_can_rebook_pickup** | **bool** |  | [optional] 
**is_international** | **bool** |  | [optional] 
**international_pickup_city** | **str** |  | [optional] 
**international_pickup_province** | **str** |  | [optional] 
**international_pickup_postcode** | **str** |  | [optional] 
**international_pickup_country_id** | **int** |  | [optional] 
**international_pickup_country** | [**Country**](Country.md) |  | [optional] 
**consignments** | [**list[ManifestForListConsignment]**](ManifestForListConsignment.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

