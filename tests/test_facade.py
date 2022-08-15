import challenges.facade
from challenges.facade import numbers1, numbers2, numbers3


def test_names():
    assert hasattr(challenges.facade, 'add')  # noqa: WPS421
    assert hasattr(challenges.facade, 'mul')  # noqa: WPS421
    assert hasattr(challenges.facade, 'power')  # noqa: WPS421
    assert hasattr(challenges.facade, 'sqrt')  # noqa: WPS421
    assert hasattr(challenges.facade, 'sub')  # noqa: WPS421


def test_references():
    assert challenges.facade.add is numbers2.add2
    assert challenges.facade.mul is numbers1.mul1
    assert challenges.facade.power is numbers2.power2
    assert challenges.facade.sqrt is numbers3.sqrt3
    assert challenges.facade.sub is numbers2.sub2


def test_all_metavar():
    assert 'add' in challenges.facade.__all__  # noqa: WPS609
    assert 'mul' in challenges.facade.__all__  # noqa: WPS609
    assert 'power' in challenges.facade.__all__  # noqa: WPS609
    assert 'sqrt' in challenges.facade.__all__  # noqa: WPS609
    assert 'sub' in challenges.facade.__all__  # noqa: WPS609
