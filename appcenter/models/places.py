# coding: utf-8

"""
    App Center Client

    Microsoft Visual Studio App Center API  # noqa: E501

    OpenAPI spec version: preview
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from appcenter.models.place import Place  # noqa: F401,E501


class Places(object):
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
        'total': 'int',
        'places': 'list[Place]'
    }

    attribute_map = {
        'total': 'total',
        'places': 'places'
    }

    def __init__(self, total=None, places=None):  # noqa: E501
        """Places - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._places = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if places is not None:
            self.places = places

    @property
    def total(self):
        """Gets the total of this Places.  # noqa: E501


        :return: The total of this Places.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Places.


        :param total: The total of this Places.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def places(self):
        """Gets the places of this Places.  # noqa: E501


        :return: The places of this Places.  # noqa: E501
        :rtype: list[Place]
        """
        return self._places

    @places.setter
    def places(self, places):
        """Sets the places of this Places.


        :param places: The places of this Places.  # noqa: E501
        :type: list[Place]
        """

        self._places = places

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
        if issubclass(Places, dict):
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
        if not isinstance(other, Places):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other