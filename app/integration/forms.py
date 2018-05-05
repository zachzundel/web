# -*- coding: utf-8 -*-
"""Define the forms logic for Integration.

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
from django import forms

from .models import Integration


class IntegrationForm(forms.ModelForm):
    """Define the Integration form."""

    class Meta:
        """Define the metadata for the Integration form."""

        model = Integration
        fields = ['name', 'config', 'profile']
