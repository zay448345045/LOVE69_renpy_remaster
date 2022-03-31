# --------------------------------
# LOVE69_Renpy_Remaster_Project
# scene08 的脚本（剧本）
# Author:Luckykeeper
# 部分句子翻译协助：
# 版本 0.8 "LuckyDev"
# Blog：http://luckykeeper.site
# 项目组网站：https://love69renpyremasterproject.github.io/
# 项目开源地址：https://github.com/luckykeeper/LOVE69_renpy_remaster
# 修订日期 2022年3月31日

# 当前流程：编写脚本AIO Process

label scene08:
    # scene08 开始

    # scene08 场景1 【时隔许久的心爱夜访】 开始

    # 地点：葛城家玄关
    # 人物：心爱  莲
    # BGM：无

    scene black with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)
    scene 玄関_夜 at love69_bg1440 with ImageDissolve("images/tr/ysr006.png", 0.8, ramplen=64, reverse=False, alpha=True, time_warp=None)

    # 显示 quick_menu
    $ quick_menu = True

    # 心爱 「ぶえええええ、あっぶねー！」
    ## 没有跳过
    show 心愛_制服_基本_ポカーン at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0850.ogg"
    ai 心愛_制服_基本_ポカーン "呜欸欸欸欸欸，好险啊——！"

    # 莲 「夜襲とは洒落た真似を…」
    lian "把夜袭说的这么惊险..."

    # 心爱 「ぜぇー…はぁー…危うくビショビショになる所でした」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0851.ogg"
    ai 心愛_制服_基本_泣き "呼啊——……呼啊——……差点吓死我了"
    hide 心愛_制服_基本_ポカーン

    # 莲 「間一髪と。新品のＴシャツとお土産のケーキを濡らすなんてかっこつかねーしな」
    lian "千钧一发呢，要是把新T恤和特产蛋糕弄湿了可就不酷了"

    # nil 「心愛との帰宅途中、ゲリラ豪雨第二波を受けて、二人して全力ダッシュでスライディング帰宅を決める。」
    "在与心爱一起回家的路上，受到了游击队暴雨的第二波袭击，于是两个人决定全力冲刺滑行回家"

    # 莲 「しっかし、お前足はやくね？　普通に俺より早かったんだけど」
    lian "可是说起来，你走得可真是快啊，一般来说应该是我快一些吧"

    # 心爱 「三連ヘアピンで溝に落としたまでさ」
    # 参考资料：http://k.sina.com.cn/article_1906385094_m71a120c603300tinz.html
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0852.ogg"
    ai 心愛_制服_基本_真顔 "在三连发夹弯掉到沟里了（L:三连发夹弯就是那种几个180°弯组合起来的大急弯，具体百度一下就能知道）"
    hide 心愛_制服_基本_泣き

    # 莲 「豆腐屋のダウンヒルかよ」
    lian "是豆腐店的下坡吗"

    # nil 「心愛が何でもできる事は知っていたが、運動神経も良いとは…。」
    "虽然知道心爱什么都做得到，但没想到他还有运动神经……"

    # nil 「男としてのプライドが揺るぎます。」
    "作为男人的自尊心动摇了"

    # 心爱 「そういえば、まふまふちゃんの部屋電気ついてたね。起きてるのかな」
    voice "voice/心愛/cca_a1_0853.ogg"
    ai 心愛_制服_基本_真顔 "说起来，嘛呼嘛呼酱的房间开着灯呢。是不是起来了？"

    # 莲 「よく見てたなそんな所まで」
    lian "你怎么能在这就能看到的"

    # 心爱 「まっふゆちゃーん！　お前の好きな心愛ちゃんをかってきたぞー！」
    show 心愛_制服_基本_にっこり at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0854.ogg"
    ai 心愛_制服_基本_にっこり "嘛呼哟酱——！我给你带来了你最喜欢的心爱酱哦！"
    hide 心愛_制服_基本_真顔

    # 莲 「そのフレーズどっかで聞いたことあるな」
    lian "我总感觉这句话好像在哪听过"

    # 心爱 「君がいったんでしょう…」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0855.ogg"
    ai 心愛_制服_基本_泣き "是你之前说过的吧……"
    hide 心愛_制服_基本_にっこり

    # 莲 「そうでした」
    lian "那就是这样的了"

    # nil 「心愛は玄関で叫ぶが、返事はない。」
    "心爱在玄关这里大喊，但却没有回应"

    # nil 「聞こえてないのか…。」
    "是没有听见吗…"

    # 莲 「見てくるわ」
    lian "我去康康"

    # 心爱 「あ、じゃぁ私シャワー借りてい？　汗かいてもうたけん」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0856.ogg"
    ai 心愛_制服_基本_嬉しい "啊，那我可以借用一下淋浴吗？出了不少汗呢"
    hide 心愛_制服_基本_泣き

    # 莲 「あいよ。下着は適当に真冬の使って。部屋からとってくるから」
    lian "嗯嗯，内衣就随便找件真冬的穿就行，我去房间那儿拿来"

    # 心爱 「残念ながら、サイズが合わないんだな。ていうか、まふまふちゃんの下着の場所知ってるんだね…」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0857.ogg"
    ai 心愛_制服_基本_真顔 "有点遗憾，尺寸不大合适啊。话说回来，你知道真冬酱的内衣位置吧…"
    hide 心愛_制服_基本_嬉しい

    # 莲 「そりゃ知ってますよ。我が家の洗濯大臣ですから」
    lian "这个我知道，因为我是我们家的洗衣大臣"

    # 心爱 「じゃーあー、真冬ちゃんに『今日はこの下着を着けろ』とか、やるの？」
    voice "voice/心愛/cca_a1_0858.ogg"
    ai 心愛_制服_基本_真顔 "那—么——，要和真冬酱说『今天我就穿这件内衣』吗？"

    # 莲 「やられたことならある」
    lian "我已经有了这样的经历"

    # 心爱 「い、いなぁ…私も蓮君をコーディネートしたい。私色に染めたいな…」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0859.ogg"
    ai 心愛_制服_基本_泣き "真、真好啊……我也想让莲君穿我的衣服，染上我的颜色呢"
    hide 心愛_制服_基本_真顔

    # 莲 「我ながらピンク色のスーツは似合わないと思うんだ」
    lian "我觉得粉红色的衣服不适合我"

    # 心爱 「人のセンスをなんだと思ってるんだね」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0860.ogg"
    ai 心愛_制服_基本_真顔 "你认为别人的品味是什么样的呢？"
    hide 心愛_制服_基本_泣き

    # nil 「とりあえず、家にあがって心愛を家にあげる。」
    "总之，先把心爱送过去"

    # nil 「勝手知ったるは人の家。心愛はまっすぐに風呂場へと向かう。」
    "因为比较熟悉这里，心爱直奔浴室"

    # 心爱 「ほーい。じゃぁ、ちゃちゃちゃっと浴びさせてもらいまーす」
    show 心愛_制服_基本_笑顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0861.ogg"
    ai 心愛_制服_基本_笑顔 "真是的——那么，让我好好地洗一下吧"
    hide 心愛_制服_基本_真顔

    # 莲 「シャンプーの容器にリンス入ってるから気をつけてな」ピンク色のスーツは似合わないと思うんだ」
    lian "洗发水的瓶子里装了护发素，请注意哦"

    # 心爱 「はーい♪」
    show 心愛_制服_基本_にっこり at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0862.ogg"
    ai 心愛_制服_基本_にっこり "好——♪"
    hide 心愛_制服_基本_笑顔

    # nil 「心愛は脱衣所のドアをあけて、風呂場へと入っていった。」
    "心爱打开更衣室的门，走进了浴室"

    # nil 「が、出てきた。」
    "马上，又出来了"

    # 心爱 「のぞかないでね？」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0863.ogg"
    ai 心愛_制服_基本_嬉しい "不要偷看哦？"
    hide 心愛_制服_基本_にっこり

    # nil 「お邪魔するのは？」
    "那么，我就打扰了？"

    # 心爱 「っ…！　きょ、今日はだめ！」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0864.ogg"
    ai 心愛_制服_基本_不機嫌 "今、今天不行！"
    hide 心愛_制服_基本_嬉しい

    # 莲 「今日は？　まぁいや、じゃぁ真冬の様子見たら部屋いるわ」
    lian "今天？好吧，那我去房间里面康康真冬的情况"

    # nil 「心愛が脱衣所に入ったのを確認して、廊下の電気を落とした。」
    "确认了心爱进入更衣室后，把走廊的灯关掉了"

    # nil 「冷蔵庫にお土産をしまってから、寝ているかもしれないので、忍び足で階段を登る。」
    "把特产蛋糕放进冰箱后，考虑到真冬可能已经睡着了，所以悄悄地爬上楼梯"

    image bg 自宅二階廊下_夜 = "images/bg/自宅二階廊下_夜.png"
    scene 自宅二階廊下_夜 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「真冬の部屋の扉をノック。」
    "轻敲真冬房间的门"

    # 敲门声
    play sound "voice/effect/04_ドア～ノックする3.ogg"

    # 莲 「真冬」
    lian "真冬"

    # nil 「……」
    "……"

    # nil 「返事はない。」
    "没有回答"

    # nil 「もう一度。」
    "再敲一次"

    # 敲门声
    play sound "voice/effect/04_ドア～ノックする3.ogg"

    # nil 「……」
    "……"

    # nil 「やはり返事はない。」
    "还是没有回答"

    # 莲 「入るぞ」
    lian "进来了啊"

    # 场景切换到真冬房间
    image bg 真冬部屋_夜 = "images/bg/真冬部屋_夜.png"
    scene 真冬部屋_夜 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # nil 「ガチャッ」
    "喀嚓"

    # 莲 「……」
    lian "……"

    # 这个语句是针对真冬设计的参数，能够调整真冬在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.08
    $ sideimagesize.SideImageYalign = -29.35
    $ sideimagesize.SideImageZoom = 0.95

    # 真冬 「すー…すー…」
    ## 没有跳过
    voice "voice/真冬/maf_a1_0773.ogg"
    dong 真冬_制服_基本_目閉じ "呼——……呼——……"

    # 莲 「やれやれ」
    lian "啊啦啊啦"

    # nil 「真冬は、電気をつけたま、ベッドに俯せで眠っていた。」
    "真冬开着灯趴在床上睡着了"

    # nil 「枕の上には、開きっぱなしの「妹マニュアル」が乗せられていたし、」
    "枕头上放着打开着的「妹妹手册」（L:就是开场提到的『有哥哥的妹妹指南』啦~）"

    # nil 「布団はかけられておらず、おなかが出てしまっている。」
    "没盖被子，肚子都露出来了"

    # nil 「あらかた、ゴロゴロしながら本を読んでいたらそのま寝てしまったというところだろう。」
    "大概是，在床上无所事事地看书，然后就睡着了吧"

    # 莲 「ていうか窓あいてんじゃん、吹き込んでるわ…」
    lian "话说窗户还开着呢，风都吹进来了…"

    # nil 「きっと雨上がりの冷たい空気が心地よかったのだろう。」
    "（夏天）雨后的冷空气一定很舒服吧"

    # nil 「ベッド脇の窓が開いており、今降り注いでる豪雨が、横殴りに吹き込みはじめている。」
    "床边的窗户开着，刚才倾注下来的暴雨，开始横扫而入"

    # nil 「俺は、真冬の身体を上からまたぐようにして、背中をのばし、窓を閉めた。」
    "我从上面跨过真冬的身体，挺直背，关上了窗户"

    # nil 「スマートフォンは充電ケーブルにさっておらず、常駐させているチャットツールのせいで無駄に電池を食ってしまっているようだ。」
    "智能手机（Smart Phone）没有在充电，而且似乎因为聊天工具在前台常驻的正在无端浪费电力"

    # nil 「ベッド脇の電源からコードを引っ張り出して、真冬の手元に無造作におかれているスマートフォンにケーブルを繋ぐ。」
    "从床边的电源上抽出充电线，连接到真冬随意放在边上的智能手机的充电口"

    # 真冬 「すー…すー…」
    voice "voice/真冬/maf_a1_0774.ogg"
    dong 真冬_制服_基本_目閉じ "呼——……呼——……"

    # nil 「真冬を起こそうと思ったが、あまりに静かに心地よさそうに寝ているので、こは起こさないように気を遣うべきだろう。」
    "我本来想叫醒真冬，但是她睡得太安静，太舒服了，所以我小心注意，没有吵醒她"

    # 莲 「おなか冷えちゃいますよ、真冬ちゃん」
    lian "肚子会着凉的哦，真冬酱"

    # nil 「俺はそう囁きかけながら、足下に折りたまれていた掛け布団を真冬の身体にそっとかける。」
    "我一边低声说着，一边将把折叠在脚下的被子轻轻地盖在真冬的身体上"

    # 真冬 「ん…すぅ…」
    voice "voice/真冬/maf_a1_0775.ogg"
    dong 真冬_制服_基本_目閉じ "嗯…嗯…"

    # nil 「起こしてしまったかな？　と不安になりながらも、ゆっくりと布団から手を離す。」
    "我吵醒你了吗？虽然有些不安，但还是慢慢地把手从被子上拿开"

    # 莲 「しっかし…この本…」
    lian "但是……这本书……"

    # nil 「真冬は俺に、断固としてこの本を読ませてはくれなかった。ちょっとだけ誘惑にかられる。」
    "因为真冬坚决不让我读这本书，所以很想康康写了什么"

    # 莲 「が、世の中しらん事があったほうが楽しいってね…」
    lian "但是，世上有些事情不知道的话会更开心呢…"

    # nil 「誘惑に打ち勝った俺は、真冬の机の上からメモ用紙を一枚拝借して、」
    "战胜了诱惑的我，从真冬的桌子上借了一张纸条"

    # nil 「ちょっとしたメッセージを書いて、しおり代わりに開いていたページに挟んで本を閉じて、枕の脇においた。」
    "我写了一条留言，代替书签夹在刚打开的那页上，合上书放在枕头旁边"

    # nil 「これで、とりあえず真冬がぐっすり寝てしまっても風邪を引いたり、本に激突してイターイってなる事もないだろう。」
    "这样一来，即使真冬睡得很香，也不会感冒，或者撞到书本的尖角了吧"

    # 真冬 「すぅ…ん…おにいちゃ…すう…」
    voice "voice/真冬/maf_a1_0776.ogg"
    dong 真冬_制服_基本_目閉じ "呜…嗯…欧尼酱…呜…"

    # 莲 「ん？　寝言か？」
    lian "嗯？是在说梦话吗？"

    # 真冬 「すぅ…ありがと…すぅ…」
    voice "voice/真冬/maf_a1_0777.ogg"
    dong 真冬_制服_基本_目閉じ "呼…谢谢…嗯…"

    # 莲 「夢の中でお礼を言われるとはな…」
    lian "没想到你在梦里感谢我……"

    # nil 「気のせいかもしれないが、真冬の寝顔が少しだけほえんだように見えた。」
    "也许是心理作用，真冬的睡脸上似乎露出了一丝微笑"

    # nil 「俺は電気のスイッチを押して、真冬の部屋の電気を落とした。」
    "我按下电灯开关，关掉了真冬房间里的照明"

    # 莲 「おやすみ、真冬」
    lian "晚安，真冬"

    # 真冬 「すぅ…おやすみ…すぅ…」
    voice "voice/真冬/maf_a1_0778.ogg"
    dong 真冬_制服_基本_目閉じ "嗯……晚安…呼…"

    # 画面切换回葛城家二楼走廊
    # BGM起：Slide the Way
    scene 自宅二階廊下_夜 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)
    play music bgmthirtysix fadein 4.0

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「ふい～…まさか、シャンプーの入れ物にリンスが入ってるとは…」
    #（原作少了右半括号捏）
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0865.ogg"
    ai 心愛_制服_基本_不機嫌 "呜欸欸~……怎么说呢，没想到洗发水的瓶子里面竟然装了护发素……"

    # 莲 「だから言ったじゃねぇか…」
    lian "所以我不是说过了嘛…"

    # 心爱 「お？　ジャストタイミング？」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0866.ogg"
    ai 心愛_制服_基本_嬉しい "哦？Just Timing吗？"
    hide 心愛_制服_基本_不機嫌

    # nil 「俺が真冬の部屋から出ると、ちょうど、俺の部屋に入るために階段を登る心愛に鉢合わせした。」
    "我从真冬的房间出来的时候，正好撞见了为了进入我的房间而正在爬楼梯的心爱"

    # 莲 「しーっ…お姫様はぐっすりの様子でしたよ」
    lian "嘘…公主看起来睡得很香甜捏"

    # 心爱 「あ、じゃぁ、こで立ち話もあれだね…」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0867.ogg"
    ai 心愛_制服_基本_泣き "啊，那，在这里站着说话也是有点那个…"
    hide 心愛_制服_基本_嬉しい

    # nil 「不必要にひそひそ声になりながら、俺はゆっくりと自分の部屋の扉を開けて、心愛を招き入れた。」
    "在不必要的窃窃私语中，我慢慢地打开自己的房门，把心爱请了进来"

    # 场景切换：葛城家二楼走廊->莲房间
    # BGM不变

    scene 自室a_夜 at love69_bg1440 with ImageDissolve("images/tr/trans01.png", 1.5, ramplen=8, reverse=True, alpha=True, time_warp=None)

    # 心爱 「おじゃましまーす。おーこが蓮くんの部屋かぁ～！」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0868.ogg"
    ai 心愛_制服_基本_嬉しい "打扰了，哦——！这里就是莲君的房间啊~！"

    # 莲 「この間も来たじゃないか」
    lian "前几天你不是也来过嘛"

    # 心爱 「エロ本はどこにかくしてあるんだい、正直に答えよ」
    show 心愛_制服_基本_ジト目 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0869.ogg"
    ai 心愛_制服_基本_ジト目 "小黄书到底藏在哪里了？快点老实答来！"
    hide 心愛_制服_基本_嬉しい

    # 莲 「机の小物入れにぶっさってるＵＳＢメモリの中だ」
    lian "在桌子上面的杂物盒里装的ＵＳＢ存储器里"

    # 心爱 「正直かよぉ」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0870.ogg"
    ai 心愛_制服_基本_真顔 "真的吗？！"
    hide 心愛_制服_基本_ジト目

    # 莲 「だって正直にっつったじゃねぇか」
    lian "你不是让我老实说的嘛"

    # 心爱 「と、ツッコミながらも興味津々に手を伸ばす私」
    voice "voice/心愛/cca_a1_0871.ogg"
    ai 心愛_制服_基本_真顔 "一边吐槽一边兴致勃勃伸出手的我！"

    # 心爱 「そして早速パソコンに差し込んで電源を押す私」
    voice "voice/心愛/cca_a1_0872.ogg"
    ai 心愛_制服_基本_真顔 "然后马上插进电脑按电源的我！"

    # 心爱 「起動を座して待つ私」
    voice "voice/心愛/cca_a1_0873.ogg"
    ai 心愛_制服_基本_真顔 "坐着等启动的我！"

    # 莲 「ちょっとウキウキしてるだろ」
    lian "你看起来超兴奋的欸"

    # 心爱 「ウキウキしすぎてカーニバル寸前だよ…」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0874.ogg"
    ai 心愛_制服_基本_嬉しい "太兴奋了，要过狂欢节啦……"
    hide 心愛_制服_基本_真顔

    # nil 「心愛は楽しそうに身体上下に揺らしながら、ワイヤレスマウスを手のひらで踊らせた。」
    "心爱快乐地在身体上下摇晃着，让无线鼠标在手掌上跳舞"

    # nil 「ちなみに、心愛、そいつはダミーだ。残念だったな。」
    "顺带一提，心爱，那是个假的，真遗憾啊"

    # 心爱 「完全に立ち上がる前にマイコンピューターをダブルクリックして、リムーバブルディスクのアイコンを連打する私」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0875.ogg"
    ai 心愛_制服_基本_真顔 "在电脑完全启动之前双击我的电脑，连击可移动磁盘图标的我！"
    hide 心愛_制服_基本_嬉しい

    # 心爱 「画像ドットジェーピージーのアイコンを連打する私」
    voice "voice/心愛/cca_a1_0876.ogg"
    ai 心愛_制服_基本_真顔 "连击jpg文件图标打开图片的我！"

    # 心爱 「…」
    show 心愛_制服_基本_驚き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0877.ogg"
    ai 心愛_制服_基本_驚き "……"
    hide 心愛_制服_基本_真顔

    # 心爱 「…れ、蓮くん」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0878.ogg"
    ai 心愛_制服_基本_泣き "…呃，莲君"
    hide 心愛_制服_基本_驚き

    # 莲 「おう、どうしたんだい心愛君」
    lian "哦，怎么了，心爱君"

    # 心爱 「猫と犬の写真でその…するんだ…。そっか…ご、ごめんね…」
    voice "voice/心愛/cca_a1_0879.ogg"
    ai 心愛_制服_基本_泣き "用猫和狗的照片做那个……这样啊…那个，对、对不起……"

    # 莲 「マジに受けとんなよ！　普通に考えてダミーだろ！」
    lian "不要真的那么想啊！普通地想想这都是假的吧！"

    # 心爱 「第一なんでダミーのＵＳＢなんて用意してるんだよぉ！」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0880.ogg"
    ai 心愛_制服_基本_不機嫌 "首先，为什么要准备一个假的ＵＳＢ啊！"
    hide 心愛_制服_基本_泣き

    # 莲 「真冬対策だ。　ちなみに、まだあいつも俺のエロ本の隠し場所は探し当てられてない。残念だったな」
    lian "这是真冬对策。顺带一提，这家伙到现在还是没能找到我藏书的地方，真是遗憾呢"

    # 心爱 「むっきー！　じゃぁ今夜は徹底的にハードディスクの中を探しちゃるきに、覚悟しんさい！」
    voice "voice/心愛/cca_a1_0881.ogg"
    ai 心愛_制服_基本_不機嫌 "可恶——！那今晚就彻底搜查Hard Disk吧！做好觉悟吧！"

    # 莲 「そ、それだけはやめろ！」
    lian "别，别这样！"

    # 心爱 「えいマウスはわたさん！」
    voice "voice/心愛/cca_a1_0882.ogg"
    ai 心愛_制服_基本_不機嫌 "欸——！可别想拿到鼠标！"

    # 莲 「俺は心愛の手の中のマウスをひったくろうと、腕を伸ばす。」
    lian "我伸出手臂想要夺取心爱手中的鼠标"

    # nil 「しかし、心愛は椅子を回転させて身を翻し、その反動を利用して立ち上がった。」
    "但是，心爱却转动着椅子翻身，利用它的反作用力站了起来"

    # 心爱 「はどこをみている！　私はこだ！」
    show 心愛_制服_基本_笑顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0883.ogg"
    ai 心愛_制服_基本_笑顔 "哈哈哈！你这看哪儿呢！我在这儿呢！"
    hide 心愛_制服_基本_不機嫌

    # 莲 「させるか！」
    lian "怎能让你得逞！"

    # 心爱 「ぶへぇっ」
    show 心愛_制服_基本_ポカーン at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0884.ogg"
    ai 心愛_制服_基本_ポカーン "咕欸！"
    hide 心愛_制服_基本_笑顔

    # nil 「俺の右足が、心愛の足首をとらえる。」
    "我的右脚勾住了心爱的脚踝"

    # nil 「心愛の身体はバランスを大きく崩して、ベッドへとダイブした。」
    "心爱的身体失去了平衡，倒在了床上"

    # nil 「ボフッと音を立て、心愛は正面からベッドに墜落した。」
    "啪嗒一声，心爱正面朝上落在了床上"

    # 心爱 「……」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0885.ogg"
    ai 心愛_制服_基本_真顔 "……"
    hide 心愛_制服_基本_ポカーン

    # 莲 「さて、マウスを返して貰おう。ついでにもうパソコンの電源は落とした」
    lian "好了，把鼠标还给我。顺带一提，电脑的电源已经关掉了"

    # 心爱 「……」
    voice "voice/心愛/cca_a1_0886.ogg"
    ai 心愛_制服_基本_真顔 "……"

    # nil 「心愛は素直にマウスを返してはくれたが、しばらく俯せのま硬直している。」
    "虽然心爱老老实实地把鼠标还给了我，但还是低着头僵直了一会儿"

    # 心爱 「くんくん…くんくん…」
    show 心愛_制服_基本_もぐもぐ at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0887.ogg"
    ai 心愛_制服_基本_もぐもぐ "嗅嗅……嗅嗅……"
    hide 心愛_制服_基本_真顔

    # 莲 「何をやっているのだね君は」
    lian "你在干什么呢？"

    # 心爱 「くんくん…蓮くんのにおいがする…」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0888.ogg"
    ai 心愛_制服_基本_嬉しい "嗅嗅……有莲的味道……"
    hide 心愛_制服_基本_もぐもぐ

    # 莲 「枕を嗅ぐなよ恥ずかしいな！」
    lian "别闻枕头，好害羞啊！"

    # 心爱 「いじゃないかよー幼馴染みを足払いでベッドにぶっ倒しやがったんだからさ！…まったく、ロマンもへったくれもないんだから…」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0889.ogg"
    ai 心愛_制服_基本_不機嫌 "有什么不好的嘛——用脚把幼驯染绊倒在床上的！……真是的，一点浪漫也没有……"
    hide 心愛_制服_基本_嬉しい

    # 莲 「何にロマンを感じてるんだよ」
    lian "那你觉得什么浪漫呢？"

    # 心爱 「鈍感さん」
    voice "voice/心愛/cca_a1_0890.ogg"
    ai 心愛_制服_基本_不機嫌 "迟钝先生"

    # nil 「心愛はぴょこっと身体を起こすと、ベッドに座った。」
    "心爱一下子抬起了身子，坐在了床上"

    # 心爱 「雨、止まないね」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0891.ogg"
    ai 心愛_制服_基本_泣き "雨下个不停啊"
    hide 心愛_制服_基本_不機嫌

    # nil 「窓の向うでは、しきりに雨が降り注いでいる。ていうか、風も強い。」
    "窗外不停地下着雨，而且风也很大"

    # nil 「雨を見つめるその物憂げな表情に、少しの切なさと色気を感じてしまい、ドキドキする。」
    "从她凝视着雨水的忧郁表情中，我感受到了一丝的悲伤和性感，心跳不已"

    # 莲 「天気予報やってねぇかな」
    lian "天气预报还没开始播吗？"

    # nil 「俺はこの空気を紛らわすために、部屋においてあるテレビをつける。」
    "我为了排解这种气氛，打开了房间里的电视"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # TV  「『はい！　こっちはすごい風と雨でーす！　気を抜いたら倒れてしまいそうなくらいです！』」
    # 这里的TV是里昂，需要注意坐下小人物框的位置以及音声的位置捏
    # 467-983 跳过
    voice "voice/リオン/ron_a1_0984.ogg"
    tv リオン_私服_基本_ジト目 "『是的！这里风雨交加！简直是一不小心就会倒下的程度！』"

    # 莲 「あ、リオンだ。何やってんだこの人」
    lian "哟，这不是里昂嘛，她搁这儿干啥子呢"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「およ？　知り合い？」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0892.ogg"
    ai 心愛_制服_基本_真顔 "哦哟？认识吗？"
    hide 心愛_制服_基本_泣き

    # 莲 「ちょっとした友達」
    lian "只是朋友罢了"

    # 这个语句是针对里昂设计的参数，能够调整里昂在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.09
    $ sideimagesize.SideImageYalign = -7.32
    $ sideimagesize.SideImageZoom = 1.0

    # TV  「『この辺一体に大雨・洪水・暴風警報がでてますんで！　住民の皆さんは家からでないようにおねがいしまあす！　ていうか私も家に帰らせてくださーい！』」
    # 这里的TV是里昂，需要注意坐下小人物框的位置以及音声的位置捏
    voice "voice/リオン/ron_a1_0985.ogg"
    tv リオン_私服_基本_ジト目 "『这附近到处都有暴雨・洪水・风暴警报！居民们请千万不要从家里出来！总之让我也回家吧！』"

    # 这个语句是针对心爱设计的参数，能够调整心爱在对话框里面的位置
    $ sideimagesize.SideImageXalign = 0.10
    $ sideimagesize.SideImageYalign = 15.72
    $ sideimagesize.SideImageZoom = 0.96

    # 心爱 「半泣きのビショビショじゃん」
    voice "voice/心愛/cca_a1_0893.ogg"
    ai 心愛_制服_基本_真顔 "这不是哭的很厉害吗"

    # 莲 「可哀想だな…」
    lian "真可怜啊…"

    # nil 「ピッ。」
    "哔——"

    # 莲 「とりあえず、外に出ちゃいけない事はわかった」
    lian "总之，这会儿就不能出去了"

    # 心爱 「はぁうー…これじゃ帰れないなー」
    voice "voice/心愛/cca_a1_0894.ogg"
    ai 心愛_制服_基本_真顔 "哈呜——……这样的话就回不去了呢"

    # nil 「心愛は俺と目線を合わせずに、天井の照明を眺めながらつぶやいた。」
    "心爱没有和我四目相对，看着天花板上的灯光喃喃自语"

    # 莲 「…そう…だな…」
    lian "…是啊……"

    # 心爱 「…ていうか座らないの？」
    show 心愛_制服_基本_驚き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0895.ogg"
    ai 心愛_制服_基本_驚き "……话说你不坐下嘛？"
    hide 心愛_制服_基本_真顔 at love69_xinai_center with dissolve

    # 莲 「なんとなく、心愛の考えはわかっていた。」
    lian "总感觉，我知道了心爱的想法"

    # nil 「心愛の顔は笑顔ではなく、限りなく無表情に近いものだった」
    "心爱的脸上没有笑容，而是无限接近无表情的表情"

    # 莲 「なぁ、心愛…俺は…」
    lian "呐，心爱……我……"

    # 心爱 「うー？」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0896.ogg"
    ai 心愛_制服_基本_真顔 "哦——？"
    hide 心愛_制服_基本_驚き

    # 莲 「いや…」
    lian "没什么……"

    # nil 「果たして、今の俺に、心愛を求める資格があるのだろうか。」
    "说到底，现在的我，还有资格追求心爱吗"

    # nil 「以前の時とは違い、俺はすでに真冬とも身体を重ねてしまっている。」
    "和之前的时候不同，现在的我已经和真冬的身体重合过了"

    # nil 「それを心愛は知らずに、きっと、前と同じように求めてくれているのだろう。」
    "并不知道这一点的心爱，肯定还是和以前一样追求着我吧"

    # nil 「ましてや、今日は例のアイスで発情してるとかではなく、」
    "更不用说，今天还不是用那个冰淇淋发情的"

    # nil 「平常心の心愛だ。」
    "这是平常心的心爱"

    # nil 「でも、雨は当分止みそうにないし、こで心愛を拒んでしまったら、それはきっと心愛にとっても辛い事だろうし、気まずくなってしまう事も目に見えている。」
    "但是，雨似乎一时半会儿不会停下来，如果在这里拒绝了心爱，这对心爱来说一定是很痛苦的事情，也会让两个人非常尴尬"

    # nil 「俺は、どうすればいんだろうか。」
    "我该怎么办呢"

    # 心爱 「……」
    voice "voice/心愛/cca_a1_0897.ogg"
    ai 心愛_制服_基本_真顔 "……"

    # 心爱 「くすっ」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0898.ogg"
    ai 心愛_制服_基本_嬉しい "嘿嘿"
    hide 心愛_制服_基本_真顔

    # nil 「俺の事を真顔で見つめていた心愛から、小さな笑いがこぼれた。」
    "看见一脸严肃表情的我，心爱露出了小小的笑容"

    # 莲 「ど、どうしたんだよ」
    lian "怎、怎么了？"

    # 心爱 「あー…いや、色々考えていらっしゃるなーと思いましてね」
    voice "voice/心愛/cca_a1_0899.ogg"
    ai 心愛_制服_基本_嬉しい "啊……没什么，我只是觉得你在考虑各种各样的事情呢"

    # 莲 「そんなことは…いや、バレバレか…」
    lian "没有那种事…不，暴露了呢…"

    # 心爱 「うん。だって、一回してるのに、こまで悩むなんておかしい話でしょ？」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0900.ogg"
    ai 心愛_制服_基本_真顔 "嗯。可是，明明都已经做过一次了，还这么烦恼，不是很奇怪吗？"
    hide 心愛_制服_基本_嬉しい

    # 莲 「いやまぁ…なんだ、前は…その…」
    lian "不，不是，之前是…那个…"

    # 心爱 「アレだよ蓮くん」
    voice "voice/心愛/cca_a1_0901.ogg"
    ai 心愛_制服_基本_真顔 "就是那个啊，莲君"

    # 莲 「はい」
    lian "是的"

    # 心爱 「蓮君…次第だよ？優しくされたいんじゃなくて、一緒に温かい気持ちになれたら嬉しいなって思ってるだけだから、私の気持ちじゃなくて、自分の気持ちを尊重してね？」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0902.ogg"
    ai 心愛_制服_基本_嬉しい "莲君…就看你的了？我不是想被人温柔对待，只是想如果能一起感受到温暖的心情就很开心了，所以不用考虑我的心情，而是要尊重自己的感受，好吗？"
    hide 心愛_制服_基本_真顔

    # 莲 「心愛は…本当にそれでいのか？」
    lian "心爱……你确定这样真的的可以吗？"

    # 心爱 「ねぇ」
    show 心愛_制服_基本_真顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0903.ogg"
    ai 心愛_制服_基本_真顔 "呐"
    hide 心愛_制服_基本_嬉しい

    # 心爱 「好きって気持ち以外に、何が必要かな」
    voice "voice/心愛/cca_a1_0904.ogg"
    ai 心愛_制服_基本_真顔 "除了喜欢的心情以外，还需要什么呢？"

    # nil 「心愛のその一言で、俺のスイッチが切り替わった。」
    "心爱的这句话，打开了我的开关"

    # nil 「気づいたら俺は、心愛の両肩を掴んで、ベッドに押し倒していた。」
    "回过神来，我已经抓住了心爱的双肩，把她推倒在床上了"

    # 心爱 「わっ」
    show 心愛_制服_基本_驚き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0905.ogg"
    ai 心愛_制服_基本_驚き "哇啊！"
    hide 心愛_制服_基本_真顔

    # 莲 「好きだよ、心愛」
    lian "我喜欢你，心爱"

    # 心爱 「…い、いきなり強引は…て、照れるよー」
    show 心愛_制服_基本_泣き at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0906.ogg"
    ai 心愛_制服_基本_泣き "…突、突然强、硬起来……我、我会害羞的……"
    hide 心愛_制服_基本_驚き

    # 莲 「良いのか？　本当に」
    lian "可以吗？讲真"

    # 心爱 「これが、蓮くんの答えなら…私は全部受け止めたい…かな」
    show 心愛_制服_基本_嬉しい at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0907.ogg"
    ai 心愛_制服_基本_嬉しい "如果这是莲的回答的话…我想全部接受…吧"
    hide 心愛_制服_基本_泣き

    # 莲 「わかった」
    lian "我知道了"

    # 心爱 「えへ…良かった。てっきり、拒否られるかと思ってたから…すっごく嬉しいよ」
    show 心愛_制服_基本_にっこり at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0908.ogg"
    ai 心愛_制服_基本_にっこり "欸嘿嘿…太好了。我以为一定会被拒绝的…非常开心呢"
    hide 心愛_制服_基本_嬉しい

    # 莲 「そんな事するかよ」
    lian "我不会那么做的"

    # 心爱 「ちょっと考えてたくせにー」
    show 心愛_制服_基本_不機嫌 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0909.ogg"
    ai 心愛_制服_基本_不機嫌 "你刚才还在想呢"
    hide 心愛_制服_基本_にっこり

    # 莲 「いや、むしろ心愛がんむっ―」
    lian "不，我宁愿只拥有你"

    # 心爱 「ちゅー…ぷはっ。お話の続きは終わってから…ね…。今は、蓮くんが欲しい…から…」
    show 心愛_制服_基本_キス at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0910.ogg"
    ai 心愛_制服_基本_キス "啾——……呜欸……想说的话之后再说吧……现在，我想要你……（L:原作这里后半就莫得配音捏……）"
    hide 心愛_制服_基本_不機嫌

    # nil 「心愛はそっと目を閉じた。」
    "心爱轻轻地闭上了眼睛"

    # nil 「そっと、心愛の唇に自分の唇を重ねた。」
    "轻轻地，在心爱的嘴唇上重叠上自己的嘴唇"

    # 莲 「ごめん…心愛…今日は…なんか…優しくできそうにない…かも…」
    lian "对不起……心爱……今天……总觉得……好像不能温柔地对待你呢……大概……"

    # 心爱 「くすっ…じゃぁ…強引な蓮君を発注…で…っ♪」
    show 心愛_制服_基本_にっこり at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0911.ogg"
    ai 心愛_制服_基本_にっこり "欸嘿……那么~我就订购强硬的莲君吧……然后♪"
    hide 心愛_制服_基本_キス

    # 莲 「ありがとう心愛」
    lian "谢谢你，心爱"

    # 心爱 「どーいたしまして♪うん、じゃぁ…おいで…？　あれ？　なんか…私が抱いっ…んむっ…んぅ…ちゅぅ…」
    show 心愛_制服_基本_笑顔 at love69_xinai_center with dissolve
    voice "voice/心愛/cca_a1_0912.ogg"
    ai 心愛_制服_基本_笑顔 "不客气♪嗯，那么…来吧…？咦？我抱你…嗯…呜…"
    hide 心愛_制服_基本_にっこり

    # nil 「これ以上続けると話がやこしくなりそうなので、強引に唇を奪って事を進める。」
    "如果再这样继续拖下去的话，事情会变得很麻烦呢，所以这里我就强行夺走嘴唇继续下去"

    # nil 「結局…心愛のペースか。」
    "结果……是落进了心爱的节奏吗"

    # nil 「自嘲しながらも、自らの欲望に従う事を決める。心愛がそれを求めているのなら…してやりたい。」
    "在自嘲的同时，决定顺从自己的欲望。如果心爱想要这样... 我愿意做下去"

    # 心爱 HScene 02 Skip~
    # 913-1044
    # 2022年1月5日：正式版最开始的HS放宁宁举牌，后面的就放鬼畜名场面好了，我感觉很行！
    image bg 华强 = "images/extra/luckykeeper/华强.png"
    if persistent.hsceneG:
        scene 华强 with dissolve
        pause 2.0

    else:
        pass

    # scene08 场景1 【时隔许久的心爱夜访】 结束！

    # scene08 结束

    # 过场：心爱（常服），没有过场音乐，打算加一个

    stop music fadeout 4.0

    # 隐藏 quick_menu
    $ quick_menu = False

    play sound "voice/effect/moosehead honk (stinger).ogg"

    scene black
    scene アイキャッチ心愛 with ImageDissolve("images/tr/縦ブラインド.png", 1.5, ramplen=128, reverse=True, alpha=True, time_warp=None)

    $ renpy.pause(1.5, hard=True)
    $ renpy.end_replay()

    jump scene09
