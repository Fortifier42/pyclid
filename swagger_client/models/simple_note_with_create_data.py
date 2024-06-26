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

class SimpleNoteWithCreateData(object):
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
        'entity_type': 'EntityType',
        'entity_id': 'int',
        'note': 'str',
        'show_user': 'bool',
        'created_by_system': 'bool',
        'created_by': 'str',
        'created_by_id': 'int',
        'created_date': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'entity_type': 'entityType',
        'entity_id': 'entityId',
        'note': 'note',
        'show_user': 'showUser',
        'created_by_system': 'createdBySystem',
        'created_by': 'createdBy',
        'created_by_id': 'createdById',
        'created_date': 'createdDate'
    }

    def __init__(self, id=None, entity_type=None, entity_id=None, note=None, show_user=None, created_by_system=None, created_by=None, created_by_id=None, created_date=None):  # noqa: E501
        """SimpleNoteWithCreateData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._entity_type = None
        self._entity_id = None
        self._note = None
        self._show_user = None
        self._created_by_system = None
        self._created_by = None
        self._created_by_id = None
        self._created_date = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if entity_type is not None:
            self.entity_type = entity_type
        if entity_id is not None:
            self.entity_id = entity_id
        if note is not None:
            self.note = note
        if show_user is not None:
            self.show_user = show_user
        if created_by_system is not None:
            self.created_by_system = created_by_system
        if created_by is not None:
            self.created_by = created_by
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date

    @property
    def id(self):
        """Gets the id of this SimpleNoteWithCreateData.  # noqa: E501


        :return: The id of this SimpleNoteWithCreateData.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimpleNoteWithCreateData.


        :param id: The id of this SimpleNoteWithCreateData.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def entity_type(self):
        """Gets the entity_type of this SimpleNoteWithCreateData.  # noqa: E501


        :return: The entity_type of this SimpleNoteWithCreateData.  # noqa: E501
        :rtype: EntityType
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this SimpleNoteWithCreateData.


        :param entity_type: The entity_type of this SimpleNoteWithCreateData.  # noqa: E501
        :type: EntityType
        """

        self._entity_type = entity_type

    @property
    def entity_id(self):
        """Gets the entity_id of this SimpleNoteWithCreateData.  # noqa: E501


        :return: The entity_id of this SimpleNoteWithCreateData.  # noqa: E501
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this SimpleNoteWithCreateData.


        :param entity_id: The entity_id of this SimpleNoteWithCreateData.  # noqa: E501
        :type: int
        """

        self._entity_id = entity_id

    @property
    def note(self):
        """Gets the note of this SimpleNoteWithCreateData.  # noqa: E501


        :return: The note of this SimpleNoteWithCreateData.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this SimpleNoteWithCreateData.


        :param note: The note of this SimpleNoteWithCreateData.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def show_user(self):
        """Gets the show_user of this SimpleNoteWithCreateData.  # noqa: E501


        :return: The show_user of this SimpleNoteWithCreateData.  # noqa: E501
        :rtype: bool
        """
        return self._show_user

    @show_user.setter
    def show_user(self, show_user):
        """Sets the show_user of this SimpleNoteWithCreateData.


        :param show_user: The show_user of this SimpleNoteWithCreateData.  # noqa: E501
        :type: bool
        """

        self._show_user = show_user

    @property
    def created_by_system(self):
        """Gets the created_by_system of this SimpleNoteWithCreateData.  # noqa: E501


        :return: The created_by_system of this SimpleNoteWithCreateData.  # noqa: E501
        :rtype: bool
        """
        return self._created_by_system

    @created_by_system.setter
    def created_by_system(self, created_by_system):
        """Sets the created_by_system of this SimpleNoteWithCreateData.


        :param created_by_system: The created_by_system of this SimpleNoteWithCreateData.  # noqa: E501
        :type: bool
        """

        self._created_by_system = created_by_system

    @property
    def created_by(self):
        """Gets the created_by of this SimpleNoteWithCreateData.  # noqa: E501


        :return: The created_by of this SimpleNoteWithCreateData.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this SimpleNoteWithCreateData.


        :param created_by: The created_by of this SimpleNoteWithCreateData.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_by_id(self):
        """Gets the created_by_id of this SimpleNoteWithCreateData.  # noqa: E501


        :return: The created_by_id of this SimpleNoteWithCreateData.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this SimpleNoteWithCreateData.


        :param created_by_id: The created_by_id of this SimpleNoteWithCreateData.  # noqa: E501
        :type: int
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this SimpleNoteWithCreateData.  # noqa: E501


        :return: The created_date of this SimpleNoteWithCreateData.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this SimpleNoteWithCreateData.


        :param created_date: The created_date of this SimpleNoteWithCreateData.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

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
        if issubclass(SimpleNoteWithCreateData, dict):
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
        if not isinstance(other, SimpleNoteWithCreateData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
