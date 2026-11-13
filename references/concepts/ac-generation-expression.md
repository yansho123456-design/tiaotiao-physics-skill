---
concept: 正余弦交流电的产生与瞬时表达式
slug: ac-generation-expression
aliases: [交流发电机, 正弦交流电表达式, 余弦交流电, e=NBSωsinωt, 判断sin还是cos, 你爸是我, 瞬时值表达式, 峰值Em=NBSω, 转轴条件, 直流与交流的区别]
modules: [jiaobian]
lectures: [jiaobian-01, jiaobian-02, jiaobian-03, jiaobian-04, jiaobian-05, jiaobian-12, jiaobian-13, jiaobian-16]
---
# 正余弦交流电的产生与瞬时表达式

一句话：线框在匀强磁场里绕与 $B$ 垂直的轴匀速转动，就产生正余弦交流电，电动势是 $e=NBS\omega\sin\omega t$ 或 $e=NBS\omega\cos\omega t$。外面的系数永远是 $NBS\omega$（口诀「你爸是我」），里面永远是 $\omega t$，选 sin 还是 cos 只看 0 时刻线框切割边的速度 $v$ 与 $B$ 是否平行。〔卡 jiaobian-01-c12、jiaobian-01-c13、jiaobian-01-c15、jiaobian-01-c17、jiaobian-01-c18〕

## 老师怎么讲

### 直流与交流怎么区分（交变电流第 1 讲）

老师说，进入交变电流这个新模块，体系只有两块：先讲交流电，再讲理想变压器。〔卡 jiaobian-01-c01〕

直流电简称 DC，指方向不随时间变化的电流；交流电简称 AC，指方向随时间周期性变化的电流。老师讲了四张图：直流的两张图里电流的大小可以变大变小，方向始终没变，所以都是直流；交流的两张图里，一张是图线从 $t$ 轴上方跑到下方、之后又回到上方，另一张是正弦曲线，电流方向都在变，所以是交流。〔卡 jiaobian-01-c02〕

判断时不要看电流是变大还是变小，只看方向：方向一直在变就是交流，方向始终不变，大小再怎么变都是直流。落到 $i$-$t$ 图上，交流电的图线一定是 $t$ 轴上方、下方都有。图线只在一侧，说明方向没变，不是交流电；图线从一侧穿到另一侧的那个时刻，就是电流方向变化的时刻。〔卡 jiaobian-01-c03、jiaobian-01-c04〕

### 什么是正余弦交流电，怎样产生（交变电流第 1 讲）

老师说，正余弦交流电是最常见、也最爱考的一种，指电动势或电流随时间变化的图线是正弦函数或余弦函数。$i$-$t$ 图从 0 出发就是正弦交流电，从最大值出发就是余弦交流电。〔卡 jiaobian-01-c06〕

产生办法很简单：找一个线框，让它在磁场里绕图中的轴 $OO'$ 转动，线框的 $CD$ 边和 $AB$ 边切割磁感线，产生的感应电流就是正余弦交流电。图中线框在 $N$、$S$ 两极之间，用电刷和滑环把线框接到外电路。〔卡 jiaobian-01-c07〕

