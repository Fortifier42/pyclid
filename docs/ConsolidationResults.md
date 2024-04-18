# ConsolidationResults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** | The Machship Company ID that consolidation should / has been performed against | [optional] 
**consignments** | [**list[ConsolidatedConsignment]**](ConsolidatedConsignment.md) | The consolidated consignments and their details | [optional] 
**consolidation_performed** | **bool** | Whether or not consolidation has been performed and saved or if these results are merely indicative of  what will occur | [optional] 
**contains_pending_consignments** | **bool** | Does the consolidation include any consignments that were pending consignments | [optional] 
**contains_unmanifested_consignments** | **bool** | Does the consolidation include any consignments that were unmanifested (not pending) consignments | [optional] 
**validation_results** | [**list[MachshipValidationResult]**](MachshipValidationResult.md) | A list of validation results from the consolidation process | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

