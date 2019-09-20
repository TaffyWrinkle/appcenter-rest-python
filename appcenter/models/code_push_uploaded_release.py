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
from appcenter.models.code_push_release_upload import CodePushReleaseUpload  # noqa: F401,E501


class CodePushUploadedRelease(object):
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
        'release_upload': 'CodePushReleaseUpload',
        'target_binary_version': 'str',
        'deployment_name': 'str',
        'description': 'str',
        'disabled': 'bool',
        'mandatory': 'bool',
        'no_duplicate_release_error': 'bool',
        'rollout': 'int'
    }

    attribute_map = {
        'release_upload': 'release_upload',
        'target_binary_version': 'target_binary_version',
        'deployment_name': 'deployment_name',
        'description': 'description',
        'disabled': 'disabled',
        'mandatory': 'mandatory',
        'no_duplicate_release_error': 'no_duplicate_release_error',
        'rollout': 'rollout'
    }

    def __init__(self, release_upload=None, target_binary_version=None, deployment_name=None, description=None, disabled=None, mandatory=None, no_duplicate_release_error=None, rollout=None):  # noqa: E501
        """CodePushUploadedRelease - a model defined in Swagger"""  # noqa: E501
        self._release_upload = None
        self._target_binary_version = None
        self._deployment_name = None
        self._description = None
        self._disabled = None
        self._mandatory = None
        self._no_duplicate_release_error = None
        self._rollout = None
        self.discriminator = None
        self.release_upload = release_upload
        self.target_binary_version = target_binary_version
        if deployment_name is not None:
            self.deployment_name = deployment_name
        if description is not None:
            self.description = description
        if disabled is not None:
            self.disabled = disabled
        if mandatory is not None:
            self.mandatory = mandatory
        if no_duplicate_release_error is not None:
            self.no_duplicate_release_error = no_duplicate_release_error
        if rollout is not None:
            self.rollout = rollout

    @property
    def release_upload(self):
        """Gets the release_upload of this CodePushUploadedRelease.  # noqa: E501


        :return: The release_upload of this CodePushUploadedRelease.  # noqa: E501
        :rtype: CodePushReleaseUpload
        """
        return self._release_upload

    @release_upload.setter
    def release_upload(self, release_upload):
        """Sets the release_upload of this CodePushUploadedRelease.


        :param release_upload: The release_upload of this CodePushUploadedRelease.  # noqa: E501
        :type: CodePushReleaseUpload
        """
        if release_upload is None:
            raise ValueError("Invalid value for `release_upload`, must not be `None`")  # noqa: E501

        self._release_upload = release_upload

    @property
    def target_binary_version(self):
        """Gets the target_binary_version of this CodePushUploadedRelease.  # noqa: E501

        the binary version of the application  # noqa: E501

        :return: The target_binary_version of this CodePushUploadedRelease.  # noqa: E501
        :rtype: str
        """
        return self._target_binary_version

    @target_binary_version.setter
    def target_binary_version(self, target_binary_version):
        """Sets the target_binary_version of this CodePushUploadedRelease.

        the binary version of the application  # noqa: E501

        :param target_binary_version: The target_binary_version of this CodePushUploadedRelease.  # noqa: E501
        :type: str
        """
        if target_binary_version is None:
            raise ValueError("Invalid value for `target_binary_version`, must not be `None`")  # noqa: E501

        self._target_binary_version = target_binary_version

    @property
    def deployment_name(self):
        """Gets the deployment_name of this CodePushUploadedRelease.  # noqa: E501

        This specifies which deployment you want to release the update to. Default is Staging.  # noqa: E501

        :return: The deployment_name of this CodePushUploadedRelease.  # noqa: E501
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        """Sets the deployment_name of this CodePushUploadedRelease.

        This specifies which deployment you want to release the update to. Default is Staging.  # noqa: E501

        :param deployment_name: The deployment_name of this CodePushUploadedRelease.  # noqa: E501
        :type: str
        """

        self._deployment_name = deployment_name

    @property
    def description(self):
        """Gets the description of this CodePushUploadedRelease.  # noqa: E501

        This provides an optional \"change log\" for the deployment.  # noqa: E501

        :return: The description of this CodePushUploadedRelease.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CodePushUploadedRelease.

        This provides an optional \"change log\" for the deployment.  # noqa: E501

        :param description: The description of this CodePushUploadedRelease.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def disabled(self):
        """Gets the disabled of this CodePushUploadedRelease.  # noqa: E501

        This specifies whether an update should be downloadable by end users or not.  # noqa: E501

        :return: The disabled of this CodePushUploadedRelease.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this CodePushUploadedRelease.

        This specifies whether an update should be downloadable by end users or not.  # noqa: E501

        :param disabled: The disabled of this CodePushUploadedRelease.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def mandatory(self):
        """Gets the mandatory of this CodePushUploadedRelease.  # noqa: E501

        This specifies whether the update should be considered mandatory or not (e.g. it includes a critical security fix).  # noqa: E501

        :return: The mandatory of this CodePushUploadedRelease.  # noqa: E501
        :rtype: bool
        """
        return self._mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        """Sets the mandatory of this CodePushUploadedRelease.

        This specifies whether the update should be considered mandatory or not (e.g. it includes a critical security fix).  # noqa: E501

        :param mandatory: The mandatory of this CodePushUploadedRelease.  # noqa: E501
        :type: bool
        """

        self._mandatory = mandatory

    @property
    def no_duplicate_release_error(self):
        """Gets the no_duplicate_release_error of this CodePushUploadedRelease.  # noqa: E501

        This specifies that if the update is identical to the latest release on the deployment, the CLI should generate a warning instead of an error.  # noqa: E501

        :return: The no_duplicate_release_error of this CodePushUploadedRelease.  # noqa: E501
        :rtype: bool
        """
        return self._no_duplicate_release_error

    @no_duplicate_release_error.setter
    def no_duplicate_release_error(self, no_duplicate_release_error):
        """Sets the no_duplicate_release_error of this CodePushUploadedRelease.

        This specifies that if the update is identical to the latest release on the deployment, the CLI should generate a warning instead of an error.  # noqa: E501

        :param no_duplicate_release_error: The no_duplicate_release_error of this CodePushUploadedRelease.  # noqa: E501
        :type: bool
        """

        self._no_duplicate_release_error = no_duplicate_release_error

    @property
    def rollout(self):
        """Gets the rollout of this CodePushUploadedRelease.  # noqa: E501

        This specifies the percentage of users (as an integer between 1 and 100) that should be eligible to receive this update.  # noqa: E501

        :return: The rollout of this CodePushUploadedRelease.  # noqa: E501
        :rtype: int
        """
        return self._rollout

    @rollout.setter
    def rollout(self, rollout):
        """Sets the rollout of this CodePushUploadedRelease.

        This specifies the percentage of users (as an integer between 1 and 100) that should be eligible to receive this update.  # noqa: E501

        :param rollout: The rollout of this CodePushUploadedRelease.  # noqa: E501
        :type: int
        """

        self._rollout = rollout

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
        if issubclass(CodePushUploadedRelease, dict):
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
        if not isinstance(other, CodePushUploadedRelease):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other