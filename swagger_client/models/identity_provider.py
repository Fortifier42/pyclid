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

class IdentityProvider(object):
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
        'organisation_id': 'int',
        'name': 'str',
        'description': 'str',
        'provider_identifier': 'str',
        'unknown_identity_triggers_creation': 'bool',
        'is_machship_managed': 'bool',
        'identifying_claim_name': 'str',
        'identifying_claim_description': 'str',
        'new_user_default_company_id': 'int',
        'new_user_default_role_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'organisation_id': 'organisationId',
        'name': 'name',
        'description': 'description',
        'provider_identifier': 'providerIdentifier',
        'unknown_identity_triggers_creation': 'unknownIdentityTriggersCreation',
        'is_machship_managed': 'isMachshipManaged',
        'identifying_claim_name': 'identifyingClaimName',
        'identifying_claim_description': 'identifyingClaimDescription',
        'new_user_default_company_id': 'newUserDefaultCompanyId',
        'new_user_default_role_id': 'newUserDefaultRoleId'
    }

    def __init__(self, id=None, organisation_id=None, name=None, description=None, provider_identifier=None, unknown_identity_triggers_creation=None, is_machship_managed=None, identifying_claim_name=None, identifying_claim_description=None, new_user_default_company_id=None, new_user_default_role_id=None):  # noqa: E501
        """IdentityProvider - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._organisation_id = None
        self._name = None
        self._description = None
        self._provider_identifier = None
        self._unknown_identity_triggers_creation = None
        self._is_machship_managed = None
        self._identifying_claim_name = None
        self._identifying_claim_description = None
        self._new_user_default_company_id = None
        self._new_user_default_role_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if organisation_id is not None:
            self.organisation_id = organisation_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if provider_identifier is not None:
            self.provider_identifier = provider_identifier
        if unknown_identity_triggers_creation is not None:
            self.unknown_identity_triggers_creation = unknown_identity_triggers_creation
        if is_machship_managed is not None:
            self.is_machship_managed = is_machship_managed
        if identifying_claim_name is not None:
            self.identifying_claim_name = identifying_claim_name
        if identifying_claim_description is not None:
            self.identifying_claim_description = identifying_claim_description
        if new_user_default_company_id is not None:
            self.new_user_default_company_id = new_user_default_company_id
        if new_user_default_role_id is not None:
            self.new_user_default_role_id = new_user_default_role_id

    @property
    def id(self):
        """Gets the id of this IdentityProvider.  # noqa: E501


        :return: The id of this IdentityProvider.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdentityProvider.


        :param id: The id of this IdentityProvider.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def organisation_id(self):
        """Gets the organisation_id of this IdentityProvider.  # noqa: E501


        :return: The organisation_id of this IdentityProvider.  # noqa: E501
        :rtype: int
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this IdentityProvider.


        :param organisation_id: The organisation_id of this IdentityProvider.  # noqa: E501
        :type: int
        """

        self._organisation_id = organisation_id

    @property
    def name(self):
        """Gets the name of this IdentityProvider.  # noqa: E501


        :return: The name of this IdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IdentityProvider.


        :param name: The name of this IdentityProvider.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this IdentityProvider.  # noqa: E501


        :return: The description of this IdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IdentityProvider.


        :param description: The description of this IdentityProvider.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def provider_identifier(self):
        """Gets the provider_identifier of this IdentityProvider.  # noqa: E501


        :return: The provider_identifier of this IdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._provider_identifier

    @provider_identifier.setter
    def provider_identifier(self, provider_identifier):
        """Sets the provider_identifier of this IdentityProvider.


        :param provider_identifier: The provider_identifier of this IdentityProvider.  # noqa: E501
        :type: str
        """

        self._provider_identifier = provider_identifier

    @property
    def unknown_identity_triggers_creation(self):
        """Gets the unknown_identity_triggers_creation of this IdentityProvider.  # noqa: E501


        :return: The unknown_identity_triggers_creation of this IdentityProvider.  # noqa: E501
        :rtype: bool
        """
        return self._unknown_identity_triggers_creation

    @unknown_identity_triggers_creation.setter
    def unknown_identity_triggers_creation(self, unknown_identity_triggers_creation):
        """Sets the unknown_identity_triggers_creation of this IdentityProvider.


        :param unknown_identity_triggers_creation: The unknown_identity_triggers_creation of this IdentityProvider.  # noqa: E501
        :type: bool
        """

        self._unknown_identity_triggers_creation = unknown_identity_triggers_creation

    @property
    def is_machship_managed(self):
        """Gets the is_machship_managed of this IdentityProvider.  # noqa: E501


        :return: The is_machship_managed of this IdentityProvider.  # noqa: E501
        :rtype: bool
        """
        return self._is_machship_managed

    @is_machship_managed.setter
    def is_machship_managed(self, is_machship_managed):
        """Sets the is_machship_managed of this IdentityProvider.


        :param is_machship_managed: The is_machship_managed of this IdentityProvider.  # noqa: E501
        :type: bool
        """

        self._is_machship_managed = is_machship_managed

    @property
    def identifying_claim_name(self):
        """Gets the identifying_claim_name of this IdentityProvider.  # noqa: E501


        :return: The identifying_claim_name of this IdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._identifying_claim_name

    @identifying_claim_name.setter
    def identifying_claim_name(self, identifying_claim_name):
        """Sets the identifying_claim_name of this IdentityProvider.


        :param identifying_claim_name: The identifying_claim_name of this IdentityProvider.  # noqa: E501
        :type: str
        """

        self._identifying_claim_name = identifying_claim_name

    @property
    def identifying_claim_description(self):
        """Gets the identifying_claim_description of this IdentityProvider.  # noqa: E501


        :return: The identifying_claim_description of this IdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._identifying_claim_description

    @identifying_claim_description.setter
    def identifying_claim_description(self, identifying_claim_description):
        """Sets the identifying_claim_description of this IdentityProvider.


        :param identifying_claim_description: The identifying_claim_description of this IdentityProvider.  # noqa: E501
        :type: str
        """

        self._identifying_claim_description = identifying_claim_description

    @property
    def new_user_default_company_id(self):
        """Gets the new_user_default_company_id of this IdentityProvider.  # noqa: E501


        :return: The new_user_default_company_id of this IdentityProvider.  # noqa: E501
        :rtype: int
        """
        return self._new_user_default_company_id

    @new_user_default_company_id.setter
    def new_user_default_company_id(self, new_user_default_company_id):
        """Sets the new_user_default_company_id of this IdentityProvider.


        :param new_user_default_company_id: The new_user_default_company_id of this IdentityProvider.  # noqa: E501
        :type: int
        """

        self._new_user_default_company_id = new_user_default_company_id

    @property
    def new_user_default_role_id(self):
        """Gets the new_user_default_role_id of this IdentityProvider.  # noqa: E501


        :return: The new_user_default_role_id of this IdentityProvider.  # noqa: E501
        :rtype: int
        """
        return self._new_user_default_role_id

    @new_user_default_role_id.setter
    def new_user_default_role_id(self, new_user_default_role_id):
        """Sets the new_user_default_role_id of this IdentityProvider.


        :param new_user_default_role_id: The new_user_default_role_id of this IdentityProvider.  # noqa: E501
        :type: int
        """

        self._new_user_default_role_id = new_user_default_role_id

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
        if issubclass(IdentityProvider, dict):
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
        if not isinstance(other, IdentityProvider):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other