import pytest
import mycroft.data as d

def test_data_objects():
    loc = d.Dimension('Location')
    dim = d.Dimension('Person')
    dim['phone'] = d.Attribute('Phone')
    dim['loyalty'] = d.Attribute(None,domain_values = ['Gold','Silver','NA'])
    dim['country'] = d.Attribute(None, is_history = True)
    dim['actual'] = d.Version(None)
    dim['plan'] = d.Version(None, reconcile_with_version = dim['actual'])
    dim['home_location'] = d.DimensionReference(None,loc, is_history = True)
    dim['work_location'] = d.DimensionReference(None, loc)

    assert (loc.name == 'Location')
    assert (dim.name == 'Person')
    assert (dim['phone'].name == 'Phone')
    assert (not dim['phone'].is_history)
    assert (dim['loyalty'].domain_values == ['Gold','Silver','NA'])
    assert (dim['country'].name == 'country')
    assert (dim['country'].is_history)
    assert (dim['actual'].name == 'actual')
    assert (dim['plan'].name == 'plan')
    assert (dim['plan'].reconcile_with_version.name == 'actual')
    assert (dim['home_location'].dimension.name == 'Location')
    assert (dim['home_location'].is_history)
    assert (dim['work_location'].dimension.name == 'Location')
    assert (not dim['work_location'].is_history)