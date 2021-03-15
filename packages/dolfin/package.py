# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Dolfin(AutotoolsPackage,PythonPackage):
    """DOLFIN HPC is a special branch of DOLFIN optimized for
       distributed memory architectures. """

    homepage = "https://bitbucket.org/adaptivesimulations/dolfin-hpc"
    maintainers = ['njansson']

    version('0.9.0p1-hpc', url='https://bitbucket.org/adaptivesimulations/dolfin-hpc/downloads/dolfin-0.9.0p1-hpc.tar.gz', sha256='9d1aaff6dafc3a408677ec00016bac7a480518f29f520cd0995def1776df1d76')
    version('0.9.1-hpc', url='https://bitbucket.org/adaptivesimulations/dolfin-hpc/downloads/dolfin-0.9.1-hpc.tar.gz', sha256='a34a7a2565ec435331cb867b307205d56ddfe7c07a3332d4713d356b25dc8e44')
    version('0.9.2-hpc', url='https://bitbucket.org/adaptivesimulations/dolfin-hpc/downloads/dolfin-0.9.2-hpc.tar.gz', sha256='c3b7f7c9c552f216b3376fda925129f2918d5eff938edfb6ebc0810558df4f62')
    version('0.9.3-hpc', url='https://bitbucket.org/adaptivesimulations/dolfin-hpc/downloads/dolfin-0.9.3-hpc.tar.gz', sha256='b826bbd7b36199ca234958f5c6661457adb625d86289c7711c4de00835c68a11')
    version('0.9.4-hpc', url='https://bitbucket.org/adaptivesimulations/dolfin-hpc/downloads/dolfin-0.9.4-hpc.tar.gz', sha256='52657aeaee82954f82799769912d3fdb92941c88a6b8f2e147ee3d1c2b360e63')

    variant('debug', default=False, description='Debug symbols and asserts')
    variant('gts', default=False, description='Compile with support for GTS')
    variant('petsc', default=True, description='Compile with support for PETSc')
    variant('mpi', default=True, description='Compile with Support for MPI')
    variant('xml', default=False, description='Support for reading/writing XML data')
    variant('convert', default=False, description='Build external mesh converter tool')
    variant('python', default=False, description='Install Python modules')
    variant('fcache', default=False, description='Local data cache in functions')
    variant('p1opt', default=False, description='Optimization for P1 elements')
    variant('optb', default=False, description='Basis function optimization')
    variant('quad', default=False, description='Enable various quadrature rules')

    depends_on('pkgconf', type=('build','run'))
    depends_on('python@:2', type=('build','run'), when=('@0.9.0p1-hpc+python'))
    depends_on('ffc@1.0.2-hpc', type=('build','run'), when=('@0.9.0p1-hpc+python'))
    depends_on('ffc@1.1.0-hpc', type=('build','run'), when=('@0.9.1-hpc:0.9.3-hpc +python'))
    depends_on('ffc@1.2.0-hpc', type=('build','run'), when=('@0.9.4-hpc'))
    depends_on('python@3:', type=('build','run'), when=('@0.9.1-hpc:0.9.3-hpc +python'))
    depends_on('python@3:', type=('build','run'), when=('@0.9.4-hpc:'))
    depends_on('ufc@2.1.4', when='@0.9.0p1-hpc')
    depends_on('ufc@2.2.0', when='@0.9.1-hpc:0.9.3-hpc')
    depends_on('libxml2', when='@0.9.0p1-hpc+xml')
    depends_on('libxml2', when='@0.9.1-hpc:+convert')
    depends_on('mpi', when='+mpi')
    depends_on('petsc', when='+petsc')
    depends_on('parmetis', when='+mpi')
    depends_on('gts', when='+gts')
    depends_on('blas', when='+quad')
    depends_on('lapack', when='+quad')


    def configure_args(self):
        args = []
        if '+debug' in self.spec:
            args.append('--enable-debug')
        if '+mpi' in self.spec:
            args.append('--enable-mpi')
            args.append('--enable-mpi-io')
            args.append('--with-parmetis')
        if '+petsc' in self.spec:
            args.append('--with-petsc={0}'.format(self.spec['petsc'].prefix))
        if '+python' in self.spec:
            args.append('--enable-python')
        if '+gts' in self.spec:
            args.append('--with-gts')
        if '+quad' in self.spec:
            args.append('--enable-quadrature')
        if self.spec.satisfies('@0.9.1-hpc:'):
            if '+convert' in self.spec:
                args.append('--with-convert')
            if '+p1opt' in self.spec:
                args.append('--enable-optimize-p1')
            if '+fcache' in self.spec:
                args.append('--enable-function-cache')
            if '+optb' in self.spec:
                args.append('--enable-opt-basis')
        if self.spec.satisfies('@0.9.0p1-hpc'):
            if '~xml' in self.spec:
                args.append('--without-xml')


        return args

    

