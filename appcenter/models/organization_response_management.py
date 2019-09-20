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
from appcenter.models.organization_response_internal import OrganizationResponseInternal  # noqa: F401,E501


class OrganizationResponseManagement(OrganizationResponseInternal):
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
        'email': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }
    if hasattr(OrganizationResponseInternal, "swagger_types"):
        swagger_types.update(OrganizationResponseInternal.swagger_types)

    attribute_map = {
        'email': 'email',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }
    if hasattr(OrganizationResponseInternal, "attribute_map"):
        attribute_map.update(OrganizationResponseInternal.attribute_map)

    def __init__(self, email=None, created_at=None, updated_at=None, *args, **kwargs):  # noqa: E501
        """OrganizationResponseManagement - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        if email is not None:
            self.email = email
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        OrganizationResponseInternal.__init__(self, *args, **kwargs)

    @property
    def email(self):
        """Gets the email of this OrganizationResponseManagement.  # noqa: E501

        The organization email, if the app was synced from HockeyApp  # noqa: E501

        :return: The email of this OrganizationResponseManagement.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this OrganizationResponseManagement.

        The organization email, if the app was synced from HockeyApp  # noqa: E501

        :param email: The email of this OrganizationResponseManagement.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def created_at(self):
        """Gets the created_at of this OrganizationResponseManagement.  # noqa: E501

        The date when the organization was created  # noqa: E501

        :return: The created_at of this OrganizationResponseManagement.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OrganizationResponseManagement.

        The date when the organization was created  # noqa: E501

        :param created_at: The created_at of this OrganizationResponseManagement.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this OrganizationResponseManagement.  # noqa: E501

        The date when the organization was updated  # noqa: E501

        :return: The updated_at of this OrganizationResponseManagement.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this OrganizationResponseManagement.

        The date when the organization was updated  # noqa: E501

        :param updated_at: The updated_at of this OrganizationResponseManagement.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

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
        if issubclass(OrganizationResponseManagement, dict):
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
        if not isinstance(other, OrganizationResponseManagement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other