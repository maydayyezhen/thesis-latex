# thesis-latex

武汉大学本科毕业论文 LaTeX 项目。

论文主题：听桥 / HearBridge：面向听障交流与训练的多端协同系统设计与实现。

## 项目状态

当前项目已经完成：

- LaTeX 基础工程搭建
- VSCode + LaTeX Workshop 自动编译配置
- 武汉大学本科毕业论文基础格式配置
- 中英文摘要迁移
- 第 1 章《引言》迁移
- 第 2 章《相关技术分析》迁移
- 第 3 章《系统需求分析》迁移
- 第 3 章用例图、流程图 TikZ 化
- 第 5 章模型发布流程图 TikZ 化
- 统一图片插入命令封装

当前主要工作分支：

- `migrate-word-draft`

## 项目目录

- `.vscode/`：VSCode + LaTeX Workshop 配置
- `backmatter/`：致谢、附录等结尾部分
- `chapters/`：正文章节
- `diagrams/`：TikZ 图形源码
- `docs/`：项目说明和格式检查清单
- `figures/`：外部图片资源，例如 PNG、JPG、PDF
- `frontmatter/`：封面、声明、摘要等前置部分
- `refs/`：参考文献数据库
- `source-docs/`：Word 草稿、原始材料等源文件
- `main.tex`：论文主入口
- `README.md`：项目说明

## 编译方式

推荐使用 VSCode + LaTeX Workshop。

命令行手动编译：

latexmk -pdfxe -interaction=nonstopmode -file-line-error -outdir=build main.tex

清理编译产物：

latexmk -C -outdir=build main.tex

打开生成的 PDF：

Start-Process .\build\main.pdf

## 自动预览

`.vscode/settings.json` 已配置：

- 使用 XeLaTeX / pdfxe 编译
- 输出目录为 `build/`
- 文件变化后自动编译
- VSCode 内置 PDF 标签页预览

打开项目：

code .

打开 `main.tex` 后按 `Ctrl + Alt + V` 查看 PDF 预览。

## 写作方式

论文正文按章节拆分在 `chapters/` 目录中。

主要章节：

1. 引言
2. 相关技术分析
3. 系统需求分析
4. 系统设计
5. 系统实现
6. 系统测试
7. 总结与展望

## Word 草稿迁移规则

迁移 Word 草稿时遵循以下原则：

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
- migrate chapter 3 requirements first part
- migrate chapter 3 requirements second part
- add chapter 3 TikZ diagrams

## 图片与图形规范

论文图形分为两类：

1. TikZ / LaTeX 源码图
2. PNG / JPG / PDF 外部图片

TikZ 图源码统一放在：

diagrams/

外部图片统一放在：

figures/

第三章图形源码目前位于：

diagrams/chapter03/

包括：

- fig3-1-user-usecase.tex
- fig3-2-admin-usecase.tex
- fig3-3-user-flow.tex
- fig3-4-training-flow.tex
- fig3-5-sentence-video-flow.tex

第五章模型发布流程图源码位于：

diagrams/chapter05/

包括：

- fig5-4-model-release-flow.tex

## 统一图片命令

项目在 `main.tex` 中封装了两个统一插图命令。

### 插入 TikZ / LaTeX 源码图

默认写法：

\WhuDiagramFigure{图源码路径}{图标题}{图标签}

示例：

\WhuDiagramFigure{diagrams/chapter03/fig3-5-sentence-video-flow.tex}{句子视频识别流程图}{fig:sentence-video-flow}

指定最大宽度和最大高度：

\WhuDiagramFigure[0.68\textwidth][0.55\textheight]{diagrams/chapter03/fig3-5-sentence-video-flow.tex}{句子视频识别流程图}{fig:sentence-video-flow}

### 插入 PNG / JPG / PDF 图片

默认写法：

\WhuImageFigure{图片路径}{图标题}{图标签}

示例：

\WhuImageFigure{figures/chapter04/system-architecture.png}{系统总体架构图}{fig:system-architecture}

指定最大宽度和最大高度：

\WhuImageFigure[0.9\textwidth][0.6\textheight]{figures/chapter04/system-architecture.png}{系统总体架构图}{fig:system-architecture}

第五章模型发布流程图成品示例：

\WhuImageFigure{figures/chapter05/fig5-4-model-release-flow.pdf}{模型版本发布与识别服务联动流程图}{fig:model-release-flow}

## 图片尺寸控制原则

所有论文图片默认需要限制最大宽度和最大高度，避免竖向流程图占满整页。

默认建议：

- 普通图：最大宽度不超过 `0.86\textwidth`
- 普通图：最大高度不超过 `0.58\textheight`
- 特别宽的架构图可以适当增大宽度
- 特别高的流程图应优先压缩节点和间距，再调整最大高度

不要直接用很大的截图塞进论文。用例图、流程图、架构图优先使用 TikZ、PlantUML、Mermaid 等源码化方式维护。

## 表格规范

用例规约、需求表等较长表格优先使用 `longtable`。

表格要求：

- 表题在表上方
- 表格按章自动编号
- 推荐使用三线表
- 长表可以跨页
- 表格内容不要超出页面边界

## 参考文献计划

当前迁移阶段暂时保留 Word 原文中的 `[1]`、`[2]` 等顺序编号。

后续计划：

1. 迁移第 1 至第 3 章正文
2. 建立 `docs/citation-map.md`
3. 整理 `refs/references.bib`
4. 将正文中的手写编号替换为 `\cite{}`
5. 使用 `biber` 生成 GB/T 7714-2015 格式参考文献

## 注意事项

- 不提交 `build/` 编译产物
- 不直接修改 `build/` 内文件
- 图片统一放入 `figures/`
- 图形源码统一放入 `diagrams/`
- 参考文献统一维护在 `refs/references.bib`
- Word 原稿和源材料放入 `source-docs/`
- 格式检查项见 `docs/format-checklist.md`
- 每次大改前先确认 `git status`
- 每次迁移一章后先编译，再提交

## 常用命令

查看当前状态：

git status

手动编译：

latexmk -pdfxe -interaction=nonstopmode -file-line-error -outdir=build main.tex

打开 PDF：

Start-Process .\build\main.pdf

提交当前修改：

git add .
git commit -m "update message"
git push
