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

class CompanyLocation(object):
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
        'location_type': 'CompanyLocationType',
        'name': 'str',
        'abbreviation': 'str',
        'display_name': 'str',
        'contact': 'str',
        'phone': 'str',
        'email': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'address_lines_friendly': 'str',
        'company_id': 'int',
        'location_id': 'int',
        'location': 'Location',
        'location_as_string': 'str',
        'is_locked': 'bool',
        'special_instructions': 'str',
        'carrier_accounts': 'list[BaseCarrierAccount]',
        'permanent_pickups': 'list[PermanentPickup]',
        'very_frequent_address': 'bool',
        'total_rows': 'int',
        'company': 'CompanyLite',
        'insertion_guid': 'str',
        'company_location_receiver_accounts': 'list[CompanyLocationReceiverAccount]',
        'reference1': 'str',
        'reference2': 'str',
        'default_pickup_time': 'TimeSpan',
        'default_closing_time': 'TimeSpan',
        'default_pickup_instructions': 'str',
        'pickup_question_ids': 'list[int]',
        'delivery_question_ids': 'list[int]',
        'is_international': 'bool',
        'country_id': 'int',
        'country': 'Country',
        'international_city': 'str',
        'international_province': 'str',
        'international_postcode': 'str',
        'location_description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'location_type': 'locationType',
        'name': 'name',
        'abbreviation': 'abbreviation',
        'display_name': 'displayName',
        'contact': 'contact',
        'phone': 'phone',
        'email': 'email',
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'address_lines_friendly': 'addressLinesFriendly',
        'company_id': 'companyId',
        'location_id': 'locationId',
        'location': 'location',
        'location_as_string': 'locationAsString',
        'is_locked': 'isLocked',
        'special_instructions': 'specialInstructions',
        'carrier_accounts': 'carrierAccounts',
        'permanent_pickups': 'permanentPickups',
        'very_frequent_address': 'veryFrequentAddress',
        'total_rows': 'totalRows',
        'company': 'company',
        'insertion_guid': 'insertionGuid',
        'company_location_receiver_accounts': 'companyLocationReceiverAccounts',
        'reference1': 'reference1',
        'reference2': 'reference2',
        'default_pickup_time': 'defaultPickupTime',
        'default_closing_time': 'defaultClosingTime',
        'default_pickup_instructions': 'defaultPickupInstructions',
        'pickup_question_ids': 'pickupQuestionIds',
        'delivery_question_ids': 'deliveryQuestionIds',
        'is_international': 'isInternational',
        'country_id': 'countryId',
        'country': 'country',
        'international_city': 'internationalCity',
        'international_province': 'internationalProvince',
        'international_postcode': 'internationalPostcode',
        'location_description': 'locationDescription'
    }

    def __init__(self, id=None, location_type=None, name=None, abbreviation=None, display_name=None, contact=None, phone=None, email=None, address_line1=None, address_line2=None, address_lines_friendly=None, company_id=None, location_id=None, location=None, location_as_string=None, is_locked=None, special_instructions=None, carrier_accounts=None, permanent_pickups=None, very_frequent_address=None, total_rows=None, company=None, insertion_guid=None, company_location_receiver_accounts=None, reference1=None, reference2=None, default_pickup_time=None, default_closing_time=None, default_pickup_instructions=None, pickup_question_ids=None, delivery_question_ids=None, is_international=None, country_id=None, country=None, international_city=None, international_province=None, international_postcode=None, location_description=None):  # noqa: E501
        """CompanyLocation - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._location_type = None
        self._name = None
        self._abbreviation = None
        self._display_name = None
        self._contact = None
        self._phone = None
        self._email = None
        self._address_line1 = None
        self._address_line2 = None
        self._address_lines_friendly = None
        self._company_id = None
        self._location_id = None
        self._location = None
        self._location_as_string = None
        self._is_locked = None
        self._special_instructions = None
        self._carrier_accounts = None
        self._permanent_pickups = None
        self._very_frequent_address = None
        self._total_rows = None
        self._company = None
        self._insertion_guid = None
        self._company_location_receiver_accounts = None
        self._reference1 = None
        self._reference2 = None
        self._default_pickup_time = None
        self._default_closing_time = None
        self._default_pickup_instructions = None
        self._pickup_question_ids = None
        self._delivery_question_ids = None
        self._is_international = None
        self._country_id = None
        self._country = None
        self._international_city = None
        self._international_province = None
        self._international_postcode = None
        self._location_description = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if location_type is not None:
            self.location_type = location_type
        self.name = name
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if display_name is not None:
            self.display_name = display_name
        if contact is not None:
            self.contact = contact
        if phone is not None:
            self.phone = phone
        if email is not None:
            self.email = email
        self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if address_lines_friendly is not None:
            self.address_lines_friendly = address_lines_friendly
        if company_id is not None:
            self.company_id = company_id
        if location_id is not None:
            self.location_id = location_id
        if location is not None:
            self.location = location
        if location_as_string is not None:
            self.location_as_string = location_as_string
        if is_locked is not None:
            self.is_locked = is_locked
        if special_instructions is not None:
            self.special_instructions = special_instructions
        if carrier_accounts is not None:
            self.carrier_accounts = carrier_accounts
        if permanent_pickups is not None:
            self.permanent_pickups = permanent_pickups
        if very_frequent_address is not None:
            self.very_frequent_address = very_frequent_address
        if total_rows is not None:
            self.total_rows = total_rows
        if company is not None:
            self.company = company
        if insertion_guid is not None:
            self.insertion_guid = insertion_guid
        if company_location_receiver_accounts is not None:
            self.company_location_receiver_accounts = company_location_receiver_accounts
        if reference1 is not None:
            self.reference1 = reference1
        if reference2 is not None:
            self.reference2 = reference2
        if default_pickup_time is not None:
            self.default_pickup_time = default_pickup_time
        if default_closing_time is not None:
            self.default_closing_time = default_closing_time
        if default_pickup_instructions is not None:
            self.default_pickup_instructions = default_pickup_instructions
        if pickup_question_ids is not None:
            self.pickup_question_ids = pickup_question_ids
        if delivery_question_ids is not None:
            self.delivery_question_ids = delivery_question_ids
        if is_international is not None:
            self.is_international = is_international
        if country_id is not None:
            self.country_id = country_id
        if country is not None:
            self.country = country
        if international_city is not None:
            self.international_city = international_city
        if international_province is not None:
            self.international_province = international_province
        if international_postcode is not None:
            self.international_postcode = international_postcode
        if location_description is not None:
            self.location_description = location_description

    @property
    def id(self):
        """Gets the id of this CompanyLocation.  # noqa: E501


        :return: The id of this CompanyLocation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CompanyLocation.


        :param id: The id of this CompanyLocation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def location_type(self):
        """Gets the location_type of this CompanyLocation.  # noqa: E501


        :return: The location_type of this CompanyLocation.  # noqa: E501
        :rtype: CompanyLocationType
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this CompanyLocation.


        :param location_type: The location_type of this CompanyLocation.  # noqa: E501
        :type: CompanyLocationType
        """

        self._location_type = location_type

    @property
    def name(self):
        """Gets the name of this CompanyLocation.  # noqa: E501


        :return: The name of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CompanyLocation.


        :param name: The name of this CompanyLocation.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this CompanyLocation.  # noqa: E501


        :return: The abbreviation of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this CompanyLocation.


        :param abbreviation: The abbreviation of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def display_name(self):
        """Gets the display_name of this CompanyLocation.  # noqa: E501


        :return: The display_name of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CompanyLocation.


        :param display_name: The display_name of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def contact(self):
        """Gets the contact of this CompanyLocation.  # noqa: E501


        :return: The contact of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this CompanyLocation.


        :param contact: The contact of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._contact = contact

    @property
    def phone(self):
        """Gets the phone of this CompanyLocation.  # noqa: E501


        :return: The phone of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CompanyLocation.


        :param phone: The phone of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email(self):
        """Gets the email of this CompanyLocation.  # noqa: E501


        :return: The email of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CompanyLocation.


        :param email: The email of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def address_line1(self):
        """Gets the address_line1 of this CompanyLocation.  # noqa: E501


        :return: The address_line1 of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this CompanyLocation.


        :param address_line1: The address_line1 of this CompanyLocation.  # noqa: E501
        :type: str
        """
        if address_line1 is None:
            raise ValueError("Invalid value for `address_line1`, must not be `None`")  # noqa: E501

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this CompanyLocation.  # noqa: E501


        :return: The address_line2 of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this CompanyLocation.


        :param address_line2: The address_line2 of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def address_lines_friendly(self):
        """Gets the address_lines_friendly of this CompanyLocation.  # noqa: E501


        :return: The address_lines_friendly of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._address_lines_friendly

    @address_lines_friendly.setter
    def address_lines_friendly(self, address_lines_friendly):
        """Sets the address_lines_friendly of this CompanyLocation.


        :param address_lines_friendly: The address_lines_friendly of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._address_lines_friendly = address_lines_friendly

    @property
    def company_id(self):
        """Gets the company_id of this CompanyLocation.  # noqa: E501


        :return: The company_id of this CompanyLocation.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this CompanyLocation.


        :param company_id: The company_id of this CompanyLocation.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def location_id(self):
        """Gets the location_id of this CompanyLocation.  # noqa: E501


        :return: The location_id of this CompanyLocation.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this CompanyLocation.


        :param location_id: The location_id of this CompanyLocation.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def location(self):
        """Gets the location of this CompanyLocation.  # noqa: E501


        :return: The location of this CompanyLocation.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CompanyLocation.


        :param location: The location of this CompanyLocation.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def location_as_string(self):
        """Gets the location_as_string of this CompanyLocation.  # noqa: E501


        :return: The location_as_string of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._location_as_string

    @location_as_string.setter
    def location_as_string(self, location_as_string):
        """Sets the location_as_string of this CompanyLocation.


        :param location_as_string: The location_as_string of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._location_as_string = location_as_string

    @property
    def is_locked(self):
        """Gets the is_locked of this CompanyLocation.  # noqa: E501


        :return: The is_locked of this CompanyLocation.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this CompanyLocation.


        :param is_locked: The is_locked of this CompanyLocation.  # noqa: E501
        :type: bool
        """

        self._is_locked = is_locked

    @property
    def special_instructions(self):
        """Gets the special_instructions of this CompanyLocation.  # noqa: E501


        :return: The special_instructions of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._special_instructions

    @special_instructions.setter
    def special_instructions(self, special_instructions):
        """Sets the special_instructions of this CompanyLocation.


        :param special_instructions: The special_instructions of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._special_instructions = special_instructions

    @property
    def carrier_accounts(self):
        """Gets the carrier_accounts of this CompanyLocation.  # noqa: E501


        :return: The carrier_accounts of this CompanyLocation.  # noqa: E501
        :rtype: list[BaseCarrierAccount]
        """
        return self._carrier_accounts

    @carrier_accounts.setter
    def carrier_accounts(self, carrier_accounts):
        """Sets the carrier_accounts of this CompanyLocation.


        :param carrier_accounts: The carrier_accounts of this CompanyLocation.  # noqa: E501
        :type: list[BaseCarrierAccount]
        """

        self._carrier_accounts = carrier_accounts

    @property
    def permanent_pickups(self):
        """Gets the permanent_pickups of this CompanyLocation.  # noqa: E501


        :return: The permanent_pickups of this CompanyLocation.  # noqa: E501
        :rtype: list[PermanentPickup]
        """
        return self._permanent_pickups

    @permanent_pickups.setter
    def permanent_pickups(self, permanent_pickups):
        """Sets the permanent_pickups of this CompanyLocation.


        :param permanent_pickups: The permanent_pickups of this CompanyLocation.  # noqa: E501
        :type: list[PermanentPickup]
        """

        self._permanent_pickups = permanent_pickups

    @property
    def very_frequent_address(self):
        """Gets the very_frequent_address of this CompanyLocation.  # noqa: E501


        :return: The very_frequent_address of this CompanyLocation.  # noqa: E501
        :rtype: bool
        """
        return self._very_frequent_address

    @very_frequent_address.setter
    def very_frequent_address(self, very_frequent_address):
        """Sets the very_frequent_address of this CompanyLocation.


        :param very_frequent_address: The very_frequent_address of this CompanyLocation.  # noqa: E501
        :type: bool
        """

        self._very_frequent_address = very_frequent_address

    @property
    def total_rows(self):
        """Gets the total_rows of this CompanyLocation.  # noqa: E501


        :return: The total_rows of this CompanyLocation.  # noqa: E501
        :rtype: int
        """
        return self._total_rows

    @total_rows.setter
    def total_rows(self, total_rows):
        """Sets the total_rows of this CompanyLocation.


        :param total_rows: The total_rows of this CompanyLocation.  # noqa: E501
        :type: int
        """

        self._total_rows = total_rows

    @property
    def company(self):
        """Gets the company of this CompanyLocation.  # noqa: E501


        :return: The company of this CompanyLocation.  # noqa: E501
        :rtype: CompanyLite
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this CompanyLocation.


        :param company: The company of this CompanyLocation.  # noqa: E501
        :type: CompanyLite
        """

        self._company = company

    @property
    def insertion_guid(self):
        """Gets the insertion_guid of this CompanyLocation.  # noqa: E501


        :return: The insertion_guid of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._insertion_guid

    @insertion_guid.setter
    def insertion_guid(self, insertion_guid):
        """Sets the insertion_guid of this CompanyLocation.


        :param insertion_guid: The insertion_guid of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._insertion_guid = insertion_guid

    @property
    def company_location_receiver_accounts(self):
        """Gets the company_location_receiver_accounts of this CompanyLocation.  # noqa: E501


        :return: The company_location_receiver_accounts of this CompanyLocation.  # noqa: E501
        :rtype: list[CompanyLocationReceiverAccount]
        """
        return self._company_location_receiver_accounts

    @company_location_receiver_accounts.setter
    def company_location_receiver_accounts(self, company_location_receiver_accounts):
        """Sets the company_location_receiver_accounts of this CompanyLocation.


        :param company_location_receiver_accounts: The company_location_receiver_accounts of this CompanyLocation.  # noqa: E501
        :type: list[CompanyLocationReceiverAccount]
        """

        self._company_location_receiver_accounts = company_location_receiver_accounts

    @property
    def reference1(self):
        """Gets the reference1 of this CompanyLocation.  # noqa: E501


        :return: The reference1 of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._reference1

    @reference1.setter
    def reference1(self, reference1):
        """Sets the reference1 of this CompanyLocation.


        :param reference1: The reference1 of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._reference1 = reference1

    @property
    def reference2(self):
        """Gets the reference2 of this CompanyLocation.  # noqa: E501


        :return: The reference2 of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._reference2

    @reference2.setter
    def reference2(self, reference2):
        """Sets the reference2 of this CompanyLocation.


        :param reference2: The reference2 of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._reference2 = reference2

    @property
    def default_pickup_time(self):
        """Gets the default_pickup_time of this CompanyLocation.  # noqa: E501


        :return: The default_pickup_time of this CompanyLocation.  # noqa: E501
        :rtype: TimeSpan
        """
        return self._default_pickup_time

    @default_pickup_time.setter
    def default_pickup_time(self, default_pickup_time):
        """Sets the default_pickup_time of this CompanyLocation.


        :param default_pickup_time: The default_pickup_time of this CompanyLocation.  # noqa: E501
        :type: TimeSpan
        """

        self._default_pickup_time = default_pickup_time

    @property
    def default_closing_time(self):
        """Gets the default_closing_time of this CompanyLocation.  # noqa: E501


        :return: The default_closing_time of this CompanyLocation.  # noqa: E501
        :rtype: TimeSpan
        """
        return self._default_closing_time

    @default_closing_time.setter
    def default_closing_time(self, default_closing_time):
        """Sets the default_closing_time of this CompanyLocation.


        :param default_closing_time: The default_closing_time of this CompanyLocation.  # noqa: E501
        :type: TimeSpan
        """

        self._default_closing_time = default_closing_time

    @property
    def default_pickup_instructions(self):
        """Gets the default_pickup_instructions of this CompanyLocation.  # noqa: E501


        :return: The default_pickup_instructions of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._default_pickup_instructions

    @default_pickup_instructions.setter
    def default_pickup_instructions(self, default_pickup_instructions):
        """Sets the default_pickup_instructions of this CompanyLocation.


        :param default_pickup_instructions: The default_pickup_instructions of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._default_pickup_instructions = default_pickup_instructions

    @property
    def pickup_question_ids(self):
        """Gets the pickup_question_ids of this CompanyLocation.  # noqa: E501


        :return: The pickup_question_ids of this CompanyLocation.  # noqa: E501
        :rtype: list[int]
        """
        return self._pickup_question_ids

    @pickup_question_ids.setter
    def pickup_question_ids(self, pickup_question_ids):
        """Sets the pickup_question_ids of this CompanyLocation.


        :param pickup_question_ids: The pickup_question_ids of this CompanyLocation.  # noqa: E501
        :type: list[int]
        """

        self._pickup_question_ids = pickup_question_ids

    @property
    def delivery_question_ids(self):
        """Gets the delivery_question_ids of this CompanyLocation.  # noqa: E501


        :return: The delivery_question_ids of this CompanyLocation.  # noqa: E501
        :rtype: list[int]
        """
        return self._delivery_question_ids

    @delivery_question_ids.setter
    def delivery_question_ids(self, delivery_question_ids):
        """Sets the delivery_question_ids of this CompanyLocation.


        :param delivery_question_ids: The delivery_question_ids of this CompanyLocation.  # noqa: E501
        :type: list[int]
        """

        self._delivery_question_ids = delivery_question_ids

    @property
    def is_international(self):
        """Gets the is_international of this CompanyLocation.  # noqa: E501


        :return: The is_international of this CompanyLocation.  # noqa: E501
        :rtype: bool
        """
        return self._is_international

    @is_international.setter
    def is_international(self, is_international):
        """Sets the is_international of this CompanyLocation.


        :param is_international: The is_international of this CompanyLocation.  # noqa: E501
        :type: bool
        """

        self._is_international = is_international

    @property
    def country_id(self):
        """Gets the country_id of this CompanyLocation.  # noqa: E501


        :return: The country_id of this CompanyLocation.  # noqa: E501
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """Sets the country_id of this CompanyLocation.


        :param country_id: The country_id of this CompanyLocation.  # noqa: E501
        :type: int
        """

        self._country_id = country_id

    @property
    def country(self):
        """Gets the country of this CompanyLocation.  # noqa: E501


        :return: The country of this CompanyLocation.  # noqa: E501
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CompanyLocation.


        :param country: The country of this CompanyLocation.  # noqa: E501
        :type: Country
        """

        self._country = country

    @property
    def international_city(self):
        """Gets the international_city of this CompanyLocation.  # noqa: E501


        :return: The international_city of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._international_city

    @international_city.setter
    def international_city(self, international_city):
        """Sets the international_city of this CompanyLocation.


        :param international_city: The international_city of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._international_city = international_city

    @property
    def international_province(self):
        """Gets the international_province of this CompanyLocation.  # noqa: E501


        :return: The international_province of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._international_province

    @international_province.setter
    def international_province(self, international_province):
        """Sets the international_province of this CompanyLocation.


        :param international_province: The international_province of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._international_province = international_province

    @property
    def international_postcode(self):
        """Gets the international_postcode of this CompanyLocation.  # noqa: E501


        :return: The international_postcode of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._international_postcode

    @international_postcode.setter
    def international_postcode(self, international_postcode):
        """Sets the international_postcode of this CompanyLocation.


        :param international_postcode: The international_postcode of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._international_postcode = international_postcode

    @property
    def location_description(self):
        """Gets the location_description of this CompanyLocation.  # noqa: E501


        :return: The location_description of this CompanyLocation.  # noqa: E501
        :rtype: str
        """
        return self._location_description

    @location_description.setter
    def location_description(self, location_description):
        """Sets the location_description of this CompanyLocation.


        :param location_description: The location_description of this CompanyLocation.  # noqa: E501
        :type: str
        """

        self._location_description = location_description

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
        if issubclass(CompanyLocation, dict):
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
        if not isinstance(other, CompanyLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
