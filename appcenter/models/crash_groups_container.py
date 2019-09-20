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
from appcenter.models.crash_group import CrashGroup  # noqa: F401,E501


class CrashGroupsContainer(object):
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
        'limited_result_set': 'bool',
        'continuation_token': 'str',
        'crash_groups': 'list[CrashGroup]'
    }

    attribute_map = {
        'limited_result_set': 'limited_result_set',
        'continuation_token': 'continuation_token',
        'crash_groups': 'crash_groups'
    }

    def __init__(self, limited_result_set=None, continuation_token=None, crash_groups=None):  # noqa: E501
        """CrashGroupsContainer - a model defined in Swagger"""  # noqa: E501
        self._limited_result_set = None
        self._continuation_token = None
        self._crash_groups = None
        self.discriminator = None
        self.limited_result_set = limited_result_set
        if continuation_token is not None:
            self.continuation_token = continuation_token
        self.crash_groups = crash_groups

    @property
    def limited_result_set(self):
        """Gets the limited_result_set of this CrashGroupsContainer.  # noqa: E501


        :return: The limited_result_set of this CrashGroupsContainer.  # noqa: E501
        :rtype: bool
        """
        return self._limited_result_set

    @limited_result_set.setter
    def limited_result_set(self, limited_result_set):
        """Sets the limited_result_set of this CrashGroupsContainer.


        :param limited_result_set: The limited_result_set of this CrashGroupsContainer.  # noqa: E501
        :type: bool
        """
        if limited_result_set is None:
            raise ValueError("Invalid value for `limited_result_set`, must not be `None`")  # noqa: E501

        self._limited_result_set = limited_result_set

    @property
    def continuation_token(self):
        """Gets the continuation_token of this CrashGroupsContainer.  # noqa: E501

        Cassandra request continuation token. The token is used for pagination.  # noqa: E501

        :return: The continuation_token of this CrashGroupsContainer.  # noqa: E501
        :rtype: str
        """
        return self._continuation_token

    @continuation_token.setter
    def continuation_token(self, continuation_token):
        """Sets the continuation_token of this CrashGroupsContainer.

        Cassandra request continuation token. The token is used for pagination.  # noqa: E501

        :param continuation_token: The continuation_token of this CrashGroupsContainer.  # noqa: E501
        :type: str
        """

        self._continuation_token = continuation_token

    @property
    def crash_groups(self):
        """Gets the crash_groups of this CrashGroupsContainer.  # noqa: E501


        :return: The crash_groups of this CrashGroupsContainer.  # noqa: E501
        :rtype: list[CrashGroup]
        """
        return self._crash_groups

    @crash_groups.setter
    def crash_groups(self, crash_groups):
        """Sets the crash_groups of this CrashGroupsContainer.


        :param crash_groups: The crash_groups of this CrashGroupsContainer.  # noqa: E501
        :type: list[CrashGroup]
        """
        if crash_groups is None:
            raise ValueError("Invalid value for `crash_groups`, must not be `None`")  # noqa: E501

        self._crash_groups = crash_groups

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
        if issubclass(CrashGroupsContainer, dict):
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
        if not isinstance(other, CrashGroupsContainer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other