#!/usr/bin/env python
#
# Copyright (c) 2020 Seagate Technology LLC and/or its Affiliates
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# For any questions about this software or licensing,
# please email opensource@seagate.com or cortx-questions@seagate.com.
#
#
from .form_window import FormWindow
from provisioner import set_hostname
from ..data.data_store import PillarStore, ConfStore
from ..data.models import HostnameModel
from ..cli.executer import SetHostname

class HostnameWindow(FormWindow):

    data = {
               'Hostname': {
                               'default': 'test.seagate.com',
                               'validation': 'hostname'
                           }
           }
    component_type = 'hostname'

    def action(self):
       content = {'_'.join(key.split(" ")): val['default'] for key, val in self.data.items()}
       host = HostnameModel(**content)
       pillar = PillarStore()
       pillar.store_data(host)
       result = True
       err = None
       try:
           set_hostname()
           #SetHostname().run(config_file=conf.get_location())
       except Exception as exc:
           result = False
           err = str(exc)
       return result, err
