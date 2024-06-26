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

class ManualTrackingStatus(object):
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
        'status': 'TrackingStatus',
        'status_date_time_local': 'datetime',
        'item_reference': 'str',
        'extra_information': 'str'
    }

    attribute_map = {
        'consignment_id': 'consignmentId',
        'status': 'status',
        'status_date_time_local': 'statusDateTimeLocal',
        'item_reference': 'itemReference',
        'extra_information': 'extraInformation'
    }

    def __init__(self, consignment_id=None, status=None, status_date_time_local=None, item_reference=None, extra_information=None):  # noqa: E501
        """ManualTrackingStatus - a model defined in Swagger"""  # noqa: E501
        self._consignment_id = None
        self._status = None
        self._status_date_time_local = None
        self._item_reference = None
        self._extra_information = None
        self.discriminator = None
        if consignment_id is not None:
            self.consignment_id = consignment_id
        if status is not None:
            self.status = status
        if status_date_time_local is not None:
            self.status_date_time_local = status_date_time_local
        if item_reference is not None:
            self.item_reference = item_reference
        if extra_information is not None:
            self.extra_information = extra_information

    @property
    def consignment_id(self):
        """Gets the consignment_id of this ManualTrackingStatus.  # noqa: E501

        The ID of the consignment in MachShip  # noqa: E501

        :return: The consignment_id of this ManualTrackingStatus.  # noqa: E501
        :rtype: int
        """
        return self._consignment_id

    @consignment_id.setter
    def consignment_id(self, consignment_id):
        """Sets the consignment_id of this ManualTrackingStatus.

        The ID of the consignment in MachShip  # noqa: E501

        :param consignment_id: The consignment_id of this ManualTrackingStatus.  # noqa: E501
        :type: int
        """

        self._consignment_id = consignment_id

    @property
    def status(self):
        """Gets the status of this ManualTrackingStatus.  # noqa: E501


        :return: The status of this ManualTrackingStatus.  # noqa: E501
        :rtype: TrackingStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ManualTrackingStatus.


        :param status: The status of this ManualTrackingStatus.  # noqa: E501
        :type: TrackingStatus
        """

        self._status = status

    @property
    def status_date_time_local(self):
        """Gets the status_date_time_local of this ManualTrackingStatus.  # noqa: E501

        Optional.  # noqa: E501

        :return: The status_date_time_local of this ManualTrackingStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._status_date_time_local

    @status_date_time_local.setter
    def status_date_time_local(self, status_date_time_local):
        """Sets the status_date_time_local of this ManualTrackingStatus.

        Optional.  # noqa: E501

        :param status_date_time_local: The status_date_time_local of this ManualTrackingStatus.  # noqa: E501
        :type: datetime
        """

        self._status_date_time_local = status_date_time_local

    @property
    def item_reference(self):
        """Gets the item_reference of this ManualTrackingStatus.  # noqa: E501

        When present this tracking status relates to an item on the consignment. When absent it relates  to the consignment as a whole.  # noqa: E501

        :return: The item_reference of this ManualTrackingStatus.  # noqa: E501
        :rtype: str
        """
        return self._item_reference

    @item_reference.setter
    def item_reference(self, item_reference):
        """Sets the item_reference of this ManualTrackingStatus.

        When present this tracking status relates to an item on the consignment. When absent it relates  to the consignment as a whole.  # noqa: E501

        :param item_reference: The item_reference of this ManualTrackingStatus.  # noqa: E501
        :type: str
        """

        self._item_reference = item_reference

    @property
    def extra_information(self):
        """Gets the extra_information of this ManualTrackingStatus.  # noqa: E501

        Any extra information about this status - this will be shown in MachShip when viewing the tracking history  # noqa: E501

        :return: The extra_information of this ManualTrackingStatus.  # noqa: E501
        :rtype: str
        """
        return self._extra_information

    @extra_information.setter
    def extra_information(self, extra_information):
        """Sets the extra_information of this ManualTrackingStatus.

        Any extra information about this status - this will be shown in MachShip when viewing the tracking history  # noqa: E501

        :param extra_information: The extra_information of this ManualTrackingStatus.  # noqa: E501
        :type: str
        """

        self._extra_information = extra_information

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
        if issubclass(ManualTrackingStatus, dict):
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
        if not isinstance(other, ManualTrackingStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
