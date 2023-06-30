#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file

Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class StorageLevel(google.protobuf.message.Message):
    """StorageLevel for persisting Datasets/Tables."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USE_DISK_FIELD_NUMBER: builtins.int
    USE_MEMORY_FIELD_NUMBER: builtins.int
    USE_OFF_HEAP_FIELD_NUMBER: builtins.int
    DESERIALIZED_FIELD_NUMBER: builtins.int
    REPLICATION_FIELD_NUMBER: builtins.int
    use_disk: builtins.bool
    """(Required) Whether the cache should use disk or not."""
    use_memory: builtins.bool
    """(Required) Whether the cache should use memory or not."""
    use_off_heap: builtins.bool
    """(Required) Whether the cache should use off-heap or not."""
    deserialized: builtins.bool
    """(Required) Whether the cached data is deserialized or not."""
    replication: builtins.int
    """(Required) The number of replicas."""
    def __init__(
        self,
        *,
        use_disk: builtins.bool = ...,
        use_memory: builtins.bool = ...,
        use_off_heap: builtins.bool = ...,
        deserialized: builtins.bool = ...,
        replication: builtins.int = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "deserialized",
            b"deserialized",
            "replication",
            b"replication",
            "use_disk",
            b"use_disk",
            "use_memory",
            b"use_memory",
            "use_off_heap",
            b"use_off_heap",
        ],
    ) -> None: ...

global___StorageLevel = StorageLevel
