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

class CompanyItemV2(object):
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
        'item_type': 'ItemType',
        'name': 'str',
        'sku': 'str',
        'quantity': 'int',
        'height': 'float',
        'weight': 'float',
        'length': 'float',
        'width': 'float'
    }

    attribute_map = {
        'id': 'id',
        'item_type': 'itemType',
        'name': 'name',
        'sku': 'sku',
        'quantity': 'quantity',
        'height': 'height',
        'weight': 'weight',
        'length': 'length',
        'width': 'width'
    }

    def __init__(self, id=None, item_type=None, name=None, sku=None, quantity=None, height=None, weight=None, length=None, width=None):  # noqa: E501
        """CompanyItemV2 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._item_type = None
        self._name = None
        self._sku = None
        self._quantity = None
        self._height = None
        self._weight = None
        self._length = None
        self._width = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.item_type = item_type
        self.name = name
        if sku is not None:
            self.sku = sku
        self.quantity = quantity
        self.height = height
        self.weight = weight
        self.length = length
        self.width = width

    @property
    def id(self):
        """Gets the id of this CompanyItemV2.  # noqa: E501

        The Machship Id for this item  # noqa: E501

        :return: The id of this CompanyItemV2.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompanyItemV2.

        The Machship Id for this item  # noqa: E501

        :param id: The id of this CompanyItemV2.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def item_type(self):
        """Gets the item_type of this CompanyItemV2.  # noqa: E501


        :return: The item_type of this CompanyItemV2.  # noqa: E501
        :rtype: ItemType
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """Sets the item_type of this CompanyItemV2.


        :param item_type: The item_type of this CompanyItemV2.  # noqa: E501
        :type: ItemType
        """
        if item_type is None:
            raise ValueError("Invalid value for `item_type`, must not be `None`")  # noqa: E501

        self._item_type = item_type

    @property
    def name(self):
        """Gets the name of this CompanyItemV2.  # noqa: E501

        Name or description of the goods you are sending  # noqa: E501

        :return: The name of this CompanyItemV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CompanyItemV2.

        Name or description of the goods you are sending  # noqa: E501

        :param name: The name of this CompanyItemV2.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def sku(self):
        """Gets the sku of this CompanyItemV2.  # noqa: E501

        Optional: the SKU or code of the item you are sending  # noqa: E501

        :return: The sku of this CompanyItemV2.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this CompanyItemV2.

        Optional: the SKU or code of the item you are sending  # noqa: E501

        :param sku: The sku of this CompanyItemV2.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def quantity(self):
        """Gets the quantity of this CompanyItemV2.  # noqa: E501

        Number of items  # noqa: E501

        :return: The quantity of this CompanyItemV2.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CompanyItemV2.

        Number of items  # noqa: E501

        :param quantity: The quantity of this CompanyItemV2.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def height(self):
        """Gets the height of this CompanyItemV2.  # noqa: E501

        Height of the item in cm  # noqa: E501

        :return: The height of this CompanyItemV2.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CompanyItemV2.

        Height of the item in cm  # noqa: E501

        :param height: The height of this CompanyItemV2.  # noqa: E501
        :type: float
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def weight(self):
        """Gets the weight of this CompanyItemV2.  # noqa: E501

        Weight of the item in kg  # noqa: E501

        :return: The weight of this CompanyItemV2.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this CompanyItemV2.

        Weight of the item in kg  # noqa: E501

        :param weight: The weight of this CompanyItemV2.  # noqa: E501
        :type: float
        """
        if weight is None:
            raise ValueError("Invalid value for `weight`, must not be `None`")  # noqa: E501

        self._weight = weight

    @property
    def length(self):
        """Gets the length of this CompanyItemV2.  # noqa: E501

        Length of the item in cm  # noqa: E501

        :return: The length of this CompanyItemV2.  # noqa: E501
        :rtype: float
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this CompanyItemV2.

        Length of the item in cm  # noqa: E501

        :param length: The length of this CompanyItemV2.  # noqa: E501
        :type: float
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def width(self):
        """Gets the width of this CompanyItemV2.  # noqa: E501

        Width of the item in cm  # noqa: E501

        :return: The width of this CompanyItemV2.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this CompanyItemV2.

        Width of the item in cm  # noqa: E501

        :param width: The width of this CompanyItemV2.  # noqa: E501
        :type: float
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

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
        if issubclass(CompanyItemV2, dict):
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
        if not isinstance(other, CompanyItemV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
