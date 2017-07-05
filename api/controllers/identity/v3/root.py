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

"""Root controller for /identity/v3"""

from sentinel.api.controllers.identity.v3 import auth
from sentinel.api.controllers.identity.v3 import users

class IdentityV3Controller(object):
    def __init__(self):
        self.auth = auth.IdentityV3AuthController()
        self.users = users.IdentityV3UsersController()

# vi: ts=4 et: