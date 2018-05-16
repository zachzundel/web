# -*- coding: utf-8 -*-
"""Define the models for Account.

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
from django.contrib.auth.models import Group
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.fields import AutoSlugField
from marketing.models import SuperModel
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase, TaggedItemBase


class Keyword(TagBase):
    """Define the Profile Keyword tag item."""

    class Meta:
        verbose_name = _('Keyword')
        verbose_name_plural = _('Keywords')


class TaggedKeyword(GenericTaggedItemBase):
    """Define the generic keyword base for use across Profile and Organization."""

    tag = models.ForeignKey(
        Keyword,
        related_name='%(app_label)s_%(class)s_keywords',
        on_delete=models.CASCADE)


class Organization(Group):
    """Define the Organization schema."""

    slug = AutoSlugField(populate_from='name', blank=True)
    description = models.TextField(blank=True)
    website_url = models.URLField(blank=True)
    vc_url = models.URLField(blank=True)
    avatar = models.ImageField(null=True, upload_to='orgs/avatar/')
    display_publicly = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    vc_data = JSONField(default=dict)
    # The config field will hold repositories, auth data, etc.
    followers = models.ForeignKey('dashboard.Profile', related_name='follows', on_delete=models.CASCADE)
    keywords = TaggableManager(blank=True, through=TaggedKeyword)

    class Meta:
        """Define the metadata for the Organization model."""

        ordering = ('-created_on', )

    def __str__(self):
        """Define the string representation of Organization."""
        return self.slug

    def get_absolute_url(self):
        """Get the absolute URL for the Organization."""
        return reverse('account:organization_detail', args=(self.slug, ))

    def get_update_url(self):
        """Get the update URL for the Organization."""
        return reverse('account:organization_update', args=(self.slug, ))
