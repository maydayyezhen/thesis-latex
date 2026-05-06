# thesis-latex

姝︽眽澶у鏈姣曚笟璁烘枃 LaTeX 椤圭洰銆?
璁烘枃涓婚锛?*鍚ˉ / HearBridge锛氶潰鍚戝惉闅滀氦娴佷笌璁粌鐨勫绔崗鍚岀郴缁熻璁′笌瀹炵幇**銆?
鏈粨搴撶敤浜庣淮鎶ゆ瘯涓氳鏂?LaTeX 姝ｆ枃銆佸浘琛ㄣ€佸弬鑰冩枃鐚拰缂栬瘧閰嶇疆銆傝鏂囧唴瀹逛互 HearBridge / 鍚ˉ涓哄噯锛屼笉杩佸叆 GMRL 鐩稿叧鍐呭銆?
## 褰撳墠鐘舵€?
褰撳墠椤圭洰宸茬粡瀹屾垚锛?
- LaTeX 鍩虹宸ョ▼鎼缓
- VSCode + LaTeX Workshop 鑷姩缂栬瘧閰嶇疆
- 姝︽眽澶у鏈姣曚笟璁烘枃鍩虹鏍煎紡閰嶇疆
- 涓嫳鏂囨憳瑕佽縼绉?- 绗?1 绔犮€婂紩瑷€銆嬭縼绉讳笌鎷嗗垎
- 绗?2 绔犮€婄浉鍏虫妧鏈垎鏋愩€嬭縼绉讳笌鎷嗗垎
- 绗?3 绔犮€婄郴缁熼渶姹傚垎鏋愩€嬭縼绉讳笌鎷嗗垎
- 绗?4 绔犮€婄郴缁熻璁°€嬫寜 Word 涓荤嚎璋冩暣骞舵媶鍒?- 绗?5 绔犮€婄郴缁熸牳蹇冨姛鑳藉疄鐜般€嬭縼绉诲苟鎷嗗垎
- 绗?6 绔犮€婃墜鍔胯瘑鍒湇鍔″疄鐜颁笌瀹為獙鍒嗘瀽銆嬩富浣撹縼绉伙紝骞舵寜 section / subsection 杩涗竴姝ユ媶鍒?- 绗?7 绔犮€婃€荤粨涓庡睍鏈涖€嬫媶鍒?- 绗?3 绔犵敤渚嬪浘銆佹祦绋嬪浘 TikZ 鍖?- 绗?4 绔犵郴缁熸灦鏋勫浘銆佸姛鑳芥ā鍧楀浘銆丒-R 鍥炬帴鍏?- 绗?5 绔犵Щ鍔ㄧ銆佺鐞嗙椤甸潰鎴浘鍜屾ā鍨嬪彂甯冩祦绋嬪浘鎺ュ叆
- 绗?6 绔犲浘鐗囨櫤鑳藉崰浣嶅浘鎺ュ叆
- 鍏ㄥ眬琛ㄦ牸鍒楀涓庨暱鑻辨枃鏂浼樺寲
- 姝ｆ枃婧愮爜鎸夆€滀竴鍙ヤ竴琛屸€濇柟寮忔牸寮忓寲锛屾彁鍗囧彲璇绘€у拰 Git diff 浣撻獙
- 鏈湴澶囦唤鏂囦欢銆佺紪璇戜骇鐗┿€佽櫄鎷熺幆澧冨拰涓存椂鐩綍鏍戞枃浠舵竻鐞嗚鍒欓厤缃?
褰撳墠涓昏宸ヤ綔鍒嗘敮锛?
- `migrate-chapter05`

## 椤圭洰鐩綍

