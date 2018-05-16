# -*- coding: utf-8 -*-
"""Define the Discord integration backend.

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
import logging

from django.conf import settings

import requests

logger = logging.getLogger(__name__)


class Client:
    """Define the Discord backend client.

    Keyword Arguments:
        token (str):
        api_version (str):
        auth_url (str):
        bot_name (str):
        home_url (str):
        version (str):

    """

    request = None
    backend_type = 'discord'
    headers = None

    def __init__(self, *args, **kwargs):
        """Initialize the backend client."""
        self.token = kwargs.get('token') or settings.DISCORD_BOT_TOKEN
        self.api_version = kwargs.get('api_version', '6')
        self.auth_url = f'https://discordapp.com/api/v{self.api_version}'
        self.bot_name = kwargs.get('bot_name', 'GitcoinBot')
        self.home_url = kwargs.get('home_url', 'https://gitcoin.co')
        self.version = kwargs.get('version', '0.1.0')
        self.headers = {
            'Authentication': self.get_auth_header(),
            'User-Agent': f'{self.bot_name} ({self.home_url}, {self.version})',
            'Content-Type': 'application/json',
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def get_auth_header(self, user_type='Bot'):
        if user_type not in ['Bot', 'Bearer']:
            logger.warning('Unknown authentication user type provided.')
            return ''
        elif not self.token:
            logger.warning('No {backend_type} authentication token found.')
            return ''

        return f'{user_type} {self.token}'

    def get_auth(self):
        """Authenticate with the backend provider."""
        self.request = requests.post(self.auth_url, headers=self.headers)

    def send_message(self):
        """Send a message."""
        self.session.get(f'{self.auth_url}/')

    def get_channel_messages(self, channel_id=''):
        response = self.session.get(f'{self.auth_url}/channels/{channel_id}/messages')
        print(f'RESPONSE: {response}')
