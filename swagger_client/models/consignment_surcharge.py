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

class ConsignmentSurcharge(object):
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
        'guid': 'str',
        'id': 'int',
        'surcharge': 'Surcharge',
        'invoice_item_id': 'int',
        'invoice_item': 'InvoiceItem',
        'surcharge_id': 'int',
        'selected': 'bool',
        'cost_price': 'float',
        'sell_price': 'float',
        'markup_percentage': 'float',
        'original_price': 'float',
        'price_type': 'SurchargePriceType',
        'quantity': 'int',
        'name': 'str',
        'abbreviation': 'str',
        'consignment_item_consignment_surcharges': 'list[ConsignmentItemConsignmentSurcharge]',
        'percentage_of_sell_price': 'float'
    }

    attribute_map = {
        'guid': 'guid',
        'id': 'id',
        'surcharge': 'surcharge',
        'invoice_item_id': 'invoiceItemId',
        'invoice_item': 'invoiceItem',
        'surcharge_id': 'surchargeId',
        'selected': 'selected',
        'cost_price': 'costPrice',
        'sell_price': 'sellPrice',
        'markup_percentage': 'markupPercentage',
        'original_price': 'originalPrice',
        'price_type': 'priceType',
        'quantity': 'quantity',
        'name': 'name',
        'abbreviation': 'abbreviation',
        'consignment_item_consignment_surcharges': 'consignmentItemConsignmentSurcharges',
        'percentage_of_sell_price': 'percentageOfSellPrice'
    }

    def __init__(self, guid=None, id=None, surcharge=None, invoice_item_id=None, invoice_item=None, surcharge_id=None, selected=None, cost_price=None, sell_price=None, markup_percentage=None, original_price=None, price_type=None, quantity=None, name=None, abbreviation=None, consignment_item_consignment_surcharges=None, percentage_of_sell_price=None):  # noqa: E501
        """ConsignmentSurcharge - a model defined in Swagger"""  # noqa: E501
        self._guid = None
        self._id = None
        self._surcharge = None
        self._invoice_item_id = None
        self._invoice_item = None
        self._surcharge_id = None
        self._selected = None
        self._cost_price = None
        self._sell_price = None
        self._markup_percentage = None
        self._original_price = None
        self._price_type = None
        self._quantity = None
        self._name = None
        self._abbreviation = None
        self._consignment_item_consignment_surcharges = None
        self._percentage_of_sell_price = None
        self.discriminator = None
        if guid is not None:
            self.guid = guid
        if id is not None:
            self.id = id
        if surcharge is not None:
            self.surcharge = surcharge
        if invoice_item_id is not None:
            self.invoice_item_id = invoice_item_id
        if invoice_item is not None:
            self.invoice_item = invoice_item
        if surcharge_id is not None:
            self.surcharge_id = surcharge_id
        if selected is not None:
            self.selected = selected
        if cost_price is not None:
            self.cost_price = cost_price
        if sell_price is not None:
            self.sell_price = sell_price
        if markup_percentage is not None:
            self.markup_percentage = markup_percentage
        if original_price is not None:
            self.original_price = original_price
        if price_type is not None:
            self.price_type = price_type
        if quantity is not None:
            self.quantity = quantity
        if name is not None:
            self.name = name
        if abbreviation is not None:
            self.abbreviation = abbreviation
        if consignment_item_consignment_surcharges is not None:
            self.consignment_item_consignment_surcharges = consignment_item_consignment_surcharges
        if percentage_of_sell_price is not None:
            self.percentage_of_sell_price = percentage_of_sell_price

    @property
    def guid(self):
        """Gets the guid of this ConsignmentSurcharge.  # noqa: E501


        :return: The guid of this ConsignmentSurcharge.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this ConsignmentSurcharge.


        :param guid: The guid of this ConsignmentSurcharge.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def id(self):
        """Gets the id of this ConsignmentSurcharge.  # noqa: E501


        :return: The id of this ConsignmentSurcharge.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConsignmentSurcharge.


        :param id: The id of this ConsignmentSurcharge.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def surcharge(self):
        """Gets the surcharge of this ConsignmentSurcharge.  # noqa: E501


        :return: The surcharge of this ConsignmentSurcharge.  # noqa: E501
        :rtype: Surcharge
        """
        return self._surcharge

    @surcharge.setter
    def surcharge(self, surcharge):
        """Sets the surcharge of this ConsignmentSurcharge.


        :param surcharge: The surcharge of this ConsignmentSurcharge.  # noqa: E501
        :type: Surcharge
        """

        self._surcharge = surcharge

    @property
    def invoice_item_id(self):
        """Gets the invoice_item_id of this ConsignmentSurcharge.  # noqa: E501


        :return: The invoice_item_id of this ConsignmentSurcharge.  # noqa: E501
        :rtype: int
        """
        return self._invoice_item_id

    @invoice_item_id.setter
    def invoice_item_id(self, invoice_item_id):
        """Sets the invoice_item_id of this ConsignmentSurcharge.


        :param invoice_item_id: The invoice_item_id of this ConsignmentSurcharge.  # noqa: E501
        :type: int
        """

        self._invoice_item_id = invoice_item_id

    @property
    def invoice_item(self):
        """Gets the invoice_item of this ConsignmentSurcharge.  # noqa: E501


        :return: The invoice_item of this ConsignmentSurcharge.  # noqa: E501
        :rtype: InvoiceItem
        """
        return self._invoice_item

    @invoice_item.setter
    def invoice_item(self, invoice_item):
        """Sets the invoice_item of this ConsignmentSurcharge.


        :param invoice_item: The invoice_item of this ConsignmentSurcharge.  # noqa: E501
        :type: InvoiceItem
        """

        self._invoice_item = invoice_item

    @property
    def surcharge_id(self):
        """Gets the surcharge_id of this ConsignmentSurcharge.  # noqa: E501


        :return: The surcharge_id of this ConsignmentSurcharge.  # noqa: E501
        :rtype: int
        """
        return self._surcharge_id

    @surcharge_id.setter
    def surcharge_id(self, surcharge_id):
        """Sets the surcharge_id of this ConsignmentSurcharge.


        :param surcharge_id: The surcharge_id of this ConsignmentSurcharge.  # noqa: E501
        :type: int
        """

        self._surcharge_id = surcharge_id

    @property
    def selected(self):
        """Gets the selected of this ConsignmentSurcharge.  # noqa: E501

        used when the user selects elective surcharges  # noqa: E501

        :return: The selected of this ConsignmentSurcharge.  # noqa: E501
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this ConsignmentSurcharge.

        used when the user selects elective surcharges  # noqa: E501

        :param selected: The selected of this ConsignmentSurcharge.  # noqa: E501
        :type: bool
        """

        self._selected = selected

    @property
    def cost_price(self):
        """Gets the cost_price of this ConsignmentSurcharge.  # noqa: E501


        :return: The cost_price of this ConsignmentSurcharge.  # noqa: E501
        :rtype: float
        """
        return self._cost_price

    @cost_price.setter
    def cost_price(self, cost_price):
        """Sets the cost_price of this ConsignmentSurcharge.


        :param cost_price: The cost_price of this ConsignmentSurcharge.  # noqa: E501
        :type: float
        """

        self._cost_price = cost_price

    @property
    def sell_price(self):
        """Gets the sell_price of this ConsignmentSurcharge.  # noqa: E501


        :return: The sell_price of this ConsignmentSurcharge.  # noqa: E501
        :rtype: float
        """
        return self._sell_price

    @sell_price.setter
    def sell_price(self, sell_price):
        """Sets the sell_price of this ConsignmentSurcharge.


        :param sell_price: The sell_price of this ConsignmentSurcharge.  # noqa: E501
        :type: float
        """

        self._sell_price = sell_price

    @property
    def markup_percentage(self):
        """Gets the markup_percentage of this ConsignmentSurcharge.  # noqa: E501

        This is used by the routing engine when this surcharge is based on a percentage rather than a price  # noqa: E501

        :return: The markup_percentage of this ConsignmentSurcharge.  # noqa: E501
        :rtype: float
        """
        return self._markup_percentage

    @markup_percentage.setter
    def markup_percentage(self, markup_percentage):
        """Sets the markup_percentage of this ConsignmentSurcharge.

        This is used by the routing engine when this surcharge is based on a percentage rather than a price  # noqa: E501

        :param markup_percentage: The markup_percentage of this ConsignmentSurcharge.  # noqa: E501
        :type: float
        """

        self._markup_percentage = markup_percentage

    @property
    def original_price(self):
        """Gets the original_price of this ConsignmentSurcharge.  # noqa: E501

        This is the 'price' field from the surcharge. This is needed for the front end so it can figure out price changes on the fly  # noqa: E501

        :return: The original_price of this ConsignmentSurcharge.  # noqa: E501
        :rtype: float
        """
        return self._original_price

    @original_price.setter
    def original_price(self, original_price):
        """Sets the original_price of this ConsignmentSurcharge.

        This is the 'price' field from the surcharge. This is needed for the front end so it can figure out price changes on the fly  # noqa: E501

        :param original_price: The original_price of this ConsignmentSurcharge.  # noqa: E501
        :type: float
        """

        self._original_price = original_price

    @property
    def price_type(self):
        """Gets the price_type of this ConsignmentSurcharge.  # noqa: E501


        :return: The price_type of this ConsignmentSurcharge.  # noqa: E501
        :rtype: SurchargePriceType
        """
        return self._price_type

    @price_type.setter
    def price_type(self, price_type):
        """Sets the price_type of this ConsignmentSurcharge.


        :param price_type: The price_type of this ConsignmentSurcharge.  # noqa: E501
        :type: SurchargePriceType
        """

        self._price_type = price_type

    @property
    def quantity(self):
        """Gets the quantity of this ConsignmentSurcharge.  # noqa: E501


        :return: The quantity of this ConsignmentSurcharge.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ConsignmentSurcharge.


        :param quantity: The quantity of this ConsignmentSurcharge.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

    @property
    def name(self):
        """Gets the name of this ConsignmentSurcharge.  # noqa: E501


        :return: The name of this ConsignmentSurcharge.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConsignmentSurcharge.


        :param name: The name of this ConsignmentSurcharge.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def abbreviation(self):
        """Gets the abbreviation of this ConsignmentSurcharge.  # noqa: E501


        :return: The abbreviation of this ConsignmentSurcharge.  # noqa: E501
        :rtype: str
        """
        return self._abbreviation

    @abbreviation.setter
    def abbreviation(self, abbreviation):
        """Sets the abbreviation of this ConsignmentSurcharge.


        :param abbreviation: The abbreviation of this ConsignmentSurcharge.  # noqa: E501
        :type: str
        """

        self._abbreviation = abbreviation

    @property
    def consignment_item_consignment_surcharges(self):
        """Gets the consignment_item_consignment_surcharges of this ConsignmentSurcharge.  # noqa: E501


        :return: The consignment_item_consignment_surcharges of this ConsignmentSurcharge.  # noqa: E501
        :rtype: list[ConsignmentItemConsignmentSurcharge]
        """
        return self._consignment_item_consignment_surcharges

    @consignment_item_consignment_surcharges.setter
    def consignment_item_consignment_surcharges(self, consignment_item_consignment_surcharges):
        """Sets the consignment_item_consignment_surcharges of this ConsignmentSurcharge.


        :param consignment_item_consignment_surcharges: The consignment_item_consignment_surcharges of this ConsignmentSurcharge.  # noqa: E501
        :type: list[ConsignmentItemConsignmentSurcharge]
        """

        self._consignment_item_consignment_surcharges = consignment_item_consignment_surcharges

    @property
    def percentage_of_sell_price(self):
        """Gets the percentage_of_sell_price of this ConsignmentSurcharge.  # noqa: E501


        :return: The percentage_of_sell_price of this ConsignmentSurcharge.  # noqa: E501
        :rtype: float
        """
        return self._percentage_of_sell_price

    @percentage_of_sell_price.setter
    def percentage_of_sell_price(self, percentage_of_sell_price):
        """Sets the percentage_of_sell_price of this ConsignmentSurcharge.


        :param percentage_of_sell_price: The percentage_of_sell_price of this ConsignmentSurcharge.  # noqa: E501
        :type: float
        """

        self._percentage_of_sell_price = percentage_of_sell_price

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
        if issubclass(ConsignmentSurcharge, dict):
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
        if not isinstance(other, ConsignmentSurcharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
