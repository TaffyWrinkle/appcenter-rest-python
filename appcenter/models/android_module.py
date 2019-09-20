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


class AndroidModule(object):
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
        'name': 'str',
        'has_bundle': 'bool',
        'product_flavors': 'list[str]',
        'build_variants': 'list[str]',
        'build_types': 'list[str]',
        'is_root': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'has_bundle': 'hasBundle',
        'product_flavors': 'productFlavors',
        'build_variants': 'buildVariants',
        'build_types': 'buildTypes',
        'is_root': 'isRoot'
    }

    def __init__(self, name=None, has_bundle=None, product_flavors=None, build_variants=None, build_types=None, is_root=None):  # noqa: E501
        """AndroidModule - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._has_bundle = None
        self._product_flavors = None
        self._build_variants = None
        self._build_types = None
        self._is_root = None
        self.discriminator = None
        self.name = name
        if has_bundle is not None:
            self.has_bundle = has_bundle
        if product_flavors is not None:
            self.product_flavors = product_flavors
        if build_variants is not None:
            self.build_variants = build_variants
        if build_types is not None:
            self.build_types = build_types
        if is_root is not None:
            self.is_root = is_root

    @property
    def name(self):
        """Gets the name of this AndroidModule.  # noqa: E501

        Name of the Android module  # noqa: E501

        :return: The name of this AndroidModule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AndroidModule.

        Name of the Android module  # noqa: E501

        :param name: The name of this AndroidModule.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def has_bundle(self):
        """Gets the has_bundle of this AndroidModule.  # noqa: E501

        Module contains bundle settings  # noqa: E501

        :return: The has_bundle of this AndroidModule.  # noqa: E501
        :rtype: bool
        """
        return self._has_bundle

    @has_bundle.setter
    def has_bundle(self, has_bundle):
        """Sets the has_bundle of this AndroidModule.

        Module contains bundle settings  # noqa: E501

        :param has_bundle: The has_bundle of this AndroidModule.  # noqa: E501
        :type: bool
        """

        self._has_bundle = has_bundle

    @property
    def product_flavors(self):
        """Gets the product_flavors of this AndroidModule.  # noqa: E501

        The product flavors of the Android module  # noqa: E501

        :return: The product_flavors of this AndroidModule.  # noqa: E501
        :rtype: list[str]
        """
        return self._product_flavors

    @product_flavors.setter
    def product_flavors(self, product_flavors):
        """Sets the product_flavors of this AndroidModule.

        The product flavors of the Android module  # noqa: E501

        :param product_flavors: The product_flavors of this AndroidModule.  # noqa: E501
        :type: list[str]
        """

        self._product_flavors = product_flavors

    @property
    def build_variants(self):
        """Gets the build_variants of this AndroidModule.  # noqa: E501

        The detected build variants of the Android module (matrix of product flavor + build type (debug|release))  # noqa: E501

        :return: The build_variants of this AndroidModule.  # noqa: E501
        :rtype: list[str]
        """
        return self._build_variants

    @build_variants.setter
    def build_variants(self, build_variants):
        """Sets the build_variants of this AndroidModule.

        The detected build variants of the Android module (matrix of product flavor + build type (debug|release))  # noqa: E501

        :param build_variants: The build_variants of this AndroidModule.  # noqa: E501
        :type: list[str]
        """

        self._build_variants = build_variants

    @property
    def build_types(self):
        """Gets the build_types of this AndroidModule.  # noqa: E501

        The detected build types fo the Android module  # noqa: E501

        :return: The build_types of this AndroidModule.  # noqa: E501
        :rtype: list[str]
        """
        return self._build_types

    @build_types.setter
    def build_types(self, build_types):
        """Sets the build_types of this AndroidModule.

        The detected build types fo the Android module  # noqa: E501

        :param build_types: The build_types of this AndroidModule.  # noqa: E501
        :type: list[str]
        """

        self._build_types = build_types

    @property
    def is_root(self):
        """Gets the is_root of this AndroidModule.  # noqa: E501

        Whether the module is at the root level of the project  # noqa: E501

        :return: The is_root of this AndroidModule.  # noqa: E501
        :rtype: bool
        """
        return self._is_root

    @is_root.setter
    def is_root(self, is_root):
        """Sets the is_root of this AndroidModule.

        Whether the module is at the root level of the project  # noqa: E501

        :param is_root: The is_root of this AndroidModule.  # noqa: E501
        :type: bool
        """

        self._is_root = is_root

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
        if issubclass(AndroidModule, dict):
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
        if not isinstance(other, AndroidModule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other