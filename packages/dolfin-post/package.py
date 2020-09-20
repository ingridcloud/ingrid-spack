# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class DolfinPost(AutotoolsPackage):
    """DOLFINPost is a tool for converting DOLFIN binary into various formats."""

    homepage = "https://bitbucket.org/fenics-hpc/dolfin-post"    
    url      = "https://bitbucket.org/fenics-hpc/dolfin-post/downloads/dolfinpost-0.0.3.tar.gz"

    version('0.0.3', sha256='6dc4f4be555b8eb5bd3c98c74c888639135ede7a296065d6bde480829a905b71')

    variant('zlib', default=False)
    variant('glib', default=False)
    variant('silo', default=False)

    depends_on('zlib', when='+zlib')
    depends_on('glib', when='+glib')
    depends_on('silo', when='+silo')

    def configure_args(self):
        args = []
        return args

