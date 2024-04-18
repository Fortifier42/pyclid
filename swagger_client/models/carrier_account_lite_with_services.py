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

class CarrierAccountLiteWithServices(object):
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
        'name': 'str',
        'account_code': 'str',
        'carrier_id': 'int',
        'carrier': 'CarrierLite',
        'is_in_test_mode': 'bool',
        'display_name': 'str',
        'carrier_services': 'list[CarrierServiceLiteWithSubServices]',
        'carrier_service_groups': 'list[CarrierServiceGroupLite]',
        'enable_receiver_pays': 'bool',
        'valid_services': 'bool',
        'carrier_integration_custom_field_sets': 'list[CustomFieldSet]',
        'carrier_integration_custom_fields_class': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'account_code': 'accountCode',
        'carrier_id': 'carrierId',
        'carrier': 'carrier',
        'is_in_test_mode': 'isInTestMode',
        'display_name': 'displayName',
        'carrier_services': 'carrierServices',
        'carrier_service_groups': 'carrierServiceGroups',
        'enable_receiver_pays': 'enableReceiverPays',
        'valid_services': 'validServices',
        'carrier_integration_custom_field_sets': 'carrierIntegrationCustomFieldSets',
        'carrier_integration_custom_fields_class': 'carrierIntegrationCustomFieldsClass'
    }

    def __init__(self, id=None, name=None, account_code=None, carrier_id=None, carrier=None, is_in_test_mode=None, display_name=None, carrier_services=None, carrier_service_groups=None, enable_receiver_pays=None, valid_services=None, carrier_integration_custom_field_sets=None, carrier_integration_custom_fields_class=None):  # noqa: E501
        """CarrierAccountLiteWithServices - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._account_code = None
        self._carrier_id = None
        self._carrier = None
        self._is_in_test_mode = None
        self._display_name = None
        self._carrier_services = None
        self._carrier_service_groups = None
        self._enable_receiver_pays = None
        self._valid_services = None
        self._carrier_integration_custom_field_sets = None
        self._carrier_integration_custom_fields_class = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if account_code is not None:
            self.account_code = account_code
        if carrier_id is not None:
            self.carrier_id = carrier_id
        if carrier is not None:
            self.carrier = carrier
        if is_in_test_mode is not None:
            self.is_in_test_mode = is_in_test_mode
        if display_name is not None:
            self.display_name = display_name
        if carrier_services is not None:
            self.carrier_services = carrier_services
        if carrier_service_groups is not None:
            self.carrier_service_groups = carrier_service_groups
        if enable_receiver_pays is not None:
            self.enable_receiver_pays = enable_receiver_pays
        if valid_services is not None:
            self.valid_services = valid_services
        if carrier_integration_custom_field_sets is not None:
            self.carrier_integration_custom_field_sets = carrier_integration_custom_field_sets
        if carrier_integration_custom_fields_class is not None:
            self.carrier_integration_custom_fields_class = carrier_integration_custom_fields_class

    @property
    def id(self):
        """Gets the id of this CarrierAccountLiteWithServices.  # noqa: E501


        :return: The id of this CarrierAccountLiteWithServices.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CarrierAccountLiteWithServices.


        :param id: The id of this CarrierAccountLiteWithServices.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CarrierAccountLiteWithServices.  # noqa: E501


        :return: The name of this CarrierAccountLiteWithServices.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CarrierAccountLiteWithServices.


        :param name: The name of this CarrierAccountLiteWithServices.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def account_code(self):
        """Gets the account_code of this CarrierAccountLiteWithServices.  # noqa: E501


        :return: The account_code of this CarrierAccountLiteWithServices.  # noqa: E501
        :rtype: str
        """
        return self._account_code

    @account_code.setter
    def account_code(self, account_code):
        """Sets the account_code of this CarrierAccountLiteWithServices.


        :param account_code: The account_code of this CarrierAccountLiteWithServices.  # noqa: E501
        :type: str
        """

        self._account_code = account_code

    @property
    def carrier_id(self):
        """Gets the carrier_id of this CarrierAccountLiteWithServices.  # noqa: E501


        :return: The carrier_id of this CarrierAccountLiteWithServices.  # noqa: E501
        :rtype: int
        """
        return self._carrier_id

    @carrier_id.setter
    def carrier_id(self, carrier_id):
        """Sets the carrier_id of this CarrierAccountLiteWithServices.


        :param carrier_id: The carrier_id of this CarrierAccountLiteWithServices.  # noqa: E501
        :type: int
        """

        self._carrier_id = carrier_id

    @property
    def carrier(self):
        """Gets the carrier of this CarrierAccountLiteWithServices.  # noqa: E501


        :return: The carrier of this CarrierAccountLiteWithServices.  # noqa: E501
        :rtype: CarrierLite
        """
        return self._carrier

    @carrier.setter
    def carrier(self, carrier):
        """Sets the carrier of this CarrierAccountLiteWithServices.


        :param carrier: The carrier of this CarrierAccountLiteWithServices.  # noqa: E501
        :type: CarrierLite
        """

        self._carrier = carrier

    @property
    def is_in_test_mode(self):
        """Gets the is_in_test_mode of this CarrierAccountLiteWithServices.  # noqa: E501


        :return: The is_in_test_mode of this CarrierAccountLiteWithServices.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_test_mode

    @is_in_test_mode.setter
    def is_in_test_mode(self, is_in_test_mode):
        """Sets the is_in_test_mode of this CarrierAccountLiteWithServices.


        :param is_in_test_mode: The is_in_test_mode of this CarrierAccountLiteWithServices.  # noqa: E501
        :type: bool
        """

        self._is_in_test_mode = is_in_test_mode

    @property
    def display_name(self):
        """Gets the display_name of this CarrierAccountLiteWithServices.  # noqa: E501


        :return: The display_name of this CarrierAccountLiteWithServices.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CarrierAccountLiteWithServices.


        :param display_name: The display_name of this CarrierAccountLiteWithServices.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def carrier_services(self):
        """Gets the carrier_services of this CarrierAccountLiteWithServices.  # noqa: E501


        :return: The carrier_services of this CarrierAccountLiteWithServices.  # noqa: E501
        :rtype: list[CarrierServiceLiteWithSubServices]
        """
        return self._carrier_services

    @carrier_services.setter
    def carrier_services(self, carrier_services):
        """Sets the carrier_services of this CarrierAccountLiteWithServices.


        :param carrier_services: The carrier_services of this CarrierAccountLiteWithServices.  # noqa: E501
        :type: list[CarrierServiceLiteWithSubServices]
        """

        self._carrier_services = carrier_services

    @property
    def carrier_service_groups(self):
        """Gets the carrier_service_groups of this CarrierAccountLiteWithServices.  # noqa: E501


        :return: The carrier_service_groups of this CarrierAccountLiteWithServices.  # noqa: E501
        :rtype: list[CarrierServiceGroupLite]
        """
        return self._carrier_service_groups

    @carrier_service_groups.setter
    def carrier_service_groups(self, carrier_service_groups):
        """Sets the carrier_service_groups of this CarrierAccountLiteWithServices.


        :param carrier_service_groups: The carrier_service_groups of this CarrierAccountLiteWithServices.  # noqa: E501
        :type: list[CarrierServiceGroupLite]
        """

        self._carrier_service_groups = carrier_service_groups

    @property
    def enable_receiver_pays(self):
        """Gets the enable_receiver_pays of this CarrierAccountLiteWithServices.  # noqa: E501


        :return: The enable_receiver_pays of this CarrierAccountLiteWithServices.  # noqa: E501
        :rtype: bool
        """
        return self._enable_receiver_pays

    @enable_receiver_pays.setter
    def enable_receiver_pays(self, enable_receiver_pays):
        """Sets the enable_receiver_pays of this CarrierAccountLiteWithServices.


        :param enable_receiver_pays: The enable_receiver_pays of this CarrierAccountLiteWithServices.  # noqa: E501
        :type: bool
        """

        self._enable_receiver_pays = enable_receiver_pays

    @property
    def valid_services(self):
        """Gets the valid_services of this CarrierAccountLiteWithServices.  # noqa: E501


        :return: The valid_services of this CarrierAccountLiteWithServices.  # noqa: E501
        :rtype: bool
        """
        return self._valid_services

    @valid_services.setter
    def valid_services(self, valid_services):
        """Sets the valid_services of this CarrierAccountLiteWithServices.


        :param valid_services: The valid_services of this CarrierAccountLiteWithServices.  # noqa: E501
        :type: bool
        """

        self._valid_services = valid_services

    @property
    def carrier_integration_custom_field_sets(self):
        """Gets the carrier_integration_custom_field_sets of this CarrierAccountLiteWithServices.  # noqa: E501


        :return: The carrier_integration_custom_field_sets of this CarrierAccountLiteWithServices.  # noqa: E501
        :rtype: list[CustomFieldSet]
        """
        return self._carrier_integration_custom_field_sets

    @carrier_integration_custom_field_sets.setter
    def carrier_integration_custom_field_sets(self, carrier_integration_custom_field_sets):
        """Sets the carrier_integration_custom_field_sets of this CarrierAccountLiteWithServices.


        :param carrier_integration_custom_field_sets: The carrier_integration_custom_field_sets of this CarrierAccountLiteWithServices.  # noqa: E501
        :type: list[CustomFieldSet]
        """

        self._carrier_integration_custom_field_sets = carrier_integration_custom_field_sets

    @property
    def carrier_integration_custom_fields_class(self):
        """Gets the carrier_integration_custom_fields_class of this CarrierAccountLiteWithServices.  # noqa: E501


        :return: The carrier_integration_custom_fields_class of this CarrierAccountLiteWithServices.  # noqa: E501
        :rtype: str
        """
        return self._carrier_integration_custom_fields_class

    @carrier_integration_custom_fields_class.setter
    def carrier_integration_custom_fields_class(self, carrier_integration_custom_fields_class):
        """Sets the carrier_integration_custom_fields_class of this CarrierAccountLiteWithServices.


        :param carrier_integration_custom_fields_class: The carrier_integration_custom_fields_class of this CarrierAccountLiteWithServices.  # noqa: E501
        :type: str
        """

        self._carrier_integration_custom_fields_class = carrier_integration_custom_fields_class

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
        if issubclass(CarrierAccountLiteWithServices, dict):
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
        if not isinstance(other, CarrierAccountLiteWithServices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other