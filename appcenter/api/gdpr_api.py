# coding: utf-8

"""
    App Center Client

    Microsoft Visual Studio App Center API  # noqa: E501

    OpenAPI spec version: preview
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from appcenter.api_client import ApiClient


class GdprApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def data_subject_right_cancel_delete_request(self, token, **kwargs):  # noqa: E501
        """data_subject_right_cancel_delete_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_subject_right_cancel_delete_request(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: Unique request ID (GUID) (required)
        :param DataSubjectRightEmailRequest body:
        :return: DataSubjectRightResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_subject_right_cancel_delete_request_with_http_info(token, **kwargs)  # noqa: E501
        else:
            (data) = self.data_subject_right_cancel_delete_request_with_http_info(token, **kwargs)  # noqa: E501
            return data

    def data_subject_right_cancel_delete_request_with_http_info(self, token, **kwargs):  # noqa: E501
        """data_subject_right_cancel_delete_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_subject_right_cancel_delete_request_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: Unique request ID (GUID) (required)
        :param DataSubjectRightEmailRequest body:
        :return: DataSubjectRightResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_subject_right_cancel_delete_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `data_subject_right_cancel_delete_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token' in params:
            path_params['token'] = params['token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/user/dsr/delete/{token}/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataSubjectRightResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_subject_right_cancel_export_request(self, token, **kwargs):  # noqa: E501
        """data_subject_right_cancel_export_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_subject_right_cancel_export_request(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: Unique request ID (GUID) (required)
        :return: DataSubjectRightResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_subject_right_cancel_export_request_with_http_info(token, **kwargs)  # noqa: E501
        else:
            (data) = self.data_subject_right_cancel_export_request_with_http_info(token, **kwargs)  # noqa: E501
            return data

    def data_subject_right_cancel_export_request_with_http_info(self, token, **kwargs):  # noqa: E501
        """data_subject_right_cancel_export_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_subject_right_cancel_export_request_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: Unique request ID (GUID) (required)
        :return: DataSubjectRightResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_subject_right_cancel_export_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `data_subject_right_cancel_export_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token' in params:
            path_params['token'] = params['token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/user/dsr/export/{token}/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataSubjectRightResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_subject_right_delete_request(self, **kwargs):  # noqa: E501
        """data_subject_right_delete_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_subject_right_delete_request(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DataSubjectRightResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_subject_right_delete_request_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.data_subject_right_delete_request_with_http_info(**kwargs)  # noqa: E501
            return data

    def data_subject_right_delete_request_with_http_info(self, **kwargs):  # noqa: E501
        """data_subject_right_delete_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_subject_right_delete_request_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DataSubjectRightResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_subject_right_delete_request" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/user/dsr/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataSubjectRightResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_subject_right_delete_status_request(self, token, email, **kwargs):  # noqa: E501
        """data_subject_right_delete_status_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_subject_right_delete_status_request(token, email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: Unique request ID (GUID) (required)
        :param str email: Email used for delete with x-authz-bypass headers (required)
        :return: DataSubjectRightStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_subject_right_delete_status_request_with_http_info(token, email, **kwargs)  # noqa: E501
        else:
            (data) = self.data_subject_right_delete_status_request_with_http_info(token, email, **kwargs)  # noqa: E501
            return data

    def data_subject_right_delete_status_request_with_http_info(self, token, email, **kwargs):  # noqa: E501
        """data_subject_right_delete_status_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_subject_right_delete_status_request_with_http_info(token, email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: Unique request ID (GUID) (required)
        :param str email: Email used for delete with x-authz-bypass headers (required)
        :return: DataSubjectRightStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'email']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_subject_right_delete_status_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `data_subject_right_delete_status_request`")  # noqa: E501
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `data_subject_right_delete_status_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token' in params:
            path_params['token'] = params['token']  # noqa: E501

        query_params = []
        if 'email' in params:
            query_params.append(('email', params['email']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/user/dsr/delete/{token}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataSubjectRightStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_subject_right_export_request(self, **kwargs):  # noqa: E501
        """data_subject_right_export_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_subject_right_export_request(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DataSubjectRightResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_subject_right_export_request_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.data_subject_right_export_request_with_http_info(**kwargs)  # noqa: E501
            return data

    def data_subject_right_export_request_with_http_info(self, **kwargs):  # noqa: E501
        """data_subject_right_export_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_subject_right_export_request_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DataSubjectRightResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_subject_right_export_request" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/user/dsr/export', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataSubjectRightResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def data_subject_right_export_status_request(self, token, **kwargs):  # noqa: E501
        """data_subject_right_export_status_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_subject_right_export_status_request(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: Unique request ID (GUID) (required)
        :return: DataSubjectRightStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.data_subject_right_export_status_request_with_http_info(token, **kwargs)  # noqa: E501
        else:
            (data) = self.data_subject_right_export_status_request_with_http_info(token, **kwargs)  # noqa: E501
            return data

    def data_subject_right_export_status_request_with_http_info(self, token, **kwargs):  # noqa: E501
        """data_subject_right_export_status_request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.data_subject_right_export_status_request_with_http_info(token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str token: Unique request ID (GUID) (required)
        :return: DataSubjectRightStatusResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method data_subject_right_export_status_request" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params or
                params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `data_subject_right_export_status_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'token' in params:
            path_params['token'] = params['token']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIToken']  # noqa: E501

        return self.api_client.call_api(
            '/v0.1/user/dsr/export/{token}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DataSubjectRightStatusResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)