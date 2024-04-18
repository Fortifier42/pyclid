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

class CarrierItemType(object):
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
        'carrier_id': 'int',
        'carrier': 'Carrier',
        'name': 'str',
        'abbreviation': 'str',
        'display_name': 'str',
        'order': 'int',
        'min_length': 'float',
        'max_length': 'float',
        'min_width': 'float',
        'max_width': 'float',
        'min_height': 'float',
        'max_height': 'float',
        'min_weight': 'float',
        'max_weight': 'float',
        'min_volume': 'float',
        'max_volume': 'float',
        'min_cubic_weight': 'float',
        'max_cubic_weight': 'float',
        'can_exceed_weight': 'bool',
        'can_exceed_height': 'bool',
        'can_exceed_length': 'bool',
        'can_exceed_width': 'bool',
        'can_exceed_volume': 'bool',
        'can_exceed_cubic_weight': 'bool',
        'total': 'int',
        'carrier_item_type_linked_item_types': 'list[CarrierItemTypeLinkedItemType]'
    }

    attribute_map = {
        'id': 'id',
        'carrier_id': 'carrierId',
        'carrier': 'carrier',
        'name': 'name',
        'abbreviation': 'abbreviation',
        'display_name': 'displayName',
        'order': 'order',
        'min_length': 'minLength',
        'max_length': 'maxLength',
        'min_width': 'minWidth',
        'max_width': 'maxWidth',
        'min_height': 'minHeight',
        'max_height': 'maxHeight',
        'min_weight': 'minWeight',
        'max_weight': 'maxWeight',
        'min_volume': 'minVolume',
        'max_volume': 'maxVolume',
        'min_cubic_weight': 'minCubicWeight',
        'max_cubic_weight': 'maxCubicWeight',
        'can_exceed_weight': 'canExceedWeight',
        'can_exceed_height': 'canExceedHeight',
        'can_exceed_length': 'canExceedLength',
        'can_exceed_width': 'canExceedWidth',
        'can_exceed_volume': 'canExceedVolume',
        'can_exceed_cubic_weight': 'canExceedCubicWeight',
        'total': 'total',
        'carrier_item_type_linked_item_types': 'carrierItemTypeLinkedItemTypes'
    }

    def __init__(self, id=None, carrier_id=None, carrier=None, name=None, abbreviation=None, display_name=None, order=None, min_length=None, max_length=None, min_width=None, max_width=None, min_height=None, max_height=None, min_weight=None, max_weight=None, min_volume=None, max_volume=None, min_cubic_weight=None, max_cubic_weight=None, can_exceed_weight=None, can_exceed_height=None, can_exceed_length=None, can_exceed_width=None, can_exceed_volume=None, can_exceed_cubic_weight=None, total=None, carrier_item_type_linked_item_types=None):  # noqa: E501
        """CarrierItemType - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._carrier_id = None
        self._carrier = None
        self._name = None
        self._abbreviation = None
        self._display_name = None
        self._order = None
        self._min_length = None
        self._max_length = None
        self._min_width = None
        self._max_width = None
        self._min_height = None
        self._max_height = None
        self._min_weight = None
        self._max_weight = None
        self._min_volume = None
        self._max_volume = None
        self._min_cubic_weight = None
        self._max_cubic_weight = None
        self._can_exceed_weight = None
        self._can_exceed_height = None
        self._can_exceed_length = None
        self._can_exceed_width = None
        self._can_exceed_volume = None
        self._can_exceed_cubic_weight = None
        self._total = None
        self._carrier_item_type_linked_item_types = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if carrier_id is not None:
            self.carrier_id = carrier_id
        if carrier is not None:
            self.carrier = carrier
        self.name = name
        self.abbreviation = abbreviation
        if display_name is not None:
            self.display_name = display_name
        if order is not None:
            self.order = order
        if min_length is not None:
            self.min_length = min_length
        if max_length is not None:
            self.max_length = max_length
        if min_width is not None:
            self.min_width = min_width
        if max_width is not None:
            self.max_width = max_width
        if min_height is not None:
            self.min_height = min_height
        if max_height is not None:
            self.max_height = max_height
        if min_weight is not None:
            self.min_weight = min_weight
        if max_weight is not None:
            self.max_weight = max_weight
        if min_volume is not None:
            self.min_volume = min_volume
        if max_volume is not None:
            self.max_volume = max_volume
        if min_cubic_weight is not None:
            self.min_cubic_weight = min_cubic_weight
        if max_cubic_weight is not None:
            self.max_cubic_weight = max_cubic_weight
        if can_exceed_weight is not None:
            self.can_exceed_weight = can_exceed_weight
        if can_exceed_height is not None:
            self.can_exceed_height = can_exceed_height
        if can_exceed_length is not None:
            self.can_exceed_length = can_exceed_length
        if can_exceed_width is not None:
            self.can_exceed_width = can_exceed_width
        if can_exceed_volume is not None:
            self.can_exceed_volume = can_exceed_volume
        if can_exceed_cubic_weight is not None:
            self.can_exceed_cubic_weight = can_exceed_cubic_weight
        if total is not None:
            self.total = total
        if carrier_item_type_linked_item_types is not None:
            self.carrier_item_type_linked_item_types = carrier_item_type_linked_item_types

    @property
    def id(self):
        """Gets the id of this CarrierItemType.  # noqa: E501


        :return: The id of this CarrierItemType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CarrierItemType.


        :param id: The id of this CarrierItemType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def carrier_id(self):
        """Gets the carrier_id of this CarrierItemType.  # noqa: E501


        :return: The carrier_id of this CarrierItemType.  # noqa: E501
        :rtype: int
        """
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, carrier_id):
        """Sets the carrier_id of this CarrierItemType.


        :param carrier_id: The carrier_id of this CarrierItemType.  # noqa: E501
        :type: int
        """

        self._carrier_id = carrier_id

    @property
    def carrier(self):
        """Gets the carrier of this CarrierItemType.  # noqa: E501


        :return: The carrier of this CarrierItemType.  # noqa: E501
        :rtype: Carrier
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this CarrierItemType.


        :param carrier: The carrier of this CarrierItemType.  # noqa: E501
        :type: Carrier
        """

        self._carrier = carrier

    @property
    def name(self):
        """Gets the name of this CarrierItemType.  # noqa: E501


        :return: The name of this CarrierItemType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CarrierItemType.


        :param name: The name of this CarrierItemType.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this CarrierItemType.  # noqa: E501


        :return: The abbreviation of this CarrierItemType.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this CarrierItemType.


        :param abbreviation: The abbreviation of this CarrierItemType.  # noqa: E501
        :type: str
        """
        if abbreviation is None:
            raise ValueError("Invalid value for `abbreviation`, must not be `None`")  # noqa: E501

        self._abbreviation = abbreviation

    @property
    def display_name(self):
        """Gets the display_name of this CarrierItemType.  # noqa: E501


        :return: The display_name of this CarrierItemType.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CarrierItemType.


        :param display_name: The display_name of this CarrierItemType.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def order(self):
        """Gets the order of this CarrierItemType.  # noqa: E501

        This is the order that the these items are assigned for a given carrier.  The lower the number, the \"smaller\" the item is.  This is used to determine which item type is used when converting consingment items to carrier items.  ie. if an item can be a carton or a large carton, the carton order is lower so the carton is selected.    Pro rataing is only considered if an item is bigger then the largest carrier item (ie. item with the largest order)  # noqa: E501

        :return: The order of this CarrierItemType.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CarrierItemType.

        This is the order that the these items are assigned for a given carrier.  The lower the number, the \"smaller\" the item is.  This is used to determine which item type is used when converting consingment items to carrier items.  ie. if an item can be a carton or a large carton, the carton order is lower so the carton is selected.    Pro rataing is only considered if an item is bigger then the largest carrier item (ie. item with the largest order)  # noqa: E501

        :param order: The order of this CarrierItemType.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def min_length(self):
        """Gets the min_length of this CarrierItemType.  # noqa: E501


        :return: The min_length of this CarrierItemType.  # noqa: E501
        :rtype: float
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this CarrierItemType.


        :param min_length: The min_length of this CarrierItemType.  # noqa: E501
        :type: float
        """

        self._min_length = min_length

    @property
    def max_length(self):
        """Gets the max_length of this CarrierItemType.  # noqa: E501


        :return: The max_length of this CarrierItemType.  # noqa: E501
        :rtype: float
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this CarrierItemType.


        :param max_length: The max_length of this CarrierItemType.  # noqa: E501
        :type: float
        """

        self._max_length = max_length

    @property
    def min_width(self):
        """Gets the min_width of this CarrierItemType.  # noqa: E501


        :return: The min_width of this CarrierItemType.  # noqa: E501
        :rtype: float
        """
        return self._min_width

    @min_width.setter
    def min_width(self, min_width):
        """Sets the min_width of this CarrierItemType.


        :param min_width: The min_width of this CarrierItemType.  # noqa: E501
        :type: float
        """

        self._min_width = min_width

    @property
    def max_width(self):
        """Gets the max_width of this CarrierItemType.  # noqa: E501


        :return: The max_width of this CarrierItemType.  # noqa: E501
        :rtype: float
        """
        return self._max_width

    @max_width.setter
    def max_width(self, max_width):
        """Sets the max_width of this CarrierItemType.


        :param max_width: The max_width of this CarrierItemType.  # noqa: E501
        :type: float
        """

        self._max_width = max_width

    @property
    def min_height(self):
        """Gets the min_height of this CarrierItemType.  # noqa: E501


        :return: The min_height of this CarrierItemType.  # noqa: E501
        :rtype: float
        """
        return self._min_height

    @min_height.setter
    def min_height(self, min_height):
        """Sets the min_height of this CarrierItemType.


        :param min_height: The min_height of this CarrierItemType.  # noqa: E501
        :type: float
        """

        self._min_height = min_height

    @property
    def max_height(self):
        """Gets the max_height of this CarrierItemType.  # noqa: E501


        :return: The max_height of this CarrierItemType.  # noqa: E501
        :rtype: float
        """
        return self._max_height

    @max_height.setter
    def max_height(self, max_height):
        """Sets the max_height of this CarrierItemType.


        :param max_height: The max_height of this CarrierItemType.  # noqa: E501
        :type: float
        """

        self._max_height = max_height

    @property
    def min_weight(self):
        """Gets the min_weight of this CarrierItemType.  # noqa: E501


        :return: The min_weight of this CarrierItemType.  # noqa: E501
        :rtype: float
        """
        return self._min_weight

    @min_weight.setter
    def min_weight(self, min_weight):
        """Sets the min_weight of this CarrierItemType.


        :param min_weight: The min_weight of this CarrierItemType.  # noqa: E501
        :type: float
        """

        self._min_weight = min_weight

    @property
    def max_weight(self):
        """Gets the max_weight of this CarrierItemType.  # noqa: E501


        :return: The max_weight of this CarrierItemType.  # noqa: E501
        :rtype: float
        """
        return self._max_weight

    @max_weight.setter
    def max_weight(self, max_weight):
        """Sets the max_weight of this CarrierItemType.


        :param max_weight: The max_weight of this CarrierItemType.  # noqa: E501
        :type: float
        """

        self._max_weight = max_weight

    @property
    def min_volume(self):
        """Gets the min_volume of this CarrierItemType.  # noqa: E501


        :return: The min_volume of this CarrierItemType.  # noqa: E501
        :rtype: float
        """
        return self._min_volume

    @min_volume.setter
    def min_volume(self, min_volume):
        """Sets the min_volume of this CarrierItemType.


        :param min_volume: The min_volume of this CarrierItemType.  # noqa: E501
        :type: float
        """

        self._min_volume = min_volume

    @property
    def max_volume(self):
        """Gets the max_volume of this CarrierItemType.  # noqa: E501


        :return: The max_volume of this CarrierItemType.  # noqa: E501
        :rtype: float
        """
        return self._max_volume

    @max_volume.setter
    def max_volume(self, max_volume):
        """Sets the max_volume of this CarrierItemType.


        :param max_volume: The max_volume of this CarrierItemType.  # noqa: E501
        :type: float
        """

        self._max_volume = max_volume

    @property
    def min_cubic_weight(self):
        """Gets the min_cubic_weight of this CarrierItemType.  # noqa: E501


        :return: The min_cubic_weight of this CarrierItemType.  # noqa: E501
        :rtype: float
        """
        return self._min_cubic_weight

    @min_cubic_weight.setter
    def min_cubic_weight(self, min_cubic_weight):
        """Sets the min_cubic_weight of this CarrierItemType.


        :param min_cubic_weight: The min_cubic_weight of this CarrierItemType.  # noqa: E501
        :type: float
        """

        self._min_cubic_weight = min_cubic_weight

    @property
    def max_cubic_weight(self):
        """Gets the max_cubic_weight of this CarrierItemType.  # noqa: E501


        :return: The max_cubic_weight of this CarrierItemType.  # noqa: E501
        :rtype: float
        """
        return self._max_cubic_weight

    @max_cubic_weight.setter
    def max_cubic_weight(self, max_cubic_weight):
        """Sets the max_cubic_weight of this CarrierItemType.


        :param max_cubic_weight: The max_cubic_weight of this CarrierItemType.  # noqa: E501
        :type: float
        """

        self._max_cubic_weight = max_cubic_weight

    @property
    def can_exceed_weight(self):
        """Gets the can_exceed_weight of this CarrierItemType.  # noqa: E501


        :return: The can_exceed_weight of this CarrierItemType.  # noqa: E501
        :rtype: bool
        """
        return self._can_exceed_weight

    @can_exceed_weight.setter
    def can_exceed_weight(self, can_exceed_weight):
        """Sets the can_exceed_weight of this CarrierItemType.


        :param can_exceed_weight: The can_exceed_weight of this CarrierItemType.  # noqa: E501
        :type: bool
        """

        self._can_exceed_weight = can_exceed_weight

    @property
    def can_exceed_height(self):
        """Gets the can_exceed_height of this CarrierItemType.  # noqa: E501


        :return: The can_exceed_height of this CarrierItemType.  # noqa: E501
        :rtype: bool
        """
        return self._can_exceed_height

    @can_exceed_height.setter
    def can_exceed_height(self, can_exceed_height):
        """Sets the can_exceed_height of this CarrierItemType.


        :param can_exceed_height: The can_exceed_height of this CarrierItemType.  # noqa: E501
        :type: bool
        """

        self._can_exceed_height = can_exceed_height

    @property
    def can_exceed_length(self):
        """Gets the can_exceed_length of this CarrierItemType.  # noqa: E501


        :return: The can_exceed_length of this CarrierItemType.  # noqa: E501
        :rtype: bool
        """
        return self._can_exceed_length

    @can_exceed_length.setter
    def can_exceed_length(self, can_exceed_length):
        """Sets the can_exceed_length of this CarrierItemType.


        :param can_exceed_length: The can_exceed_length of this CarrierItemType.  # noqa: E501
        :type: bool
        """

        self._can_exceed_length = can_exceed_length

    @property
    def can_exceed_width(self):
        """Gets the can_exceed_width of this CarrierItemType.  # noqa: E501


        :return: The can_exceed_width of this CarrierItemType.  # noqa: E501
        :rtype: bool
        """
        return self._can_exceed_width

    @can_exceed_width.setter
    def can_exceed_width(self, can_exceed_width):
        """Sets the can_exceed_width of this CarrierItemType.


        :param can_exceed_width: The can_exceed_width of this CarrierItemType.  # noqa: E501
        :type: bool
        """

        self._can_exceed_width = can_exceed_width

    @property
    def can_exceed_volume(self):
        """Gets the can_exceed_volume of this CarrierItemType.  # noqa: E501


        :return: The can_exceed_volume of this CarrierItemType.  # noqa: E501
        :rtype: bool
        """
        return self._can_exceed_volume

    @can_exceed_volume.setter
    def can_exceed_volume(self, can_exceed_volume):
        """Sets the can_exceed_volume of this CarrierItemType.


        :param can_exceed_volume: The can_exceed_volume of this CarrierItemType.  # noqa: E501
        :type: bool
        """

        self._can_exceed_volume = can_exceed_volume

    @property
    def can_exceed_cubic_weight(self):
        """Gets the can_exceed_cubic_weight of this CarrierItemType.  # noqa: E501


        :return: The can_exceed_cubic_weight of this CarrierItemType.  # noqa: E501
        :rtype: bool
        """
        return self._can_exceed_cubic_weight

    @can_exceed_cubic_weight.setter
    def can_exceed_cubic_weight(self, can_exceed_cubic_weight):
        """Sets the can_exceed_cubic_weight of this CarrierItemType.


        :param can_exceed_cubic_weight: The can_exceed_cubic_weight of this CarrierItemType.  # noqa: E501
        :type: bool
        """

        self._can_exceed_cubic_weight = can_exceed_cubic_weight

    @property
    def total(self):
        """Gets the total of this CarrierItemType.  # noqa: E501


        :return: The total of this CarrierItemType.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CarrierItemType.


        :param total: The total of this CarrierItemType.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def carrier_item_type_linked_item_types(self):
        """Gets the carrier_item_type_linked_item_types of this CarrierItemType.  # noqa: E501


        :return: The carrier_item_type_linked_item_types of this CarrierItemType.  # noqa: E501
        :rtype: list[CarrierItemTypeLinkedItemType]
        """
        return self._carrier_item_type_linked_item_types

    @carrier_item_type_linked_item_types.setter
    def carrier_item_type_linked_item_types(self, carrier_item_type_linked_item_types):
        """Sets the carrier_item_type_linked_item_types of this CarrierItemType.


        :param carrier_item_type_linked_item_types: The carrier_item_type_linked_item_types of this CarrierItemType.  # noqa: E501
        :type: list[CarrierItemTypeLinkedItemType]
        """

        self._carrier_item_type_linked_item_types = carrier_item_type_linked_item_types

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
        if issubclass(CarrierItemType, dict):
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
        if not isinstance(other, CarrierItemType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other