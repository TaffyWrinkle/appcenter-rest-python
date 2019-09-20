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


class DistributionGroupRelease(object):
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
        'version': 'str',
        'origin': 'str',
        'short_version': 'str',
        'mandatory_update': 'bool',
        'uploaded_at': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'origin': 'origin',
        'short_version': 'short_version',
        'mandatory_update': 'mandatory_update',
        'uploaded_at': 'uploaded_at',
        'enabled': 'enabled'
    }

    def __init__(self, id=None, version=None, origin=None, short_version=None, mandatory_update=None, uploaded_at=None, enabled=None):  # noqa: E501
        """DistributionGroupRelease - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._version = None
        self._origin = None
        self._short_version = None
        self._mandatory_update = None
        self._uploaded_at = None
        self._enabled = None
        self.discriminator = None
        self.id = id
        self.version = version
        if origin is not None:
            self.origin = origin
        self.short_version = short_version
        self.mandatory_update = mandatory_update
        self.uploaded_at = uploaded_at
        self.enabled = enabled

    @property
    def id(self):
        """Gets the id of this DistributionGroupRelease.  # noqa: E501

        ID identifying this unique release.  # noqa: E501

        :return: The id of this DistributionGroupRelease.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DistributionGroupRelease.

        ID identifying this unique release.  # noqa: E501

        :param id: The id of this DistributionGroupRelease.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def version(self):
        """Gets the version of this DistributionGroupRelease.  # noqa: E501

        The release's version.<br> For iOS: CFBundleVersion from info.plist.<br> For Android: android:versionCode from AppManifest.xml.   # noqa: E501

        :return: The version of this DistributionGroupRelease.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DistributionGroupRelease.

        The release's version.<br> For iOS: CFBundleVersion from info.plist.<br> For Android: android:versionCode from AppManifest.xml.   # noqa: E501

        :param version: The version of this DistributionGroupRelease.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def origin(self):
        """Gets the origin of this DistributionGroupRelease.  # noqa: E501

        The release's origin  # noqa: E501

        :return: The origin of this DistributionGroupRelease.  # noqa: E501
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this DistributionGroupRelease.

        The release's origin  # noqa: E501

        :param origin: The origin of this DistributionGroupRelease.  # noqa: E501
        :type: str
        """
        allowed_values = ["hockeyapp", "appcenter"]  # noqa: E501
        if origin not in allowed_values:
            raise ValueError(
                "Invalid value for `origin` ({0}), must be one of {1}"  # noqa: E501
                .format(origin, allowed_values)
            )

        self._origin = origin

    @property
    def short_version(self):
        """Gets the short_version of this DistributionGroupRelease.  # noqa: E501

        The release's short version.<br> For iOS: CFBundleShortVersionString from info.plist.<br> For Android: android:versionName from AppManifest.xml.   # noqa: E501

        :return: The short_version of this DistributionGroupRelease.  # noqa: E501
        :rtype: str
        """
        return self._short_version

    @short_version.setter
    def short_version(self, short_version):
        """Sets the short_version of this DistributionGroupRelease.

        The release's short version.<br> For iOS: CFBundleShortVersionString from info.plist.<br> For Android: android:versionName from AppManifest.xml.   # noqa: E501

        :param short_version: The short_version of this DistributionGroupRelease.  # noqa: E501
        :type: str
        """
        if short_version is None:
            raise ValueError("Invalid value for `short_version`, must not be `None`")  # noqa: E501

        self._short_version = short_version

    @property
    def mandatory_update(self):
        """Gets the mandatory_update of this DistributionGroupRelease.  # noqa: E501

        A boolean which determines whether the release is a mandatory update or not.  # noqa: E501

        :return: The mandatory_update of this DistributionGroupRelease.  # noqa: E501
        :rtype: bool
        """
        return self._mandatory_update

    @mandatory_update.setter
    def mandatory_update(self, mandatory_update):
        """Sets the mandatory_update of this DistributionGroupRelease.

        A boolean which determines whether the release is a mandatory update or not.  # noqa: E501

        :param mandatory_update: The mandatory_update of this DistributionGroupRelease.  # noqa: E501
        :type: bool
        """
        if mandatory_update is None:
            raise ValueError("Invalid value for `mandatory_update`, must not be `None`")  # noqa: E501

        self._mandatory_update = mandatory_update

    @property
    def uploaded_at(self):
        """Gets the uploaded_at of this DistributionGroupRelease.  # noqa: E501

        UTC time in ISO 8601 format of the uploaded time.  # noqa: E501

        :return: The uploaded_at of this DistributionGroupRelease.  # noqa: E501
        :rtype: str
        """
        return self._uploaded_at

    @uploaded_at.setter
    def uploaded_at(self, uploaded_at):
        """Sets the uploaded_at of this DistributionGroupRelease.

        UTC time in ISO 8601 format of the uploaded time.  # noqa: E501

        :param uploaded_at: The uploaded_at of this DistributionGroupRelease.  # noqa: E501
        :type: str
        """
        if uploaded_at is None:
            raise ValueError("Invalid value for `uploaded_at`, must not be `None`")  # noqa: E501

        self._uploaded_at = uploaded_at

    @property
    def enabled(self):
        """Gets the enabled of this DistributionGroupRelease.  # noqa: E501

        This value determines the whether a release currently is enabled or disabled.  # noqa: E501

        :return: The enabled of this DistributionGroupRelease.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this DistributionGroupRelease.

        This value determines the whether a release currently is enabled or disabled.  # noqa: E501

        :param enabled: The enabled of this DistributionGroupRelease.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

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
        if issubclass(DistributionGroupRelease, dict):
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
        if not isinstance(other, DistributionGroupRelease):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other