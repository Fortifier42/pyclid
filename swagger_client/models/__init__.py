# coding: utf-8

# flake8: noqa
"""
    Machship API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.address import Address
from swagger_client.models.attachment import Attachment
from swagger_client.models.auto_reconcile_request import AutoReconcileRequest
from swagger_client.models.base_carrier_account import BaseCarrierAccount
from swagger_client.models.base_carrier_service import BaseCarrierService
from swagger_client.models.billing_charge_type import BillingChargeType
from swagger_client.models.booked_manifest_v2 import BookedManifestV2
from swagger_client.models.booked_manifest_v2_i_collection_base_domain_entity_v2 import BookedManifestV2ICollectionBaseDomainEntityV2
from swagger_client.models.boolean_base_domain_entity_v2 import BooleanBaseDomainEntityV2
from swagger_client.models.calculation_type import CalculationType
from swagger_client.models.carrier import Carrier
from swagger_client.models.carrier_account import CarrierAccount
from swagger_client.models.carrier_account_for_consignment import CarrierAccountForConsignment
from swagger_client.models.carrier_account_lite import CarrierAccountLite
from swagger_client.models.carrier_account_lite_with_services import CarrierAccountLiteWithServices
from swagger_client.models.carrier_account_service_model import CarrierAccountServiceModel
from swagger_client.models.carrier_distance_label_type import CarrierDistanceLabelType
from swagger_client.models.carrier_for_consignment import CarrierForConsignment
from swagger_client.models.carrier_integration_lite import CarrierIntegrationLite
from swagger_client.models.carrier_invoice import CarrierInvoice
from swagger_client.models.carrier_invoice_entry import CarrierInvoiceEntry
from swagger_client.models.carrier_invoice_entry_amendment import CarrierInvoiceEntryAmendment
from swagger_client.models.carrier_invoice_entry_amendment_v2_for_get_entries_endpoint import CarrierInvoiceEntryAmendmentV2ForGetEntriesEndpoint
from swagger_client.models.carrier_invoice_entry_charge import CarrierInvoiceEntryCharge
from swagger_client.models.carrier_invoice_entry_info import CarrierInvoiceEntryInfo
from swagger_client.models.carrier_invoice_entry_reconciliation_charge import CarrierInvoiceEntryReconciliationCharge
from swagger_client.models.carrier_invoice_entry_reconciliation_charge_display import CarrierInvoiceEntryReconciliationChargeDisplay
from swagger_client.models.carrier_invoice_entry_rejection_reason import CarrierInvoiceEntryRejectionReason
from swagger_client.models.carrier_invoice_entry_status import CarrierInvoiceEntryStatus
from swagger_client.models.carrier_invoice_entry_v2_for_get_entries_endpoint import CarrierInvoiceEntryV2ForGetEntriesEndpoint
from swagger_client.models.carrier_invoice_entry_v2_for_get_entries_endpoint_i_collection_base_domain_entity_v2 import CarrierInvoiceEntryV2ForGetEntriesEndpointICollectionBaseDomainEntityV2
from swagger_client.models.carrier_invoice_information import CarrierInvoiceInformation
from swagger_client.models.carrier_invoice_information_i_collection_base_domain_entity_v2 import CarrierInvoiceInformationICollectionBaseDomainEntityV2
from swagger_client.models.carrier_item_type import CarrierItemType
from swagger_client.models.carrier_item_type_linked_item_type import CarrierItemTypeLinkedItemType
from swagger_client.models.carrier_item_type_lite import CarrierItemTypeLite
from swagger_client.models.carrier_lane_rate import CarrierLaneRate
from swagger_client.models.carrier_lane_rate_break import CarrierLaneRateBreak
from swagger_client.models.carrier_lite import CarrierLite
from swagger_client.models.carrier_lite_with_custom_field_sets import CarrierLiteWithCustomFieldSets
from swagger_client.models.carrier_pickup_type import CarrierPickupType
from swagger_client.models.carrier_print_settings import CarrierPrintSettings
from swagger_client.models.carrier_ref_pool_lite import CarrierRefPoolLite
from swagger_client.models.carrier_service_container import CarrierServiceContainer
from swagger_client.models.carrier_service_for_consignment import CarrierServiceForConsignment
from swagger_client.models.carrier_service_group import CarrierServiceGroup
from swagger_client.models.carrier_service_group_lite import CarrierServiceGroupLite
from swagger_client.models.carrier_service_lite import CarrierServiceLite
from swagger_client.models.carrier_service_lite_with_sub_services import CarrierServiceLiteWithSubServices
from swagger_client.models.carrier_service_model import CarrierServiceModel
from swagger_client.models.carrier_service_sub_service import CarrierServiceSubService
from swagger_client.models.carrier_service_sub_service_lite import CarrierServiceSubServiceLite
from swagger_client.models.carrier_surcharge import CarrierSurcharge
from swagger_client.models.carrier_surcharge_account import CarrierSurchargeAccount
from swagger_client.models.carrier_surcharge_service import CarrierSurchargeService
from swagger_client.models.carrier_with_accounts_and_services_lite import CarrierWithAccountsAndServicesLite
from swagger_client.models.carrier_with_accounts_and_services_lite_i_enumerable_base_domain_entity_v2 import CarrierWithAccountsAndServicesLiteIEnumerableBaseDomainEntityV2
from swagger_client.models.carrier_zone import CarrierZone
from swagger_client.models.carrier_zone_lite import CarrierZoneLite
from swagger_client.models.carrier_zone_location import CarrierZoneLocation
from swagger_client.models.carrier_zone_set_lite import CarrierZoneSetLite
from swagger_client.models.company import Company
from swagger_client.models.company_billing_charge import CompanyBillingCharge
from swagger_client.models.company_carrier_account import CompanyCarrierAccount
from swagger_client.models.company_carrier_account_lite import CompanyCarrierAccountLite
from swagger_client.models.company_carrier_account_sell_lane_rate_break import CompanyCarrierAccountSellLaneRateBreak
from swagger_client.models.company_carrier_account_sell_lane_rate_break_set import CompanyCarrierAccountSellLaneRateBreakSet
from swagger_client.models.company_carrier_account_sell_lane_rate_grouped_break_set import CompanyCarrierAccountSellLaneRateGroupedBreakSet
from swagger_client.models.company_carrier_account_sell_lane_rate_with_break_sets import CompanyCarrierAccountSellLaneRateWithBreakSets
from swagger_client.models.company_carrier_account_service import CompanyCarrierAccountService
from swagger_client.models.company_carrier_account_service_override import CompanyCarrierAccountServiceOverride
from swagger_client.models.company_carrier_custom_field_set_list import CompanyCarrierCustomFieldSetList
from swagger_client.models.company_carrier_setting import CompanyCarrierSetting
from swagger_client.models.company_dg_item import CompanyDgItem
from swagger_client.models.company_item_complex_v2 import CompanyItemComplexV2
from swagger_client.models.company_item_complex_v2_base_domain_entity_v2 import CompanyItemComplexV2BaseDomainEntityV2
from swagger_client.models.company_item_complex_v2_grid_domain_entity_v2 import CompanyItemComplexV2GridDomainEntityV2
from swagger_client.models.company_item_v2 import CompanyItemV2
from swagger_client.models.company_item_v2_base_domain_entity_v2 import CompanyItemV2BaseDomainEntityV2
from swagger_client.models.company_item_v2_grid_domain_entity_v2 import CompanyItemV2GridDomainEntityV2
from swagger_client.models.company_lite import CompanyLite
from swagger_client.models.company_lite_with_children import CompanyLiteWithChildren
from swagger_client.models.company_location import CompanyLocation
from swagger_client.models.company_location_receiver_account import CompanyLocationReceiverAccount
from swagger_client.models.company_location_type import CompanyLocationType
from swagger_client.models.company_location_v2 import CompanyLocationV2
from swagger_client.models.company_location_v2_base_domain_entity_v2 import CompanyLocationV2BaseDomainEntityV2
from swagger_client.models.company_location_v2_grid_domain_entity_v2 import CompanyLocationV2GridDomainEntityV2
from swagger_client.models.company_location_v2_permanent_pickups import CompanyLocationV2PermanentPickups
from swagger_client.models.company_location_v2_permanent_pickups_base_domain_entity_v2 import CompanyLocationV2PermanentPickupsBaseDomainEntityV2
from swagger_client.models.company_tier import CompanyTier
from swagger_client.models.company_type import CompanyType
from swagger_client.models.company_v2 import CompanyV2
from swagger_client.models.company_v2_with_parent_id import CompanyV2WithParentId
from swagger_client.models.company_v2_with_parent_id_i_enumerable_base_domain_entity_v2 import CompanyV2WithParentIdIEnumerableBaseDomainEntityV2
from swagger_client.models.component import Component
from swagger_client.models.component_type import ComponentType
from swagger_client.models.consignment import Consignment
from swagger_client.models.consignment_attachment_detail_v2 import ConsignmentAttachmentDetailV2
from swagger_client.models.consignment_attachment_detail_v2_i_collection_base_domain_entity_v2 import ConsignmentAttachmentDetailV2ICollectionBaseDomainEntityV2
from swagger_client.models.consignment_carrier_lane_rate import ConsignmentCarrierLaneRate
from swagger_client.models.consignment_carrier_selection_type import ConsignmentCarrierSelectionType
from swagger_client.models.consignment_combined_item import ConsignmentCombinedItem
from swagger_client.models.consignment_combined_load_size_item import ConsignmentCombinedLoadSizeItem
from swagger_client.models.consignment_creation_type import ConsignmentCreationType
from swagger_client.models.consignment_custom_status import ConsignmentCustomStatus
from swagger_client.models.consignment_hourly_pricing import ConsignmentHourlyPricing
from swagger_client.models.consignment_id_with_tracking_history_v2 import ConsignmentIdWithTrackingHistoryV2
from swagger_client.models.consignment_id_with_tracking_history_v2_i_enumerable_base_domain_entity import ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity
from swagger_client.models.consignment_item import ConsignmentItem
from swagger_client.models.consignment_item_consignment_surcharge import ConsignmentItemConsignmentSurcharge
from swagger_client.models.consignment_item_content import ConsignmentItemContent
from swagger_client.models.consignment_item_dg_item import ConsignmentItemDgItem
from swagger_client.models.consignment_item_dg_item_v2 import ConsignmentItemDgItemV2
from swagger_client.models.consignment_item_reference import ConsignmentItemReference
from swagger_client.models.consignment_item_v2 import ConsignmentItemV2
from swagger_client.models.consignment_reconciliation_charge import ConsignmentReconciliationCharge
from swagger_client.models.consignment_reconciliation_charge_display import ConsignmentReconciliationChargeDisplay
from swagger_client.models.consignment_reconciliation_charge_record_addition_type import ConsignmentReconciliationChargeRecordAdditionType
from swagger_client.models.consignment_reconciliation_charge_type import ConsignmentReconciliationChargeType
from swagger_client.models.consignment_reconciliation_data import ConsignmentReconciliationData
from swagger_client.models.consignment_response_v2 import ConsignmentResponseV2
from swagger_client.models.consignment_response_v2_i_collection_base_domain_entity_v2 import ConsignmentResponseV2ICollectionBaseDomainEntityV2
from swagger_client.models.consignment_standard_item import ConsignmentStandardItem
from swagger_client.models.consignment_status_type import ConsignmentStatusType
from swagger_client.models.consignment_sub_dg_class_types import ConsignmentSubDgClassTypes
from swagger_client.models.consignment_surcharge import ConsignmentSurcharge
from swagger_client.models.consignment_surcharge_v2 import ConsignmentSurchargeV2
from swagger_client.models.consignment_to_consolidate import ConsignmentToConsolidate
from swagger_client.models.consignment_total import ConsignmentTotal
from swagger_client.models.consignment_tracking_history_v2 import ConsignmentTrackingHistoryV2
from swagger_client.models.consignment_tracking_status import ConsignmentTrackingStatus
from swagger_client.models.consignment_tracking_status_v2 import ConsignmentTrackingStatusV2
from swagger_client.models.consignment_v2 import ConsignmentV2
from swagger_client.models.consignment_v2_base_domain_entity_v2 import ConsignmentV2BaseDomainEntityV2
from swagger_client.models.consignment_v2_i_collection_base_domain_entity_v2 import ConsignmentV2ICollectionBaseDomainEntityV2
from swagger_client.models.consignments_for_list import ConsignmentsForList
from swagger_client.models.consignments_for_list_grid_domain_entity_v2 import ConsignmentsForListGridDomainEntityV2
from swagger_client.models.consignments_for_list_with_pending_consignment_ids import ConsignmentsForListWithPendingConsignmentIds
from swagger_client.models.consignments_for_list_with_pending_consignment_ids_grid_domain_entity_v2 import ConsignmentsForListWithPendingConsignmentIdsGridDomainEntityV2
from swagger_client.models.consolidated_consignment import ConsolidatedConsignment
from swagger_client.models.consolidation import Consolidation
from swagger_client.models.consolidation_default_route_selection import ConsolidationDefaultRouteSelection
from swagger_client.models.consolidation_error_handling import ConsolidationErrorHandling
from swagger_client.models.consolidation_options import ConsolidationOptions
from swagger_client.models.consolidation_request import ConsolidationRequest
from swagger_client.models.consolidation_results import ConsolidationResults
from swagger_client.models.consolidation_results_base_domain_entity_v2 import ConsolidationResultsBaseDomainEntityV2
from swagger_client.models.consolidation_target import ConsolidationTarget
from swagger_client.models.container_type import ContainerType
from swagger_client.models.country import Country
from swagger_client.models.country_type import CountryType
from swagger_client.models.create_consignment_combined_item_v2 import CreateConsignmentCombinedItemV2
from swagger_client.models.create_consignment_combined_load_size_item_v2 import CreateConsignmentCombinedLoadSizeItemV2
from swagger_client.models.create_consignment_complex_items_v2 import CreateConsignmentComplexItemsV2
from swagger_client.models.create_consignment_complex_items_v2_base_domain_entity_v2 import CreateConsignmentComplexItemsV2BaseDomainEntityV2
from swagger_client.models.create_consignment_existing_v2 import CreateConsignmentExistingV2
from swagger_client.models.create_consignment_item_complex_v2 import CreateConsignmentItemComplexV2
from swagger_client.models.create_consignment_item_content_v2 import CreateConsignmentItemContentV2
from swagger_client.models.create_consignment_item_dg_item_v2 import CreateConsignmentItemDgItemV2
from swagger_client.models.create_consignment_item_reference_v2 import CreateConsignmentItemReferenceV2
from swagger_client.models.create_consignment_item_v2 import CreateConsignmentItemV2
from swagger_client.models.create_consignment_response_consignment_surcharge_v2 import CreateConsignmentResponseConsignmentSurchargeV2
from swagger_client.models.create_consignment_response_v2 import CreateConsignmentResponseV2
from swagger_client.models.create_consignment_response_v2_base_domain_entity_v2 import CreateConsignmentResponseV2BaseDomainEntityV2
from swagger_client.models.create_consignment_standard_item_v2 import CreateConsignmentStandardItemV2
from swagger_client.models.create_consignment_v2 import CreateConsignmentV2
from swagger_client.models.create_identity_user_and_company_link import CreateIdentityUserAndCompanyLink
from swagger_client.models.create_identity_v2 import CreateIdentityV2
from swagger_client.models.create_pending_consignment_response import CreatePendingConsignmentResponse
from swagger_client.models.create_pending_consignment_response_base_domain_entity_v2 import CreatePendingConsignmentResponseBaseDomainEntityV2
from swagger_client.models.create_pending_consignment_v2 import CreatePendingConsignmentV2
from swagger_client.models.create_quote_complex_items_v2 import CreateQuoteComplexItemsV2
from swagger_client.models.create_quote_response_v2 import CreateQuoteResponseV2
from swagger_client.models.create_quote_response_v2_base_domain_entity_v2 import CreateQuoteResponseV2BaseDomainEntityV2
from swagger_client.models.create_quote_v2 import CreateQuoteV2
from swagger_client.models.custom_field_entity_field_type import CustomFieldEntityFieldType
from swagger_client.models.custom_field_set import CustomFieldSet
from swagger_client.models.custom_field_type import CustomFieldType
from swagger_client.models.custom_value import CustomValue
from swagger_client.models.dg_class import DgClass
from swagger_client.models.dg_class_type import DgClassType
from swagger_client.models.dg_un_number_flat import DgUnNumberFlat
from swagger_client.models.edit_consignment_item_complex_v2 import EditConsignmentItemComplexV2
from swagger_client.models.edit_consignment_v2 import EditConsignmentV2
from swagger_client.models.edit_consignment_v2_base_domain_entity_v2 import EditConsignmentV2BaseDomainEntityV2
from swagger_client.models.empty_domain_entity_v2 import EmptyDomainEntityV2
from swagger_client.models.enterprise_tier import EnterpriseTier
from swagger_client.models.entity_type import EntityType
from swagger_client.models.file_info import FileInfo
from swagger_client.models.file_info_base_domain_entity_v2 import FileInfoBaseDomainEntityV2
from swagger_client.models.finance_transaction_status import FinanceTransactionStatus
from swagger_client.models.group import Group
from swagger_client.models.hide_carrier_item_type_on_invoice_type import HideCarrierItemTypeOnInvoiceType
from swagger_client.models.i_consignment_item import IConsignmentItem
from swagger_client.models.identity import Identity
from swagger_client.models.identity_company_link import IdentityCompanyLink
from swagger_client.models.identity_company_link_setter_request import IdentityCompanyLinkSetterRequest
from swagger_client.models.identity_company_link_setter_request_object import IdentityCompanyLinkSetterRequestObject
from swagger_client.models.identity_company_unsetter import IdentityCompanyUnsetter
from swagger_client.models.identity_information import IdentityInformation
from swagger_client.models.identity_provider import IdentityProvider
from swagger_client.models.identity_provider_v2 import IdentityProviderV2
from swagger_client.models.identity_provider_v2_base_domain_entity_v2 import IdentityProviderV2BaseDomainEntityV2
from swagger_client.models.identity_provider_v2_i_collection_base_domain_entity_v2 import IdentityProviderV2ICollectionBaseDomainEntityV2
from swagger_client.models.identity_public_key_v2 import IdentityPublicKeyV2
from swagger_client.models.identity_public_key_v2_i_collection_base_domain_entity_v2 import IdentityPublicKeyV2ICollectionBaseDomainEntityV2
from swagger_client.models.identity_v2 import IdentityV2
from swagger_client.models.identity_v2_i_collection_base_domain_entity_v2 import IdentityV2ICollectionBaseDomainEntityV2
from swagger_client.models.ids_container import IdsContainer
from swagger_client.models.int32_base_domain_entity_v2 import Int32BaseDomainEntityV2
from swagger_client.models.international_enabled_type import InternationalEnabledType
from swagger_client.models.invoice import Invoice
from swagger_client.models.invoice_due_date_type import InvoiceDueDateType
from swagger_client.models.invoice_integration_type import InvoiceIntegrationType
from swagger_client.models.invoice_item import InvoiceItem
from swagger_client.models.invoice_item_v2 import InvoiceItemV2
from swagger_client.models.invoice_sending_type import InvoiceSendingType
from swagger_client.models.invoice_v2 import InvoiceV2
from swagger_client.models.invoice_v2_base_domain_entity_v2 import InvoiceV2BaseDomainEntityV2
from swagger_client.models.invoice_v2_lite import InvoiceV2Lite
from swagger_client.models.invoice_v2_lite_i_collection_base_domain_entity_v2 import InvoiceV2LiteICollectionBaseDomainEntityV2
from swagger_client.models.invoice_wrapping_type import InvoiceWrappingType
from swagger_client.models.item_label_request import ItemLabelRequest
from swagger_client.models.item_type import ItemType
from swagger_client.models.label_type import LabelType
from swagger_client.models.location import Location
from swagger_client.models.location_alias import LocationAlias
from swagger_client.models.location_search_options import LocationSearchOptions
from swagger_client.models.location_search_options_v2 import LocationSearchOptionsV2
from swagger_client.models.location_type import LocationType
from swagger_client.models.location_v2 import LocationV2
from swagger_client.models.location_v2_i_collection_base_domain_entity_v2 import LocationV2ICollectionBaseDomainEntityV2
from swagger_client.models.location_v2_i_enumerable_base_domain_entity_v2 import LocationV2IEnumerableBaseDomainEntityV2
from swagger_client.models.mach_key_value_pair import MachKeyValuePair
from swagger_client.models.machship_carrier_integration import MachshipCarrierIntegration
from swagger_client.models.machship_item_type import MachshipItemType
from swagger_client.models.machship_validation_result import MachshipValidationResult
from swagger_client.models.machship_validation_result_v2 import MachshipValidationResultV2
from swagger_client.models.machship_validation_type import MachshipValidationType
from swagger_client.models.manifest_for_list_consignment import ManifestForListConsignment
from swagger_client.models.manifest_for_list_with_consignments import ManifestForListWithConsignments
from swagger_client.models.manifest_for_list_with_consignments_grid_domain_entity_v2 import ManifestForListWithConsignmentsGridDomainEntityV2
from swagger_client.models.manifest_time_past_despatch_time_type import ManifestTimePastDespatchTimeType
from swagger_client.models.manual_tracking_status import ManualTrackingStatus
from swagger_client.models.markup_type import MarkupType
from swagger_client.models.note_model_v2 import NoteModelV2
from swagger_client.models.note_model_v2_i_enumerable_base_domain_entity_v2 import NoteModelV2IEnumerableBaseDomainEntityV2
from swagger_client.models.organisation import Organisation
from swagger_client.models.organisation_admin_user import OrganisationAdminUser
from swagger_client.models.organisation_deactivated_mode import OrganisationDeactivatedMode
from swagger_client.models.organisation_detail import OrganisationDetail
from swagger_client.models.organisation_detail_base_domain_entity_v2 import OrganisationDetailBaseDomainEntityV2
from swagger_client.models.organisation_details_for_grid import OrganisationDetailsForGrid
from swagger_client.models.organisation_details_for_grid_grid_domain_entity_v2 import OrganisationDetailsForGridGridDomainEntityV2
from swagger_client.models.organisation_information import OrganisationInformation
from swagger_client.models.organisation_link_detail import OrganisationLinkDetail
from swagger_client.models.organisation_link_detail_i_collection_base_domain_entity_v2 import OrganisationLinkDetailICollectionBaseDomainEntityV2
from swagger_client.models.organisation_link_request import OrganisationLinkRequest
from swagger_client.models.organisation_status import OrganisationStatus
from swagger_client.models.organisation_unlink_request import OrganisationUnlinkRequest
from swagger_client.models.packing_group import PackingGroup
from swagger_client.models.pending_consignment_item_content_v2 import PendingConsignmentItemContentV2
from swagger_client.models.pending_consignment_item_dg_item_v2 import PendingConsignmentItemDgItemV2
from swagger_client.models.pending_consignment_item_reference import PendingConsignmentItemReference
from swagger_client.models.pending_consignment_item_v2 import PendingConsignmentItemV2
from swagger_client.models.pending_consignment_v2 import PendingConsignmentV2
from swagger_client.models.pending_consignment_v2_base_domain_entity_v2 import PendingConsignmentV2BaseDomainEntityV2
from swagger_client.models.pending_consignment_v2_for_list import PendingConsignmentV2ForList
from swagger_client.models.pending_consignment_v2_for_list_grid_domain_entity_v2 import PendingConsignmentV2ForListGridDomainEntityV2
from swagger_client.models.pending_consignment_v2_i_collection_base_domain_entity_v2 import PendingConsignmentV2ICollectionBaseDomainEntityV2
from swagger_client.models.permanent_pickup import PermanentPickup
from swagger_client.models.permanent_pickup_carrier_service import PermanentPickupCarrierService
from swagger_client.models.permanent_pickup_link import PermanentPickupLink
from swagger_client.models.permanent_pickup_v2 import PermanentPickupV2
from swagger_client.models.permission_type import PermissionType
from swagger_client.models.pricing_mechanism_type import PricingMechanismType
from swagger_client.models.primary_reference_type import PrimaryReferenceType
from swagger_client.models.printer_lite import PrinterLite
from swagger_client.models.printer_status import PrinterStatus
from swagger_client.models.pro_rata_type import ProRataType
from swagger_client.models.question_lite import QuestionLite
from swagger_client.models.quote_for_list import QuoteForList
from swagger_client.models.quote_for_list_grid_domain_entity_v2 import QuoteForListGridDomainEntityV2
from swagger_client.models.quote_total_display_type import QuoteTotalDisplayType
from swagger_client.models.quote_v2 import QuoteV2
from swagger_client.models.quote_v2_base_domain_entity_v2 import QuoteV2BaseDomainEntityV2
from swagger_client.models.ratecard_lite import RatecardLite
from swagger_client.models.ratecard_version import RatecardVersion
from swagger_client.models.raw_location import RawLocation
from swagger_client.models.raw_locations_with_location_search_options import RawLocationsWithLocationSearchOptions
from swagger_client.models.raw_pending_consignment_details_v2 import RawPendingConsignmentDetailsV2
from swagger_client.models.receiver_account import ReceiverAccount
from swagger_client.models.rejection_type import RejectionType
from swagger_client.models.reprice_consignment_v2_model import RepriceConsignmentV2Model
from swagger_client.models.return_booked_manifest_v2 import ReturnBookedManifestV2
from swagger_client.models.return_booked_manifest_v2_i_collection_base_domain_entity_v2 import ReturnBookedManifestV2ICollectionBaseDomainEntityV2
from swagger_client.models.role import Role
from swagger_client.models.role_v2 import RoleV2
from swagger_client.models.role_v2_i_collection_base_domain_entity_v2 import RoleV2ICollectionBaseDomainEntityV2
from swagger_client.models.route_despatch_option_lite import RouteDespatchOptionLite
from swagger_client.models.route_request_complex_items_v2 import RouteRequestComplexItemsV2
from swagger_client.models.route_request_v2 import RouteRequestV2
from swagger_client.models.route_service_type import RouteServiceType
from swagger_client.models.routes_response_v2 import RoutesResponseV2
from swagger_client.models.routes_response_v2_array_base_domain_entity_v2 import RoutesResponseV2ArrayBaseDomainEntityV2
from swagger_client.models.routes_response_v2_base_domain_entity_v2 import RoutesResponseV2BaseDomainEntityV2
from swagger_client.models.routing_no_lane_rates_type import RoutingNoLaneRatesType
from swagger_client.models.sell_rate_type import SellRateType
from swagger_client.models.send_location_v2 import SendLocationV2
from swagger_client.models.send_to_printer_group import SendToPrinterGroup
from swagger_client.models.send_to_printer_model import SendToPrinterModel
from swagger_client.models.send_to_printer_model_base_domain_entity_v2 import SendToPrinterModelBaseDomainEntityV2
from swagger_client.models.send_to_printer_request import SendToPrinterRequest
from swagger_client.models.show_manifest_summary_type import ShowManifestSummaryType
from swagger_client.models.simple_note_with_create_data import SimpleNoteWithCreateData
from swagger_client.models.simple_route_v2 import SimpleRouteV2
from swagger_client.models.state import State
from swagger_client.models.string_base_domain_entity_v2 import StringBaseDomainEntityV2
from swagger_client.models.sub_component import SubComponent
from swagger_client.models.sub_component_type import SubComponentType
from swagger_client.models.sub_service import SubService
from swagger_client.models.surcharge import Surcharge
from swagger_client.models.surcharge_price_type import SurchargePriceType
from swagger_client.models.surcharge_v2 import SurchargeV2
from swagger_client.models.time_span import TimeSpan
from swagger_client.models.time_zone_model import TimeZoneModel
from swagger_client.models.tolerance_type import ToleranceType
from swagger_client.models.total_volume_calculation_type import TotalVolumeCalculationType
from swagger_client.models.tracking_page_type import TrackingPageType
from swagger_client.models.tracking_status import TrackingStatus
from swagger_client.models.tracking_type import TrackingType
from swagger_client.models.unmanifested_consignment_for_list import UnmanifestedConsignmentForList
from swagger_client.models.unmanifested_consignment_for_list_grid_domain_entity_v2 import UnmanifestedConsignmentForListGridDomainEntityV2
from swagger_client.models.user import User
from swagger_client.models.user_and_company_link import UserAndCompanyLink
from swagger_client.models.user_lite import UserLite
from swagger_client.models.user_test_mode_setting import UserTestModeSetting
from swagger_client.models.user_type import UserType
from swagger_client.models.user_with_identity import UserWithIdentity
from swagger_client.models.user_with_org_admin import UserWithOrgAdmin
from swagger_client.models.weight_pro_rata_calculation_type import WeightProRataCalculationType
from swagger_client.models.weight_rounding_type import WeightRoundingType
from swagger_client.models.zone_v2 import ZoneV2
