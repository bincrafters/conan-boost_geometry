#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools


class BoostGeometryConan(ConanFile):
    name = "boost_geometry"
    version = "1.66.0"
    url = "https://github.com/bincrafters/conan-boost_geometry"
    author = "Bincrafters <bincrafters@gmail.com>"
    exports = ["LICENSE.md"]
    lib_short_names = ["geometry"]
    is_header_only = True

    def package_id_additional(self):
        self.info.header_only()

    requires = (
        "boost_package_tools/1.66.0@bincrafters/stable",
        "boost_algorithm/1.66.0@bincrafters/stable",
        "boost_array/1.66.0@bincrafters/stable",
        "boost_assert/1.66.0@bincrafters/stable",
        "boost_concept_check/1.66.0@bincrafters/stable",
        "boost_config/1.66.0@bincrafters/stable",
        "boost_container/1.66.0@bincrafters/stable",
        "boost_core/1.66.0@bincrafters/stable",
        "boost_function_types/1.66.0@bincrafters/stable",
        "boost_fusion/1.66.0@bincrafters/stable",
        "boost_integer/1.66.0@bincrafters/stable",
        "boost_iterator/1.66.0@bincrafters/stable",
        "boost_lexical_cast/1.66.0@bincrafters/stable",
        "boost_math/1.66.0@bincrafters/stable",
        "boost_move/1.66.0@bincrafters/stable",
        "boost_mpl/1.66.0@bincrafters/stable",
        "boost_multiprecision/1.66.0@bincrafters/stable",
        "boost_numeric_conversion/1.66.0@bincrafters/stable",
        "boost_polygon/1.66.0@bincrafters/stable",
        "boost_qvm/1.66.0@bincrafters/stable",
        "boost_range/1.66.0@bincrafters/stable",
        "boost_rational/1.66.0@bincrafters/stable",
        "boost_serialization/1.66.0@bincrafters/stable",
        "boost_smart_ptr/1.66.0@bincrafters/stable",
        "boost_static_assert/1.66.0@bincrafters/stable",
        "boost_throw_exception/1.66.0@bincrafters/stable",
        "boost_tokenizer/1.66.0@bincrafters/stable",
        "boost_tuple/1.66.0@bincrafters/stable",
        "boost_type_traits/1.66.0@bincrafters/stable",
        "boost_utility/1.66.0@bincrafters/stable",
        "boost_variant/1.66.0@bincrafters/stable"
    )

    # BEGIN

    description = "Please visit http://www.boost.org/doc/libs/1_66_0"
    license = "BSL-1.0"
    short_paths = True
    build_requires = "boost_generator/1.66.0@bincrafters/stable"

    def package_id(self):
        getattr(self, "package_id_additional", lambda:None)()

    def source(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.source(self)
        getattr(self, "source_additional", lambda:None)()

    def build(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.build(self)
        getattr(self, "build_additional", lambda:None)()

    def package(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package(self)
        getattr(self, "package_additional", lambda:None)()

    def package_info(self):
        with tools.pythonpath(self):
            import boost_package_tools  # pylint: disable=F0401
            boost_package_tools.package_info(self)
        getattr(self, "package_info_additional", lambda:None)()



    # END