- `.vscode/`锛歏SCode + LaTeX Workshop 閰嶇疆
- `.local-backups/`锛氭湰鍦拌嚜鍔ㄥ浠芥枃浠剁洰褰曪紝宸插姞鍏?`.gitignore`锛屼笉鎻愪氦
- `backmatter/`锛氳嚧璋€侀檮褰曠瓑缁撳熬閮ㄥ垎
- `chapters/`锛氭鏂囩珷鑺傚叆鍙ｆ枃浠朵笌绔犺妭鎷嗗垎鏂囦欢
- `diagrams/`锛歍ikZ 鍥惧舰婧愮爜
- `docs/`锛氶」鐩鏄庡拰鏍煎紡妫€鏌ユ竻鍗?- `figures/`锛氬閮ㄥ浘鐗囪祫婧愶紝渚嬪 PNG銆丣PG銆丳DF
- `frontmatter/`锛氬皝闈€佸０鏄庛€佹憳瑕佺瓑鍓嶇疆閮ㄥ垎
- `refs/`锛氬弬鑰冩枃鐚暟鎹簱
- `source-docs/`锛歐ord 鑽夌銆佸師濮嬫潗鏂欑瓑婧愭枃浠?- `main.tex`锛氳鏂囦富鍏ュ彛
- `README.md`锛氶」鐩鏄?
## 绔犺妭缁勭粐鏂瑰紡

璁烘枃涓诲叆鍙ｄ负锛?
```text
main.tex
```

姝ｆ枃鍏ュ彛鏂囦欢浣嶄簬锛?
```text
chapters/
```

姣忎竴绔犱繚鐣欎竴涓珷鍏ュ彛鏂囦欢锛屼緥濡傦細

```text
chapters/chapter06-system-test.tex
```

绔犲叆鍙ｆ枃浠跺彧璐熻矗澹版槑绔犳爣棰樸€佺珷瀵艰鍜?`\input{}` 瀛愭枃浠躲€?
绔犺妭鍐呭杩涗竴姝ユ媶鍒嗗埌瀵瑰簲瀛愮洰褰曪紝渚嬪锛?
```text
chapters/chapter06/
```

绗叚绔犲洜涓哄唴瀹硅緝闀匡紝宸茬粡杩涗竴姝ユ寜 subsection 鎷嗗垎锛屼緥濡傦細

```text
chapters/chapter06/06-01-realtime-word-recognition/
  06-01-01-data-and-tech-selection.tex
  06-01-02-raw-sample-collection.tex
  06-01-03-feature-composition.tex
  06-01-04-feature-conversion.tex
  06-01-05-fixed-vocab-training.tex
  06-01-06-model-release-reload.tex
```

杩欑缁撴瀯鐨勭洰鏍囨槸锛?
- 鍗曚釜鏂囦欢灏介噺淇濇寔鍦ㄨ緝鐭暱搴?- 鏂逛究瀹氫綅鍏蜂綋灏忚妭
- 鍑忓皯澶ф鏂囨湰淇敼閫犳垚鐨?Git diff 娣蜂贡
- 鍚庣画淇敼鍥俱€佽〃銆佸叕寮忓拰寮曠敤鏃舵洿瀹规槗缁存姢

## 缂栬瘧鏂瑰紡

鎺ㄨ崘浣跨敤 VSCode + LaTeX Workshop銆?
鍛戒护琛屽畬鏁寸紪璇戯細

