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
from appcenter.models.test_run_statistics import TestRunStatistics  # noqa: F401,E501


class TestRun(object):
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
        '_date': 'str',
        'app_version': 'str',
        'test_series': 'str',
        'platform': 'str',
        'run_status': 'str',
        'result_status': 'str',
        'state': 'str',
        'status': 'str',
        'description': 'str',
        'stats': 'TestRunStatistics',
        'test_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        '_date': 'date',
        'app_version': 'appVersion',
        'test_series': 'testSeries',
        'platform': 'platform',
        'run_status': 'runStatus',
        'result_status': 'resultStatus',
        'state': 'state',
        'status': 'status',
        'description': 'description',
        'stats': 'stats',
        'test_type': 'testType'
    }

    def __init__(self, id=None, _date=None, app_version=None, test_series=None, platform=None, run_status=None, result_status=None, state=None, status=None, description=None, stats=None, test_type=None):  # noqa: E501
        """TestRun - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self.__date = None
        self._app_version = None
        self._test_series = None
        self._platform = None
        self._run_status = None
        self._result_status = None
        self._state = None
        self._status = None
        self._description = None
        self._stats = None
        self._test_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if _date is not None:
            self._date = _date
        if app_version is not None:
            self.app_version = app_version
        if test_series is not None:
            self.test_series = test_series
        if platform is not None:
            self.platform = platform
        if run_status is not None:
            self.run_status = run_status
        if result_status is not None:
            self.result_status = result_status
        if state is not None:
            self.state = state
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if stats is not None:
            self.stats = stats
        if test_type is not None:
            self.test_type = test_type

    @property
    def id(self):
        """Gets the id of this TestRun.  # noqa: E501

        The unique id of the test upload  # noqa: E501

        :return: The id of this TestRun.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestRun.

        The unique id of the test upload  # noqa: E501

        :param id: The id of this TestRun.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def _date(self):
        """Gets the _date of this TestRun.  # noqa: E501

        The date and time the test was uploaded  # noqa: E501

        :return: The _date of this TestRun.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this TestRun.

        The date and time the test was uploaded  # noqa: E501

        :param _date: The _date of this TestRun.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def app_version(self):
        """Gets the app_version of this TestRun.  # noqa: E501

        The compiled version of the app binary  # noqa: E501

        :return: The app_version of this TestRun.  # noqa: E501
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this TestRun.

        The compiled version of the app binary  # noqa: E501

        :param app_version: The app_version of this TestRun.  # noqa: E501
        :type: str
        """

        self._app_version = app_version

    @property
    def test_series(self):
        """Gets the test_series of this TestRun.  # noqa: E501

        The name of the test series with which this test upload is associated  # noqa: E501

        :return: The test_series of this TestRun.  # noqa: E501
        :rtype: str
        """
        return self._test_series

    @test_series.setter
    def test_series(self, test_series):
        """Sets the test_series of this TestRun.

        The name of the test series with which this test upload is associated  # noqa: E501

        :param test_series: The test_series of this TestRun.  # noqa: E501
        :type: str
        """

        self._test_series = test_series

    @property
    def platform(self):
        """Gets the platform of this TestRun.  # noqa: E501

        The device platform targeted by the test. Possible values are 'ios' or 'android'  # noqa: E501

        :return: The platform of this TestRun.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this TestRun.

        The device platform targeted by the test. Possible values are 'ios' or 'android'  # noqa: E501

        :param platform: The platform of this TestRun.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def run_status(self):
        """Gets the run_status of this TestRun.  # noqa: E501

        The current status of the test run, in relation to the various phases  # noqa: E501

        :return: The run_status of this TestRun.  # noqa: E501
        :rtype: str
        """
        return self._run_status

    @run_status.setter
    def run_status(self, run_status):
        """Sets the run_status of this TestRun.

        The current status of the test run, in relation to the various phases  # noqa: E501

        :param run_status: The run_status of this TestRun.  # noqa: E501
        :type: str
        """

        self._run_status = run_status

    @property
    def result_status(self):
        """Gets the result_status of this TestRun.  # noqa: E501

        The passed/failed state  # noqa: E501

        :return: The result_status of this TestRun.  # noqa: E501
        :rtype: str
        """
        return self._result_status

    @result_status.setter
    def result_status(self, result_status):
        """Sets the result_status of this TestRun.

        The passed/failed state  # noqa: E501

        :param result_status: The result_status of this TestRun.  # noqa: E501
        :type: str
        """

        self._result_status = result_status

    @property
    def state(self):
        """Gets the state of this TestRun.  # noqa: E501

        Deprecated. Use runStatus instead.  # noqa: E501

        :return: The state of this TestRun.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TestRun.

        Deprecated. Use runStatus instead.  # noqa: E501

        :param state: The state of this TestRun.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def status(self):
        """Gets the status of this TestRun.  # noqa: E501

        Deprecated. Use resultStatus instead.  # noqa: E501

        :return: The status of this TestRun.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TestRun.

        Deprecated. Use resultStatus instead.  # noqa: E501

        :param status: The status of this TestRun.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def description(self):
        """Gets the description of this TestRun.  # noqa: E501

        Human readable explanation of the current test status  # noqa: E501

        :return: The description of this TestRun.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TestRun.

        Human readable explanation of the current test status  # noqa: E501

        :param description: The description of this TestRun.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def stats(self):
        """Gets the stats of this TestRun.  # noqa: E501


        :return: The stats of this TestRun.  # noqa: E501
        :rtype: TestRunStatistics
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this TestRun.


        :param stats: The stats of this TestRun.  # noqa: E501
        :type: TestRunStatistics
        """

        self._stats = stats

    @property
    def test_type(self):
        """Gets the test_type of this TestRun.  # noqa: E501

        The name of the test framework used to run this test  # noqa: E501

        :return: The test_type of this TestRun.  # noqa: E501
        :rtype: str
        """
        return self._test_type

    @test_type.setter
    def test_type(self, test_type):
        """Sets the test_type of this TestRun.

        The name of the test framework used to run this test  # noqa: E501

        :param test_type: The test_type of this TestRun.  # noqa: E501
        :type: str
        """

        self._test_type = test_type

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
        if issubclass(TestRun, dict):
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
        if not isinstance(other, TestRun):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other