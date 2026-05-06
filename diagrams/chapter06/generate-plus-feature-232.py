# -*- coding: utf-8 -*-
"""
生成句子视频识别 20 × 232 plus 特征构成示意图。
输出文件：
figures/chapter06/plus-feature-232.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 设置中文字体，优先使用 Windows 常见字体
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

# 创建画布
fig, ax = plt.subplots(figsize=(11, 6.2), dpi=220)

# 坐标范围
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis("off")

# 主标题
ax.text(
    6,
    7.55,
    "句子视频识别 20 × 232 plus 特征构成示意图",
    ha="center",
    va="center",
    fontsize=15,
    fontweight="bold",
)

# 左侧视频帧输入
video_box = patches.Rectangle(
    (0.5, 3.2),
    1.8,
    2.2,
    linewidth=1.2,
    edgecolor="black",
    facecolor="white",
)
ax.add_patch(video_box)
ax.text(1.4, 4.75, "输入视频片段", ha="center", va="center", fontsize=11)
ax.text(1.4, 4.25, "连续手语动作", ha="center", va="center", fontsize=10)
ax.text(1.4, 3.75, "视频帧序列", ha="center", va="center", fontsize=10)

# 箭头：输入到重采样
ax.annotate(
    "",
    xy=(3.1, 4.3),
    xytext=(2.35, 4.3),
    arrowprops=dict(arrowstyle="->", linewidth=1.2, color="black"),
)

# 重采样节点
sample_box = patches.Rectangle(
    (3.1, 3.45),
    1.8,
    1.7,
    linewidth=1.2,
    edgecolor="black",
    facecolor="white",
)
ax.add_patch(sample_box)
ax.text(4.0, 4.65, "动作窗口", ha="center", va="center", fontsize=11)
ax.text(4.0, 4.25, "重采样", ha="center", va="center", fontsize=11)
ax.text(4.0, 3.85, "20 帧", ha="center", va="center", fontsize=10)

# 箭头：重采样到矩阵
ax.annotate(
    "",
    xy=(5.55, 4.3),
    xytext=(4.95, 4.3),
    arrowprops=dict(arrowstyle="->", linewidth=1.2, color="black"),
)

# 特征矩阵外框
matrix_x = 5.55
matrix_y = 2.25
matrix_w = 5.6
matrix_h = 3.7

matrix_box = patches.Rectangle(
    (matrix_x, matrix_y),
    matrix_w,
    matrix_h,
    linewidth=1.4,
    edgecolor="black",
    facecolor="white",
)
ax.add_patch(matrix_box)

# 顶部矩阵标签
ax.text(
    matrix_x + matrix_w / 2,
    matrix_y + matrix_h + 0.42,
    "模型输入特征矩阵：20 × 232",
    ha="center",
    va="center",
    fontsize=12,
    fontweight="bold",
)

# 行方向标注
ax.text(
    matrix_x - 0.55,
    matrix_y + matrix_h / 2,
    "20 帧",
    ha="center",
    va="center",
    rotation=90,
    fontsize=11,
)

# 列方向标注
ax.text(
    matrix_x + matrix_w / 2,
    matrix_y - 0.45,
    "每帧 232 维 plus 特征",
    ha="center",
    va="center",
    fontsize=11,
)

# 矩阵内部横线，表示 20 帧
for i in range(1, 20):
    y = matrix_y + matrix_h * i / 20
    ax.plot([matrix_x, matrix_x + matrix_w], [y, y], color="black", linewidth=0.25)

# 矩阵内部竖向分组线
part1 = 166 / 232
part2 = 28 / 232
x1 = matrix_x + matrix_w * part1
x2 = matrix_x + matrix_w * (part1 + part2)

ax.plot([x1, x1], [matrix_y, matrix_y + matrix_h], color="black", linewidth=1.2)
ax.plot([x2, x2], [matrix_y, matrix_y + matrix_h], color="black", linewidth=1.2)

# 分组文字
ax.text(
    matrix_x + (x1 - matrix_x) / 2,
    matrix_y + matrix_h / 2,
    "原始关键点\n时序特征\n166 维",
    ha="center",
    va="center",
    fontsize=10,
)

ax.text(
    x1 + (x2 - x1) / 2,
    matrix_y + matrix_h / 2,
    "静态相对\n位置特征\n28 维",
    ha="center",
    va="center",
    fontsize=10,
)

ax.text(
    x2 + (matrix_x + matrix_w - x2) / 2,
    matrix_y + matrix_h / 2,
    "动态差分\n特征\n38 维",
    ha="center",
    va="center",
    fontsize=10,
)

# 底部说明
ax.text(
    6,
    0.75,
    "plus 特征 = 原始 166 维特征 + 静态相对位置 28 维 + 动态差分 38 维",
    ha="center",
    va="center",
    fontsize=11,
)

ax.text(
    6,
    0.35,
    "用于句子视频识别中词级动作片段的分类输入",
    ha="center",
    va="center",
    fontsize=10,
)

# 保存图片
plt.tight_layout()
plt.savefig(
    "figures/chapter06/plus-feature-232.png",
    dpi=220,
    bbox_inches="tight",
    facecolor="white",
)
plt.close()