from conans import ConanFile, CMake, tools


class PodofoConan(ConanFile):
    name = "podofo"
    version = "0.9.6"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Podofo here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    exports_sources = ["CMakeLists.txt"]

    def requirements(self):
        self.requires("fontconfig/2.13.1@jgsogo/stable")

    def source(self):
        url = "http://sourceforge.net/projects/podofo/files/podofo/{version}/podofo-{version}.tar.gz"
        tools.get(url.format(version=self.version))

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["PODOFO_BUILD_LIB_ONLY"] = True
        cmake.definitions["SOURCE_FOLDER"] = "{name}-{version}".format(name=self.name,
                                                                       version=self.version)
        cmake.configure(defs={'PODOFO_BUILD_SHARED:BOOL': 'TRUE' if self.options.shared else 'FALSE',
                              'PODOFO_BUILD_STATIC:BOOL': 'FALSE' if self.options.shared else 'TRUE',
                              })
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["podofo"]

