# ConsolidationOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**do_not_consolidate** | **bool** | Set this flag to true when you do not want to consolidate, rather you just want the consignments to be returned to be abl  to perform a bulk update | [optional] 
**company_id** | **int** | The Machship Company ID that consolidation should be performed for - if omitted it will be performed against the company  of the user performing consolidation | [optional] 
**consolidation_target** | [**ConsolidationTarget**](ConsolidationTarget.md) |  | [optional] 
**unmanifested_consignment_ids** | **list[int]** | Optional - list of unmanifested consignment IDs to attempt to consolidate. Will not be considered if Machship.Common.Models.Consolidation.ConsolidationOptions.ConsolidationTarget is set to Machship.Common.Models.Consolidation.Enums.ConsolidationTarget.Pending.  If omitted all unmanifested consignments will be used to attempt consolidation. | [optional] 
**pending_consignment_ids** | **list[int]** | Optional - list of pending consignment IDs to attempt to consolidate. Will not be considered if Machship.Common.Models.Consolidation.ConsolidationOptions.ConsolidationTarget is set to Machship.Common.Models.Consolidation.Enums.ConsolidationTarget.Unmanifested.  If omitted all pending consignments will be used to attempt consolidation. | [optional] 
**group_by_carrier** | **bool** | Whether the carrier will be considered when consolidating consignments | [optional] 
**group_by_service** | **bool** | Whether the service will be considered when consolidating consignments (only relevant when Machship.Common.Models.Consolidation.ConsolidationOptions.GroupByCarrier is also set to true) | [optional] 
**group_by_reference_one** | **bool** | Whether the first customer reference be used when grouping consignments for consolidation | [optional] 
**group_by_reference_two** | **bool** | Whether the second customer reference be used when grouping consignments for consolidation | [optional] 
**group_by_despatch_date** | **bool** | Whether the despatch date be used when grouping consignments for consolidation | [optional] 
**default_route_selection** | [**ConsolidationDefaultRouteSelection**](ConsolidationDefaultRouteSelection.md) |  | [optional] 
**error_handling** | [**ConsolidationErrorHandling**](ConsolidationErrorHandling.md) |  | [optional] 
**prevent_future_date_consoldation** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

