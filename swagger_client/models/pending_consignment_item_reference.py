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

class PendingConsignmentItemReference(object):
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
        'id': 'int',
        'pending_consignment_item_id': 'int',
        'carrier_item_reference': 'str',
        'item_number': 'int',
        'carrier_reference': 'str'
    }

    attribute_map = {
        'id': 'id',
        'pending_consignment_item_id': 'pendingConsignmentItemId',
        'carrier_item_reference': 'carrierItemReference',
        'item_number': 'itemNumber',
        'carrier_reference': 'carrierReference'
    }

    def __init__(self, id=None, pending_consignment_item_id=None, carrier_item_reference=None, item_number=None, carrier_reference=None):  # noqa: E501
        """PendingConsignmentItemReference - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._pending_consignment_item_id = None
        self._carrier_item_reference = None
        self._item_number = None
        self._carrier_reference = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if pending_consignment_item_id is not None:
            self.pending_consignment_item_id = pending_consignment_item_id
        if carrier_item_reference is not None:
            self.carrier_item_reference = carrier_item_reference
        if item_number is not None:
            self.item_number = item_number
        if carrier_reference is not None:
            self.carrier_reference = carrier_reference

    @property
    def id(self):
        """Gets the id of this PendingConsignmentItemReference.  # noqa: E501


        :return: The id of this PendingConsignmentItemReference.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PendingConsignmentItemReference.


        :param id: The id of this PendingConsignmentItemReference.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def pending_consignment_item_id(self):
        """Gets the pending_consignment_item_id of this PendingConsignmentItemReference.  # noqa: E501


        :return: The pending_consignment_item_id of this PendingConsignmentItemReference.  # noqa: E501
        :rtype: int
        """
        return self._pending_consignment_item_id

    @pending_consignment_item_id.setter
    def pending_consignment_item_id(self, pending_consignment_item_id):
        """Sets the pending_consignment_item_id of this PendingConsignmentItemReference.


        :param pending_consignment_item_id: The pending_consignment_item_id of this PendingConsignmentItemReference.  # noqa: E501
        :type: int
        """

        self._pending_consignment_item_id = pending_consignment_item_id

    @property
    def carrier_item_reference(self):
        """Gets the carrier_item_reference of this PendingConsignmentItemReference.  # noqa: E501


        :return: The carrier_item_reference of this PendingConsignmentItemReference.  # noqa: E501
        :rtype: str
        """
        return self._carrier_item_reference

    @carrier_item_reference.setter
    def carrier_item_reference(self, carrier_item_reference):
        """Sets the carrier_item_reference of this PendingConsignmentItemReference.


        :param carrier_item_reference: The carrier_item_reference of this PendingConsignmentItemReference.  # noqa: E501
        :type: str
        """

        self._carrier_item_reference = carrier_item_reference

    @property
    def item_number(self):
        """Gets the item_number of this PendingConsignmentItemReference.  # noqa: E501


        :return: The item_number of this PendingConsignmentItemReference.  # noqa: E501
        :rtype: int
        """
        return self._item_number

    @item_number.setter
    def item_number(self, item_number):
        """Sets the item_number of this PendingConsignmentItemReference.


        :param item_number: The item_number of this PendingConsignmentItemReference.  # noqa: E501
        :type: int
        """

        self._item_number = item_number

    @property
    def carrier_reference(self):
        """Gets the carrier_reference of this PendingConsignmentItemReference.  # noqa: E501


        :return: The carrier_reference of this PendingConsignmentItemReference.  # noqa: E501
        :rtype: str
        """
        return self._carrier_reference

    @carrier_reference.setter
    def carrier_reference(self, carrier_reference):
        """Sets the carrier_reference of this PendingConsignmentItemReference.


        :param carrier_reference: The carrier_reference of this PendingConsignmentItemReference.  # noqa: E501
        :type: str
        """

        self._carrier_reference = carrier_reference

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
        if issubclass(PendingConsignmentItemReference, dict):
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
        if not isinstance(other, PendingConsignmentItemReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other