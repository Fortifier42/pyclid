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

class ConsolidationResults(object):
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
        'company_id': 'int',
        'consignments': 'list[ConsolidatedConsignment]',
        'consolidation_performed': 'bool',
        'contains_pending_consignments': 'bool',
        'contains_unmanifested_consignments': 'bool',
        'validation_results': 'list[MachshipValidationResult]'
    }

    attribute_map = {
        'company_id': 'companyId',
        'consignments': 'consignments',
        'consolidation_performed': 'consolidationPerformed',
        'contains_pending_consignments': 'containsPendingConsignments',
        'contains_unmanifested_consignments': 'containsUnmanifestedConsignments',
        'validation_results': 'validationResults'
    }

    def __init__(self, company_id=None, consignments=None, consolidation_performed=None, contains_pending_consignments=None, contains_unmanifested_consignments=None, validation_results=None):  # noqa: E501
        """ConsolidationResults - a model defined in Swagger"""  # noqa: E501
        self._company_id = None
        self._consignments = None
        self._consolidation_performed = None
        self._contains_pending_consignments = None
        self._contains_unmanifested_consignments = None
        self._validation_results = None
        self.discriminator = None
        if company_id is not None:
            self.company_id = company_id
        if consignments is not None:
            self.consignments = consignments
        if consolidation_performed is not None:
            self.consolidation_performed = consolidation_performed
        if contains_pending_consignments is not None:
            self.contains_pending_consignments = contains_pending_consignments
        if contains_unmanifested_consignments is not None:
            self.contains_unmanifested_consignments = contains_unmanifested_consignments
        if validation_results is not None:
            self.validation_results = validation_results

    @property
    def company_id(self):
        """Gets the company_id of this ConsolidationResults.  # noqa: E501

        The Machship Company ID that consolidation should / has been performed against  # noqa: E501

        :return: The company_id of this ConsolidationResults.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this ConsolidationResults.

        The Machship Company ID that consolidation should / has been performed against  # noqa: E501

        :param company_id: The company_id of this ConsolidationResults.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def consignments(self):
        """Gets the consignments of this ConsolidationResults.  # noqa: E501

        The consolidated consignments and their details  # noqa: E501

        :return: The consignments of this ConsolidationResults.  # noqa: E501
        :rtype: list[ConsolidatedConsignment]
        """
        return self._consignments

    @consignments.setter
    def consignments(self, consignments):
        """Sets the consignments of this ConsolidationResults.

        The consolidated consignments and their details  # noqa: E501

        :param consignments: The consignments of this ConsolidationResults.  # noqa: E501
        :type: list[ConsolidatedConsignment]
        """

        self._consignments = consignments

    @property
    def consolidation_performed(self):
        """Gets the consolidation_performed of this ConsolidationResults.  # noqa: E501

        Whether or not consolidation has been performed and saved or if these results are merely indicative of  what will occur  # noqa: E501

        :return: The consolidation_performed of this ConsolidationResults.  # noqa: E501
        :rtype: bool
        """
        return self._consolidation_performed

    @consolidation_performed.setter
    def consolidation_performed(self, consolidation_performed):
        """Sets the consolidation_performed of this ConsolidationResults.

        Whether or not consolidation has been performed and saved or if these results are merely indicative of  what will occur  # noqa: E501

        :param consolidation_performed: The consolidation_performed of this ConsolidationResults.  # noqa: E501
        :type: bool
        """

        self._consolidation_performed = consolidation_performed

    @property
    def contains_pending_consignments(self):
        """Gets the contains_pending_consignments of this ConsolidationResults.  # noqa: E501

        Does the consolidation include any consignments that were pending consignments  # noqa: E501

        :return: The contains_pending_consignments of this ConsolidationResults.  # noqa: E501
        :rtype: bool
        """
        return self._contains_pending_consignments

    @contains_pending_consignments.setter
    def contains_pending_consignments(self, contains_pending_consignments):
        """Sets the contains_pending_consignments of this ConsolidationResults.

        Does the consolidation include any consignments that were pending consignments  # noqa: E501

        :param contains_pending_consignments: The contains_pending_consignments of this ConsolidationResults.  # noqa: E501
        :type: bool
        """

        self._contains_pending_consignments = contains_pending_consignments

    @property
    def contains_unmanifested_consignments(self):
        """Gets the contains_unmanifested_consignments of this ConsolidationResults.  # noqa: E501

        Does the consolidation include any consignments that were unmanifested (not pending) consignments  # noqa: E501

        :return: The contains_unmanifested_consignments of this ConsolidationResults.  # noqa: E501
        :rtype: bool
        """
        return self._contains_unmanifested_consignments

    @contains_unmanifested_consignments.setter
    def contains_unmanifested_consignments(self, contains_unmanifested_consignments):
        """Sets the contains_unmanifested_consignments of this ConsolidationResults.

        Does the consolidation include any consignments that were unmanifested (not pending) consignments  # noqa: E501

        :param contains_unmanifested_consignments: The contains_unmanifested_consignments of this ConsolidationResults.  # noqa: E501
        :type: bool
        """

        self._contains_unmanifested_consignments = contains_unmanifested_consignments

    @property
    def validation_results(self):
        """Gets the validation_results of this ConsolidationResults.  # noqa: E501

        A list of validation results from the consolidation process  # noqa: E501

        :return: The validation_results of this ConsolidationResults.  # noqa: E501
        :rtype: list[MachshipValidationResult]
        """
        return self._validation_results

    @validation_results.setter
    def validation_results(self, validation_results):
        """Sets the validation_results of this ConsolidationResults.

        A list of validation results from the consolidation process  # noqa: E501

        :param validation_results: The validation_results of this ConsolidationResults.  # noqa: E501
        :type: list[MachshipValidationResult]
        """

        self._validation_results = validation_results

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
        if issubclass(ConsolidationResults, dict):
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
        if not isinstance(other, ConsolidationResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
