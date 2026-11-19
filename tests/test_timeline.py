import pytest

from video import timeline as mod

CASES = [
    ('frame_snap', [1.04, 25], 1.04, True),
    ('merge_intervals', [[[0, 2], [2, 4], [5, 6]]], [[0, 4], [5, 6]], False),
    ('merge_intervals', [[[0, 3], [1, 2]]], [[0, 3]], False),
    ('resolve_overlaps', [[[0, 5, 1], [2, 6, 2]]], [[2, 6]], False),
    ('ripple_delete', [[[0, 2], [3, 5]], 1, 4], [[0, 1], [1, 2]], False),
    ('find_gaps', [[[0, 2], [5, 6]], 0, 8], [[2, 5], [6, 8]], False),
    ('edl_export', [[['reel', 0, 0, 1]]], ['001 reel V C 00:00:00:00 00:00:01:00'], False),
    ('frame_snap', [1.06, 25], 1.04, True),
    ('frame_snap', [0.5, 2], 0.5, True),
    ('merge_intervals', [[[0, 1], [1, 2], [3, 4]]], [[0, 2], [3, 4]], False),
    ('resolve_overlaps', [[[0, 2, 1], [1, 3, 2]]], [[1, 3]], False),
    ('resolve_overlaps', [[[0, 2, 1], [3, 4, 2]]], [[0, 2], [3, 4]], False),
    ('ripple_delete', [[[0, 5]], 2, 4], [[0, 2], [2, 3]], False),
    ('find_gaps', [[[0, 8]], 0, 8], [], False),
    ('edl_export', [[['reel', 0, 1.5, 2.5]]], ['001 reel V C 00:00:01:13 00:00:02:12'], False),
]


@pytest.mark.parametrize("func_name,args,expected,approx", CASES)
def test_timeline_contract(func_name, args, expected, approx):
    func = getattr(mod, func_name)
    result = func(*args)
    if approx:
        assert result == pytest.approx(expected)
    else:
        assert result == expected
