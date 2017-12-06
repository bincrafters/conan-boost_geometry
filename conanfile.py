from conans import ConanFile, tools


class BoostGeometryConan(ConanFile):
    name = "Boost.Geometry"
    version = "1.65.1"

    requires = \
        "Boost.Generator/1.65.1@bincrafters/testing", \
        "Boost.Algorithm/1.65.1@bincrafters/testing", \
        "Boost.Array/1.65.1@bincrafters/testing", \
        "Boost.Assert/1.65.1@bincrafters/testing", \
        "Boost.Concept_Check/1.65.1@bincrafters/testing", \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Container/1.65.1@bincrafters/testing", \
        "Boost.Core/1.65.1@bincrafters/testing", \
        "Boost.Function_Types/1.65.1@bincrafters/testing", \
        "Boost.Fusion/1.65.1@bincrafters/testing", \
        "Boost.Integer/1.65.1@bincrafters/testing", \
        "Boost.Iterator/1.65.1@bincrafters/testing", \
        "Boost.Lexical_Cast/1.65.1@bincrafters/testing", \
        "Boost.Math/1.65.1@bincrafters/testing", \
        "Boost.Move/1.65.1@bincrafters/testing", \
        "Boost.Mpl/1.65.1@bincrafters/testing", \
        "Boost.Multiprecision/1.65.1@bincrafters/testing", \
        "Boost.Numeric_Conversion/1.65.1@bincrafters/testing", \
        "Boost.Polygon/1.65.1@bincrafters/testing", \
        "Boost.Qvm/1.65.1@bincrafters/testing", \
        "Boost.Range/1.65.1@bincrafters/testing", \
        "Boost.Rational/1.65.1@bincrafters/testing", \
        "Boost.Serialization/1.65.1@bincrafters/testing", \
        "Boost.Smart_Ptr/1.65.1@bincrafters/testing", \
        "Boost.Static_Assert/1.65.1@bincrafters/testing", \
        "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
        "Boost.Tokenizer/1.65.1@bincrafters/testing", \
        "Boost.Tuple/1.65.1@bincrafters/testing", \
        "Boost.Type_Traits/1.65.1@bincrafters/testing", \
        "Boost.Utility/1.65.1@bincrafters/testing", \
        "Boost.Variant/1.65.1@bincrafters/testing"

    lib_short_names = ["geometry"]
    is_header_only = True

    # BEGIN

    url = "https://github.com/bincrafters/conan-boost-geometry"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1"
    license = "www.boost.org/users/license.html"
    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator  # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    def package_id(self):
        self.info.header_only()

    # END
