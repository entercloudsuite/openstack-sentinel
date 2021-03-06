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

from keystoneauth1.exceptions import http

from sentinel.tests.functional import base, matchers
from sentinel.tests.functional import client_fixtures as fixtures

TEST_USER = 'test'
TEST_USER_EMAIL = 'test@example.com'
TEST_USER_DESCRIPTION = 'Sentinel Test User'


class KeystoneUsersTestCase(base.BaseTestCase):

    def test_create(self):
        user = self.sentinel.identity.users.create(
            TEST_USER,
            email=TEST_USER_EMAIL,
            description=TEST_USER_DESCRIPTION)
        self.addCleanup(self.sentinel.identity.users.delete, user)
        self.assertEqual(user.name, TEST_USER)
        self.assertEqual(user.email, TEST_USER_EMAIL)
        self.assertEqual(user.description, TEST_USER_DESCRIPTION)
        self.assertEqual(user.enabled, True)

    def test_create_conflict(self):
        user = self.useFixture(fixtures.User(self.sentinel))
        self.assertRaises(http.Conflict, self.sentinel.identity.users.create, user.entity.name)

    def test_update(self):
        user_fix = self.useFixture(fixtures.User(self.sentinel))
        user = self.sentinel.identity.users.update(
            user_fix.entity,
            name=TEST_USER,
            email=TEST_USER_EMAIL,
            description=TEST_USER_DESCRIPTION,
            enabled=False)
        self.assertEqual(user.name, TEST_USER)
        self.assertEqual(user.email, TEST_USER_EMAIL)
        self.assertEqual(user.description, TEST_USER_DESCRIPTION)
        self.assertEqual(user.enabled, False)

    def test_update_taint(self):
        user = self.useFixture(fixtures.User(self.openstack))
        self.assertRaises(
            http.Forbidden,
            self.sentinel.identity.users.update,
            user.entity,
            name=TEST_USER)

    def test_get(self):
        user = self.useFixture(fixtures.User(self.sentinel))
        self.sentinel.identity.users.get(user.entity)

    def test_get_taint(self):
        user = self.useFixture(fixtures.User(self.openstack))
        self.assertRaises(http.Forbidden, self.sentinel.identity.users.get, user.entity)

    def test_delete(self):
        user = self.sentinel.identity.users.create(TEST_USER)
        self.sentinel.identity.users.delete(user)
        self.assertRaises(http.NotFound, self.sentinel.identity.users.delete, user)

    def test_delete_taint(self):
        user = self.useFixture(fixtures.User(self.openstack))
        self.assertRaises(http.Forbidden, self.sentinel.identity.users.delete, user.entity)

    def test_list(self):
        user = self.useFixture(fixtures.User(self.sentinel))
        users = self.sentinel.identity.users.list()
        self.assertThat(user.entity, matchers.IsInCollection(users))

    def test_list_filtering(self):
        user = self.useFixture(fixtures.User(self.openstack))
        users = self.sentinel.identity.users.list()
        self.assertThat(user.entity, matchers.IsNotInCollection(users))

    def test_group_list(self):
        group_user = self.useFixture(fixtures.GroupUser(self.sentinel))
        groups = self.sentinel.identity.groups.list(user=group_user.user.entity)
        self.assertThat(group_user.group.entity, matchers.IsInCollection(groups))

    def test_project_list(self):
        grant = self.useFixture(fixtures.UserProjectGrant(self.sentinel))
        projects = self.sentinel.identity.projects.list(user=grant.user.entity)
        self.assertThat(grant.project.entity, matchers.IsInCollection(projects))

# vi: ts=4 et:
