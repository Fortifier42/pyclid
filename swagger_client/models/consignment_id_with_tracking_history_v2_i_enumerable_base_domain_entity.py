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

class ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity(object):
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
        'object': 'list[ConsignmentIdWithTrackingHistoryV2]',
        'errors': 'list[MachshipValidationResult]',
        'refresh_session': 'bool'
    }

    attribute_map = {
        'object': 'object',
        'errors': 'errors',
        'refresh_session': 'refreshSession'
    }

    def __init__(self, object=None, errors=None, refresh_session=None):  # noqa: E501
        """ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._errors = None
        self._refresh_session = None
        self.discriminator = None
        if object is not None:
            self.object = object
        if errors is not None:
            self.errors = errors
        if refresh_session is not None:
            self.refresh_session = refresh_session

    @property
    def object(self):
        """Gets the object of this ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity.  # noqa: E501


        :return: The object of this ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity.  # noqa: E501
        :rtype: list[ConsignmentIdWithTrackingHistoryV2]
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity.


        :param object: The object of this ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity.  # noqa: E501
        :type: list[ConsignmentIdWithTrackingHistoryV2]
        """

        self._object = object

    @property
    def errors(self):
        """Gets the errors of this ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity.  # noqa: E501


        :return: The errors of this ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity.  # noqa: E501
        :rtype: list[MachshipValidationResult]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity.


        :param errors: The errors of this ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity.  # noqa: E501
        :type: list[MachshipValidationResult]
        """

        self._errors = errors

    @property
    def refresh_session(self):
        """Gets the refresh_session of this ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity.  # noqa: E501


        :return: The refresh_session of this ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity.  # noqa: E501
        :rtype: bool
        """
        return self._refresh_session

    @refresh_session.setter
    def refresh_session(self, refresh_session):
        """Sets the refresh_session of this ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity.


        :param refresh_session: The refresh_session of this ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity.  # noqa: E501
        :type: bool
        """

        self._refresh_session = refresh_session

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
        if issubclass(ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity, dict):
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
        if not isinstance(other, ConsignmentIdWithTrackingHistoryV2IEnumerableBaseDomainEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