```powershell
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

鎵撳紑鐢熸垚鐨?PDF锛?
```powershell
Start-Process .\main.pdf
```

蹇€熸鏌ユ鏂囨槸鍚﹁兘閫氳繃缂栬瘧锛?
```powershell
xelatex main.tex
```

## 鑷姩棰勮

`.vscode/settings.json` 宸查厤缃?LaTeX Workshop 鑷姩缂栬瘧鍜岀紪杈戜綋楠屼紭鍖栥€?
鎵撳紑椤圭洰锛?
```powershell
code .
```

鎵撳紑 `main.tex` 鍚庢寜锛?
```text
Ctrl + Alt + V
```

鍗冲彲鏌ョ湅 PDF 棰勮銆?
濡傛灉鑷姩缂栬瘧澶辨晥锛屽彲鍦?VSCode 涓墽琛岋細

```text
Ctrl + Shift + P
Developer: Reload Window
```

娉ㄦ剰锛氭湰椤圭洰浣跨敤 `fontspec`锛屽繀椤讳娇鐢?XeLaTeX 缂栬瘧锛屼笉搴斾娇鐢?pdfLaTeX銆?
## 鍐欎綔鏂瑰紡

璁烘枃姝ｆ枃鎸夌珷鑺傛媶鍒嗗湪 `chapters/` 鐩綍涓€?
涓昏绔犺妭锛?
1. 寮曡█
2. 鐩稿叧鎶€鏈垎鏋?3. 绯荤粺闇€姹傚垎鏋?4. 绯荤粺璁捐
5. 绯荤粺鏍稿績鍔熻兘瀹炵幇
6. 鎵嬪娍璇嗗埆鏈嶅姟瀹炵幇涓庡疄楠屽垎鏋?7. 鎬荤粨涓庡睍鏈?
姝ｆ枃婧愮爜鎺ㄨ崘閲囩敤鈥滀竴鍙ヨ瘽涓€琛屸€濈殑鏂瑰紡涔﹀啓銆侺aTeX 浼氬皢鍚屼竴娈靛唴鐨勬櫘閫氭崲琛岃涓虹┖鏍硷紝鍥犳 PDF 鎺掔増涓嶄細鍙楀埌褰卞搷锛屼絾婧愮爜鍙鎬у拰 Git diff 浼氭洿娓呮櫚銆?
## Word 鑽夌杩佺Щ瑙勫垯

杩佺Щ Word 鑽夌鏃堕伒寰互涓嬪師鍒欙細

- 浠?Word 鏂囨。鎴栧凡鎻愬彇鍒扮敾鏉跨殑鏍囧噯鏂囨湰涓轰緷鎹?- 鍏堣縼绉荤函鏂囨湰鍐呭
- 鍐嶅鐞嗚〃鏍?- 鍐嶅鐞嗗浘鐗?- 鏈€鍚庣粺涓€澶勭悊鍙傝€冩枃鐚紩鐢?- 姣忚縼绉讳竴绔狅紝鍏堢紪璇戞鏌ワ紝鍐嶅崟鐙彁浜?- 涓嶆妸 GMRL 鐩稿叧鍐呭杩佸叆鏈」鐩紝鏈鏂囦富棰樺彧浠?HearBridge / 鍚ˉ涓哄噯

鎺ㄨ崘鎻愪氦绮掑害锛?
- migrate abstract from Word draft
- migrate chapter 1 from Word draft
- migrate chapter 2 from Word draft
- migrate chapter 3 from Word draft
- migrate chapter 4 system design
- migrate chapter 5 system implementation
- migrate chapter 6 recognition service and experiments
- split long chapter files
- add diagrams and placeholder figures

## 鍥剧墖涓庡浘褰㈣鑼?
璁烘枃鍥惧舰鍒嗕负涓夌被锛?
1. TikZ / LaTeX 婧愮爜鍥?2. PNG / JPG / PDF 澶栭儴鍥剧墖
3. 鏅鸿兘鍗犱綅鍥?
TikZ 鍥炬簮鐮佺粺涓€鏀惧湪锛?
```text
diagrams/
```

澶栭儴鍥剧墖缁熶竴鏀惧湪锛?
```text
figures/
```

绗笁绔犲浘褰㈡簮鐮佷綅浜庯細

```text
diagrams/chapter03/
```

鍖呮嫭锛?
- `fig3-1-user-usecase.tex`
- `fig3-2-admin-usecase.tex`
- `fig3-3-user-flow.tex`
- `fig3-4-training-flow.tex`
- `fig3-5-sentence-video-flow.tex`

绗洓绔犲浘鐗囦綅浜庯細

```text
figures/chapter04/
```

绗簲绔犲浘鐗囦綅浜庯細

```text
figures/chapter05/
```

绗叚绔犲浘鐗囪祫婧愮洰褰曚綅浜庯細

```text
figures/chapter06/
```

褰撳墠绗叚绔犱娇鐢ㄦ櫤鑳藉崰浣嶅浘鏈哄埗銆傝嫢鐪熷疄鍥剧墖鏂囦欢涓嶅瓨鍦紝PDF 涓細鏄剧ず鍗犱綅妗嗭紱鍚庣画鍙渶瑕佸皢鐪熷疄鍥剧墖鏀惧埌瀵瑰簲璺緞骞堕噸鏂扮紪璇戯紝鍗冲彲鑷姩鏇挎崲鍗犱綅鍥俱€?
## 缁熶竴鍥剧墖鍛戒护

椤圭洰鍦?`main.tex` 涓皝瑁呬簡缁熶竴鎻掑浘鍛戒护銆?
### 鎻掑叆 TikZ / LaTeX 婧愮爜鍥?
榛樿鍐欐硶锛?
```tex
\WhuDiagramFigure{鍥炬簮鐮佽矾寰剗{鍥炬爣棰榼{鍥炬爣绛緘
```

绀轰緥锛?
```tex
\WhuDiagramFigure{diagrams/chapter03/sentence-video-flow.tex}{鍙ュ瓙瑙嗛璇嗗埆娴佺▼鍥緘{fig:sentence-video-flow}
```

鎸囧畾鏈€澶у搴﹀拰鏈€澶ч珮搴︼細

```tex
\WhuDiagramFigure[0.68\textwidth][0.55\textheight]{diagrams/chapter03/sentence-video-flow.tex}{鍙ュ瓙瑙嗛璇嗗埆娴佺▼鍥緘{fig:sentence-video-flow}
```

### 鎻掑叆 PNG / JPG / PDF 鍥剧墖

榛樿鍐欐硶锛?
```tex
\WhuImageFigure{鍥剧墖璺緞}{鍥炬爣棰榼{鍥炬爣绛緘
```

绀轰緥锛?
```tex
\WhuImageFigure{figures/chapter04/system-architecture.png}{绯荤粺鎬讳綋鏋舵瀯鍥緘{fig:chapter04-system-architecture}
```

鎸囧畾鏈€澶у搴﹀拰鏈€澶ч珮搴︼細

```tex
\WhuImageFigure[0.9\textwidth][0.6\textheight]{figures/chapter04/system-architecture.png}{绯荤粺鎬讳綋鏋舵瀯鍥緘{fig:chapter04-system-architecture}
```

### 鎻掑叆鏅鸿兘鍗犱綅鍥?
榛樿鍐欐硶锛?
```tex
\WhuAutoFigure{瀹藉害}{楂樺害}{鍥剧墖璺緞}{鍥炬爣棰榼{鍥炬爣绛緘
```

绀轰緥锛?
```tex
\WhuAutoFigure{0.82\textwidth}{0.42\textheight}{figures/chapter06/raw-dataset-flow.png}{鑷噰鏍锋湰閲囬泦娴佺▼鍥緘{fig:chapter06-raw-dataset-flow}
```

濡傛灉鍥剧墖瀛樺湪锛屼細鑷姩鎻掑叆鐪熷疄鍥剧墖锛涘鏋滃浘鐗囦笉瀛樺湪锛屼細鏄剧ず鍗犱綅妗嗐€?
## 绗叚绔犲崰浣嶅浘鐗囧懡鍚?
绗叚绔犲綋鍓嶉鐣欎互涓嬪浘鐗囨枃浠跺悕锛?
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

鍙鎶婄湡瀹炲浘鐗囨斁鍏ワ細

```text
figures/chapter06/
```

骞舵寜涓婅堪鏂囦欢鍚嶅懡鍚嶏紝閲嶆柊缂栬瘧鍚庡嵆鍙浛鎹㈠崰浣嶅浘銆?
## 鍥剧墖灏哄鎺у埗鍘熷垯

鎵€鏈夎鏂囧浘鐗囬粯璁ら渶瑕侀檺鍒舵渶澶у搴﹀拰鏈€澶ч珮搴︼紝閬垮厤绔栧悜娴佺▼鍥惧崰婊℃暣椤点€?
榛樿寤鸿锛?
- 鏅€氬浘锛氭渶澶у搴︿笉瓒呰繃 `0.86\textwidth`
- 鏅€氬浘锛氭渶澶ч珮搴︿笉瓒呰繃 `0.58\textheight`
- 鐗瑰埆瀹界殑鏋舵瀯鍥惧彲浠ラ€傚綋澧炲ぇ瀹藉害
- 鐗瑰埆楂樼殑娴佺▼鍥惧簲浼樺厛鍘嬬缉鑺傜偣鍜岄棿璺濓紝鍐嶈皟鏁存渶澶ч珮搴?
涓嶈鐩存帴鐢ㄥ緢澶х殑鎴浘濉炶繘璁烘枃銆傜敤渚嬪浘銆佹祦绋嬪浘銆佹灦鏋勫浘浼樺厛浣跨敤 TikZ銆丳lantUML銆丮ermaid 绛夋簮鐮佸寲鏂瑰紡缁存姢銆?
## 琛ㄦ牸瑙勮寖

鐢ㄤ緥瑙勭害銆侀渶姹傝〃銆佸疄楠岀粨鏋滆〃绛夎緝闀胯〃鏍间紭鍏堜娇鐢?`longtable`銆?
琛ㄦ牸瑕佹眰锛?
- 琛ㄩ鍦ㄨ〃涓婃柟
- 琛ㄦ牸鎸夌珷鑷姩缂栧彿
- 鎺ㄨ崘浣跨敤涓夌嚎琛?- 闀胯〃鍙互璺ㄩ〉
- 琛ㄦ牸鍐呭涓嶈瓒呭嚭椤甸潰杈圭晫
- 闀胯嫳鏂囧彉閲忓悕闇€瑕佸厑璁告柇琛?- 澶氬垪琛ㄦ牸搴旈€傚綋鍘嬬缉鍒楀锛屼笉瑕佸己琛屽婊℃暣椤?
褰撳墠椤圭洰宸插湪 `main.tex` 涓 `L/C/R` 琛ㄦ牸鍒楃被鍨嬪仛浜嗗叏灞€浼樺寲锛?
- 缂╁皬琛ㄦ牸鍒楅棿璺?- 鑷姩鎵ｉ櫎宸﹀彸鍒楅棿璺?- 鏀寔闀胯嫳鏂囦覆鍦ㄧ獎鍒椾腑鏂
- 鍑忓皯 `Overfull \hbox` 闂

## 鍙傝€冩枃鐚鍒?
褰撳墠杩佺Щ闃舵宸茬粡寮€濮嬩娇鐢?`biblatex` 鍜?`biber` 缁存姢鍙傝€冩枃鐚€?
鍚庣画璁″垝锛?
1. 妫€鏌ョ 1 鑷崇 6 绔犲紩鐢ㄦ槸鍚﹀畬鏁?2. 寤虹珛鎴栨洿鏂?`docs/citation-map.md`
3. 鏁寸悊 `refs/references.bib`
4. 灏嗘畫鐣欐墜鍐欑紪鍙锋浛鎹负 `\cite{}`
5. 浣跨敤 `biber` 鐢熸垚 GB/T 7714-2015 鏍煎紡鍙傝€冩枃鐚?
## 鏈湴鏂囦欢涓庡拷鐣ヨ鍒?
浠ヤ笅鍐呭涓嶆彁浜ゅ埌 Git锛?
- `.local-backups/`
- `.venv/`
- `build/`
- LaTeX 缂栬瘧缂撳瓨鏂囦欢
- 涓存椂鐩綍鏍戞枃浠?- 鏈湴澶囦唤鏂囦欢

甯歌涓嶆彁浜ゆ枃浠跺寘鎷細

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

## 娉ㄦ剰浜嬮」

- 涓嶆彁浜?`build/` 缂栬瘧浜х墿
- 涓嶇洿鎺ヤ慨鏀?`build/` 鍐呮枃浠?- 涓嶆彁浜?`.venv/`
- 涓嶆彁浜?`.local-backups/`
- 鍥剧墖缁熶竴鏀惧叆 `figures/`
- 鍥惧舰婧愮爜缁熶竴鏀惧叆 `diagrams/`
- 鍙傝€冩枃鐚粺涓€缁存姢鍦?`refs/references.bib`
- Word 鍘熺鍜屾簮鏉愭枡鏀惧叆 `source-docs/`
- 鏍煎紡妫€鏌ラ」瑙?`docs/format-checklist.md`
- 姣忔澶ф敼鍓嶅厛纭 `git status`
- 姣忔杩佺Щ涓€绔犲悗鍏堢紪璇戯紝鍐嶆彁浜?
## 甯哥敤鍛戒护

鏌ョ湅褰撳墠鐘舵€侊細

```powershell
git status
```

鏌ョ湅绠€鐣ョ姸鎬侊細

```powershell
git status --short
```

鎵嬪姩瀹屾暣缂栬瘧锛?
```powershell
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex
```

鎵撳紑 PDF锛?
```powershell
Start-Process .\main.pdf
```

娓呯悊甯歌 LaTeX 缂栬瘧浜х墿锛?
```powershell
Remove-Item *.aux,*.bbl,*.bcf,*.blg,*.log,*.out,*.run.xml,*.toc,*.xdv,*.synctex.gz -ErrorAction SilentlyContinue
```

鎻愪氦褰撳墠淇敼锛?
```powershell
git add .
git commit -m "update message"
git push
```
