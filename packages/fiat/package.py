# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Fiat(PythonPackage):
    """The FInite element Automatic Tabulator FIAT"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://bitbucket.org/adaptivesimulations/fiat-hpc"
    git      = "https://bitbucket.org/adaptivesimulations/fiat-hpc.git"

    version('1.6.0', tag='1.6.0')
    version('1.5.0', tag='1.5.0')
    version('1.4.0', tag='1.4.0')
    
    depends_on('python@:2', type=('build', 'run'), when='@1.4.0')
    depends_on('python@3:', type=('build', 'run'), when='@1.5.0:')

