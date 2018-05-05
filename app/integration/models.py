# -*- coding: utf-8 -*-
"""Define the models for Integration.

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
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.urls import reverse

from django_extensions.db.fields import AutoSlugField
from marketing.models import SuperModel


class Integration(SuperModel):
    """Define the Integration schema."""

    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', blank=True)
    # created = models.DateTimeField(auto_now_add=True, editable=False)
    # last_updated = models.DateTimeField(auto_now=True, editable=False)
    config = JSONField(default=dict)
    # The config field will hold repositories, auth data, etc.
    profile = models.ForeignKey('dashboard.Profile', related_name='integrations', on_delete=models.CASCADE)

    class Meta:
        """Define the metadata for the Integration model."""

        ordering = ('-created_on', )

    def __str__(self):
        """Define the string representation of Integration."""
        return self.slug

    def get_absolute_url(self):
        """Get the absolute URL for the Integration."""
        return reverse('integration_detail', args=(self.slug, ))

    def get_update_url(self):
        """Get the update URL for the Integration."""
        return reverse('integration_update', args=(self.slug, ))
