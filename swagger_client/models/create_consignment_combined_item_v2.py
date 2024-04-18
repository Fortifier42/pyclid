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

class CreateConsignmentCombinedItemV2(object):
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
        'total_height': 'float',
        'total_length': 'float',
        'total_width': 'float',
        'total_weight': 'float',
        'heaviest_individual_item': 'float',
        'number_of_pieces': 'int'
    }

    attribute_map = {
        'total_height': 'totalHeight',
        'total_length': 'totalLength',
        'total_width': 'totalWidth',
        'total_weight': 'totalWeight',
        'heaviest_individual_item': 'heaviestIndividualItem',
        'number_of_pieces': 'numberOfPieces'
    }

    def __init__(self, total_height=None, total_length=None, total_width=None, total_weight=None, heaviest_individual_item=None, number_of_pieces=None):  # noqa: E501
        """CreateConsignmentCombinedItemV2 - a model defined in Swagger"""  # noqa: E501
        self._total_height = None
        self._total_length = None
        self._total_width = None
        self._total_weight = None
        self._heaviest_individual_item = None
        self._number_of_pieces = None
        self.discriminator = None
        if total_height is not None:
            self.total_height = total_height
        if total_length is not None:
            self.total_length = total_length
        if total_width is not None:
            self.total_width = total_width
        if total_weight is not None:
            self.total_weight = total_weight
        if heaviest_individual_item is not None:
            self.heaviest_individual_item = heaviest_individual_item
        if number_of_pieces is not None:
            self.number_of_pieces = number_of_pieces

    @property
    def total_height(self):
        """Gets the total_height of this CreateConsignmentCombinedItemV2.  # noqa: E501

        Total height in cm of the combined item  # noqa: E501

        :return: The total_height of this CreateConsignmentCombinedItemV2.  # noqa: E501
        :rtype: float
        """
        return self._total_height

    @total_height.setter
    def total_height(self, total_height):
        """Sets the total_height of this CreateConsignmentCombinedItemV2.

        Total height in cm of the combined item  # noqa: E501

        :param total_height: The total_height of this CreateConsignmentCombinedItemV2.  # noqa: E501
        :type: float
        """

        self._total_height = total_height

    @property
    def total_length(self):
        """Gets the total_length of this CreateConsignmentCombinedItemV2.  # noqa: E501

        Total length in cm of the combined item  # noqa: E501

        :return: The total_length of this CreateConsignmentCombinedItemV2.  # noqa: E501
        :rtype: float
        """
        return self._total_length

    @total_length.setter
    def total_length(self, total_length):
        """Sets the total_length of this CreateConsignmentCombinedItemV2.

        Total length in cm of the combined item  # noqa: E501

        :param total_length: The total_length of this CreateConsignmentCombinedItemV2.  # noqa: E501
        :type: float
        """

        self._total_length = total_length

    @property
    def total_width(self):
        """Gets the total_width of this CreateConsignmentCombinedItemV2.  # noqa: E501

        Total width in cm of the combined item  # noqa: E501

        :return: The total_width of this CreateConsignmentCombinedItemV2.  # noqa: E501
        :rtype: float
        """
        return self._total_width

    @total_width.setter
    def total_width(self, total_width):
        """Sets the total_width of this CreateConsignmentCombinedItemV2.

        Total width in cm of the combined item  # noqa: E501

        :param total_width: The total_width of this CreateConsignmentCombinedItemV2.  # noqa: E501
        :type: float
        """

        self._total_width = total_width

    @property
    def total_weight(self):
        """Gets the total_weight of this CreateConsignmentCombinedItemV2.  # noqa: E501

        Total weight in kg of the combined item  # noqa: E501

        :return: The total_weight of this CreateConsignmentCombinedItemV2.  # noqa: E501
        :rtype: float
        """
        return self._total_weight

    @total_weight.setter
    def total_weight(self, total_weight):
        """Sets the total_weight of this CreateConsignmentCombinedItemV2.

        Total weight in kg of the combined item  # noqa: E501

        :param total_weight: The total_weight of this CreateConsignmentCombinedItemV2.  # noqa: E501
        :type: float
        """

        self._total_weight = total_weight

    @property
    def heaviest_individual_item(self):
        """Gets the heaviest_individual_item of this CreateConsignmentCombinedItemV2.  # noqa: E501

        Weight in kg of the heaviest individual item that comprises the combined item  # noqa: E501

        :return: The heaviest_individual_item of this CreateConsignmentCombinedItemV2.  # noqa: E501
        :rtype: float
        """
        return self._heaviest_individual_item

    @heaviest_individual_item.setter
    def heaviest_individual_item(self, heaviest_individual_item):
        """Sets the heaviest_individual_item of this CreateConsignmentCombinedItemV2.

        Weight in kg of the heaviest individual item that comprises the combined item  # noqa: E501

        :param heaviest_individual_item: The heaviest_individual_item of this CreateConsignmentCombinedItemV2.  # noqa: E501
        :type: float
        """

        self._heaviest_individual_item = heaviest_individual_item

    @property
    def number_of_pieces(self):
        """Gets the number_of_pieces of this CreateConsignmentCombinedItemV2.  # noqa: E501

        Number of individual pieces that comprise the combined item  # noqa: E501

        :return: The number_of_pieces of this CreateConsignmentCombinedItemV2.  # noqa: E501
        :rtype: int
        """
        return self._number_of_pieces

    @number_of_pieces.setter
    def number_of_pieces(self, number_of_pieces):
        """Sets the number_of_pieces of this CreateConsignmentCombinedItemV2.

        Number of individual pieces that comprise the combined item  # noqa: E501

        :param number_of_pieces: The number_of_pieces of this CreateConsignmentCombinedItemV2.  # noqa: E501
        :type: int
        """

        self._number_of_pieces = number_of_pieces

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
        if issubclass(CreateConsignmentCombinedItemV2, dict):
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
        if not isinstance(other, CreateConsignmentCombinedItemV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other