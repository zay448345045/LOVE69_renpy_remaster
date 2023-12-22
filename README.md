本分支对最新版 Ren'Py 8.0.0 进行适配

欢迎来到 dev-renpy8.0.0 分支，任何的新PR请提交至本分支

注意：请不要改动 `options.rpy` 中的 Build 时间 （即“（Build 20231222）”）程序会根据当前构建时间自动替换

## ChangeLog

> 基于：正式版 1.0 （Build 20220428）

### 2022-05-01

- 创建 dev 分支
- 编写&完善夜间自动构建&测试脚本

### 2022-05-03

- 加入吐槽模式的开关（2022年5月19日该功能全部开发完成）

### 2022-05-07

> 修复了 [#19](https://github.com/luckykeeper/LOVE69_renpy_remaster/issues/19) 的问题

- 修复了在STAFF表播放过程中返回菜单会把 STAFF 的 BGM 带回主菜单的问题
- 修复了在播放 staff 表时读档回到选项前再次选择播放 staff 表，会导致 staff 表卡在某一帧不动的问题

### 2022-05-09

- 更新 Scene06 脚本，添加一处梗的解释（真冬哼的一句歌，德沃夏克-自新大陆交响曲），感谢B站[@**Karma_0xCC**](https://space.bilibili.com/12020130)

### 2022-05-18

- 修复 Extra-Music 中 01_heartbeat 的按钮重复写了两次的问题（Ver1.0 中，这个问题不会造成任何 bug ，但是这个问题会导致代码冗余），修复情况见 screens.rpy#L2669 ，[本次提交详情](https://github.com/luckykeeper/LOVE69_renpy_remaster/commit/da8c40d2eb6d9a7d0d6c30e3978c34ad73c48092?diff=split)

### 2022-05-19

- 调整了 Scene19 中的一句的语序，修正了一处拼写错误，详见[提交8d33e290c6bec551b4dfd46a5c4e48a322dbb1a8](https://github.com/luckykeeper/LOVE69_renpy_remaster/commit/8d33e290c6bec551b4dfd46a5c4e48a322dbb1a8)
- 修正了 Scene20 中的一处拼写问题，详见[提交b0e930aad4b67aa6df3132745dcede1f5e307374](https://github.com/luckykeeper/LOVE69_renpy_remaster/commit/b0e930aad4b67aa6df3132745dcede1f5e307374)
- 完成“吐槽可关闭”的功能，吐槽模式可选（全部开启/仅保留梗/全部关闭），见 [#11](https://github.com/luckykeeper/LOVE69_renpy_remaster/issues/11)

### 2022-06-12

- 迁移脚本至 Ren'Py 8.0.0，通过性测试完成
- 完成可变标题的功能实现，程序标题可以在运行中变动
- 优化了部分文本的展示方式
- 移除了32位系统的支持（Ren'Py 8.0.0 特性）

### 2022-06-25

- 完成了可变标题的制作（读档时改变标题的功能暂时没有实现）
- 完成BGM名称推送的功能实现及制作

### 2023-12-22

- 根据知乎[@被诅咒的章鱼](https://zhuanlan.zhihu.com/p/362449324)大佬指点，修复了 STAFF 播放时没有同步更新 SquenceAnimator 和 SquenceAnimator2 类的 show_timebase 成员变量的问题，感谢大佬
