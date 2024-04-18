# CompanyLocation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**location_type** | [**CompanyLocationType**](CompanyLocationType.md) |  | [optional] 
**name** | **str** |  | 
**abbreviation** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**contact** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**address_line1** | **str** |  | 
**address_line2** | **str** |  | [optional] 
**address_lines_friendly** | **str** |  | [optional] 
**company_id** | **int** |  | [optional] 
**location_id** | **int** |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**location_as_string** | **str** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**special_instructions** | **str** |  | [optional] 
**carrier_accounts** | [**list[BaseCarrierAccount]**](BaseCarrierAccount.md) |  | [optional] 
**permanent_pickups** | [**list[PermanentPickup]**](PermanentPickup.md) |  | [optional] 
**very_frequent_address** | **bool** |  | [optional] 
**total_rows** | **int** |  | [optional] 
**company** | [**CompanyLite**](CompanyLite.md) |  | [optional] 
**insertion_guid** | **str** |  | [optional] 
**company_location_receiver_accounts** | [**list[CompanyLocationReceiverAccount]**](CompanyLocationReceiverAccount.md) |  | [optional] 
**reference1** | **str** |  | [optional] 
**reference2** | **str** |  | [optional] 
**default_pickup_time** | [**TimeSpan**](TimeSpan.md) |  | [optional] 
**default_closing_time** | [**TimeSpan**](TimeSpan.md) |  | [optional] 
**default_pickup_instructions** | **str** |  | [optional] 
**pickup_question_ids** | **list[int]** |  | [optional] 
**delivery_question_ids** | **list[int]** |  | [optional] 
**is_international** | **bool** |  | [optional] 
**country_id** | **int** |  | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**international_city** | **str** |  | [optional] 
**international_province** | **str** |  | [optional] 
**international_postcode** | **str** |  | [optional] 
**location_description** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

