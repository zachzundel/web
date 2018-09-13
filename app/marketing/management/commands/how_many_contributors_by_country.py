'''
    Copyright (C) 2017 Gitcoin Core

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

'''
from django.core.management.base import BaseCommand

from dashboard.models import Bounty, Tip, Profile


def user_name_to_location(funder):
    profiles = Profile.objects.filter(handle__iexact=funder)
    if profiles.exists():
        profile = profiles.first()
        location = profile.data.get('location', None)
        if location:
            return location
    return None

class Command(BaseCommand):

    help = 'sends a test email'

    def handle(self, *args, **options):

        funders = []
        recipients = []
        for bounty in Bounty.objects.filter(current_bounty=True,network='mainnet'):
            if bounty.bounty_owner_github_username:
                funders.append(bounty.bounty_owner_github_username)
            for fulfill in bounty.fulfillments.filter(accepted=True):
                if fulfill.fulfiller_github_username:
                    recipients.append(fulfill.fulfiller_github_username)

        for tip in Tip.objects.filter(network='mainnet'):
            if tip.username:
                funders.append(tip.username)
            if tip.from_username:
                funders.append(tip.from_username)

        funder_locations = {}
        for funder in set(funders):
            location = user_name_to_location(funder)
            if location not in funder_locations.keys():
                funder_locations[location] = 0
            funder_locations[location] += 1

        recipient_locations = {}
        for recipient in set(recipients):
            location = user_name_to_location(recipient)
            if location not in recipient_locations.keys():
                recipient_locations[location] = 0
            recipient_locations[location] += 1

        print(funder_locations)
        print(recipient_locations)

