from conans import ConanFile, tools, os

class BoostGeometryConan(ConanFile):
    name = "Boost.Geometry"
    version = "1.65.1"
    short_paths = True
    url = "https://github.com/bincrafters/conan-boost-geometry"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_names = ["geometry"]
    requires =  "Boost.Algorithm/1.65.1@bincrafters/stable", \
                      "Boost.Array/1.65.1@bincrafters/stable", \
                      "Boost.Assert/1.65.1@bincrafters/stable", \
                      "Boost.Concept_Check/1.65.1@bincrafters/stable", \
                      "Boost.Config/1.65.1@bincrafters/stable", \
                      "Boost.Container/1.65.1@bincrafters/stable", \
                      "Boost.Core/1.65.1@bincrafters/stable", \
                      "Boost.Function_Types/1.65.1@bincrafters/stable", \
                      "Boost.Fusion/1.65.1@bincrafters/stable", \
                      "Boost.Integer/1.65.1@bincrafters/stable", \
                      "Boost.Iterator/1.65.1@bincrafters/stable", \
                      "Boost.Lexical_Cast/1.65.1@bincrafters/stable", \
                      "Boost.Math/1.65.1@bincrafters/stable", \
                      "Boost.Move/1.65.1@bincrafters/stable", \
                      "Boost.Mpl/1.65.1@bincrafters/stable", \
                      "Boost.Multiprecision/1.65.1@bincrafters/stable", \
                      "Boost.Numeric_Conversion/1.65.1@bincrafters/stable", \
                      "Boost.Polygon/1.65.1@bincrafters/stable", \
                      "Boost.Qvm/1.65.1@bincrafters/stable", \
                      "Boost.Range/1.65.1@bincrafters/stable", \
                      "Boost.Rational/1.65.1@bincrafters/stable", \
                      "Boost.Serialization/1.65.1@bincrafters/stable", \
                      "Boost.Smart_Ptr/1.65.1@bincrafters/stable", \
                      "Boost.Static_Assert/1.65.1@bincrafters/stable", \
                      "Boost.Throw_Exception/1.65.1@bincrafters/stable", \
                      "Boost.Tokenizer/1.65.1@bincrafters/stable", \
                      "Boost.Tuple/1.65.1@bincrafters/stable", \
                      "Boost.Type_Traits/1.65.1@bincrafters/stable", \
                      "Boost.Utility/1.65.1@bincrafters/stable", \
                      "Boost.Variant/1.65.1@bincrafters/stable"

                      #algorithm9 array3 assert1 concept_check5 config0 container7 core2 function_types5 fusion5 integer3 iterator5 lexical_cast8 math8 move3 mpl5 multiprecision10 numeric~conversion6 polygon6 qvm6 range7 rational6 serialization11 smart_ptr4 static_assert1 throw_exception2 tokenizer6 tuple4 type_traits3 utility5 variant9
                      
    def source(self):
        boostorg_github = "https://github.com/boostorg"
        archive_name = "boost-" + self.version  
        for lib_short_name in self.lib_short_names:
            tools.get("{0}/{1}/archive/{2}.tar.gz"
                .format(boostorg_github, lib_short_name, archive_name))
            os.rename(lib_short_name + "-" + archive_name, lib_short_name)

    def package(self):
        for lib_short_name in self.lib_short_names:
            include_dir = os.path.join(lib_short_name, "include")
            self.copy(pattern="*", dst="include", src=include_dir)		

    def package_id(self):
        self.info.header_only()