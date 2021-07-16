# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shuup Commerce Inc. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from django.contrib.auth import get_user_model
from shuup.core.model import CompanyContact, PersonContact, Shop
from shuup.gdpr.anonymizer import Anonymizer


def anonymize(shop_id: int, contact_id: int = None, user_id: int = None):

    shop = Shop.objects.filter(
        pk=shop_id,
    ).first()

    contact = None
    if contact_id:
        contact = PersonContact.objects.get(pk=contact_id)
        if not contact:
            contact = CompanyContact.objects.get(pk=contact_id)

    user = None
    if user_id:
        user = get_user_model().objects.get(pk=user_id)

    anonymizer = Anonymizer()
    if contact or user:
        anonymizer.anonymize(shop, contact, user)
