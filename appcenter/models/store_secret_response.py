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


class StoreSecretResponse(object):
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
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'secret': 'str',
        'tenant_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'secret': 'secret',
        'tenant_id': 'tenant_id'
    }

    def __init__(self, id=None, name=None, type=None, secret=None, tenant_id=None):  # noqa: E501
        """StoreSecretResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._type = None
        self._secret = None
        self._tenant_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if secret is not None:
            self.secret = secret
        if tenant_id is not None:
            self.tenant_id = tenant_id

    @property
    def id(self):
        """Gets the id of this StoreSecretResponse.  # noqa: E501

        Store id  # noqa: E501

        :return: The id of this StoreSecretResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoreSecretResponse.

        Store id  # noqa: E501

        :param id: The id of this StoreSecretResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StoreSecretResponse.  # noqa: E501

        Store Name  # noqa: E501

        :return: The name of this StoreSecretResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StoreSecretResponse.

        Store Name  # noqa: E501

        :param name: The name of this StoreSecretResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this StoreSecretResponse.  # noqa: E501

        Store Type  # noqa: E501

        :return: The type of this StoreSecretResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StoreSecretResponse.

        Store Type  # noqa: E501

        :param type: The type of this StoreSecretResponse.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def secret(self):
        """Gets the secret of this StoreSecretResponse.  # noqa: E501

        Secret Json  # noqa: E501

        :return: The secret of this StoreSecretResponse.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this StoreSecretResponse.

        Secret Json  # noqa: E501

        :param secret: The secret of this StoreSecretResponse.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def tenant_id(self):
        """Gets the tenant_id of this StoreSecretResponse.  # noqa: E501

        Tenant Id for Intune  # noqa: E501

        :return: The tenant_id of this StoreSecretResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this StoreSecretResponse.

        Tenant Id for Intune  # noqa: E501

        :param tenant_id: The tenant_id of this StoreSecretResponse.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

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
        if issubclass(StoreSecretResponse, dict):
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
        if not isinstance(other, StoreSecretResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other