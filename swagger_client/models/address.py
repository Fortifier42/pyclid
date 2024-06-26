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

class Address(object):
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
        'name': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'location': 'Location',
        'contact': 'str',
        'phone': 'str',
        'email': 'str'
    }

    attribute_map = {
        'name': 'name',
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'location': 'location',
        'contact': 'contact',
        'phone': 'phone',
        'email': 'email'
    }

    def __init__(self, name=None, address_line1=None, address_line2=None, location=None, contact=None, phone=None, email=None):  # noqa: E501
        """Address - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._address_line1 = None
        self._address_line2 = None
        self._location = None
        self._contact = None
        self._phone = None
        self._email = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if address_line1 is not None:
            self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if location is not None:
            self.location = location
        if contact is not None:
            self.contact = contact
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email

    @property
    def name(self):
        """Gets the name of this Address.  # noqa: E501

        The name of the addresss  # noqa: E501

        :return: The name of this Address.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Address.

        The name of the addresss  # noqa: E501

        :param name: The name of this Address.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address_line1(self):
        """Gets the address_line1 of this Address.  # noqa: E501

        The first line of the address  # noqa: E501

        :return: The address_line1 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this Address.

        The first line of the address  # noqa: E501

        :param address_line1: The address_line1 of this Address.  # noqa: E501
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this Address.  # noqa: E501

        The (optional) second line of the address  # noqa: E501

        :return: The address_line2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this Address.

        The (optional) second line of the address  # noqa: E501

        :param address_line2: The address_line2 of this Address.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def location(self):
        """Gets the location of this Address.  # noqa: E501


        :return: The location of this Address.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Address.


        :param location: The location of this Address.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def contact(self):
        """Gets the contact of this Address.  # noqa: E501

        The contact name for this address  # noqa: E501

        :return: The contact of this Address.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Address.

        The contact name for this address  # noqa: E501

        :param contact: The contact of this Address.  # noqa: E501
        :type: str
        """

        self._contact = contact

    @property
    def phone(self):
        """Gets the phone of this Address.  # noqa: E501

        The phone number associated with this address  # noqa: E501

        :return: The phone of this Address.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Address.

        The phone number associated with this address  # noqa: E501

        :param phone: The phone of this Address.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this Address.  # noqa: E501

        The email address associated with this addresss  # noqa: E501

        :return: The email of this Address.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Address.

        The email address associated with this addresss  # noqa: E501

        :param email: The email of this Address.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(Address, dict):
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
        if not isinstance(other, Address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
