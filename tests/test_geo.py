from geoint_agent.geo import is_valid_bbox


def test_valid_bbox_around_brest() -> None:
    assert is_valid_bbox(-4.6, 48.3, -4.4, 48.4)


def test_invalid_bbox_min_lat_out_of_range() -> None:
    assert not is_valid_bbox(-4.6, -95, -4.4, 48.4)


def test_invalid_bbox_min_long_out_of_range() -> None:
    assert not is_valid_bbox(-190, 48.3, -4.4, 48.4)


def test_invalid_bbox_reverse_min_lat_above_max_lat() -> None:
    assert not is_valid_bbox(-4.6, 48.4, -4.4, 48.3)


def test_valid_bbox_at_world_limits() -> None:
    assert is_valid_bbox(-180, -90, 180, 90)
