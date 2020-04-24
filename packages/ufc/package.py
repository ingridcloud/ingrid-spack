# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ufc(CMakePackage):
    """UFC (Unified Form-assembly Code) is a unified framework for finite
       element assembly. More precisely, it defines a fixed interface for
       communicating low level routines (functions) for evaluating and
       assembling finite element variational forms."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://bitbucket.org/adaptivesimulations/ufc2-hpc"
    git      = "https://bitbucket.org/adaptivesimulations/ufc2-hpc.git"

    version('2.2.0', tag='v2.2.0')
    version('2.1.4', tag='v2.1.4')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
