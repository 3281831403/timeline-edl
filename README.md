# 时间线 EDL：吸附、合并与波纹删除

剪辑时间线在切点处重叠、波纹删除后空隙没合上：帧吸附按秒取整，区间合并漏掉相接，重叠按开始时间而不是优先级处理，波纹删除没平移后续片段，空隙检测漏掉首尾，EDL 时间码格式错，批量时间线只成功一半。

## 目录结构

```
README.md
conftest.py
.gitignore
video/__init__.py
video/timeline.py
tests/test_timeline.py
```

## 当前状态

`video/timeline.py` 中所有函数只保留签名与文档字符串，函数体统一
`raise NotImplementedError`。`tests/test_timeline.py` 有 15 个参数化用例，
初始全部失败。

## 需要修复的 10 个问题

1. 帧吸附
2. 区间合并含相接
3. 重叠按优先级
4. 波纹删除平移后续
5. 空隙检测含首尾
6. EDL 时间码格式
7. 批量时间线统一提交

## 验收

```bash
python -m pytest -q
```

初始应得到 `15 failed`，且没有 collection error。实现 `video/timeline.py`
后 15 条用例应全部通过。
