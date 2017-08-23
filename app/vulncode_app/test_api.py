#
# Copyright (c) 2017 nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/nexB/vulnerablecode/
# The VulnerableCode software is licensed under the Apache License version 2.0.
# Data generated with VulnerableCode require an acknowledgment.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with VulnerableCode or any VulnerableCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with VulnerableCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  VulnerableCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  VulnerableCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/nexB/vulnerablecode/ for support and download.

import json

from django.test import TestCase
from rest_framework.response import Response

from vulncode_app.data_dump import debian_dump
from vulncode_app.data_dump import ubuntu_dump

from scraper import debian
from scraper import ubuntu


class TestSerializers(TestCase):
    def test_debian_response(self):
        with open('tests/test_data/debian.json') as f:
            test_data = json.loads(f.read())

        extract_data = debian.extract_vulnerabilities(test_data)
        debian_dump(extract_data)
        response = self.client.get('/vulncode_app/data/mimetex', format='json')

        expected = {
                "name": "mimetex",
                "vulnerabilities": [
                    {
                       "summary": "Multiple stack-based buffer overflows in mimetex.cgi in mimeTeX",
                       "reference_id": "CVE-2009-2458",
                       "version": "1.50-1.1"
                    },
                    {
                       "summary": "Multiple unspecified vulnerabilities in mimeTeX.",
                       "reference_id": "CVE-2009-2459",
                       "version": "1.50-1.1"
                    }
                ]
            }

        self.assertEqual(expected, response.data)

    def test_ubuntu_response(self):
        with open('tests/test_data/ubuntu_main.html') as f:
            test_data = f.read()

        extract_data = ubuntu.extract_cves(test_data)
        ubuntu_dump(extract_data)
        response = self.client.get('/vulncode_app/data/automake', format='json')

        expected = {
               "name": "automake",
               "vulnerabilities": [
                    {
                       "summary": "",
                       "reference_id": "CVE-2012-3386",
                       "version": ""
                    }
                ]
            }

        self.assertEqual(expected, response.data)