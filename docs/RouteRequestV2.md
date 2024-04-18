# RouteRequestV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** | Optional: This GUID can be used to match up responses to requests when requesting multiple routes in the same call | [optional] 
**despatch_date_time_utc** | **datetime** | Optional: The date time the items would be available to despatched, in UTC. If this is not provided, it will default to NOW (UTC) | [optional] 
**despatch_date_time_local** | **datetime** |  | [optional] 
**from_company_location_id** | **int** | The machship ID of the saved company from (pickup) location. This only needs to be specified if this route is coming from a saved location | [optional] 
**from_location_id** | **int** | The machship ID of the from (pickup) location. Can be left blank if supplying the suburb / postcode instead | [optional] 
**from_name** | **str** | An optional Name field that can be filled. If present, a company location lookup by name will be attempted in order  to ascertain the FromCompanyLocationId | [optional] 
**from_abbreviation** | **str** | An optional Abbreviation field that can be filled. If present, a company location lookup by abbreviation will be attempted in order  to ascertain the FromCompanyLocationId | [optional] 
**from_location** | [**SendLocationV2**](SendLocationV2.md) |  | [optional] 
**to_company_location_id** | **int** | The machship ID of the saved company to (delivery) location. This only needs to be specified if this route is going to a saved location | [optional] 
**to_location_id** | **int** | The machship ID of the to (receiver) location. Can be left blank if supplying the suburb / postcode instead | [optional] 
**to_name** | **str** | An optional Name field that can be filled. If present, a company location lookup by name will be attempted in order  to ascertain the ToCompanyLocationId | [optional] 
**to_abbreviation** | **str** | An optional Abbreviation field that can be filled. If present, a company location lookup by abbreviation will be attempted in order  to ascertain the ToCompanyLocationId | [optional] 
**to_location** | [**SendLocationV2**](SendLocationV2.md) |  | [optional] 
**question_ids** | **list[int]** | A collection of Machship IDs corresponding to questions who&#x27;s result is true | [optional] 
**carrier_ids** | **list[int]** | The (optional) listing of Machship Carrier IDs to restrict the returning routes for. When left blank all carriers  you have available will be queried for routes. | [optional] 
**carrier_account_id** | **int** | An (optional) Carrier Account ID in Machship. When supplied routes returned will be restricted to those from this  carrier account. | [optional] 
**carrier_service_id** | **int** | An (optional) Machship ID of the Carrier Service. When supplied routes returned will be restricted to those for this  service. | [optional] 
**company_carrier_account_id** | **int** | An (optional) Machship ID of the Company Carrier Account. When supplied routes returned will be restricted to those for this  company carrier account. | [optional] 
**company_id** | **int** | An (optional) Machship ID of a company. When supplied the routes will be those of the company specified, when left  blank they will be routes for the company associated with the authorised user. | [optional] 
**customer_reference** | **str** | Optional | [optional] 
**customer_reference2** | **str** | Optional | [optional] 
**to_address_line1** | **str** |  | [optional] 
**to_address_line2** | **str** |  | [optional] 
**items** | [**list[CreateConsignmentItemV2]**](CreateConsignmentItemV2.md) | A collection of the items being sent | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

