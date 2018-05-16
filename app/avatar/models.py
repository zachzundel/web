from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.fields import AutoSlugField
from economy.models import SuperModel
from taggit.models import TaggedItemBase


class AssetColors(TaggedItemBase):
    """Define interest word relations stored in the relational database."""

    content_object = models.ForeignKey('avatar.AvatatItem')


class Avatar(SuperModel):
    """Stores the options necessary to render a Gitcoin avatar"""

    config = JSONField(default=dict)
    clothing_config = JSONField(default=dict)
    head_config = JSONField(default=dict)
    hat_config = JSONField(default=dict)
    hair_config = JSONField(default=dict)
    earring_config = JSONField(default=dict)
    ears_config = JSONField(default=dict)
    beard_config = JSONField(default=dict)
    mustache_config = JSONField(default=dict)
    mouth_config = JSONField(default=dict)
    nose_config = JSONField(default=dict)
    eyes_config = JSONField(default=dict)
    glasses_config = JSONField(default=dict)
    background_config = JSONField(default=dict)

    svg = models.FileField(null=True, blank=True)
    # head = models.CharField(max_length=2)
    head = models.URLField()
    hat_long = models.URLField()
    hat_short = models.URLField()
    hair_long = models.URLField()
    hair_short = models.URLField()
    earring = models.URLField()
    earring_back = models.URLField()
    clothing = models.URLField()
    ears = models.URLField()
    beard = models.URLField()
    mustache = models.URLField()
    mouth = models.URLField()
    nose = models.URLField()
    eyes = models.URLField()
    glasses = models.URLField()
    background = models.CharField(max_length=6)


class AvatarItemType(SuperModel):
    """Define the Avatar types."""

    # AvatarItem Categories
    CAT_ACCESSORIES = 'AC'
    CAT_CLOTHING = 'CL'
    CAT_EARS = 'EA'
    CAT_EYES = 'EY'
    CAT_FACIAL_HAIR = 'FH'
    CAT_HAIR_STYLE = 'HS'
    CAT_HEAD = 'HE'
    CAT_MOUTH = 'MO'
    CAT_NOSE = 'NO'

    CATEGORY_CHOICES = [
        (CAT_ACCESSORIES, 'Accessories'),
        (CAT_CLOTHING, 'Clothing'),
        (CAT_EARS, 'Ears'),
        (CAT_EYES, 'Eyes'),
        (CAT_FACIAL_HAIR, 'Facial Hair'),
        (CAT_HAIR_STYLE, 'Hair Style'),
        (CAT_HEAD, 'Head'),
        (CAT_MOUTH, 'Mouth'),
        (CAT_NOSE, 'Nose'),
    ]

    # AvatarItem Types
    # Clothing
    TYPE_CLOTHING_CARDIGAN = 'CC'
    TYPE_CLOTHING_HOODIE = 'CH'
    TYPE_CLOTHING_KNIT_SWEATER = 'CK'
    TYPE_CLOTHING_PLAID = 'CP'
    TYPE_CLOTHING_SHIRT = 'CS'
    # Accessories
    TYPE_ACCESSORIES_EARRING = 'AE'
    TYPE_ACCESSORIES_GLASSES = 'AG'
    TYPE_ACCESSORIES_HATSHORT = 'AH'

    COMPONENT_TYPES = [
        (TYPE_CLOTHING_CARDIGAN, 'Cardigan'),
        (TYPE_CLOTHING_HOODIE, 'Hoodie'),
        (TYPE_CLOTHING_KNIT_SWEATER, 'Knit Sweater'),
        (TYPE_CLOTHING_PLAID, 'Plaid'),
        (TYPE_CLOTHING_SHIRT, 'Shirt'),
    ]


class AvatarItem(SuperModel):
    """Define the Avatar components."""

    # AvatarItem Categories
    CAT_ACCESSORIES = 'AC'
    CAT_CLOTHING = 'CL'
    CAT_EARS = 'EA'
    CAT_EYES = 'EY'
    CAT_FACIAL_HAIR = 'FH'
    CAT_HAIR_STYLE = 'HS'
    CAT_HEAD = 'HE'
    CAT_MOUTH = 'MO'
    CAT_NOSE = 'NO'

    CATEGORY_CHOICES = (
        (CAT_ACCESSORIES, 'Accessories'),
        (CAT_CLOTHING, 'Clothing'),
        (CAT_EARS, 'Ears'),
        (CAT_EYES, 'Eyes'),
        (CAT_FACIAL_HAIR, 'Facial Hair'),
        (CAT_HAIR_STYLE, 'Hair Style'),
        (CAT_HEAD, 'Head'),
        (CAT_MOUTH, 'Mouth'),
        (CAT_NOSE, 'Nose'),
    )

    # AvatarItem Types
    # Clothing
    TYPE_CLOTHING_CARDIGAN = 'CC'
    TYPE_CLOTHING_HOODIE = 'CH'
    TYPE_CLOTHING_KNIT_SWEATER = 'CK'
    TYPE_CLOTHING_PLAID = 'CP'
    TYPE_CLOTHING_SHIRT = 'CS'
    # Accessories
    TYPE_ACCESSORIES_EARRING = 'AE'
    TYPE_ACCESSORIES_GLASSES = 'AG'
    TYPE_ACCESSORIES_HATSHORT = 'AH'

    COMPONENT_TYPES = (
        (TYPE_CLOTHING_CARDIGAN, 'Cardigan'),
        (TYPE_CLOTHING_HOODIE, 'Hoodie'),
        (TYPE_CLOTHING_KNIT_SWEATER, 'Knit Sweater'),
        (TYPE_CLOTHING_PLAID, 'Plaid'),
        (TYPE_CLOTHING_SHIRT, 'Shirt'),
    )

    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, help_text=_('The category of the avatar item'))
    color_palette = ArrayField(
        models.CharField(max_length=7),
        blank=True,
        default=list,
        help_text=_('A comma delimited list of available color hex codes'))
    description = models.CharField(max_length=255, blank=True, help_text=_('The description of the avatar item'))
    name = models.CharField(max_length=50, help_text=_('The name of the avatar item'))
    slug = AutoSlugField(populate_from='name', blank=True, help_text=_('The slug of the avatar item name'))
    svg = models.FileField(null=True, help_text=_('The SVG of the avatar item'))
    component_type = models.CharField(
        choices=COMPONENT_TYPES,
        max_length=2,
        help_text=_('The component type of the avatar item'))

    class Meta:
        """Define the metadata for AvatarItem."""

        ordering = ('-created', )


def get_component_svg():
    pass
