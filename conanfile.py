#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostGeometryConan(base.BoostBaseConan):
    name = "boost_geometry"
    url = "https://github.com/bincrafters/conan-boost_geometry"
    lib_short_names = ["geometry"]
    header_only_libs = ["geometry"]
    b2_requires = [
        "boost_algorithm",
        "boost_array",
        "boost_assert",
        "boost_concept_check",
        "boost_config",
        "boost_container",
        "boost_core",
        "boost_function_types",
        "boost_fusion",
        "boost_integer",
        "boost_iterator",
        "boost_lexical_cast",
        "boost_math",
        "boost_move",
        "boost_mpl",
        "boost_multiprecision",
        "boost_numeric_conversion",
        "boost_polygon",
        "boost_qvm",
        "boost_range",
        "boost_rational",
        "boost_serialization",
        "boost_smart_ptr",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_tokenizer",
        "boost_tuple",
        "boost_type_traits",
        "boost_utility",
        "boost_variant"
    ]


