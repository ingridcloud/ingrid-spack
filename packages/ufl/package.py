# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ufl(PythonPackage):
    """UFL - Unified Form Language"""


    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://bitbucket.org/adaptivesimulations/ufl-hpc"
    git      = "https://bitbucket.org/adaptivesimulations/ufl-hpc.git"

    version('1.1.0', tag='1.1.0')
    version('1.0.1', tag='1.0.1')
    
    depends_on('python@:2', type=('build', 'run'), when='@1.0.1')
    depends_on('python@3:', type=('build', 'run'), when='@1.1.0')

