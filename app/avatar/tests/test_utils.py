# -*- coding: utf-8 -*-
"""Handle avatar utility related tests.

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
from avatar.utils import build_svg
from test_plus.test import TestCase


class AvatarUtilitiesTest(TestCase):
    """Define tests for Avatar utils."""

    def test_build_svg(self):
        """Test the avatar utility build_svg method."""
        # Mimic app/assets/v2/images/avatar/Eyes/0.svg
        # +<svg id="Layer_1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 899.2 1415.7"><style>.st1{fill:#333}</style><switch><g><path fill="none" d="M147.7 570.5h603.7V812H147.7z"/><path class="st1" d="M645.2 592.2c-10-6.1-21.7-9.9-33.5-12.3-11.9-2.3-24.1-3.2-36.3-3-12.1.3-24.2 1.8-35.9 4.7-5.8 1.4-11.5 3.2-16.9 5.5-5.4 2.2-10.5 4.9-15.1 8l-9.1-13.8c6-3.7 12.3-6.6 18.6-8.8 6.4-2.3 12.8-4 19.3-5.3 13-2.6 26.1-3.5 39.1-3.3 13 .3 26 1.9 38.7 5 6.3 1.6 12.6 3.5 18.7 6s12 5.5 17.6 9.3l-5.2 8zM575.4 611.8c-12.7 0-24.7 4-35.2 11.2-10.2 6.9-16.1 18.5-16.1 30.8 13.5-15.9 31.5-25.8 51.3-25.8 19.8 0 37.8 9.8 51.3 25.8 0-12.3-5.9-23.9-16.1-30.8-10.5-7.1-22.5-11.2-35.2-11.2z"/><g><path class="st1" d="M258.6 584.3c5.6-3.8 11.5-6.8 17.6-9.3 6.1-2.5 12.4-4.5 18.7-6 12.7-3.1 25.7-4.7 38.7-5 13-.3 26.1.7 39.1 3.3 6.5 1.3 12.9 3 19.3 5.3 6.3 2.3 12.6 5.1 18.6 8.8l-9.1 13.8c-4.5-3.1-9.7-5.8-15.1-8s-11.1-4-16.9-5.5c-11.6-2.9-23.7-4.3-35.9-4.7-12.2-.3-24.4.6-36.3 3-11.8 2.4-23.5 6.1-33.5 12.3l-5.2-8zM333.7 611.8c12.7 0 24.7 4 35.2 11.2 10.2 6.9 16.1 18.5 16.1 30.8-13.5-15.9-31.5-25.8-51.3-25.8-19.8 0-37.8 9.8-51.3 25.8 0-12.3 5.9-23.9 16.1-30.8 10.5-7.1 22.4-11.2 35.2-11.2z"/></g></g></switch></svg>
        # +<svg id="Layer_1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 899.2 1415.7"><style>.st1{fill:#333}</style><switch><g><path fill="none" d="M147.7 570.5h603.7V812H147.7z"/><path class="st1" d="M393.7 602.5c-8-7.8-18.5-13.8-29.7-17.9-11.3-4.1-23.4-6.3-35.7-6.8-12.3-.4-24.6.8-36.5 4.1-11.8 3.3-23.1 8.5-32.4 16.2l-6.6-7.4c10.2-9.5 22.5-16.2 35.4-20.6 13-4.4 26.6-6.6 40.2-7 13.7-.3 27.5 1.3 40.9 5.3 13.3 4 26.4 10.2 37.6 19.8l-13.2 14.3zM632.2 601.1c-9.1-7.8-20.2-13.2-31.9-16.7-11.7-3.4-24.1-4.9-36.3-4.7-12.2.3-24.4 2.3-35.7 6.2-11.3 3.9-21.9 9.7-30 17.4l-13-14.4c11.3-9.6 24.4-15.7 37.8-19.5 13.4-3.8 27.3-5.3 41-4.9 13.7.5 27.3 2.8 40.3 7.4 12.9 4.6 25.3 11.3 35.4 21.1l-7.6 8.1z"/><ellipse transform="matrix(.00679 -1 1 .00679 -95.001 1213.604)" class="st1" cx="563.4" cy="654.6" rx="36.6" ry="29.7"/><g><ellipse transform="matrix(.00679 -1 1 .00679 -327.492 976.331)" class="st1" cx="327.7" cy="653" rx="36.6" ry="29.7"/></g></g></switch></svg>
        # +<svg id="Layer_1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 899.2 1415.7"><style>.st1{fill:#333}.st2{fill:none;stroke:#333;stroke-width:6.4919;stroke-miterlimit:10}</style><switch><g><path fill="none" d="M147.7 570.5h603.7V812H147.7z"/><ellipse class="st1" cx="557.9" cy="652.4" rx="29.8" ry="38.3"/><ellipse class="st1" cx="346.3" cy="652.4" rx="29.8" ry="38.3"/><path class="st2" d="M557.9 617.2h41.7M299.6 617.2h48.7"/><g><path class="st1" d="M399.1 595.2c-.1-.1-.5-.3-1-.6s-1.1-.6-1.8-.8c-1.3-.6-2.6-1.1-4-1.7-2.8-1.1-5.6-2.1-8.5-3.1-5.8-2-11.7-3.8-17.6-5.4-5.9-1.7-11.9-3.1-17.8-4.4-5.9-1.2-11.9-2.3-17.5-2.4-12.1-.3-24.3.6-36.2 2.9-11.8 2.3-23.5 6.1-33.6 12.2l-4.7-7.1c5.5-3.8 11.4-6.8 17.4-9.3 6-2.5 12.3-4.5 18.6-6.1 12.6-3.1 25.5-4.7 38.5-5.1 3.5-.1 6.9.1 10.2.4 3.3.3 6.5.7 9.7 1.2 6.4 1 12.7 2.2 18.9 3.6 6.3 1.4 12.5 2.9 18.7 4.7 3.1.9 6.2 1.8 9.3 2.8 1.6.5 3.2 1.1 4.8 1.7.8.3 1.7.7 2.6 1.1.9.4 1.9.9 3.1 1.6l-9.1 13.8zM637.7 594.6c-10-6.1-21.7-9.9-33.5-12.3-11.9-2.3-24.1-3.2-36.3-3-12.1.3-24.2 1.8-35.9 4.7-5.8 1.4-11.5 3.2-16.9 5.5-5.4 2.2-10.5 4.9-15.1 8l-9.1-13.8c6-3.7 12.3-6.6 18.6-8.8 6.4-2.3 12.8-4 19.3-5.3 13-2.6 26.1-3.5 39.1-3.3 13 .3 26 1.9 38.7 5 6.3 1.6 12.6 3.5 18.7 6s12 5.5 17.6 9.3l-5.2 8z"/></g></g></switch></svg>
        svg = build_svg(item_type='eyes')
        assert svg.startsWith('<svg id=')
