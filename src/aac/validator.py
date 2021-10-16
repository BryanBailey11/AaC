"""
Validate a model per the AaC DSL.
"""

from iteration_utilities import flatten

from aac import util


def is_valid(model: dict) -> bool:
    """Check if MODEL is valid per the AaC DSL.

    Return True if MODEL is valid; False, otherwise.
    """
    return len(get_all_errors(model)) == 0


def get_all_errors(model: dict) -> list:
    """Return all validation errors for MODEL.

    Return a list of all the validation errors found for MODEL. If the MODEL is
    valid, return an empty list.
    """
    return get_all_parsing_errors(model) + get_all_enum_errors(model) + get_all_data_errors(model)


def get_all_parsing_errors(model: dict) -> list:
    """Return all parsing errors for the MODEL.

    Return a list of general parsing errors for the MODEL. If the MODEL is valid,
    return an empty list.
    """
    return []


def get_all_enum_errors(model: dict) -> list:
    """Return all validation errors for the enumeration MODEL.

    Return a list of all the validation errors found for the enumeration MODEL.
    If the enumeration MODEL is valid, return an empty list.
    """
    if not is_enum_model(model):
        return []

    enum = model["enum"]
    required = ["name", "values"]
    types = [str, list]

    return filter_out_empty_strings(
        get_all_errors_if_missing_required_properties(enum, required),
        get_all_errors_if_properties_have_wrong_type(enum, required, types),
    )


def is_enum_model(model: dict) -> bool:
    """Determine if the MODEL represents an enumeration model."""
    return "enum" in model


def get_all_errors_if_missing_required_properties(model: dict, required: list) -> iter:
    """Get error messages if the model is missing required properties.

    Return an iterable object containing any error messages for all REQUIRED
    properties that are not present in the MODEL. If the MODEL has all of the
    required properties, the returned collection will be empty.
    """

    def get_error(model, key):
        if key not in model.keys():
            return 'missing required field property: "{}"'.format(key)
        return ""

    def get_error_if_missing_required_property(key):
        return get_error(model, key)

    return map(get_error_if_missing_required_property, required)


def get_all_errors_if_properties_have_wrong_type(model: dict, required: list, types: list) -> iter:
    """Get error messages if the model has required properties of the wrong type.

    Return an iterable object containing any error messages for all REQUIRED
    properties that are not the permitted type in the MODEL. If the MODEL's
    required properties are all of the correct type, the returned collection
    will be empty.
    """

    def get_error(model, key, instance):
        if key in model.keys() and not isinstance(model[key], instance):
            return 'wrong type for field property: "{}"'.format(key)
        return ""

    def get_error_if_property_has_wrong_type(key, instance):
        return get_error(model, key, instance)

    return map(get_error_if_property_has_wrong_type, required, types)


def filter_out_empty_strings(*xs: list) -> list:
    """Return XS with all empty strings removed."""
    return list(filter(lambda x: x != "", flatten(xs)))


def get_all_data_errors(model: dict) -> list:
    """Return all validation errors for the data MODEL.

    Return a list of all the validation errors found for the data MODEL. If the
    data MODEL is valid, return an empty list.
    """
    if not is_data_model(model):
        return []

    data = model["data"]
    required = ["name", "fields"]
    types = [str, list]

    return filter_out_empty_strings(
        get_all_errors_if_missing_required_properties(data, required),
        get_all_errors_if_properties_have_wrong_type(
            data, required + ["required"], types + [list]
        ),
    )


def is_data_model(model: dict) -> bool:
    """Determine if the MODEL represents a data model."""
    return "data" in model
