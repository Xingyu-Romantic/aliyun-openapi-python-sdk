# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest

class GetPropertiesRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'LRG', '2019-10-10', 'GetProperties')
		self.set_uri_pattern('/api/v2/[productName]/node/[nodeName]/properties')
		self.set_method('GET')

	def get_nodeName(self):
		return self.get_path_params().get('nodeName')

	def set_nodeName(self,nodeName):
		self.add_path_param('nodeName',nodeName)

	def get_productName(self):
		return self.get_path_params().get('productName')

	def set_productName(self,productName):
		self.add_path_param('productName',productName)