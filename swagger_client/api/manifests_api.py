# coding: utf-8

"""
    Machship API V2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: V2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ManifestsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def apiv2_manifests_get_all_get(self, **kwargs):  # noqa: E501
        """Get a list of (up to 200) manifests for a company.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apiv2_manifests_get_all_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int company_id: Optional - defaults to your company. Must be a valid company ID in MachShip
        :param int start_index: Defaults to 1. Can be used to \"page\" through subsequent requests
        :param int retrieve_size: The number of manifests to return. Defaults to 40, will return a maximum of 200 rows
        :param int carrier_id: Optional to limit the results to manifests for that carrier
        :param bool include_child_companies: Whether to include companies that are \"children\" below companyId
        :param datetime start_date: Start Date which is compared against the manifest's creation date (all date times are local to the pickup location)
        :param datetime end_date: End Date which is compared against the manifest's creation date (all date times are local to the pickup location)
        :return: ManifestForListWithConsignmentsGridDomainEntityV2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apiv2_manifests_get_all_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.apiv2_manifests_get_all_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def apiv2_manifests_get_all_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of (up to 200) manifests for a company.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apiv2_manifests_get_all_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int company_id: Optional - defaults to your company. Must be a valid company ID in MachShip
        :param int start_index: Defaults to 1. Can be used to \"page\" through subsequent requests
        :param int retrieve_size: The number of manifests to return. Defaults to 40, will return a maximum of 200 rows
        :param int carrier_id: Optional to limit the results to manifests for that carrier
        :param bool include_child_companies: Whether to include companies that are \"children\" below companyId
        :param datetime start_date: Start Date which is compared against the manifest's creation date (all date times are local to the pickup location)
        :param datetime end_date: End Date which is compared against the manifest's creation date (all date times are local to the pickup location)
        :return: ManifestForListWithConsignmentsGridDomainEntityV2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['company_id', 'start_index', 'retrieve_size', 'carrier_id', 'include_child_companies', 'start_date', 'end_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apiv2_manifests_get_all_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'company_id' in params:
            query_params.append(('companyId', params['company_id']))  # noqa: E501
        if 'start_index' in params:
            query_params.append(('startIndex', params['start_index']))  # noqa: E501
        if 'retrieve_size' in params:
            query_params.append(('retrieveSize', params['retrieve_size']))  # noqa: E501
        if 'carrier_id' in params:
            query_params.append(('carrierId', params['carrier_id']))  # noqa: E501
        if 'include_child_companies' in params:
            query_params.append(('includeChildCompanies', params['include_child_companies']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['User API Token']  # noqa: E501

        return self.api_client.call_api(
            '/apiv2/manifests/getAll', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ManifestForListWithConsignmentsGridDomainEntityV2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apiv2_manifests_group_all_unmanifested_consignments_for_manifest_post(self, **kwargs):  # noqa: E501
        """Groups all unmanifested consignments for a company into manifests.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apiv2_manifests_group_all_unmanifested_consignments_for_manifest_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int body: Machship's company Id
        :return: BookedManifestV2ICollectionBaseDomainEntityV2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apiv2_manifests_group_all_unmanifested_consignments_for_manifest_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.apiv2_manifests_group_all_unmanifested_consignments_for_manifest_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def apiv2_manifests_group_all_unmanifested_consignments_for_manifest_post_with_http_info(self, **kwargs):  # noqa: E501
        """Groups all unmanifested consignments for a company into manifests.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apiv2_manifests_group_all_unmanifested_consignments_for_manifest_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int body: Machship's company Id
        :return: BookedManifestV2ICollectionBaseDomainEntityV2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apiv2_manifests_group_all_unmanifested_consignments_for_manifest_post" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['User API Token']  # noqa: E501

        return self.api_client.call_api(
            '/apiv2/manifests/groupAllUnmanifestedConsignmentsForManifest', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BookedManifestV2ICollectionBaseDomainEntityV2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apiv2_manifests_group_consignments_for_manifest_post(self, **kwargs):  # noqa: E501
        """Groups a set of consignments into manifests.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apiv2_manifests_group_consignments_for_manifest_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] body:
        :return: BookedManifestV2ICollectionBaseDomainEntityV2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apiv2_manifests_group_consignments_for_manifest_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.apiv2_manifests_group_consignments_for_manifest_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def apiv2_manifests_group_consignments_for_manifest_post_with_http_info(self, **kwargs):  # noqa: E501
        """Groups a set of consignments into manifests.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apiv2_manifests_group_consignments_for_manifest_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] body:
        :return: BookedManifestV2ICollectionBaseDomainEntityV2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apiv2_manifests_group_consignments_for_manifest_post" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['User API Token']  # noqa: E501

        return self.api_client.call_api(
            '/apiv2/manifests/groupConsignmentsForManifest', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BookedManifestV2ICollectionBaseDomainEntityV2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def apiv2_manifests_manifest_post(self, **kwargs):  # noqa: E501
        """apiv2_manifests_manifest_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apiv2_manifests_manifest_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[BookedManifestV2] body:
        :return: ReturnBookedManifestV2ICollectionBaseDomainEntityV2
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.apiv2_manifests_manifest_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.apiv2_manifests_manifest_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def apiv2_manifests_manifest_post_with_http_info(self, **kwargs):  # noqa: E501
        """apiv2_manifests_manifest_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.apiv2_manifests_manifest_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[BookedManifestV2] body:
        :return: ReturnBookedManifestV2ICollectionBaseDomainEntityV2
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apiv2_manifests_manifest_post" % key
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
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['User API Token']  # noqa: E501

        return self.api_client.call_api(
            '/apiv2/manifests/manifest', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReturnBookedManifestV2ICollectionBaseDomainEntityV2',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
