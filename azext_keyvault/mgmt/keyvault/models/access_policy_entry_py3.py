# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccessPolicyEntry(Model):
    """An identity that have access to the key vault. All identities in the array
    must use the same tenant ID as the key vault's tenant ID.

    All required parameters must be populated in order to send to Azure.

    :param tenant_id: Required. The Azure Active Directory tenant ID that
     should be used for authenticating requests to the key vault.
    :type tenant_id: str
    :param object_id: Required. The object ID of a user, service principal or
     security group in the Azure Active Directory tenant for the vault. The
     object ID must be unique for the list of access policies.
    :type object_id: str
    :param application_id:  Application ID of the client making request on
     behalf of a principal
    :type application_id: str
    :param permissions: Required. Permissions the identity has for keys,
     secrets and certificates.
    :type permissions: ~azure.mgmt.keyvault.models.Permissions
    """

    _validation = {
        'tenant_id': {'required': True},
        'object_id': {'required': True},
        'permissions': {'required': True},
    }

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'object_id': {'key': 'objectId', 'type': 'str'},
        'application_id': {'key': 'applicationId', 'type': 'str'},
        'permissions': {'key': 'permissions', 'type': 'Permissions'},
    }

    def __init__(self, *, tenant_id: str, object_id: str, permissions, application_id: str=None, **kwargs) -> None:
        super(AccessPolicyEntry, self).__init__(**kwargs)
        self.tenant_id = tenant_id
        self.object_id = object_id
        self.application_id = application_id
        self.permissions = permissions
