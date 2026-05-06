# thesis-latex

武汉大学本科毕业论文 LaTeX 项目。

论文主题：**听桥 / HearBridge：面向听障交流与训练的多端协同系统设计与实现**。

本仓库用于维护毕业论文 LaTeX 正文、图表、参考文献和编译配置。论文内容以 HearBridge / 听桥为准，不迁入 GMRL 相关内容。

## 当前状态

当前项目已经完成：

- LaTeX 基础工程搭建
- VSCode + LaTeX Workshop 自动编译配置
- 武汉大学本科毕业论文基础格式配置
- 中英文摘要迁移
- 第 1 章《引言》迁移与拆分
- 第 2 章《相关技术分析》迁移与拆分
- 第 3 章《系统需求分析》迁移与拆分
- 第 4 章《系统设计》按 Word 主线调整并拆分
- 第 5 章《系统核心功能实现》迁移并拆分
- 第 6 章《手势识别服务实现与实验分析》主体迁移，并按 section / subsection 进一步拆分
- 第 7 章《总结与展望》拆分
- 第 3 章用例图、流程图 TikZ 化
- 第 4 章系统架构图、功能模块图、E-R 图接入
- 第 5 章移动端、管理端页面截图和模型发布流程图接入
- 第 6 章图片智能占位图接入
- 全局表格列宽与长英文断行优化
- 正文源码按“一句一行”方式格式化，提升可读性和 Git diff 体验
- 本地备份文件、编译产物、虚拟环境和临时目录树文件清理规则配置

当前主要工作分支：

- `migrate-word-draft`

## 项目目录

- `.vscode/`：VSCode + LaTeX Workshop 配置
- `.local-backups/`：本地自动备份文件目录，已加入 `.gitignore`，不提交
- `backmatter/`：致谢、附录等结尾部分
- `chapters/`：正文章节入口文件与章节拆分文件
- `diagrams/`：TikZ 图形源码
- `docs/`：项目说明和格式检查清单
- `figures/`：外部图片资源，例如 PNG、JPG、PDF
- `frontmatter/`：封面、声明、摘要等前置部分
- `refs/`：参考文献数据库
- `source-docs/`：Word 草稿、原始材料等源文件
- `main.tex`：论文主入口
- `README.md`：项目说明

## 章节组织方式

论文主入口为：

```text
main.tex
```

正文入口文件位于：

```text
chapters/
```

每一章保留一个章入口文件，例如：

```text
chapters/chapter06-system-test.tex
```

章入口文件只负责声明章标题、章导语和 `\input{}` 子文件。

章节内容进一步拆分到对应子目录，例如：

```text
chapters/chapter06/
```

第六章因为内容较长，已经进一步按 subsection 拆分，例如：

```text
chapters/chapter06/06-01-realtime-word-recognition/
  06-01-01-data-and-tech-selection.tex
  06-01-02-raw-sample-collection.tex
  06-01-03-feature-composition.tex
  06-01-04-feature-conversion.tex
  06-01-05-fixed-vocab-training.tex
  06-01-06-model-release-reload.tex
```

这种结构的目标是：

- 单个文件尽量保持在较短长度
- 方便定位具体小节
- 减少大段文本修改造成的 Git diff 混乱
- 后续修改图、表、公式和引用时更容易维护

## 编译方式

推荐使用 VSCode + LaTeX Workshop。

命令行完整编译：

