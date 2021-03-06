# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from .helper import secure_params, ShopinvaderService
from ..backend import shopinvader
from .address import AddressService


@shopinvader
class CustomerService(ShopinvaderService):
    _model_name = 'res.partner'

    # The following method are 'public' and can be called from the controller.
    # All params are untrusted so please check it by using the decorator
    # secure params and the linked validator !

    @secure_params
    def get(self, params):
        if self.partner:
            address = self.service_for(AddressService)
            customer = address._to_json(self.partner)[0]
            return {
                'data': customer,
                'store_cache': {'customer': customer},
                }
        else:
            return {'data': {}}

    # The following method are 'private' and should be never never NEVER call
    # from the controller.
    # All params are trusted as they have been checked before

    def _validator_get(self):
        return {}
