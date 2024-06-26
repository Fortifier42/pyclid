# coding: utf-8

"""
    Machship API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ConsolidationOptions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'do_not_consolidate': 'bool',
        'company_id': 'int',
        'consolidation_target': 'ConsolidationTarget',
        'unmanifested_consignment_ids': 'list[int]',
        'pending_consignment_ids': 'list[int]',
        'group_by_carrier': 'bool',
        'group_by_service': 'bool',
        'group_by_reference_one': 'bool',
        'group_by_reference_two': 'bool',
        'group_by_despatch_date': 'bool',
        'default_route_selection': 'ConsolidationDefaultRouteSelection',
        'error_handling': 'ConsolidationErrorHandling',
        'prevent_future_date_consoldation': 'bool'
    }

    attribute_map = {
        'do_not_consolidate': 'doNotConsolidate',
        'company_id': 'companyId',
        'consolidation_target': 'consolidationTarget',
        'unmanifested_consignment_ids': 'unmanifestedConsignmentIds',
        'pending_consignment_ids': 'pendingConsignmentIds',
        'group_by_carrier': 'groupByCarrier',
        'group_by_service': 'groupByService',
        'group_by_reference_one': 'groupByReferenceOne',
        'group_by_reference_two': 'groupByReferenceTwo',
        'group_by_despatch_date': 'groupByDespatchDate',
        'default_route_selection': 'defaultRouteSelection',
        'error_handling': 'errorHandling',
        'prevent_future_date_consoldation': 'preventFutureDateConsoldation'
    }

    def __init__(self, do_not_consolidate=None, company_id=None, consolidation_target=None, unmanifested_consignment_ids=None, pending_consignment_ids=None, group_by_carrier=None, group_by_service=None, group_by_reference_one=None, group_by_reference_two=None, group_by_despatch_date=None, default_route_selection=None, error_handling=None, prevent_future_date_consoldation=None):  # noqa: E501
        """ConsolidationOptions - a model defined in Swagger"""  # noqa: E501
        self._do_not_consolidate = None
        self._company_id = None
        self._consolidation_target = None
        self._unmanifested_consignment_ids = None
        self._pending_consignment_ids = None
        self._group_by_carrier = None
        self._group_by_service = None
        self._group_by_reference_one = None
        self._group_by_reference_two = None
        self._group_by_despatch_date = None
        self._default_route_selection = None
        self._error_handling = None
        self._prevent_future_date_consoldation = None
        self.discriminator = None
        if do_not_consolidate is not None:
            self.do_not_consolidate = do_not_consolidate
        if company_id is not None:
            self.company_id = company_id
        if consolidation_target is not None:
            self.consolidation_target = consolidation_target
        if unmanifested_consignment_ids is not None:
            self.unmanifested_consignment_ids = unmanifested_consignment_ids
        if pending_consignment_ids is not None:
            self.pending_consignment_ids = pending_consignment_ids
        if group_by_carrier is not None:
            self.group_by_carrier = group_by_carrier
        if group_by_service is not None:
            self.group_by_service = group_by_service
        if group_by_reference_one is not None:
            self.group_by_reference_one = group_by_reference_one
        if group_by_reference_two is not None:
            self.group_by_reference_two = group_by_reference_two
        if group_by_despatch_date is not None:
            self.group_by_despatch_date = group_by_despatch_date
        if default_route_selection is not None:
            self.default_route_selection = default_route_selection
        if error_handling is not None:
            self.error_handling = error_handling
        if prevent_future_date_consoldation is not None:
            self.prevent_future_date_consoldation = prevent_future_date_consoldation

    @property
    def do_not_consolidate(self):
        """Gets the do_not_consolidate of this ConsolidationOptions.  # noqa: E501

        Set this flag to true when you do not want to consolidate, rather you just want the consignments to be returned to be abl  to perform a bulk update  # noqa: E501

        :return: The do_not_consolidate of this ConsolidationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._do_not_consolidate

    @do_not_consolidate.setter
    def do_not_consolidate(self, do_not_consolidate):
        """Sets the do_not_consolidate of this ConsolidationOptions.

        Set this flag to true when you do not want to consolidate, rather you just want the consignments to be returned to be abl  to perform a bulk update  # noqa: E501

        :param do_not_consolidate: The do_not_consolidate of this ConsolidationOptions.  # noqa: E501
        :type: bool
        """

        self._do_not_consolidate = do_not_consolidate

    @property
    def company_id(self):
        """Gets the company_id of this ConsolidationOptions.  # noqa: E501

        The Machship Company ID that consolidation should be performed for - if omitted it will be performed against the company  of the user performing consolidation  # noqa: E501

        :return: The company_id of this ConsolidationOptions.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this ConsolidationOptions.

        The Machship Company ID that consolidation should be performed for - if omitted it will be performed against the company  of the user performing consolidation  # noqa: E501

        :param company_id: The company_id of this ConsolidationOptions.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def consolidation_target(self):
        """Gets the consolidation_target of this ConsolidationOptions.  # noqa: E501


        :return: The consolidation_target of this ConsolidationOptions.  # noqa: E501
        :rtype: ConsolidationTarget
        """
        return self._consolidation_target

    @consolidation_target.setter
    def consolidation_target(self, consolidation_target):
        """Sets the consolidation_target of this ConsolidationOptions.


        :param consolidation_target: The consolidation_target of this ConsolidationOptions.  # noqa: E501
        :type: ConsolidationTarget
        """

        self._consolidation_target = consolidation_target

    @property
    def unmanifested_consignment_ids(self):
        """Gets the unmanifested_consignment_ids of this ConsolidationOptions.  # noqa: E501

        Optional - list of unmanifested consignment IDs to attempt to consolidate. Will not be considered if Machship.Common.Models.Consolidation.ConsolidationOptions.ConsolidationTarget is set to Machship.Common.Models.Consolidation.Enums.ConsolidationTarget.Pending.  If omitted all unmanifested consignments will be used to attempt consolidation.  # noqa: E501

        :return: The unmanifested_consignment_ids of this ConsolidationOptions.  # noqa: E501
        :rtype: list[int]
        """
        return self._unmanifested_consignment_ids

    @unmanifested_consignment_ids.setter
    def unmanifested_consignment_ids(self, unmanifested_consignment_ids):
        """Sets the unmanifested_consignment_ids of this ConsolidationOptions.

        Optional - list of unmanifested consignment IDs to attempt to consolidate. Will not be considered if Machship.Common.Models.Consolidation.ConsolidationOptions.ConsolidationTarget is set to Machship.Common.Models.Consolidation.Enums.ConsolidationTarget.Pending.  If omitted all unmanifested consignments will be used to attempt consolidation.  # noqa: E501

        :param unmanifested_consignment_ids: The unmanifested_consignment_ids of this ConsolidationOptions.  # noqa: E501
        :type: list[int]
        """

        self._unmanifested_consignment_ids = unmanifested_consignment_ids

    @property
    def pending_consignment_ids(self):
        """Gets the pending_consignment_ids of this ConsolidationOptions.  # noqa: E501

        Optional - list of pending consignment IDs to attempt to consolidate. Will not be considered if Machship.Common.Models.Consolidation.ConsolidationOptions.ConsolidationTarget is set to Machship.Common.Models.Consolidation.Enums.ConsolidationTarget.Unmanifested.  If omitted all pending consignments will be used to attempt consolidation.  # noqa: E501

        :return: The pending_consignment_ids of this ConsolidationOptions.  # noqa: E501
        :rtype: list[int]
        """
        return self._pending_consignment_ids

    @pending_consignment_ids.setter
    def pending_consignment_ids(self, pending_consignment_ids):
        """Sets the pending_consignment_ids of this ConsolidationOptions.

        Optional - list of pending consignment IDs to attempt to consolidate. Will not be considered if Machship.Common.Models.Consolidation.ConsolidationOptions.ConsolidationTarget is set to Machship.Common.Models.Consolidation.Enums.ConsolidationTarget.Unmanifested.  If omitted all pending consignments will be used to attempt consolidation.  # noqa: E501

        :param pending_consignment_ids: The pending_consignment_ids of this ConsolidationOptions.  # noqa: E501
        :type: list[int]
        """

        self._pending_consignment_ids = pending_consignment_ids

    @property
    def group_by_carrier(self):
        """Gets the group_by_carrier of this ConsolidationOptions.  # noqa: E501

        Whether the carrier will be considered when consolidating consignments  # noqa: E501

        :return: The group_by_carrier of this ConsolidationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._group_by_carrier

    @group_by_carrier.setter
    def group_by_carrier(self, group_by_carrier):
        """Sets the group_by_carrier of this ConsolidationOptions.

        Whether the carrier will be considered when consolidating consignments  # noqa: E501

        :param group_by_carrier: The group_by_carrier of this ConsolidationOptions.  # noqa: E501
        :type: bool
        """

        self._group_by_carrier = group_by_carrier

    @property
    def group_by_service(self):
        """Gets the group_by_service of this ConsolidationOptions.  # noqa: E501

        Whether the service will be considered when consolidating consignments (only relevant when Machship.Common.Models.Consolidation.ConsolidationOptions.GroupByCarrier is also set to true)  # noqa: E501

        :return: The group_by_service of this ConsolidationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._group_by_service

    @group_by_service.setter
    def group_by_service(self, group_by_service):
        """Sets the group_by_service of this ConsolidationOptions.

        Whether the service will be considered when consolidating consignments (only relevant when Machship.Common.Models.Consolidation.ConsolidationOptions.GroupByCarrier is also set to true)  # noqa: E501

        :param group_by_service: The group_by_service of this ConsolidationOptions.  # noqa: E501
        :type: bool
        """

        self._group_by_service = group_by_service

    @property
    def group_by_reference_one(self):
        """Gets the group_by_reference_one of this ConsolidationOptions.  # noqa: E501

        Whether the first customer reference be used when grouping consignments for consolidation  # noqa: E501

        :return: The group_by_reference_one of this ConsolidationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._group_by_reference_one

    @group_by_reference_one.setter
    def group_by_reference_one(self, group_by_reference_one):
        """Sets the group_by_reference_one of this ConsolidationOptions.

        Whether the first customer reference be used when grouping consignments for consolidation  # noqa: E501

        :param group_by_reference_one: The group_by_reference_one of this ConsolidationOptions.  # noqa: E501
        :type: bool
        """

        self._group_by_reference_one = group_by_reference_one

    @property
    def group_by_reference_two(self):
        """Gets the group_by_reference_two of this ConsolidationOptions.  # noqa: E501

        Whether the second customer reference be used when grouping consignments for consolidation  # noqa: E501

        :return: The group_by_reference_two of this ConsolidationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._group_by_reference_two

    @group_by_reference_two.setter
    def group_by_reference_two(self, group_by_reference_two):
        """Sets the group_by_reference_two of this ConsolidationOptions.

        Whether the second customer reference be used when grouping consignments for consolidation  # noqa: E501

        :param group_by_reference_two: The group_by_reference_two of this ConsolidationOptions.  # noqa: E501
        :type: bool
        """

        self._group_by_reference_two = group_by_reference_two

    @property
    def group_by_despatch_date(self):
        """Gets the group_by_despatch_date of this ConsolidationOptions.  # noqa: E501

        Whether the despatch date be used when grouping consignments for consolidation  # noqa: E501

        :return: The group_by_despatch_date of this ConsolidationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._group_by_despatch_date

    @group_by_despatch_date.setter
    def group_by_despatch_date(self, group_by_despatch_date):
        """Sets the group_by_despatch_date of this ConsolidationOptions.

        Whether the despatch date be used when grouping consignments for consolidation  # noqa: E501

        :param group_by_despatch_date: The group_by_despatch_date of this ConsolidationOptions.  # noqa: E501
        :type: bool
        """

        self._group_by_despatch_date = group_by_despatch_date

    @property
    def default_route_selection(self):
        """Gets the default_route_selection of this ConsolidationOptions.  # noqa: E501


        :return: The default_route_selection of this ConsolidationOptions.  # noqa: E501
        :rtype: ConsolidationDefaultRouteSelection
        """
        return self._default_route_selection

    @default_route_selection.setter
    def default_route_selection(self, default_route_selection):
        """Sets the default_route_selection of this ConsolidationOptions.


        :param default_route_selection: The default_route_selection of this ConsolidationOptions.  # noqa: E501
        :type: ConsolidationDefaultRouteSelection
        """

        self._default_route_selection = default_route_selection

    @property
    def error_handling(self):
        """Gets the error_handling of this ConsolidationOptions.  # noqa: E501


        :return: The error_handling of this ConsolidationOptions.  # noqa: E501
        :rtype: ConsolidationErrorHandling
        """
        return self._error_handling

    @error_handling.setter
    def error_handling(self, error_handling):
        """Sets the error_handling of this ConsolidationOptions.


        :param error_handling: The error_handling of this ConsolidationOptions.  # noqa: E501
        :type: ConsolidationErrorHandling
        """

        self._error_handling = error_handling

    @property
    def prevent_future_date_consoldation(self):
        """Gets the prevent_future_date_consoldation of this ConsolidationOptions.  # noqa: E501


        :return: The prevent_future_date_consoldation of this ConsolidationOptions.  # noqa: E501
        :rtype: bool
        """
        return self._prevent_future_date_consoldation

    @prevent_future_date_consoldation.setter
    def prevent_future_date_consoldation(self, prevent_future_date_consoldation):
        """Sets the prevent_future_date_consoldation of this ConsolidationOptions.


        :param prevent_future_date_consoldation: The prevent_future_date_consoldation of this ConsolidationOptions.  # noqa: E501
        :type: bool
        """

        self._prevent_future_date_consoldation = prevent_future_date_consoldation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConsolidationOptions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConsolidationOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
