# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ufc(CMakePackage, PythonPackage):
    """UFC (Unified Form-assembly Code) is a unified framework for finite
       element assembly. More precisely, it defines a fixed interface for
       communicating low level routines (functions) for evaluating and
       assembling finite element variational forms."""

    homepage = "https://bitbucket.org/adaptivesimulations/ufc2-hpc"
    git      = "https://bitbucket.org/adaptivesimulations/ufc2-hpc.git"

    version('2.2.0', tag='v2.2.0')
    version('2.1.4', tag='v2.1.4')

    depends_on('python@3:', type='run', when='2.2.0')
    depends_on('python@:2', type='run', when='2.1.4')