![线框在 N、S 极间绕轴 OO′ 转动，CD 边和 AB 边切割磁感线产生交流电](https://panda-1.tail2e9885.ts.net/wuli/img/jiaobian-01-generator.png)

### 推导正弦交流电（交变电流第 1 讲）

设定是这样的：$N$ 极在左，$S$ 极在右，把中间的磁场近似成匀强磁场，$B$ 水平向右；线框 $abcd$ 绕 $OO'$ 逆时针匀速转动，角速度为 $\omega$。第一件事是定 0 时刻：以线框面与 $B$ 垂直的时刻为 0 时刻，也就是线框竖直的时候。老师又画了一张正面看的图，线框变成一条线绕转轴 $O$ 转。经过时间 $t$ 线框转过的角度 $\theta=\omega t$，因为角速度就是单位时间转过的角度。〔卡 jiaobian-01-c08〕

线框转到任意位置时，$CD$ 边和 $AB$ 边的速度与 $B$ 都不垂直。算切割的动生电动势要用与 $B$ 垂直的那个速度，所以把速度正交分解成与 $B$ 平行的 $v_\parallel$ 和与 $B$ 垂直的 $v_\perp$，只要 $v_\perp$，不要 $v_\parallel$。用右手定则判断：$CD$ 边中电流由 $c$ 流向 $d$，$AB$ 边中电流由 $a$ 流向 $b$，沿 $a$、$b$、$c$、$d$ 绕行是同一个方向，所以两边的电动势要叠加。〔卡 jiaobian-01-c09〕

先算 $CD$ 边：

1. $E_{CD}=BL_{CD}v_\perp$。
2. $v$ 与水平方向的夹角也是 $\theta$，$\theta$ 的对边是 $v_\perp$，斜边是 $v$，所以 $v_\perp=v\sin\theta$。
3. 线速度等于角速度乘半径，这里半径是 $AD$ 边的一半，$v=\omega\cdot\dfrac{L_{AD}}{2}$。
4. 把 $\theta=\omega t$ 代入，$E_{CD}=BL_{CD}\cdot\omega\cdot\dfrac{L_{AD}}{2}\sin\omega t$。矩形线框的 $L_{CD}L_{AD}$ 就是面积 $S$，所以 $E_{CD}=\dfrac{BS\omega}{2}\sin\omega t$。

$AB$ 边的过程一模一样，夹角同样是 $\theta$，$E_{AB}=\dfrac{BS\omega}{2}\sin\omega t$。〔卡 jiaobian-01-c10〕

两边电流方向一样要叠加，所以单匝时 $e=E_{CD}+E_{AB}=BS\omega\sin\omega t$。线框有 $N$ 匝，还要乘 $N$，得 $e=NBS\omega\sin\omega t$。$e$ 与 $t$ 是 sin 函数关系，所以叫正弦交流电。〔卡 jiaobian-01-c12〕

![正面看线框：0 时刻线框面与 B 垂直，转过 θ=ωt 后把速度分解成 v∥ 和 v⊥，得 v⊥=v sinθ](https://panda-1.tail2e9885.ts.net/wuli/img/jiaobian-01-sine-front-view.png)

### 余弦交流电和快速判断 sin 还是 cos（交变电流第 1 讲）

老师说，产生正弦和余弦的装置一模一样，唯一的区别是 0 时刻选的位置：这次以线框面与 $B$ 平行的时刻（线框转到水平位置）为 0 时刻。推导步骤还是那几步，只有一处不同：这时 $v_\perp$ 变成了邻边，$v_\perp=v\cos\theta$，所以单匝 $e=BS\omega\cos\omega t$，$N$ 匝 $e=NBS\omega\cos\omega t$。〔卡 jiaobian-01-c13〕

老师总结，正弦和余弦交流电没有本质区别，装置相同，只看 0 时刻选哪个位置：线框面与 $B$ 垂直的时刻为 0 时刻是 sin，平行的时刻为 0 时刻是 cos。老师同时提醒，这一句不建议死记。〔卡 jiaobian-01-c14〕

老师教的小妙招是不用记，画一画 0 时刻的 $v$ 和 $B$：

- 线框面与 $B$ 垂直的时刻为 0 时刻：切割的两条边速度与 $B$ 平行，不切割，$e=0$。sin 函数在 0 时刻为 0，所以是 sin。
- 线框面与 $B$ 平行的时刻为 0 时刻：切割边速度与 $B$ 垂直，$e$ 最大。cos 函数在 0 时刻最大，所以是 cos。

老师在讲义上写的结论是：0 时刻 $B$、$v$ 平行，不切割，函数值为 0，对应 sin；0 时刻 $v\perp B$，$E$ 最大，函数值最大，对应 cos。〔卡 jiaobian-01-c15〕

![0 时刻 v 与 B 平行，不切割，e=0，对应 sin 函数](https://panda-1.tail2e9885.ts.net/wuli/img/jiaobian-01-judge-sin.png)

![0 时刻 v 与 B 垂直，切割最强，e 最大，对应 cos 函数](https://panda-1.tail2e9885.ts.net/wuli/img/jiaobian-01-judge-cos.png)

老师还强烈不建议记「垂直是 sin、平行是 cos」这类对应关系，原因是容易记混，负担也大。老师说自己现在也记不住，分析时靠的就是上面的画图办法。〔卡 jiaobian-01-c16〕

### 表达式的结构和系数（交变电流第 1 讲）

老师总结：sin 或 cos 前面一定是 $NBS\omega$，里面一定是 $\omega t$，因为 $\omega t$ 对应的是角度 $\theta$。判断 sin 还是 cos 看 0 时刻，系数用「你爸是我」记。老师说交流电这一块经常把电动势写成小写的 $e$，都是一回事，不用纠结；由 $e=E_{\rm m}\sin\omega t$ 可知 $E_{\rm m}=NBS\omega$，也就是 sin、cos 外面那一坨就是电动势的最大值。〔卡 jiaobian-01-c18〕

### 转轴条件（交变电流第 1 讲）

基础课最后一个小点讲转轴。转轴 $OO'$ 与 $B$ 垂直时，线框转动可以产生交流电。转轴与 $B$ 平行时，不能产生交流电。〔卡 jiaobian-01-c25、jiaobian-01-c26〕

不能的原因，老师画了左视图：这时只有与转轴垂直的两条边在切割，左视图里磁场垂直纸面向里，这条边绕中间的点转动，就是前面讲过的旋转切割模型。设这一段长为 $R$，电动势 $E=\dfrac12BR^2\omega$，电流方向从转动中心往外，相当于中心是电源负极、两个端点是正极。接上外电路后，流过电阻的电流方向始终不变，所以是直流电，不是交流电。老师的总结是：转轴跟 $B$ 平行时，这种转法的本质是旋转切割模型，没有办法产生交流电。〔卡 jiaobian-01-c27〕

![转轴与 B 平行时的左视图：切割的边绕中点转动，E=Br²ω/2，电流从中心流向两端，方向不变](https://panda-1.tail2e9885.ts.net/wuli/img/jiaobian-01-axis-left-view.png)

〔整理注：旋转切割的电动势大小公式 $E=\dfrac12BR^2\omega$ 卡里是这样写的；图说里写作 $E=Br^2\omega/2$，是同一个式子，只是半径的字母不同。〕

本讲小结里，老师把几点收在一起：交流电是方向随时间周期性变化的电流；正弦 $e=NBS\omega\sin\omega t$，余弦 $e=NBS\omega\cos\omega t$；判断 sin 还是 cos 不要记，看 0 时刻 $B$、$v$ 的关系，是 0 就是 sin，是最大值就是 cos；记忆大法是「你爸是我」；转轴跟 $B$ 平行时不产生交流电。〔卡 jiaobian-01-c29〕

### 由图读 $\omega$、峰值，写表达式（交变电流第 2 讲 $i$-$t$ 图基础篇）

老师说，线圈在磁场中匀速转动，角速度与周期的关系在必修二讲过：$\omega=2\pi/T$。要求 $\omega$ 先从图上读周期，频率是周期的倒数 $f=1/T$。例如 $T=0.04\ \mathrm{s}$ 时，$f=25\ \mathrm{Hz}$，$\omega=2\pi/0.04=50\pi\ \mathrm{rad/s}$。瞬时表达式写成「峰值乘 $\sin\omega t$」，只要把读出的峰值和 $\omega$ 代进去。〔卡 jiaobian-02-c04〕

同一个交流电，不管题目给的是电动势 $e$ 的图、电阻两端电压 $u$ 的图还是电流 $i$ 的图，函数类型（sin 还是 cos）和周期都一样，只有最大值不同。老师的证明：设线圈内阻为 $r$，外电路电阻为 $R$，则 $i=\dfrac{e}{R+r}$，$u=iR=\dfrac{eR}{R+r}$，它们与 $e$ 只差一个常数倍，所以函数类型和周期不变。如果给的是 $e$-$t$ 图，它的最大值就是 $NBS\omega$。〔卡 jiaobian-02-c05〕

### 两次转速不同的双图问题（交变电流第 3 讲 $i$-$t$ 图进阶篇）

这里承接第 1 讲的 $E_{\rm m}=NBS\omega$。老师说，双图问题是同一个线圈、同一个磁场，区别只是角速度不同，$N$、$B$、$S$ 都一样，所以两次最大电动势之比等于角速度之比，$\dfrac{E_{ma}}{E_{mb}}=\dfrac{\omega_a}{\omega_b}$。换成最大电压、最大电流也一样，都跟转速成正比。所以不管图是 $e$-$t$、$u$-$t$ 还是 $i$-$t$，两次最大值之比都等于转速之比。〔卡 jiaobian-03-c03〕

写某条图线的瞬时表达式时有一个典型错误。老师的例子里，最大值是 10，$a$ 是 sin 函数，所以 $u=10\sin\omega t$，只差 $\omega$。$a$ 的周期是 $0.4\ \mathrm{s}$，$\omega=2\pi/0.4=5\pi\ \mathrm{rad/s}$，所以是 $u=10\sin5\pi t\ \mathrm{V}$，而不是 $10\sin0.4\pi t$，选项 B 错。〔卡 jiaobian-03-c08〕〔整理注：B 选项把周期数值 0.4 当成了 $\omega$ 的系数，周期不能直接写进 sin 里，要先求 $\omega$。〕

转轴位置的问题，老师讲了两次。第一次在第 3 讲：轴在中间和轴在边上（磁场铺满），最大电动势一样，都是 $NBS\omega$。轴在边上时只有 $AB$ 一条边切割，取最大值时 $e=NBL_{ab}v$，$v=\omega L_{ad}$（半径是 $AD$ 边的长度），所以 $e_{\rm m}=NBL_{ab}L_{ad}\omega=NBS\omega$。老师的直观解释：只有一条边切割，比轴在中间少了一半，但半径是两倍、速度也是两倍，一半乘以二，结果相同。〔卡 jiaobian-03-c18〕

![俯视示意：轴在中间时两条边各以 L_ad/2 为半径转，轴在边上时只有一条边、半径 L_ad，两种情形最大电动势都是 NBSω](https://panda-1.tail2e9885.ts.net/wuli/img/jiaobian-03-edge-axis-emf.png)

### 由 $\Phi$-$t$ 图写表达式（交变电流第 4 讲 $\Phi$-$t$ 图）

老师说，最大电动势 $NBS\omega$ 里的 $BS$ 就是最大磁通量 $\Phi_{\rm m}$：线圈面与磁场垂直也就是中性面时，$\Phi=BS$，这是最大磁通量，也是 $\Phi$-$t$ 图函数的最大值。所以给的是 $\Phi$-$t$ 图时，把 $BS$ 代换成 $\Phi_{\rm m}$ 即可。〔卡 jiaobian-04-c04〕

求最大电动势 $E_{\rm m}=NBS\omega=N\Phi_{\rm m}\omega$，步骤是：读周期，用 $\omega=2\pi/T$ 算 $\omega$；读 $\Phi_{\rm m}$；用 $E_{\rm m}=N\Phi_{\rm m}\omega$ 算出，匝数 $N$ 题目给。〔卡 jiaobian-04-c05〕

写表达式需要三样：$\omega$（读周期）、$E_{\rm m}$（上一步）、sin 还是 cos（看 0 时刻）。表达式的形式永远是 $E_{\rm m}\sin\omega t$ 或 $E_{\rm m}\cos\omega t$。〔卡 jiaobian-04-c12〕

![由 Φ-t 图求交流电表达式的三步：读周期求 ω，读 Φm 求 Em，看 0 时刻的 Φ 定 sin 还是 cos；求 u、i 时先求 e，再用 u = e÷R总×R、i = e÷R总](https://panda-1.tail2e9885.ts.net/wuli/img/jiaobian-04-expr-steps.png)

在 $\Phi$-$t$ 图里判断 sin 还是 cos，看 0 时刻的 $\Phi$：$\Phi$ 最大，说明 $e$ 为 0，是 sin；$\Phi$ 为 0，说明 $e$ 最大，是 cos。写表达式的顺序是先求 $\omega$ 和 $E_{\rm m}$，再看 0 时刻的 $\Phi$。〔卡 jiaobian-04-c13〕〔整理注：本讲例题的 $\Phi$-$t$ 图从原点出发，0 时刻 $\Phi=0$，所以 $e$ 都是 cos。这是卡里的整理注。〕

要求 $u$ 或 $i$ 的表达式，先求出 $e$，再用 $u=\dfrac{e}{R_{总}}\cdot R$、$i=\dfrac{e}{R_{总}}$ 换算。$R_{总}$ 是回路总电阻，$R$ 是所求电压对应的那段电阻。〔卡 jiaobian-04-c14〕

反求磁感应强度 $B$ 时，仍用 $E_{\rm m}=NBS\omega$ 反解，$B=\dfrac{E_{\rm m}}{NS\omega}$，$S$ 由边长算出。〔卡 jiaobian-04-c21〕

### 四值里的最大值与转轴不在中间（交变电流第 5 讲 交流电的四值）

老师说，最大值就是瞬时值里最大的那个。电动势最大值 $E_{\rm m}=NBS\omega$（老师用谐音「你爸是我」提醒 $N$、$B$、$S$、$\omega$ 四个量），电流最大值 $I_{\rm m}=E_{\rm m}/R$，$R$ 是总电阻。$e$-$t$ 图纵轴标 $E_{\rm m}$，$i$-$t$ 图纵轴标 $I_{\rm m}$。〔卡 jiaobian-05-c03〕

转轴不在线框正中间，老师总结：和在正中间完全没有区别，最大电动势都是 $BS\omega$。证明（一匝）：设竖边长 $L_1$，左边这条边到轴的距离是 $L_2$，右边那条是 $L_3$。当两条边的速度都与 $B$ 垂直时，$E_{\rm m}=BL_1L_2\omega+BL_1L_3\omega=BL_1\omega(L_2+L_3)$，$L_2+L_3$ 是线框的宽，再乘 $L_1$ 就是面积 $S$，所以 $E_{\rm m}=BS\omega$。老师说这类题不要纠结，按转轴在正中间算。〔卡 jiaobian-05-c21〕

![例题 3 的图重画：转轴 O1O2 不在正中间；两条竖边长 L1 在切割磁感线，左边到轴距离 L2，右边到轴距离 L3，L2+L3 就是线框的宽，L1(L2+L3)=S](https://panda-1.tail2e9885.ts.net/wuli/img/jiaobian-05-ex3-axis-offcenter.png)

题目给某一时刻的瞬时值要反求最大值时，先写出瞬时表达式再代入。老师的例子：0 时刻线圈与磁场平行，$\Phi=0$，$e$ 最大，所以 $e=BS\omega\cos\omega t$；电流表达式是 $e$ 除以总电阻（$2\ \Omega$），$i=\dfrac{BS\omega}{2}\cos\omega t$。转到 $60^\circ$ 时 $\omega t=60^\circ$，电流是 $1\ \mathrm{A}$，代入 $1=\dfrac{BS\omega}{2}\cos60^\circ$，$\cos60^\circ=\dfrac12$，解出 $BS\omega=4\ \mathrm{V}$，这就是最大电动势；除以电阻得 $I_{\rm m}=2\ \mathrm{A}$；再除以 $\sqrt2$ 得有效值；最后 $P=I^2R=4\ \mathrm{W}$。〔卡 jiaobian-05-c22〕

写瞬时值表达式的完整办法，老师在第 5 讲归成三样：$\omega$ 由周期 $\omega=2\pi/T$ 求；最大值，已知电流最大值时电压最大值用 $U_{\rm m}=I_{\rm m}R$；sin 还是 cos 看计时零点。从中性面开始（0 时刻 $\Phi$ 最大，$e$ 为 0）是 sin，从与磁场平行的位置开始（0 时刻 $\Phi=0$，$e$ 最大）是 cos；图像从原点出发是 sin，从最大值出发是 cos。电流是 sin，电压肯定也是 sin，因为电流等于电压除以常数 $R$。例题里 $T=0.02\ \mathrm{s}$，$\omega=100\pi\ \mathrm{rad/s}$，$U_{\rm m}=10\sqrt2\ \mathrm{V}$，是 sin，$e=10\sqrt2\sin100\pi t\ \mathrm{V}$。〔卡 jiaobian-05-c25〕〔整理注：这条卡是把第 5 讲几道例题的判断方法合成的，它把「看 0 时刻 $\Phi$」「看图像从哪出发」放在一起，和第 1 讲「看 0 时刻 $v$ 与 $B$」是同一件事的三种说法。〕

### 变压器题里的发电机电源（交变电流第 12、13、16 讲）

后面的变压器题型课里，这个概念以电源的身份出现。第 12 讲老师说，$U_1$ 是输入的交流电的电源电压，要改变它只能改电源：如果电源是线圈在磁场中转动产生的正弦式交流电，就要改 $B$、$N$、$S$、$\omega$。只改变变压器的匝数，$U_1$ 不变。〔卡 jiaobian-12-c03〕

第 13 讲讲发电机转速改变：最大值 $E_{\rm m}=NBS\omega$，转速变为原来的一半，$\omega$ 减半，最大值和有效值都减半，变压器输入电压 $U_1$ 减半。然后沿 $U_1$、$U_2$、$I_2$、$I_1$ 逐个推：匝数比没变，$U_2$ 减半；$R$ 没变，$I_2$ 减半；$\dfrac{I_1}{I_2}=\dfrac{n_2}{n_1}$ 右边没变，$I_1$ 也减半。功率要用 $P=U_2I_2$ 算，两个都减半，乘起来变为原来的四分之一。频率跟角速度走，也减半。〔卡 jiaobian-13-c14〕

第 16 讲远距离输电的例题 8 是一道大综合题，第 1 问是复习交流电表达式，sin 还是 cos 看 0 时刻。〔卡 jiaobian-16-c31〕

## 做题套路

1. 判断直流还是交流：不看电流大小，只看方向有没有变；在 $i$-$t$ 图上看图线是否 $t$ 轴上下都有。〔卡 jiaobian-01-c03、jiaobian-01-c04〕
2. 写 $e=E_{\rm m}\sin\omega t$ 或 $E_{\rm m}\cos\omega t$，要确定三样：$\omega$、$E_{\rm m}$、sin 还是 cos。〔卡 jiaobian-04-c12、jiaobian-05-c25〕
3. 求 $\omega$：读周期，$\omega=2\pi/T$；频率 $f=1/T$。〔卡 jiaobian-02-c04〕
4. 求 $E_{\rm m}$：用 $NBS\omega$。给了 $\Phi$-$t$ 图就换成 $N\Phi_{\rm m}\omega$；给了 $e$-$t$ 图就直接读峰值。电流最大值用 $E_{\rm m}$ 除以总电阻。〔卡 jiaobian-04-c05、jiaobian-02-c05、jiaobian-05-c03〕
5. 定 sin 还是 cos：在线框图里画 0 时刻的 $v$ 与 $B$，平行是 sin，垂直是 cos；在 $\Phi$-$t$ 图里看 0 时刻 $\Phi$ 最大是 sin、为 0 是 cos；在 $e$、$i$、$u$ 的图里看图线从原点出发是 sin、从最大值出发是 cos。〔卡 jiaobian-01-c15、jiaobian-04-c13、jiaobian-05-c25〕
6. 要 $u$ 或 $i$ 的表达式：先求 $e$，再用 $u=\dfrac{e}{R_{总}}R$、$i=\dfrac{e}{R_{总}}$ 换算；$u$、$i$、$e$ 三个量函数类型与周期都相同。〔卡 jiaobian-04-c14、jiaobian-02-c05〕
7. 已知某时刻的瞬时值要反求最大值：先写出瞬时表达式，把角度和瞬时值代入。〔卡 jiaobian-05-c22〕
8. 两次转速不同的双图：最大值之比等于角速度之比等于转速之比。〔卡 jiaobian-03-c03〕
9. 转轴不在线框正中间，或在边上：按在正中间算，最大电动势都是 $NBS\omega$。〔卡 jiaobian-05-c21、jiaobian-03-c18〕
10. 判断某种转法能不能产生交流电：转轴与 $B$ 垂直可以，平行不行。〔卡 jiaobian-01-c25、jiaobian-01-c26〕

## 口诀

- 你爸是我：$N$ 是你，$B$ 是爸，$S$ 是「是」，$\omega$ 是我，合起来就是 $NBS\omega$。老师说这个点从现在开始一直到高考完你一定不会忘。〔卡 jiaobian-01-c17〕

## 易错

- sin 里面的 $\omega t$ 是一个整体，不是先 $\sin\omega$ 再乘 $t$。〔卡 jiaobian-01-c11〕
- 老师不建议死记「垂直是 sin、平行是 cos」，容易记混，要靠画 0 时刻的 $v$ 与 $B$ 来判断。〔卡 jiaobian-01-c16〕
- 点和叉不只能表示 $B$ 的方向，也能表示速度的方向。例题 4 里 $bc$ 边向纸面里转，速度方向就是叉；$ad$ 边向外转，速度方向就是点。〔卡 jiaobian-01-c22〕
- 一条边与 $B$ 平行时，虽然上面有电流，这条边的安培力也是 0，因为只有 $L$ 和 $B$ 不平行时才有安培力。〔卡 jiaobian-01-c24〕
- 写瞬时值表达式时，不能把周期的数值直接写进 sin 里，要先由 $\omega=2\pi/T$ 求出 $\omega$，如 $10\sin5\pi t$ 而不是 $10\sin0.4\pi t$。〔卡 jiaobian-03-c08〕
- 例题 3（第 1 讲）里 sin 里面的 $\omega$ 也要跟着变，不要只改系数。〔卡 jiaobian-01-c20〕

## 例题

- **交变电流第 1 讲 例题 1**：四种电流随时间变化的图，哪些是交变电流。答案：CD。老师要点：抓住图线上下都有。〔卡 jiaobian-01-c05〕
- **交变电流第 1 讲 例题 2**：矩形线圈从图示位置开始转动，求 $t$ 时刻感应电动势的大小。答案：C。老师要点：考两件事，系数用 $NBS\omega$，sin 还是 cos 看初始时刻 $v$ 与 $B$ 的关系；题目没写匝数就默认 1 匝。图中线圈面与 $B$ 垂直，位置与推导 sin 时相同。〔卡 jiaobian-01-c19〕
- **交变电流第 1 讲 例题 3**：角速度提高一倍、面积减小一半，电动势表达式变成什么。答案：C。老师要点：用 $E_{\rm m}=NBS\omega$，系数里 $S$ 和 $\omega$ 的乘积不变，里面的 $\omega$ 换成 $2\omega$，不要忘了 sin 里面的 $\omega$ 也跟着变。〔卡 jiaobian-01-c20〕
- **交变电流第 1 讲 例题 4**：线圈转到图示位置时，判断电流方向、电动势、磁通量变化率、安培力。卡里只给出 D 选项不对。老师要点：用右手定则判电流方向；$v\perp B$ 时 $e$ 最大，等于 $nBL_1L_2\omega$，磁通量变化率也最大；$ab$ 边与 $B$ 平行，安培力为 0。〔卡 jiaobian-01-c21、jiaobian-01-c22、jiaobian-01-c23、jiaobian-01-c24〕
- **交变电流第 1 讲 例题 5**：下图中不能产生交变电流的是哪个。答案：A。老师要点：用「转轴与 $B$ 平行不能产生交流电」逐项看。〔卡 jiaobian-01-c28〕
- **交变电流第 4 讲 讲例**：由 $\Phi$-$t$ 图写出电动势的瞬时表达式（设 $N=1$）。答案 $e=\pi\cos5\pi t$。要点：$T=0.4\ \mathrm{s}$，$\omega=2\pi/T=5\pi\ \mathrm{rad/s}$，$E_{\rm m}=N\Phi_{\rm m}\omega=\pi\ \mathrm{V}$，0 时刻 $\Phi=0$ 所以是 cos；求 $u$ 或 $i$ 时先求 $e$ 再换算。〔卡 jiaobian-04-c15〕
- **交变电流第 4 讲 例题 2**：50 匝线圈的 $\Phi$-$t$ 图，判断电动势最大、电流变向、最大值、瞬时表达式。答案：D。老师要点：A、B 用要点三，C 用要点一和二，D 用要点四；计算 $E_{\rm m}$ 时 $\pi$ 直接代 3.14，$50\times3.14=157$。〔卡 jiaobian-04-c16〕〔整理注：卡里记录转录里讲到 B 时把 0.2 s 记成 0.3 s，后面又记回来，按讲义是 0.2 s 和 0.4 s。〕
- **交变电流第 4 讲 例题 3**：由 $\Phi$-$t$ 图反求磁感应强度 $B$。答案 $B=0.4\ \mathrm{T}$。要点：$E_{\rm m}=20\pi\ \mathrm{V}$，$B=\dfrac{E_{\rm m}}{NS\omega}=\dfrac{20\pi}{100\times0.1^2\times50\pi}=0.4\ \mathrm{T}$。〔卡 jiaobian-04-c21〕〔整理注：卡里补了一条更快的做法 $B=\Phi_{\rm m}/S=0.4\ \mathrm{T}$，两种结果一致，老师讲的是前一种。〕
- **交变电流第 5 讲 例题 3**：转轴不在正中间，从线圈平面与磁场平行开始计时，转 $60^\circ$ 时电流 $1\ \mathrm{A}$，判断功率、表达式、有效值、磁通量。答案 B。功率是 $4\ \mathrm{W}$ 不是 $8\ \mathrm{W}$，A 错；磁通量表达式的系数应是 $\dfrac{2T}{\pi}$，D 错。要点：转轴不在正中间等同正中间；平行面开始计时用 cos；代入 $60^\circ$ 和 $1\ \mathrm{A}$ 解出 $BS\omega=4\ \mathrm{V}$，$I_{\rm m}=2\ \mathrm{A}$，$P=I^2R=4\ \mathrm{W}$。〔卡 jiaobian-05-c20、jiaobian-05-c21、jiaobian-05-c22〕
- **交变电流第 5 讲 例题 4**：由 $i$-$t$ 图写电压瞬时值表达式。答案 $e=10\sqrt2\sin100\pi t\ \mathrm{V}$。要点：$T=0.02\ \mathrm{s}$，$\omega=100\pi\ \mathrm{rad/s}$，$U_{\rm m}=I_{\rm m}R=10\sqrt2\ \mathrm{V}$，图像从原点出发所以是 sin。〔卡 jiaobian-05-c25〕
- **交变电流第 16 讲 例题 8**：交流发电机向远处供电的大综合题，求 $E_{\rm m}$ 和表达式、损耗功率 $\Delta P$、升压变压器原线圈电压 $U_1$。答案：(1) $E_m=300\sqrt2$ V，$e=300\sqrt2\cos100\pi t$ (V)；(2) $\Delta P=160$ W；(3) $U_1=280$ V。老师要点：第 1 问复习交流电表达式，sin 还是 cos 看 0 时刻；第 2 问用输电线损耗 $I^2R$；第 3 问考变压器加电阻分压。〔卡 jiaobian-16-c31〕

## 相关概念

- 中性面与平行面（concepts/neutral-plane.md）
