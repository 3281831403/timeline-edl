"""时间线 EDL：吸附、合并与波纹删除：待实现的核心模块。"""


def frame_snap(time, fps):
    """吸附到最近帧。"""
    raise NotImplementedError

def merge_intervals(intervals):
    """合并重叠/相接区间。"""
    raise NotImplementedError

def resolve_overlaps(intervals):
    """按优先级保留区间。"""
    raise NotImplementedError

def ripple_delete(intervals, start, end):
    """删除区间并平移后续。"""
    raise NotImplementedError

def find_gaps(intervals, start, end):
    """查找空隙。"""
    raise NotImplementedError

def edl_export(events):
    """导出 EDL 行。"""
    raise NotImplementedError
