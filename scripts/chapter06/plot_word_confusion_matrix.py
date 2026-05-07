import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

csv_path = Path(r"D:\datasets\WLASL-mini-v2-25\models_20f_plus\confusion_matrix.csv")
out_path = Path(r".\figures\chapter06\word-model-confusion-matrix.png")

df = pd.read_csv(csv_path)

true_labels = df.iloc[:, 0].astype(str).tolist()
pred_labels = [str(col) for col in df.columns[1:]]
cm = df.iloc[:, 1:].to_numpy(dtype=float)

fig, ax = plt.subplots(figsize=(12, 10))
im = ax.imshow(cm, interpolation="nearest")

ax.set_xticks(np.arange(len(pred_labels)))
ax.set_yticks(np.arange(len(true_labels)))
ax.set_xticklabels(pred_labels, rotation=45, ha="right", fontsize=8)
ax.set_yticklabels(true_labels, fontsize=8)
ax.set_xlabel("Predicted label")
ax.set_ylabel("True label")

cbar = fig.colorbar(im, ax=ax)
cbar.ax.set_ylabel("Count", rotation=90, va="bottom")

threshold = cm.max() / 2.0 if cm.size > 0 else 0
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        value = int(cm[i, j])
        if value != 0:
            ax.text(
                j, i, str(value),
                ha="center", va="center",
                color="white" if cm[i, j] > threshold else "black",
                fontsize=6
            )

fig.tight_layout()
out_path.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(out_path, dpi=300, bbox_inches="tight")
plt.close(fig)

print(f"[完成] 已生成混淆矩阵图片：{out_path}")