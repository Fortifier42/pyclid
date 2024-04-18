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

class ConsignmentReconciliationChargeDisplay(object):
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
        'consignment_id': 'int',
        'invoice_item_id': 'int',
        'insertion_guid': 'str',
        'charge_type': 'ConsignmentReconciliationChargeType',
        'base_sell': 'float',
        'tax_sell': 'float',
        'fuel_sell': 'float',
        'total_sell': 'float',
        'before_tax_sell': 'float',
        'base_cost': 'float',
        'tax_cost': 'float',
        'fuel_cost': 'float',
        'total_cost': 'float',
        'before_tax_cost': 'float',
        'reason': 'str',
        'carrier_invoice_entry_reconciliation_charges': 'list[CarrierInvoiceEntryReconciliationChargeDisplay]'
    }

    attribute_map = {
        'id': 'id',
        'consignment_id': 'consignmentId',
        'invoice_item_id': 'invoiceItemId',
        'insertion_guid': 'insertionGuid',
        'charge_type': 'chargeType',
        'base_sell': 'baseSell',
        'tax_sell': 'taxSell',
        'fuel_sell': 'fuelSell',
        'total_sell': 'totalSell',
        'before_tax_sell': 'beforeTaxSell',
        'base_cost': 'baseCost',
        'tax_cost': 'taxCost',
        'fuel_cost': 'fuelCost',
        'total_cost': 'totalCost',
        'before_tax_cost': 'beforeTaxCost',
        'reason': 'reason',
        'carrier_invoice_entry_reconciliation_charges': 'carrierInvoiceEntryReconciliationCharges'
    }

    def __init__(self, id=None, consignment_id=None, invoice_item_id=None, insertion_guid=None, charge_type=None, base_sell=None, tax_sell=None, fuel_sell=None, total_sell=None, before_tax_sell=None, base_cost=None, tax_cost=None, fuel_cost=None, total_cost=None, before_tax_cost=None, reason=None, carrier_invoice_entry_reconciliation_charges=None):  # noqa: E501
        """ConsignmentReconciliationChargeDisplay - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._consignment_id = None
        self._invoice_item_id = None
        self._insertion_guid = None
        self._charge_type = None
        self._base_sell = None
        self._tax_sell = None
        self._fuel_sell = None
        self._total_sell = None
        self._before_tax_sell = None
        self._base_cost = None
        self._tax_cost = None
        self._fuel_cost = None
        self._total_cost = None
        self._before_tax_cost = None
        self._reason = None
        self._carrier_invoice_entry_reconciliation_charges = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if consignment_id is not None:
            self.consignment_id = consignment_id
        if invoice_item_id is not None:
            self.invoice_item_id = invoice_item_id
        if insertion_guid is not None:
            self.insertion_guid = insertion_guid
        if charge_type is not None:
            self.charge_type = charge_type
        if base_sell is not None:
            self.base_sell = base_sell
        if tax_sell is not None:
            self.tax_sell = tax_sell
        if fuel_sell is not None:
            self.fuel_sell = fuel_sell
        if total_sell is not None:
            self.total_sell = total_sell
        if before_tax_sell is not None:
            self.before_tax_sell = before_tax_sell
        if base_cost is not None:
            self.base_cost = base_cost
        if tax_cost is not None:
            self.tax_cost = tax_cost
        if fuel_cost is not None:
            self.fuel_cost = fuel_cost
        if total_cost is not None:
            self.total_cost = total_cost
        if before_tax_cost is not None:
            self.before_tax_cost = before_tax_cost
        if reason is not None:
            self.reason = reason
        if carrier_invoice_entry_reconciliation_charges is not None:
            self.carrier_invoice_entry_reconciliation_charges = carrier_invoice_entry_reconciliation_charges

    @property
    def id(self):
        """Gets the id of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The id of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConsignmentReconciliationChargeDisplay.


        :param id: The id of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def consignment_id(self):
        """Gets the consignment_id of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The consignment_id of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: int
        """
        return self._consignment_id

    @consignment_id.setter
    def consignment_id(self, consignment_id):
        """Sets the consignment_id of this ConsignmentReconciliationChargeDisplay.


        :param consignment_id: The consignment_id of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: int
        """

        self._consignment_id = consignment_id

    @property
    def invoice_item_id(self):
        """Gets the invoice_item_id of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The invoice_item_id of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: int
        """
        return self._invoice_item_id

    @invoice_item_id.setter
    def invoice_item_id(self, invoice_item_id):
        """Sets the invoice_item_id of this ConsignmentReconciliationChargeDisplay.


        :param invoice_item_id: The invoice_item_id of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: int
        """

        self._invoice_item_id = invoice_item_id

    @property
    def insertion_guid(self):
        """Gets the insertion_guid of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The insertion_guid of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: str
        """
        return self._insertion_guid

    @insertion_guid.setter
    def insertion_guid(self, insertion_guid):
        """Sets the insertion_guid of this ConsignmentReconciliationChargeDisplay.


        :param insertion_guid: The insertion_guid of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: str
        """

        self._insertion_guid = insertion_guid

    @property
    def charge_type(self):
        """Gets the charge_type of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The charge_type of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: ConsignmentReconciliationChargeType
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this ConsignmentReconciliationChargeDisplay.


        :param charge_type: The charge_type of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: ConsignmentReconciliationChargeType
        """

        self._charge_type = charge_type

    @property
    def base_sell(self):
        """Gets the base_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The base_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: float
        """
        return self._base_sell

    @base_sell.setter
    def base_sell(self, base_sell):
        """Sets the base_sell of this ConsignmentReconciliationChargeDisplay.


        :param base_sell: The base_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: float
        """

        self._base_sell = base_sell

    @property
    def tax_sell(self):
        """Gets the tax_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The tax_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: float
        """
        return self._tax_sell

    @tax_sell.setter
    def tax_sell(self, tax_sell):
        """Sets the tax_sell of this ConsignmentReconciliationChargeDisplay.


        :param tax_sell: The tax_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: float
        """

        self._tax_sell = tax_sell

    @property
    def fuel_sell(self):
        """Gets the fuel_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The fuel_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: float
        """
        return self._fuel_sell

    @fuel_sell.setter
    def fuel_sell(self, fuel_sell):
        """Sets the fuel_sell of this ConsignmentReconciliationChargeDisplay.


        :param fuel_sell: The fuel_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: float
        """

        self._fuel_sell = fuel_sell

    @property
    def total_sell(self):
        """Gets the total_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The total_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: float
        """
        return self._total_sell

    @total_sell.setter
    def total_sell(self, total_sell):
        """Sets the total_sell of this ConsignmentReconciliationChargeDisplay.


        :param total_sell: The total_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: float
        """

        self._total_sell = total_sell

    @property
    def before_tax_sell(self):
        """Gets the before_tax_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The before_tax_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: float
        """
        return self._before_tax_sell

    @before_tax_sell.setter
    def before_tax_sell(self, before_tax_sell):
        """Sets the before_tax_sell of this ConsignmentReconciliationChargeDisplay.


        :param before_tax_sell: The before_tax_sell of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: float
        """

        self._before_tax_sell = before_tax_sell

    @property
    def base_cost(self):
        """Gets the base_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The base_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: float
        """
        return self._base_cost

    @base_cost.setter
    def base_cost(self, base_cost):
        """Sets the base_cost of this ConsignmentReconciliationChargeDisplay.


        :param base_cost: The base_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: float
        """

        self._base_cost = base_cost

    @property
    def tax_cost(self):
        """Gets the tax_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The tax_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: float
        """
        return self._tax_cost

    @tax_cost.setter
    def tax_cost(self, tax_cost):
        """Sets the tax_cost of this ConsignmentReconciliationChargeDisplay.


        :param tax_cost: The tax_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: float
        """

        self._tax_cost = tax_cost

    @property
    def fuel_cost(self):
        """Gets the fuel_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The fuel_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: float
        """
        return self._fuel_cost

    @fuel_cost.setter
    def fuel_cost(self, fuel_cost):
        """Sets the fuel_cost of this ConsignmentReconciliationChargeDisplay.


        :param fuel_cost: The fuel_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: float
        """

        self._fuel_cost = fuel_cost

    @property
    def total_cost(self):
        """Gets the total_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The total_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: float
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this ConsignmentReconciliationChargeDisplay.


        :param total_cost: The total_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: float
        """

        self._total_cost = total_cost

    @property
    def before_tax_cost(self):
        """Gets the before_tax_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The before_tax_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: float
        """
        return self._before_tax_cost

    @before_tax_cost.setter
    def before_tax_cost(self, before_tax_cost):
        """Sets the before_tax_cost of this ConsignmentReconciliationChargeDisplay.


        :param before_tax_cost: The before_tax_cost of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: float
        """

        self._before_tax_cost = before_tax_cost

    @property
    def reason(self):
        """Gets the reason of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The reason of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ConsignmentReconciliationChargeDisplay.


        :param reason: The reason of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def carrier_invoice_entry_reconciliation_charges(self):
        """Gets the carrier_invoice_entry_reconciliation_charges of this ConsignmentReconciliationChargeDisplay.  # noqa: E501


        :return: The carrier_invoice_entry_reconciliation_charges of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :rtype: list[CarrierInvoiceEntryReconciliationChargeDisplay]
        """
        return self._carrier_invoice_entry_reconciliation_charges

    @carrier_invoice_entry_reconciliation_charges.setter
    def carrier_invoice_entry_reconciliation_charges(self, carrier_invoice_entry_reconciliation_charges):
        """Sets the carrier_invoice_entry_reconciliation_charges of this ConsignmentReconciliationChargeDisplay.


        :param carrier_invoice_entry_reconciliation_charges: The carrier_invoice_entry_reconciliation_charges of this ConsignmentReconciliationChargeDisplay.  # noqa: E501
        :type: list[CarrierInvoiceEntryReconciliationChargeDisplay]
        """

        self._carrier_invoice_entry_reconciliation_charges = carrier_invoice_entry_reconciliation_charges

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
        if issubclass(ConsignmentReconciliationChargeDisplay, dict):
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
        if not isinstance(other, ConsignmentReconciliationChargeDisplay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other