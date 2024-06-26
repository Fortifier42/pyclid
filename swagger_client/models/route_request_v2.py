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

class RouteRequestV2(object):
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
        'request_id': 'str',
        'despatch_date_time_utc': 'datetime',
        'despatch_date_time_local': 'datetime',
        'from_company_location_id': 'int',
        'from_location_id': 'int',
        'from_name': 'str',
        'from_abbreviation': 'str',
        'from_location': 'SendLocationV2',
        'to_company_location_id': 'int',
        'to_location_id': 'int',
        'to_name': 'str',
        'to_abbreviation': 'str',
        'to_location': 'SendLocationV2',
        'question_ids': 'list[int]',
        'carrier_ids': 'list[int]',
        'carrier_account_id': 'int',
        'carrier_service_id': 'int',
        'company_carrier_account_id': 'int',
        'company_id': 'int',
        'customer_reference': 'str',
        'customer_reference2': 'str',
        'to_address_line1': 'str',
        'to_address_line2': 'str',
        'items': 'list[CreateConsignmentItemV2]'
    }

    attribute_map = {
        'request_id': 'requestId',
        'despatch_date_time_utc': 'despatchDateTimeUtc',
        'despatch_date_time_local': 'despatchDateTimeLocal',
        'from_company_location_id': 'fromCompanyLocationId',
        'from_location_id': 'fromLocationId',
        'from_name': 'fromName',
        'from_abbreviation': 'fromAbbreviation',
        'from_location': 'fromLocation',
        'to_company_location_id': 'toCompanyLocationId',
        'to_location_id': 'toLocationId',
        'to_name': 'toName',
        'to_abbreviation': 'toAbbreviation',
        'to_location': 'toLocation',
        'question_ids': 'questionIds',
        'carrier_ids': 'carrierIds',
        'carrier_account_id': 'carrierAccountId',
        'carrier_service_id': 'carrierServiceId',
        'company_carrier_account_id': 'companyCarrierAccountId',
        'company_id': 'companyId',
        'customer_reference': 'customerReference',
        'customer_reference2': 'customerReference2',
        'to_address_line1': 'toAddressLine1',
        'to_address_line2': 'toAddressLine2',
        'items': 'items'
    }

    def __init__(self, request_id=None, despatch_date_time_utc=None, despatch_date_time_local=None, from_company_location_id=None, from_location_id=None, from_name=None, from_abbreviation=None, from_location=None, to_company_location_id=None, to_location_id=None, to_name=None, to_abbreviation=None, to_location=None, question_ids=None, carrier_ids=None, carrier_account_id=None, carrier_service_id=None, company_carrier_account_id=None, company_id=None, customer_reference=None, customer_reference2=None, to_address_line1=None, to_address_line2=None, items=None):  # noqa: E501
        """RouteRequestV2 - a model defined in Swagger"""  # noqa: E501
        self._request_id = None
        self._despatch_date_time_utc = None
        self._despatch_date_time_local = None
        self._from_company_location_id = None
        self._from_location_id = None
        self._from_name = None
        self._from_abbreviation = None
        self._from_location = None
        self._to_company_location_id = None
        self._to_location_id = None
        self._to_name = None
        self._to_abbreviation = None
        self._to_location = None
        self._question_ids = None
        self._carrier_ids = None
        self._carrier_account_id = None
        self._carrier_service_id = None
        self._company_carrier_account_id = None
        self._company_id = None
        self._customer_reference = None
        self._customer_reference2 = None
        self._to_address_line1 = None
        self._to_address_line2 = None
        self._items = None
        self.discriminator = None
        if request_id is not None:
            self.request_id = request_id
        if despatch_date_time_utc is not None:
            self.despatch_date_time_utc = despatch_date_time_utc
        if despatch_date_time_local is not None:
            self.despatch_date_time_local = despatch_date_time_local
        if from_company_location_id is not None:
            self.from_company_location_id = from_company_location_id
        if from_location_id is not None:
            self.from_location_id = from_location_id
        if from_name is not None:
            self.from_name = from_name
        if from_abbreviation is not None:
            self.from_abbreviation = from_abbreviation
        if from_location is not None:
            self.from_location = from_location
        if to_company_location_id is not None:
            self.to_company_location_id = to_company_location_id
        if to_location_id is not None:
            self.to_location_id = to_location_id
        if to_name is not None:
            self.to_name = to_name
        if to_abbreviation is not None:
            self.to_abbreviation = to_abbreviation
        if to_location is not None:
            self.to_location = to_location
        if question_ids is not None:
            self.question_ids = question_ids
        if carrier_ids is not None:
            self.carrier_ids = carrier_ids
        if carrier_account_id is not None:
            self.carrier_account_id = carrier_account_id
        if carrier_service_id is not None:
            self.carrier_service_id = carrier_service_id
        if company_carrier_account_id is not None:
            self.company_carrier_account_id = company_carrier_account_id
        if company_id is not None:
            self.company_id = company_id
        if customer_reference is not None:
            self.customer_reference = customer_reference
        if customer_reference2 is not None:
            self.customer_reference2 = customer_reference2
        if to_address_line1 is not None:
            self.to_address_line1 = to_address_line1
        if to_address_line2 is not None:
            self.to_address_line2 = to_address_line2
        self.items = items

    @property
    def request_id(self):
        """Gets the request_id of this RouteRequestV2.  # noqa: E501

        Optional: This GUID can be used to match up responses to requests when requesting multiple routes in the same call  # noqa: E501

        :return: The request_id of this RouteRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this RouteRequestV2.

        Optional: This GUID can be used to match up responses to requests when requesting multiple routes in the same call  # noqa: E501

        :param request_id: The request_id of this RouteRequestV2.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def despatch_date_time_utc(self):
        """Gets the despatch_date_time_utc of this RouteRequestV2.  # noqa: E501

        Optional: The date time the items would be available to despatched, in UTC. If this is not provided, it will default to NOW (UTC)  # noqa: E501

        :return: The despatch_date_time_utc of this RouteRequestV2.  # noqa: E501
        :rtype: datetime
        """
        return self._despatch_date_time_utc

    @despatch_date_time_utc.setter
    def despatch_date_time_utc(self, despatch_date_time_utc):
        """Sets the despatch_date_time_utc of this RouteRequestV2.

        Optional: The date time the items would be available to despatched, in UTC. If this is not provided, it will default to NOW (UTC)  # noqa: E501

        :param despatch_date_time_utc: The despatch_date_time_utc of this RouteRequestV2.  # noqa: E501
        :type: datetime
        """

        self._despatch_date_time_utc = despatch_date_time_utc

    @property
    def despatch_date_time_local(self):
        """Gets the despatch_date_time_local of this RouteRequestV2.  # noqa: E501


        :return: The despatch_date_time_local of this RouteRequestV2.  # noqa: E501
        :rtype: datetime
        """
        return self._despatch_date_time_local

    @despatch_date_time_local.setter
    def despatch_date_time_local(self, despatch_date_time_local):
        """Sets the despatch_date_time_local of this RouteRequestV2.


        :param despatch_date_time_local: The despatch_date_time_local of this RouteRequestV2.  # noqa: E501
        :type: datetime
        """

        self._despatch_date_time_local = despatch_date_time_local

    @property
    def from_company_location_id(self):
        """Gets the from_company_location_id of this RouteRequestV2.  # noqa: E501

        The machship ID of the saved company from (pickup) location. This only needs to be specified if this route is coming from a saved location  # noqa: E501

        :return: The from_company_location_id of this RouteRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._from_company_location_id

    @from_company_location_id.setter
    def from_company_location_id(self, from_company_location_id):
        """Sets the from_company_location_id of this RouteRequestV2.

        The machship ID of the saved company from (pickup) location. This only needs to be specified if this route is coming from a saved location  # noqa: E501

        :param from_company_location_id: The from_company_location_id of this RouteRequestV2.  # noqa: E501
        :type: int
        """

        self._from_company_location_id = from_company_location_id

    @property
    def from_location_id(self):
        """Gets the from_location_id of this RouteRequestV2.  # noqa: E501

        The machship ID of the from (pickup) location. Can be left blank if supplying the suburb / postcode instead  # noqa: E501

        :return: The from_location_id of this RouteRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._from_location_id

    @from_location_id.setter
    def from_location_id(self, from_location_id):
        """Sets the from_location_id of this RouteRequestV2.

        The machship ID of the from (pickup) location. Can be left blank if supplying the suburb / postcode instead  # noqa: E501

        :param from_location_id: The from_location_id of this RouteRequestV2.  # noqa: E501
        :type: int
        """

        self._from_location_id = from_location_id

    @property
    def from_name(self):
        """Gets the from_name of this RouteRequestV2.  # noqa: E501

        An optional Name field that can be filled. If present, a company location lookup by name will be attempted in order  to ascertain the FromCompanyLocationId  # noqa: E501

        :return: The from_name of this RouteRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this RouteRequestV2.

        An optional Name field that can be filled. If present, a company location lookup by name will be attempted in order  to ascertain the FromCompanyLocationId  # noqa: E501

        :param from_name: The from_name of this RouteRequestV2.  # noqa: E501
        :type: str
        """

        self._from_name = from_name

    @property
    def from_abbreviation(self):
        """Gets the from_abbreviation of this RouteRequestV2.  # noqa: E501

        An optional Abbreviation field that can be filled. If present, a company location lookup by abbreviation will be attempted in order  to ascertain the FromCompanyLocationId  # noqa: E501

        :return: The from_abbreviation of this RouteRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._from_abbreviation

    @from_abbreviation.setter
    def from_abbreviation(self, from_abbreviation):
        """Sets the from_abbreviation of this RouteRequestV2.

        An optional Abbreviation field that can be filled. If present, a company location lookup by abbreviation will be attempted in order  to ascertain the FromCompanyLocationId  # noqa: E501

        :param from_abbreviation: The from_abbreviation of this RouteRequestV2.  # noqa: E501
        :type: str
        """

        self._from_abbreviation = from_abbreviation

    @property
    def from_location(self):
        """Gets the from_location of this RouteRequestV2.  # noqa: E501


        :return: The from_location of this RouteRequestV2.  # noqa: E501
        :rtype: SendLocationV2
        """
        return self._from_location

    @from_location.setter
    def from_location(self, from_location):
        """Sets the from_location of this RouteRequestV2.


        :param from_location: The from_location of this RouteRequestV2.  # noqa: E501
        :type: SendLocationV2
        """

        self._from_location = from_location

    @property
    def to_company_location_id(self):
        """Gets the to_company_location_id of this RouteRequestV2.  # noqa: E501

        The machship ID of the saved company to (delivery) location. This only needs to be specified if this route is going to a saved location  # noqa: E501

        :return: The to_company_location_id of this RouteRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._to_company_location_id

    @to_company_location_id.setter
    def to_company_location_id(self, to_company_location_id):
        """Sets the to_company_location_id of this RouteRequestV2.

        The machship ID of the saved company to (delivery) location. This only needs to be specified if this route is going to a saved location  # noqa: E501

        :param to_company_location_id: The to_company_location_id of this RouteRequestV2.  # noqa: E501
        :type: int
        """

        self._to_company_location_id = to_company_location_id

    @property
    def to_location_id(self):
        """Gets the to_location_id of this RouteRequestV2.  # noqa: E501

        The machship ID of the to (receiver) location. Can be left blank if supplying the suburb / postcode instead  # noqa: E501

        :return: The to_location_id of this RouteRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._to_location_id

    @to_location_id.setter
    def to_location_id(self, to_location_id):
        """Sets the to_location_id of this RouteRequestV2.

        The machship ID of the to (receiver) location. Can be left blank if supplying the suburb / postcode instead  # noqa: E501

        :param to_location_id: The to_location_id of this RouteRequestV2.  # noqa: E501
        :type: int
        """

        self._to_location_id = to_location_id

    @property
    def to_name(self):
        """Gets the to_name of this RouteRequestV2.  # noqa: E501

        An optional Name field that can be filled. If present, a company location lookup by name will be attempted in order  to ascertain the ToCompanyLocationId  # noqa: E501

        :return: The to_name of this RouteRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._to_name

    @to_name.setter
    def to_name(self, to_name):
        """Sets the to_name of this RouteRequestV2.

        An optional Name field that can be filled. If present, a company location lookup by name will be attempted in order  to ascertain the ToCompanyLocationId  # noqa: E501

        :param to_name: The to_name of this RouteRequestV2.  # noqa: E501
        :type: str
        """

        self._to_name = to_name

    @property
    def to_abbreviation(self):
        """Gets the to_abbreviation of this RouteRequestV2.  # noqa: E501

        An optional Abbreviation field that can be filled. If present, a company location lookup by abbreviation will be attempted in order  to ascertain the ToCompanyLocationId  # noqa: E501

        :return: The to_abbreviation of this RouteRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._to_abbreviation

    @to_abbreviation.setter
    def to_abbreviation(self, to_abbreviation):
        """Sets the to_abbreviation of this RouteRequestV2.

        An optional Abbreviation field that can be filled. If present, a company location lookup by abbreviation will be attempted in order  to ascertain the ToCompanyLocationId  # noqa: E501

        :param to_abbreviation: The to_abbreviation of this RouteRequestV2.  # noqa: E501
        :type: str
        """

        self._to_abbreviation = to_abbreviation

    @property
    def to_location(self):
        """Gets the to_location of this RouteRequestV2.  # noqa: E501


        :return: The to_location of this RouteRequestV2.  # noqa: E501
        :rtype: SendLocationV2
        """
        return self._to_location

    @to_location.setter
    def to_location(self, to_location):
        """Sets the to_location of this RouteRequestV2.


        :param to_location: The to_location of this RouteRequestV2.  # noqa: E501
        :type: SendLocationV2
        """

        self._to_location = to_location

    @property
    def question_ids(self):
        """Gets the question_ids of this RouteRequestV2.  # noqa: E501

        A collection of Machship IDs corresponding to questions who's result is true  # noqa: E501

        :return: The question_ids of this RouteRequestV2.  # noqa: E501
        :rtype: list[int]
        """
        return self._question_ids

    @question_ids.setter
    def question_ids(self, question_ids):
        """Sets the question_ids of this RouteRequestV2.

        A collection of Machship IDs corresponding to questions who's result is true  # noqa: E501

        :param question_ids: The question_ids of this RouteRequestV2.  # noqa: E501
        :type: list[int]
        """

        self._question_ids = question_ids

    @property
    def carrier_ids(self):
        """Gets the carrier_ids of this RouteRequestV2.  # noqa: E501

        The (optional) listing of Machship Carrier IDs to restrict the returning routes for. When left blank all carriers  you have available will be queried for routes.  # noqa: E501

        :return: The carrier_ids of this RouteRequestV2.  # noqa: E501
        :rtype: list[int]
        """
        return self._carrier_ids

    @carrier_ids.setter
    def carrier_ids(self, carrier_ids):
        """Sets the carrier_ids of this RouteRequestV2.

        The (optional) listing of Machship Carrier IDs to restrict the returning routes for. When left blank all carriers  you have available will be queried for routes.  # noqa: E501

        :param carrier_ids: The carrier_ids of this RouteRequestV2.  # noqa: E501
        :type: list[int]
        """

        self._carrier_ids = carrier_ids

    @property
    def carrier_account_id(self):
        """Gets the carrier_account_id of this RouteRequestV2.  # noqa: E501

        An (optional) Carrier Account ID in Machship. When supplied routes returned will be restricted to those from this  carrier account.  # noqa: E501

        :return: The carrier_account_id of this RouteRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._carrier_account_id

    @carrier_account_id.setter
    def carrier_account_id(self, carrier_account_id):
        """Sets the carrier_account_id of this RouteRequestV2.

        An (optional) Carrier Account ID in Machship. When supplied routes returned will be restricted to those from this  carrier account.  # noqa: E501

        :param carrier_account_id: The carrier_account_id of this RouteRequestV2.  # noqa: E501
        :type: int
        """

        self._carrier_account_id = carrier_account_id

    @property
    def carrier_service_id(self):
        """Gets the carrier_service_id of this RouteRequestV2.  # noqa: E501

        An (optional) Machship ID of the Carrier Service. When supplied routes returned will be restricted to those for this  service.  # noqa: E501

        :return: The carrier_service_id of this RouteRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._carrier_service_id

    @carrier_service_id.setter
    def carrier_service_id(self, carrier_service_id):
        """Sets the carrier_service_id of this RouteRequestV2.

        An (optional) Machship ID of the Carrier Service. When supplied routes returned will be restricted to those for this  service.  # noqa: E501

        :param carrier_service_id: The carrier_service_id of this RouteRequestV2.  # noqa: E501
        :type: int
        """

        self._carrier_service_id = carrier_service_id

    @property
    def company_carrier_account_id(self):
        """Gets the company_carrier_account_id of this RouteRequestV2.  # noqa: E501

        An (optional) Machship ID of the Company Carrier Account. When supplied routes returned will be restricted to those for this  company carrier account.  # noqa: E501

        :return: The company_carrier_account_id of this RouteRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._company_carrier_account_id

    @company_carrier_account_id.setter
    def company_carrier_account_id(self, company_carrier_account_id):
        """Sets the company_carrier_account_id of this RouteRequestV2.

        An (optional) Machship ID of the Company Carrier Account. When supplied routes returned will be restricted to those for this  company carrier account.  # noqa: E501

        :param company_carrier_account_id: The company_carrier_account_id of this RouteRequestV2.  # noqa: E501
        :type: int
        """

        self._company_carrier_account_id = company_carrier_account_id

    @property
    def company_id(self):
        """Gets the company_id of this RouteRequestV2.  # noqa: E501

        An (optional) Machship ID of a company. When supplied the routes will be those of the company specified, when left  blank they will be routes for the company associated with the authorised user.  # noqa: E501

        :return: The company_id of this RouteRequestV2.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this RouteRequestV2.

        An (optional) Machship ID of a company. When supplied the routes will be those of the company specified, when left  blank they will be routes for the company associated with the authorised user.  # noqa: E501

        :param company_id: The company_id of this RouteRequestV2.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def customer_reference(self):
        """Gets the customer_reference of this RouteRequestV2.  # noqa: E501

        Optional  # noqa: E501

        :return: The customer_reference of this RouteRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._customer_reference

    @customer_reference.setter
    def customer_reference(self, customer_reference):
        """Sets the customer_reference of this RouteRequestV2.

        Optional  # noqa: E501

        :param customer_reference: The customer_reference of this RouteRequestV2.  # noqa: E501
        :type: str
        """

        self._customer_reference = customer_reference

    @property
    def customer_reference2(self):
        """Gets the customer_reference2 of this RouteRequestV2.  # noqa: E501

        Optional  # noqa: E501

        :return: The customer_reference2 of this RouteRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._customer_reference2

    @customer_reference2.setter
    def customer_reference2(self, customer_reference2):
        """Sets the customer_reference2 of this RouteRequestV2.

        Optional  # noqa: E501

        :param customer_reference2: The customer_reference2 of this RouteRequestV2.  # noqa: E501
        :type: str
        """

        self._customer_reference2 = customer_reference2

    @property
    def to_address_line1(self):
        """Gets the to_address_line1 of this RouteRequestV2.  # noqa: E501


        :return: The to_address_line1 of this RouteRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._to_address_line1

    @to_address_line1.setter
    def to_address_line1(self, to_address_line1):
        """Sets the to_address_line1 of this RouteRequestV2.


        :param to_address_line1: The to_address_line1 of this RouteRequestV2.  # noqa: E501
        :type: str
        """

        self._to_address_line1 = to_address_line1

    @property
    def to_address_line2(self):
        """Gets the to_address_line2 of this RouteRequestV2.  # noqa: E501


        :return: The to_address_line2 of this RouteRequestV2.  # noqa: E501
        :rtype: str
        """
        return self._to_address_line2

    @to_address_line2.setter
    def to_address_line2(self, to_address_line2):
        """Sets the to_address_line2 of this RouteRequestV2.


        :param to_address_line2: The to_address_line2 of this RouteRequestV2.  # noqa: E501
        :type: str
        """

        self._to_address_line2 = to_address_line2

    @property
    def items(self):
        """Gets the items of this RouteRequestV2.  # noqa: E501

        A collection of the items being sent  # noqa: E501

        :return: The items of this RouteRequestV2.  # noqa: E501
        :rtype: list[CreateConsignmentItemV2]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this RouteRequestV2.

        A collection of the items being sent  # noqa: E501

        :param items: The items of this RouteRequestV2.  # noqa: E501
        :type: list[CreateConsignmentItemV2]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")  # noqa: E501

        self._items = items

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
        if issubclass(RouteRequestV2, dict):
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
        if not isinstance(other, RouteRequestV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
