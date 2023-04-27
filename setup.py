# Copyright 2022 DeepMind Technologies Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Setup for pip package."""

from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = [
    'absl-py',
    'attrs',
    'chex',
    'jax',
    'jaxlib',
    'jaxline',
    'ml-collections',
    'optax',
    'numpy',
    'pandas',
    'scipy',
    'tensorflow',
    'typing_extensions',
]


setup(
    name='eigengame',
    version='1.0',
    description=('Top-k Eigendecompositions for Large, Streaming Data.'),
    url='https://github.com/deepmind/eigengame',
    author='DeepMind',
    author_email='no-reply@google.com',
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    platforms=['any'],
    license='Apache 2.0',
)
