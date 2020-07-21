# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Dolfin(AutotoolsPackage):
    """DOLFIN HPC is a special branch of DOLFIN optimized for
       distributed memory architectures. """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://bitbucket.org/adaptivesimulations/dolfin-hpc"

    version('0.9.0p1-hpc', url='https://bitbucket.org/adaptivesimulations/dolfin-hpc/downloads/dolfin-0.9.0p1-hpc.tar.gz', sha256='9d1aaff6dafc3a408677ec00016bac7a480518f29f520cd0995def1776df1d76')
    version('0.9.1-hpc', url='https://bitbucket.org/adaptivesimulations/dolfin-hpc/downloads/dolfin-0.9.1-hpc.tar.gz', sha256='a34a7a2565ec435331cb867b307205d56ddfe7c07a3332d4713d356b25dc8e44')

    variant('gts', default=False)
    variant('petsc', default=True)
    variant('parmetis', default=True)
    variant('mpi', default=True)
    variant('xml', default=False)

    # FIXME: Add dependencies if required.
    depends_on('ufc@2.1.4', when='@0.9.0p1-hpc')
    depends_on('ufc@2.2.0', when='@0.9.1-hpc')
    depends_on('libxml2', when='@0.9.0p1-hpc+xml')
    depends_on('mpi', when='+mpi')
    depends_on('petsc', when='+petsc')
    depends_on('parmetis', when='+parmetis')
    depends_on('gts', when='+gts')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        if '+mpi' in self.spec:
            args.append('--enable-mpi')
            args.append('--enable-mpi-io')
        if '+parmetis' in self.spec:
            args.append('--with-parmetis')
        if '+petsc' in self.spec:
            args.append('--with-petsc={0}'.format(self.spec['petsc'].prefix))
        if '+gts' in self.spec:
            args.append('--with-gts')
        if '~xml' in self.spec:
            args.append('--without-xml')
        return args
