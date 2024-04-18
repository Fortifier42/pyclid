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

class SurchargeV2(object):
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
        'abbreviation': 'str',
        'company_id': 'int',
        'description': 'str',
        'price': 'float',
        'sell_price': 'float',
        'hard_set_sell_price': 'float',
        'percentage_of_sell_price': 'float',
        'cost_minimum': 'float',
        'sell_minimum': 'float',
        'markup': 'float',
        'automatic': 'bool',
        'is_fuel_levy_exempt': 'bool',
        'only_apply_surcharge_to_dg': 'bool',
        'is_conditional': 'bool',
        'per_lane_rate': 'bool',
        'per_matching_item': 'bool',
        'price_type': 'SurchargePriceType',
        'special_instructions': 'str',
        'sell_ratecard_id': 'int',
        'cost_ratecard_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'abbreviation': 'abbreviation',
        'company_id': 'companyId',
        'description': 'description',
        'price': 'price',
        'sell_price': 'sellPrice',
        'hard_set_sell_price': 'hardSetSellPrice',
        'percentage_of_sell_price': 'percentageOfSellPrice',
        'cost_minimum': 'costMinimum',
        'sell_minimum': 'sellMinimum',
        'markup': 'markup',
        'automatic': 'automatic',
        'is_fuel_levy_exempt': 'isFuelLevyExempt',
        'only_apply_surcharge_to_dg': 'onlyApplySurchargeToDG',
        'is_conditional': 'isConditional',
        'per_lane_rate': 'perLaneRate',
        'per_matching_item': 'perMatchingItem',
        'price_type': 'priceType',
        'special_instructions': 'specialInstructions',
        'sell_ratecard_id': 'sellRatecardId',
        'cost_ratecard_id': 'costRatecardId'
    }

    def __init__(self, id=None, name=None, abbreviation=None, company_id=None, description=None, price=None, sell_price=None, hard_set_sell_price=None, percentage_of_sell_price=None, cost_minimum=None, sell_minimum=None, markup=None, automatic=None, is_fuel_levy_exempt=None, only_apply_surcharge_to_dg=None, is_conditional=None, per_lane_rate=None, per_matching_item=None, price_type=None, special_instructions=None, sell_ratecard_id=None, cost_ratecard_id=None):  # noqa: E501
        """SurchargeV2 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._abbreviation = None
        self._company_id = None
        self._description = None
        self._price = None
        self._sell_price = None
        self._hard_set_sell_price = None
        self._percentage_of_sell_price = None
        self._cost_minimum = None
        self._sell_minimum = None
        self._markup = None
        self._automatic = None
        self._is_fuel_levy_exempt = None
        self._only_apply_surcharge_to_dg = None
        self._is_conditional = None
        self._per_lane_rate = None
        self._per_matching_item = None
        self._price_type = None
        self._special_instructions = None
        self._sell_ratecard_id = None
        self._cost_ratecard_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if company_id is not None:
            self.company_id = company_id
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if sell_price is not None:
            self.sell_price = sell_price
        if hard_set_sell_price is not None:
            self.hard_set_sell_price = hard_set_sell_price
        if percentage_of_sell_price is not None:
            self.percentage_of_sell_price = percentage_of_sell_price
        if cost_minimum is not None:
            self.cost_minimum = cost_minimum
        if sell_minimum is not None:
            self.sell_minimum = sell_minimum
        if markup is not None:
            self.markup = markup
        if automatic is not None:
            self.automatic = automatic
        if is_fuel_levy_exempt is not None:
            self.is_fuel_levy_exempt = is_fuel_levy_exempt
        if only_apply_surcharge_to_dg is not None:
            self.only_apply_surcharge_to_dg = only_apply_surcharge_to_dg
        if is_conditional is not None:
            self.is_conditional = is_conditional
        if per_lane_rate is not None:
            self.per_lane_rate = per_lane_rate
        if per_matching_item is not None:
            self.per_matching_item = per_matching_item
        if price_type is not None:
            self.price_type = price_type
        if special_instructions is not None:
            self.special_instructions = special_instructions
        if sell_ratecard_id is not None:
            self.sell_ratecard_id = sell_ratecard_id
        if cost_ratecard_id is not None:
            self.cost_ratecard_id = cost_ratecard_id

    @property
    def id(self):
        """Gets the id of this SurchargeV2.  # noqa: E501


        :return: The id of this SurchargeV2.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SurchargeV2.


        :param id: The id of this SurchargeV2.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SurchargeV2.  # noqa: E501


        :return: The name of this SurchargeV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SurchargeV2.


        :param name: The name of this SurchargeV2.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this SurchargeV2.  # noqa: E501


        :return: The abbreviation of this SurchargeV2.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this SurchargeV2.


        :param abbreviation: The abbreviation of this SurchargeV2.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def company_id(self):
        """Gets the company_id of this SurchargeV2.  # noqa: E501


        :return: The company_id of this SurchargeV2.  # noqa: E501
        :rtype: int
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this SurchargeV2.


        :param company_id: The company_id of this SurchargeV2.  # noqa: E501
        :type: int
        """

        self._company_id = company_id

    @property
    def description(self):
        """Gets the description of this SurchargeV2.  # noqa: E501


        :return: The description of this SurchargeV2.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SurchargeV2.


        :param description: The description of this SurchargeV2.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def price(self):
        """Gets the price of this SurchargeV2.  # noqa: E501

        This is the base price of the surcharge before markups have been applied  # noqa: E501

        :return: The price of this SurchargeV2.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SurchargeV2.

        This is the base price of the surcharge before markups have been applied  # noqa: E501

        :param price: The price of this SurchargeV2.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def sell_price(self):
        """Gets the sell_price of this SurchargeV2.  # noqa: E501


        :return: The sell_price of this SurchargeV2.  # noqa: E501
        :rtype: float
        """
        return self._sell_price

    @sell_price.setter
    def sell_price(self, sell_price):
        """Sets the sell_price of this SurchargeV2.


        :param sell_price: The sell_price of this SurchargeV2.  # noqa: E501
        :type: float
        """

        self._sell_price = sell_price

    @property
    def hard_set_sell_price(self):
        """Gets the hard_set_sell_price of this SurchargeV2.  # noqa: E501


        :return: The hard_set_sell_price of this SurchargeV2.  # noqa: E501
        :rtype: float
        """
        return self._hard_set_sell_price

    @hard_set_sell_price.setter
    def hard_set_sell_price(self, hard_set_sell_price):
        """Sets the hard_set_sell_price of this SurchargeV2.


        :param hard_set_sell_price: The hard_set_sell_price of this SurchargeV2.  # noqa: E501
        :type: float
        """

        self._hard_set_sell_price = hard_set_sell_price

    @property
    def percentage_of_sell_price(self):
        """Gets the percentage_of_sell_price of this SurchargeV2.  # noqa: E501


        :return: The percentage_of_sell_price of this SurchargeV2.  # noqa: E501
        :rtype: float
        """
        return self._percentage_of_sell_price

    @percentage_of_sell_price.setter
    def percentage_of_sell_price(self, percentage_of_sell_price):
        """Sets the percentage_of_sell_price of this SurchargeV2.


        :param percentage_of_sell_price: The percentage_of_sell_price of this SurchargeV2.  # noqa: E501
        :type: float
        """

        self._percentage_of_sell_price = percentage_of_sell_price

    @property
    def cost_minimum(self):
        """Gets the cost_minimum of this SurchargeV2.  # noqa: E501


        :return: The cost_minimum of this SurchargeV2.  # noqa: E501
        :rtype: float
        """
        return self._cost_minimum

    @cost_minimum.setter
    def cost_minimum(self, cost_minimum):
        """Sets the cost_minimum of this SurchargeV2.


        :param cost_minimum: The cost_minimum of this SurchargeV2.  # noqa: E501
        :type: float
        """

        self._cost_minimum = cost_minimum

    @property
    def sell_minimum(self):
        """Gets the sell_minimum of this SurchargeV2.  # noqa: E501


        :return: The sell_minimum of this SurchargeV2.  # noqa: E501
        :rtype: float
        """
        return self._sell_minimum

    @sell_minimum.setter
    def sell_minimum(self, sell_minimum):
        """Sets the sell_minimum of this SurchargeV2.


        :param sell_minimum: The sell_minimum of this SurchargeV2.  # noqa: E501
        :type: float
        """

        self._sell_minimum = sell_minimum

    @property
    def markup(self):
        """Gets the markup of this SurchargeV2.  # noqa: E501


        :return: The markup of this SurchargeV2.  # noqa: E501
        :rtype: float
        """
        return self._markup

    @markup.setter
    def markup(self, markup):
        """Sets the markup of this SurchargeV2.


        :param markup: The markup of this SurchargeV2.  # noqa: E501
        :type: float
        """

        self._markup = markup

    @property
    def automatic(self):
        """Gets the automatic of this SurchargeV2.  # noqa: E501

        Indicates this surcharge is mandatory  # noqa: E501

        :return: The automatic of this SurchargeV2.  # noqa: E501
        :rtype: bool
        """
        return self._automatic

    @automatic.setter
    def automatic(self, automatic):
        """Sets the automatic of this SurchargeV2.

        Indicates this surcharge is mandatory  # noqa: E501

        :param automatic: The automatic of this SurchargeV2.  # noqa: E501
        :type: bool
        """

        self._automatic = automatic

    @property
    def is_fuel_levy_exempt(self):
        """Gets the is_fuel_levy_exempt of this SurchargeV2.  # noqa: E501

        True if the fuel levy should not be applied to this surcharge  # noqa: E501

        :return: The is_fuel_levy_exempt of this SurchargeV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_fuel_levy_exempt

    @is_fuel_levy_exempt.setter
    def is_fuel_levy_exempt(self, is_fuel_levy_exempt):
        """Sets the is_fuel_levy_exempt of this SurchargeV2.

        True if the fuel levy should not be applied to this surcharge  # noqa: E501

        :param is_fuel_levy_exempt: The is_fuel_levy_exempt of this SurchargeV2.  # noqa: E501
        :type: bool
        """

        self._is_fuel_levy_exempt = is_fuel_levy_exempt

    @property
    def only_apply_surcharge_to_dg(self):
        """Gets the only_apply_surcharge_to_dg of this SurchargeV2.  # noqa: E501

        True if the Surcharge should only apply to DGs  # noqa: E501

        :return: The only_apply_surcharge_to_dg of this SurchargeV2.  # noqa: E501
        :rtype: bool
        """
        return self._only_apply_surcharge_to_dg

    @only_apply_surcharge_to_dg.setter
    def only_apply_surcharge_to_dg(self, only_apply_surcharge_to_dg):
        """Sets the only_apply_surcharge_to_dg of this SurchargeV2.

        True if the Surcharge should only apply to DGs  # noqa: E501

        :param only_apply_surcharge_to_dg: The only_apply_surcharge_to_dg of this SurchargeV2.  # noqa: E501
        :type: bool
        """

        self._only_apply_surcharge_to_dg = only_apply_surcharge_to_dg

    @property
    def is_conditional(self):
        """Gets the is_conditional of this SurchargeV2.  # noqa: E501


        :return: The is_conditional of this SurchargeV2.  # noqa: E501
        :rtype: bool
        """
        return self._is_conditional

    @is_conditional.setter
    def is_conditional(self, is_conditional):
        """Sets the is_conditional of this SurchargeV2.


        :param is_conditional: The is_conditional of this SurchargeV2.  # noqa: E501
        :type: bool
        """

        self._is_conditional = is_conditional

    @property
    def per_lane_rate(self):
        """Gets the per_lane_rate of this SurchargeV2.  # noqa: E501


        :return: The per_lane_rate of this SurchargeV2.  # noqa: E501
        :rtype: bool
        """
        return self._per_lane_rate

    @per_lane_rate.setter
    def per_lane_rate(self, per_lane_rate):
        """Sets the per_lane_rate of this SurchargeV2.


        :param per_lane_rate: The per_lane_rate of this SurchargeV2.  # noqa: E501
        :type: bool
        """

        self._per_lane_rate = per_lane_rate

    @property
    def per_matching_item(self):
        """Gets the per_matching_item of this SurchargeV2.  # noqa: E501


        :return: The per_matching_item of this SurchargeV2.  # noqa: E501
        :rtype: bool
        """
        return self._per_matching_item

    @per_matching_item.setter
    def per_matching_item(self, per_matching_item):
        """Sets the per_matching_item of this SurchargeV2.


        :param per_matching_item: The per_matching_item of this SurchargeV2.  # noqa: E501
        :type: bool
        """

        self._per_matching_item = per_matching_item

    @property
    def price_type(self):
        """Gets the price_type of this SurchargeV2.  # noqa: E501


        :return: The price_type of this SurchargeV2.  # noqa: E501
        :rtype: SurchargePriceType
        """
        return self._price_type

    @price_type.setter
    def price_type(self, price_type):
        """Sets the price_type of this SurchargeV2.


        :param price_type: The price_type of this SurchargeV2.  # noqa: E501
        :type: SurchargePriceType
        """

        self._price_type = price_type

    @property
    def special_instructions(self):
        """Gets the special_instructions of this SurchargeV2.  # noqa: E501


        :return: The special_instructions of this SurchargeV2.  # noqa: E501
        :rtype: str
        """
        return self._special_instructions

    @special_instructions.setter
    def special_instructions(self, special_instructions):
        """Sets the special_instructions of this SurchargeV2.


        :param special_instructions: The special_instructions of this SurchargeV2.  # noqa: E501
        :type: str
        """

        self._special_instructions = special_instructions

    @property
    def sell_ratecard_id(self):
        """Gets the sell_ratecard_id of this SurchargeV2.  # noqa: E501


        :return: The sell_ratecard_id of this SurchargeV2.  # noqa: E501
        :rtype: int
        """
        return self._sell_ratecard_id

    @sell_ratecard_id.setter
    def sell_ratecard_id(self, sell_ratecard_id):
        """Sets the sell_ratecard_id of this SurchargeV2.


        :param sell_ratecard_id: The sell_ratecard_id of this SurchargeV2.  # noqa: E501
        :type: int
        """

        self._sell_ratecard_id = sell_ratecard_id

    @property
    def cost_ratecard_id(self):
        """Gets the cost_ratecard_id of this SurchargeV2.  # noqa: E501


        :return: The cost_ratecard_id of this SurchargeV2.  # noqa: E501
        :rtype: int
        """
        return self._cost_ratecard_id

    @cost_ratecard_id.setter
    def cost_ratecard_id(self, cost_ratecard_id):
        """Sets the cost_ratecard_id of this SurchargeV2.


        :param cost_ratecard_id: The cost_ratecard_id of this SurchargeV2.  # noqa: E501
        :type: int
        """

        self._cost_ratecard_id = cost_ratecard_id

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
        if issubclass(SurchargeV2, dict):
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
        if not isinstance(other, SurchargeV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other