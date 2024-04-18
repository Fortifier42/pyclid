# SubComponent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**sub_component_type** | [**SubComponentType**](SubComponentType.md) |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**allowed_user_types** | [**list[UserType]**](UserType.md) |  | [optional] 
**allowed_enterprise_tiers** | [**list[EnterpriseTier]**](EnterpriseTier.md) | These are only in effect if a) the user is of type \&quot;Enterprise\&quot; and b) the collection is not-null or empty | [optional] 
**permission** | [**PermissionType**](PermissionType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

