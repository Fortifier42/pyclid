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

class ConsignmentIdWithTrackingHistoryV2(object):
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
        'consignment_id': 'int',
        'status_history': 'list[ConsignmentTrackingHistoryV2]',
        'attachments': 'list[ConsignmentAttachmentDetailV2]'
    }

    attribute_map = {
        'consignment_id': 'consignmentId',
        'status_history': 'statusHistory',
        'attachments': 'attachments'
    }

    def __init__(self, consignment_id=None, status_history=None, attachments=None):  # noqa: E501
        """ConsignmentIdWithTrackingHistoryV2 - a model defined in Swagger"""  # noqa: E501
        self._consignment_id = None
        self._status_history = None
        self._attachments = None
        self.discriminator = None
        if consignment_id is not None:
            self.consignment_id = consignment_id
        if status_history is not None:
            self.status_history = status_history
        if attachments is not None:
            self.attachments = attachments

    @property
    def consignment_id(self):
        """Gets the consignment_id of this ConsignmentIdWithTrackingHistoryV2.  # noqa: E501


        :return: The consignment_id of this ConsignmentIdWithTrackingHistoryV2.  # noqa: E501
        :rtype: int
        """
        return self._consignment_id

    @consignment_id.setter
    def consignment_id(self, consignment_id):
        """Sets the consignment_id of this ConsignmentIdWithTrackingHistoryV2.


        :param consignment_id: The consignment_id of this ConsignmentIdWithTrackingHistoryV2.  # noqa: E501
        :type: int
        """

        self._consignment_id = consignment_id

    @property
    def status_history(self):
        """Gets the status_history of this ConsignmentIdWithTrackingHistoryV2.  # noqa: E501


        :return: The status_history of this ConsignmentIdWithTrackingHistoryV2.  # noqa: E501
        :rtype: list[ConsignmentTrackingHistoryV2]
        """
        return self._status_history

    @status_history.setter
    def status_history(self, status_history):
        """Sets the status_history of this ConsignmentIdWithTrackingHistoryV2.


        :param status_history: The status_history of this ConsignmentIdWithTrackingHistoryV2.  # noqa: E501
        :type: list[ConsignmentTrackingHistoryV2]
        """

        self._status_history = status_history

    @property
    def attachments(self):
        """Gets the attachments of this ConsignmentIdWithTrackingHistoryV2.  # noqa: E501


        :return: The attachments of this ConsignmentIdWithTrackingHistoryV2.  # noqa: E501
        :rtype: list[ConsignmentAttachmentDetailV2]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this ConsignmentIdWithTrackingHistoryV2.


        :param attachments: The attachments of this ConsignmentIdWithTrackingHistoryV2.  # noqa: E501
        :type: list[ConsignmentAttachmentDetailV2]
        """

        self._attachments = attachments

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
        if issubclass(ConsignmentIdWithTrackingHistoryV2, dict):
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
        if not isinstance(other, ConsignmentIdWithTrackingHistoryV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
