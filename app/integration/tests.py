# -*- coding: utf-8 -*-
"""Define the unit tests for Integration.

Copyright (C) 2018 Gitcoin Core

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
import unittest

from django.contrib.auth.models import Group, User
from django.contrib.contenttypes.models import ContentType
from django.test import Client
from django.urls import reverse

from dashboard.models import Profile

from .models import Integration


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults['username'] = 'username'
    defaults['email'] = 'username@gitcoin.co'
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults['name'] = 'group'
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_integration(**kwargs):
    defaults = {}
    defaults['name'] = 'name'
    defaults['config'] = 'config'
    defaults.update(**kwargs)
    if 'profile' not in defaults:
        defaults['profile'] = create_profile()
    return Integration.objects.create(**defaults)


def create_profile(**kwargs):
    defaults = {
        'data': {},
        'handle': 'handle',
        'last_sync_date': 'last_sync_date',
        'email': 'email@gitcoin.co',
        'github_access_token': 'github_access_token',
        'pref_lang_code': 'EN',
        'slack_repos': ['gitcoinco/web', ],
        'slack_token': 'slack_token',
        'slack_channel': 'slack_channel',
        'suppress_leaderboard': False,
        'repos_data': {}
    }
    defaults.update(**kwargs)
    if 'user' not in defaults:
        pass  # TODO: Create the user obj.
    return Profile.objects.create(**defaults)


class IntegrationViewTest(unittest.TestCase):
    """General tests for Integration logic."""

    def setUp(self):
        self.client = Client()

    def test_list_integration(self):
        url = reverse('integration_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_integration(self):
        url = reverse('integration_create')
        data = {
            'name': 'name',
            'config': 'config',
            'profile': create_profile().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_integration(self):
        integration = create_integration()
        url = reverse(
            'integration_detail', args=[
                integration.slug,
            ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_integration(self):
        integration = create_integration()
        data = {
            'name': 'name',
            'config': 'config',
            'profile': create_profile().pk,
        }
        url = reverse(
            'integration_update', args=[
                integration.slug,
            ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
