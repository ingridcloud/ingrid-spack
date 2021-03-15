# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ffc(PythonPackage):
    """FFC is a compiler for finite element variational forms. From a
       high-level description of the form, it generates efficient low-level
       C++ code that can be used to assemble the corresponding discrete
       operator (tensor). In particular, a bilinear form may be assembled
       into a matrix and a linear form may be assembled into a vector."""

    homepage = "https://bitbucket.org/adaptivesimulations/ffc-hpc"
    git      = "https://bitbucket.org/adaptivesimulations/ffc-hpc.git"

    version('1.2.0-hpc', tag='1.2.0-hpc')
    version('1.1.0-hpc', tag='1.1.0-hpc')
    version('1.0.2-hpc', tag='1.0.2-hpc')
    
    depends_on('python@:2',  type=('build', 'run'), when='@1.0.2-hpc')
    depends_on('ufl@1.0.1',  type=('build', 'run'), when='@1.0.2-hpc')
    depends_on('ufc@2.1.4',  type=('build', 'run'), when='@1.0.2-hpc')
    depends_on('fiat@1.4.0', type=('build', 'run'), when='@1.0.2-hpc')
    depends_on('fiat@1.5.0', type=('build', 'run'), when='@1.1.0-hpc')
    depends_on('python@3:',  type=('build', 'run'), when='@1.1.0-hpc')
    depends_on('py-sympy',   type=('run'), when='@1.1.0-hpc:')
    depends_on('py-numpy',   type=('run'), when='@1.1.0-hpc:')
    depends_on('ufl@1.1.0',  type=('run'), when='@1.1.0-hpc')
    depends_on('ufc@2.2.0',  type=('run'), when='@1.1.0-hpc')
    depends_on('ufl@1.2.0',  type=('run'), when='@1.2.0-hpc')
    depends_on('fiat@1.6.0', type=('run'), when='@1.2.0-hpc')
    depends_on('py-setuptools', type=('build'), when='@1.2.0-hpc')
    depends_on('pkgconf', type=('run'), when='@1.2.0-hpc')
