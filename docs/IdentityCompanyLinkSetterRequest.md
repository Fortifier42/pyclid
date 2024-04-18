# IdentityCompanyLinkSetterRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_id** | **int** | The ID in MachShip of an identity owned by your Organisation. Either the IdentityId OR IdentityPublicKey must be provided | [optional] 
**identity_public_key** | **str** | The \&quot;public key\&quot; of an identity from another organisation (who has been linked to your organisation). Either the IdentityId OR IdentityPublicKey must be provided | [optional] 
**company_id** | **int** | The ID in MachShip of a company within your organisation | 
**roles** | **list[int]** | One ore more role IDs to assign the identity | 
**test_mode_setting** | [**UserTestModeSetting**](UserTestModeSetting.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