```powershell
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

打开生成的 PDF：

```powershell
Start-Process .\main.pdf
```

快速检查正文是否能通过编译：

```powershell
xelatex main.tex
```

## 自动预览

`.vscode/settings.json` 已配置 LaTeX Workshop 自动编译和编辑体验优化。

打开项目：

```powershell
code .
```

打开 `main.tex` 后按：

```text
Ctrl + Alt + V
```

即可查看 PDF 预览。

如果自动编译失效，可在 VSCode 中执行：

```text
Ctrl + Shift + P
Developer: Reload Window
```

注意：本项目使用 `fontspec`，必须使用 XeLaTeX 编译，不应使用 pdfLaTeX。

## 写作方式

论文正文按章节拆分在 `chapters/` 目录中。

主要章节：

1. 引言
2. 相关技术分析
3. 系统需求分析
4. 系统设计
5. 系统核心功能实现
6. 手势识别服务实现与实验分析
7. 总结与展望

正文源码推荐采用“一句话一行”的方式书写。LaTeX 会将同一段内的普通换行视为空格，因此 PDF 排版不会受到影响，但源码可读性和 Git diff 会更清晰。

## Word 草稿迁移规则

迁移 Word 草稿时遵循以下原则：

- 以 Word 文档或已提取到画板的标准文本为依据
- 先迁移纯文本内容
- 再处理表格
- 再处理图片
- 最后统一处理参考文献引用
- 每迁移一章，先编译检查，再单独提交
- 不把 GMRL 相关内容迁入本项目，本论文主题只以 HearBridge / 听桥为准

推荐提交粒度：

- migrate abstract from Word draft
- migrate chapter 1 from Word draft
- migrate chapter 2 from Word draft
- migrate chapter 3 from Word draft
- migrate chapter 4 system design
- migrate chapter 5 system implementation
- migrate chapter 6 recognition service and experiments
- split long chapter files
- add diagrams and placeholder figures

## 图片与图形规范

论文图形分为三类：

1. TikZ / LaTeX 源码图
2. PNG / JPG / PDF 外部图片
3. 智能占位图

TikZ 图源码统一放在：

```text
diagrams/
```

外部图片统一放在：

```text
figures/
```

第三章图形源码位于：

```text
diagrams/chapter03/
```

包括：

- `fig3-1-user-usecase.tex`
- `fig3-2-admin-usecase.tex`
- `fig3-3-user-flow.tex`
- `fig3-4-training-flow.tex`
- `fig3-5-sentence-video-flow.tex`

第四章图片位于：

```text
figures/chapter04/
```

第五章图片位于：

```text
figures/chapter05/
```

第六章图片资源目录位于：

```text
figures/chapter06/
```

当前第六章使用智能占位图机制。若真实图片文件不存在，PDF 中会显示占位框；后续只需要将真实图片放到对应路径并重新编译，即可自动替换占位图。

## 统一图片命令

项目在 `main.tex` 中封装了统一插图命令。

### 插入 TikZ / LaTeX 源码图

默认写法：

```tex
\WhuDiagramFigure{图源码路径}{图标题}{图标签}
```

示例：

```tex
\WhuDiagramFigure{diagrams/chapter03/fig3-5-sentence-video-flow.tex}{句子视频识别流程图}{fig:sentence-video-flow}
```

指定最大宽度和最大高度：

```tex
\WhuDiagramFigure[0.68\textwidth][0.55\textheight]{diagrams/chapter03/fig3-5-sentence-video-flow.tex}{句子视频识别流程图}{fig:sentence-video-flow}
```

### 插入 PNG / JPG / PDF 图片

默认写法：

```tex
\WhuImageFigure{图片路径}{图标题}{图标签}
```

示例：

```tex
\WhuImageFigure{figures/chapter04/fig4-1-system-architecture.png}{系统总体架构图}{fig:chapter04-system-architecture}
```

指定最大宽度和最大高度：

```tex
\WhuImageFigure[0.9\textwidth][0.6\textheight]{figures/chapter04/fig4-1-system-architecture.png}{系统总体架构图}{fig:chapter04-system-architecture}
```

### 插入智能占位图

默认写法：

```tex
\WhuAutoFigure{宽度}{高度}{图片路径}{图标题}{图标签}
```

示例：

```tex
\WhuAutoFigure{0.82\textwidth}{0.42\textheight}{figures/chapter06/fig6-1-raw-dataset-flow.png}{自采样本采集流程图}{fig:chapter06-raw-dataset-flow}
```

如果图片存在，会自动插入真实图片；如果图片不存在，会显示占位框。

## 第六章占位图片命名

第六章当前预留以下图片文件名：

- `fig6-1-raw-dataset-flow.png`
- `fig6-2-realtime-feature-166.png`
- `fig6-3-realtime-cnn.png`
- `fig6-4-model-release-reload-flow.png`
- `fig6-5-realtime-training-curve.png`
- `fig6-6-realtime-confusion-matrix.png`
- `fig6-7-mobile-realtime-result.png`
- `fig6-8-plus-feature-232.png`
- `fig6-9-sentence-feature-build-flow.png`
- `fig6-10-word-classifier-structure.png`
- `fig6-11-frame-cache-flow.png`
- `fig6-12-sliding-window.png`
- `fig6-13-window-predict-to-gloss.png`
- `fig6-14-deepseek-candidate-correction.png`
- `fig6-15-word-model-confusion-matrix.png`
- `fig6-16-typical-sentence-result.png`

只要把真实图片放入：

```text
figures/chapter06/
```

并按上述文件名命名，重新编译后即可替换占位图。

## 图片尺寸控制原则

所有论文图片默认需要限制最大宽度和最大高度，避免竖向流程图占满整页。

默认建议：

- 普通图：最大宽度不超过 `0.86\textwidth`
- 普通图：最大高度不超过 `0.58\textheight`
- 特别宽的架构图可以适当增大宽度
- 特别高的流程图应优先压缩节点和间距，再调整最大高度

不要直接用很大的截图塞进论文。用例图、流程图、架构图优先使用 TikZ、PlantUML、Mermaid 等源码化方式维护。

## 表格规范

用例规约、需求表、实验结果表等较长表格优先使用 `longtable`。

表格要求：

- 表题在表上方
- 表格按章自动编号
- 推荐使用三线表
- 长表可以跨页
- 表格内容不要超出页面边界
- 长英文变量名需要允许断行
- 多列表格应适当压缩列宽，不要强行塞满整页

当前项目已在 `main.tex` 中对 `L/C/R` 表格列类型做了全局优化：

- 缩小表格列间距
- 自动扣除左右列间距
- 支持长英文串在窄列中断行
- 减少 `Overfull \hbox` 问题

## 参考文献计划

当前迁移阶段已经开始使用 `biblatex` 和 `biber` 维护参考文献。

后续计划：

1. 检查第 1 至第 6 章引用是否完整
2. 建立或更新 `docs/citation-map.md`
3. 整理 `refs/references.bib`
4. 将残留手写编号替换为 `\cite{}`
5. 使用 `biber` 生成 GB/T 7714-2015 格式参考文献

## 本地文件与忽略规则

以下内容不提交到 Git：

- `.local-backups/`
- `.venv/`
- `build/`
- LaTeX 编译缓存文件
- 临时目录树文件
- 本地备份文件

常见不提交文件包括：

```text
*.aux
*.bbl
*.bcf
*.blg
*.log
*.out
*.run.xml
*.toc
*.xdv
*.synctex.gz
*.bak
*.backup.tex
project-tree.txt
project-tree-clean.txt
git-files.txt
```

## 注意事项

- 不提交 `build/` 编译产物
- 不直接修改 `build/` 内文件
- 不提交 `.venv/`
- 不提交 `.local-backups/`
- 图片统一放入 `figures/`
- 图形源码统一放入 `diagrams/`
- 参考文献统一维护在 `refs/references.bib`
- Word 原稿和源材料放入 `source-docs/`
- 格式检查项见 `docs/format-checklist.md`
- 每次大改前先确认 `git status`
- 每次迁移一章后先编译，再提交

## 常用命令

查看当前状态：

```powershell
git status
```

查看简略状态：

```powershell
git status --short
```

手动完整编译：

```powershell
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

打开 PDF：

```powershell
Start-Process .\main.pdf
```

清理常见 LaTeX 编译产物：

```powershell
Remove-Item *.aux,*.bbl,*.bcf,*.blg,*.log,*.out,*.run.xml,*.toc,*.xdv,*.synctex.gz -ErrorAction SilentlyContinue
```

提交当前修改：

```powershell
git add .
git commit -m "update message"
git push
```