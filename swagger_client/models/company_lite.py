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

class CompanyLite(object):
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
        'company_type': 'CompanyType',
        'enterprise_tier': 'EnterpriseTier',
        'name': 'str',
        'account_code': 'str',
        'display_name': 'str',
        'is_disabled': 'bool',
        'phone': 'str',
        'email': 'str'
    }

    attribute_map = {
        'id': 'id',
        'company_type': 'companyType',
        'enterprise_tier': 'enterpriseTier',
        'name': 'name',
        'account_code': 'accountCode',
        'display_name': 'displayName',
        'is_disabled': 'isDisabled',
        'phone': 'phone',
        'email': 'email'
    }

    def __init__(self, id=None, company_type=None, enterprise_tier=None, name=None, account_code=None, display_name=None, is_disabled=None, phone=None, email=None):  # noqa: E501
        """CompanyLite - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._company_type = None
        self._enterprise_tier = None
        self._name = None
        self._account_code = None
        self._display_name = None
        self._is_disabled = None
        self._phone = None
        self._email = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if company_type is not None:
            self.company_type = company_type
        if enterprise_tier is not None:
            self.enterprise_tier = enterprise_tier
        if name is not None:
            self.name = name
        if account_code is not None:
            self.account_code = account_code
        if display_name is not None:
            self.display_name = display_name
        if is_disabled is not None:
            self.is_disabled = is_disabled
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email

    @property
    def id(self):
        """Gets the id of this CompanyLite.  # noqa: E501


        :return: The id of this CompanyLite.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompanyLite.


        :param id: The id of this CompanyLite.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def company_type(self):
        """Gets the company_type of this CompanyLite.  # noqa: E501


        :return: The company_type of this CompanyLite.  # noqa: E501
        :rtype: CompanyType
        """
        return self._company_type

    @company_type.setter
    def company_type(self, company_type):
        """Sets the company_type of this CompanyLite.


        :param company_type: The company_type of this CompanyLite.  # noqa: E501
        :type: CompanyType
        """

        self._company_type = company_type

    @property
    def enterprise_tier(self):
        """Gets the enterprise_tier of this CompanyLite.  # noqa: E501


        :return: The enterprise_tier of this CompanyLite.  # noqa: E501
        :rtype: EnterpriseTier
        """
        return self._enterprise_tier

    @enterprise_tier.setter
    def enterprise_tier(self, enterprise_tier):
        """Sets the enterprise_tier of this CompanyLite.


        :param enterprise_tier: The enterprise_tier of this CompanyLite.  # noqa: E501
        :type: EnterpriseTier
        """

        self._enterprise_tier = enterprise_tier

    @property
    def name(self):
        """Gets the name of this CompanyLite.  # noqa: E501


        :return: The name of this CompanyLite.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CompanyLite.


        :param name: The name of this CompanyLite.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def account_code(self):
        """Gets the account_code of this CompanyLite.  # noqa: E501


        :return: The account_code of this CompanyLite.  # noqa: E501
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this CompanyLite.


        :param account_code: The account_code of this CompanyLite.  # noqa: E501
        :type: str
        """

        self._account_code = account_code

    @property
    def display_name(self):
        """Gets the display_name of this CompanyLite.  # noqa: E501


        :return: The display_name of this CompanyLite.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CompanyLite.


        :param display_name: The display_name of this CompanyLite.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def is_disabled(self):
        """Gets the is_disabled of this CompanyLite.  # noqa: E501


        :return: The is_disabled of this CompanyLite.  # noqa: E501
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this CompanyLite.


        :param is_disabled: The is_disabled of this CompanyLite.  # noqa: E501
        :type: bool
        """

        self._is_disabled = is_disabled

    @property
    def phone(self):
        """Gets the phone of this CompanyLite.  # noqa: E501


        :return: The phone of this CompanyLite.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CompanyLite.


        :param phone: The phone of this CompanyLite.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this CompanyLite.  # noqa: E501


        :return: The email of this CompanyLite.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CompanyLite.


        :param email: The email of this CompanyLite.  # noqa: E501
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
        if issubclass(CompanyLite, dict):
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
        if not isinstance(other, CompanyLite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
