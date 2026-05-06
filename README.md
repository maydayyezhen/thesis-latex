# thesis-latex

武汉大学本科毕业论文 LaTeX 项目。

论文主题：听桥 / HearBridge：面向听障交流与训练的多端协同系统设计与实现。

## 项目目录

- `.vscode/`：VSCode + LaTeX Workshop 配置
- `backmatter/`：致谢、附录等结尾部分
- `chapters/`：正文章节
- `diagrams/`：论文图形源码
- `docs/`：项目说明和格式检查清单
- `figures/`：论文图片
- `frontmatter/`：封面、声明、摘要等前置部分
- `refs/`：参考文献数据库
- `source-docs/`：论文迁移或参考用的原始文档
- `main.tex`：论文主入口
- `README.md`：项目说明

## 编译方式

推荐使用 VSCode + LaTeX Workshop。

命令行手动编译：

~~~powershell
latexmk -xelatex -interaction=nonstopmode -file-line-error -outdir=build main.tex
~~~

清理编译产物：

~~~powershell
latexmk -C -outdir=build main.tex
~~~

## 自动预览

`.vscode/settings.json` 已配置：

- XeLaTeX 编译
- 输出目录为 `build/`
- 文件变化后自动编译
- VSCode 内置 PDF 标签页预览

打开方式：

~~~powershell
code .
~~~

打开 `main.tex` 后按 `Ctrl + Alt + V` 查看 PDF 预览。

## 写作方式

正文按章节拆分在 `chapters/` 目录中。

主要章节：

1. 绪论
2. 相关技术基础
3. 系统需求分析
4. 系统总体设计
5. 系统详细设计与实现
6. 系统测试与结果分析
7. 总结与展望

## 图表维护

- 论文插图统一放入 `figures/`。
- 可维护的图形源码统一放入 `diagrams/`。
- 参考文献统一维护在 `refs/references.bib`。
- 格式检查项见 `docs/format-checklist.md`。

## 注意事项

- 不提交 `build/` 编译产物。
- 不提交 `main.pdf` 等本地生成文件。
- 不提交 `.local-backups/`、`.bak`、`.backup.tex` 等临时备份文件。
- 修改章节文件后，优先确认 `main.tex` 中是否已正确引用。