from conans import ConanFile, tools, os

class BoostGeometryConan(ConanFile):
    name = "Boost.Geometry"
    version = "1.64.0"
    generators = "txt"
    url = "https://github.com/boostorg/geometry"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "geometry"
    requires =  "Boost.Algorithm/1.64.0@bincrafters/testing", \
                      "Boost.Array/1.64.0@bincrafters/testing", \
                      "Boost.Assert/1.64.0@bincrafters/testing", \
                      "Boost.Concept_Check/1.64.0@bincrafters/testing", \
                      "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Container/1.64.0@bincrafters/testing", \
                      "Boost.Core/1.64.0@bincrafters/testing", \
                      "Boost.Function_Types/1.64.0@bincrafters/testing", \
                      "Boost.Fusion/1.64.0@bincrafters/testing", \
                      "Boost.Integer/1.64.0@bincrafters/testing", \
                      "Boost.Iterator/1.64.0@bincrafters/testing", \
                      "Boost.Lexical_Cast/1.64.0@bincrafters/testing", \
                      "Boost.Math/1.64.0@bincrafters/testing", \
                      "Boost.Move/1.64.0@bincrafters/testing", \
                      "Boost.Mpl/1.64.0@bincrafters/testing", \
                      "Boost.Multiprecision/1.64.0@bincrafters/testing", \
                      "Boost.Numeric_Conversion/1.64.0@bincrafters/testing", \
                      "Boost.Polygon/1.64.0@bincrafters/testing", \
                      "Boost.Qvm/1.64.0@bincrafters/testing", \
                      "Boost.Range/1.64.0@bincrafters/testing", \
                      "Boost.Rational/1.64.0@bincrafters/testing", \
                      "Boost.Serialization/1.64.0@bincrafters/testing", \
                      "Boost.Smart_Ptr/1.64.0@bincrafters/testing", \
                      "Boost.Static_Assert/1.64.0@bincrafters/testing", \
                      "Boost.Throw_Exception/1.64.0@bincrafters/testing", \
                      "Boost.Tokenizer/1.64.0@bincrafters/testing", \
                      "Boost.Tuple/1.64.0@bincrafters/testing", \
                      "Boost.Type_Traits/1.64.0@bincrafters/testing", \
                      "Boost.Utility/1.64.0@bincrafters/testing", \
                      "Boost.Variant/1.64.0@bincrafters/testing"

                      #algorithm9 array3 assert1 concept_check5 config0 container7 core2 function_types5 fusion5 integer3 iterator5 lexical_cast8 math8 move3 mpl5 multiprecision10 numeric~conversion6 polygon6 qvm6 range7 rational6 serialization11 smart_ptr4 static_assert1 throw_exception2 tokenizer6 tuple4 type_traits3 utility5 variant9
                      
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="", src=include_dir)

    def package_id(self):
        self.info.header_only()