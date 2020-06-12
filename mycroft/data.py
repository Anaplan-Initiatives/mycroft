import mycroft.base as mc


class Attribute(mc.BaseDataObject):
    """
    Attributes describe the characteristics of dimensions. A person's name is an attribute of a person.
    Attributes should be attached as children on Dimensions.  They have no children of their own.
    Attributed may be time variant or non-time variant.

    optional keyword args:

        domain_values: list of strings to be used as a domain of values for the dimension
        is_history: bool - Track changes over time


    """

    is_attribute = True

    def __init__(self, name, *children, **kwargs):

        self.is_history = False
        super().__init__(name, *children, **kwargs)

class Dimension(mc.BaseDataObject):

    """
    Dimensions are structures for categorising and summarising data. Each dimension has at minimum a
    domain of discrete values. Dimensions can also have other attributes and dimensions that
    describe each member of the domain. Dimensions are intended to be normalized. Normalization is
    achieved by modeling different "levels" as separate dimensions and declaring DimensionReferences
    as children.

    optional keyword args:

        domain_values: list of strings to be used as a domain of values for the dimension

    """

    is_dimension  = True

    def __init__(self, name, *children, **kwargs ):

        super().__init__(name, *children, **kwargs)


class Formula (Attribute):

    """
    Formulae describe calculated attributes
    """

    is_formula = True

    def __init__(self, name, formula,  *children, **kwargs ):

        self.formula = formula
        super().__init__(name, *children, **kwargs)


class DimensionReference(mc.BaseDataObject):

    is_dimension_reference = True

    """
    DimensionReferences are used to relate dimensions to other dimensions

    Optional keyword arguments

        is_history: bool - Track changes over time

    """

    def __init__ (self, name, dimension, **kwargs):

        self.is_history = False
        self.dimension = dimension
        super().__init__ (name, **kwargs)


class Subset(mc.BaseDataObject):

    is_subset = True

    """
    Subsets describe sub-populations of members. The formula for a subset
    must return a boolean.
    
    """

    def __init__(self, name, formula, *children, **kwargs):

        self.formula = formula
        super().__init__(name, *children, **kwargs)


class Version(mc.BaseDataObject):

    is_version = True

    """
    Versions are used to denote the fact that a data object exists in multiple versions,
    e.g. plan and actual. 

    Optional keyword arguments

        reconcile_with_version: bool. Another Version object.
    """

    def __init__ (self, name, *children, **kwargs):

        self.reconcile_with_version = None
        super().__init__(name, *children, **kwargs)


