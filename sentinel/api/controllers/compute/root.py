# Copyright 2017 DataCentred Ltd
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Root controller for /compute"""

from sentinel.api.controllers.compute.v2 import root as v2

class ComputeController(object):
    def __init__(self):
        self.v2 = v2.ComputeV2Controller()


class Service(object):
    service_name = u'nova'
    service_type = u'compute'
    service_endpoint = u'/compute/v2'

    @staticmethod
    def controller():
        return ComputeController()

# vi: ts=4 et:
