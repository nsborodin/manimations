from manim import *
from manim.utils.tex import TexTemplate

config.tex_compiler = "pdflatex"

tpl = TexTemplate()
tpl.preamble = r"""
\usepackage[utf8]{inputenc}
\usepackage[T2A]{fontenc}
\usepackage[english,russian]{babel}
\usepackage{amsmath}
\usepackage{amssymb}
"""
config.tex_template = tpl

class LaTexSimple(Scene):
    def construct(self):
        pyt = MathTex('a^2 + b^2 = c^2')
        self.play(Write(pyt), run_time=3)
        self.wait()
        self.play(Unwrite(pyt))

        fib = MathTex("a_n = a_{n-1} + a_{n-2}", font_size=48)
        self.wait()
        self.play(Create(fib), run_time=3)
        self.play(Uncreate(fib))

        ineq = MathTex("f(x,y) > g(x,y)", font_size=60)
        self.wait()
        self.play(FadeIn(ineq))
        self.wait()
        self.play(FadeOut(ineq))
        self.wait()

class LaTexCommands(Scene):
    def construct(self):
        pi = MathTex("\\pi \\neq 3 \\!.14", font_size=100)
        self.play(Write(pi))
        self.wait()
        self.play(Unwrite(pi))

        sc = MathTex("\\sin^2 \\alpha + \\cos^2 \\alpha = 1")
        self.play(Write(sc), run_time=3)
        self.wait()
        self.play(Unwrite(sc))

        sl = MathTex("\\log_2(a \\cdot b) = \\log_2a + \\log_2b")
        self.wait()
        self.play(GrowFromCenter(sl), run_time=1.5)
        self.wait(3)

class LaTexSizeAndColor(Scene):
    def construct(self):
        tangent_value = MathTex(
            r"\tan \frac{\pi}{3} = \sqrt{3}",
            font_size=70,
            color=YELLOW
        )
        self.play(Write(tangent_value), run_time=3)
        self.wait()
        self.play(Unwrite(tangent_value))

        number_set = MathTex(
            r"(\infty; -1] \cup \{0\} \cup [1; + \infty)"
        )
        self.play(Write(number_set), run_time=3)
        self.wait()
        self.play(Unwrite(number_set))

        sin_of_triangles = MathTex(
            r"\triangle ABC \sim \triangle A_1B_1C_1",
            color=BLUE
        )
        self.wait()
        self.play(FadeIn(sin_of_triangles))
        self.wait(3)

class LaTexDesign(Scene):
    def construct(self):
        latex_str = r"(a\perp l, \ b\perp l) \Rightarrow a\parallel b"
        parallel_test = MathTex(latex_str)
        self.play(Write(parallel_test), run_time=3)
        self.wait()
        self.play(Unwrite(parallel_test), run_time=2)

        limit_def = MathTex(
            r"\lim_{n \to \infty}x_n=a",
            r"\ \Leftrightarrow \,",
            r"\forall \varepsilon >0" +
            r"\hspace{2mm} \exists N(\varepsilon )"
            r"\in \mathbb {N} \colon "
            r"n\geqslant N \Rightarrow |x_{n} - a|<\varepsilon"
        )

        self.play(FadeIn(limit_def[0], shift=DOWN))
        self.wait()
        self.play(GrowFromCenter(limit_def[1]))
        self.wait()
        self.play(FadeIn(limit_def[2], shift=DOWN))
        self.wait()
        self.play(Unwrite(limit_def), run_time=3)
        self.wait(3)

class LaTexBraceBracket(Scene):
    def construct(self):
        system_brace = MathTex(r"\begin{cases}x>0, \\ x <1 \end{cases}")
        self.play(Write(system_brace), run_time=3)
        self.wait()
        self.play(Unwrite(system_brace))

        union_bracket = MathTex(r"\left[ \begin{gathered} "
        r"x = \pm 1, \\ x \geqslant 3. \hfill "
        r"\end{gathered} \right.")
        self.play(Write(union_bracket), run_time=3)
        self.wait(3)

class LaTexText(Scene):
    def construct(self):
        hello = Tex("Hello, Manim!", color=GOLD)
        self.play(Write(hello), run_time=2)
        self.wait(2)
        self.play(Unwrite(hello))

        kol = Tex("Andrey Nikolaevich Kolmogorov (1903-1987) "
        "was a Soviet mathematician who contributed to the "
        "mathematics of probability theory, topology, \\newline intuition"
        "istic logic, turbulence, classical mechanics, algorithmic"
        " information theory and computational complexity \\break \\ldots",
        font_size=36 )
        self.wait()
        self.play(FadeIn(kol), run_time=1.5)
        self.wait(3)

class LaTexRussian(Scene):
    def construct(self):
        
        russian_language = Tex("Привет \\ "
        "2я строчка "
        r"\$manim"
        r"$\$ util$\$tex.py",
        font_size=32)
        self.play(Write(russian_language), run_time=5)
        self.wait(3)

class LaTexTextWithFormulas(Scene):
    def construct(self):
        euler = Tex(r"Euler's identity: $e^{i\pi}+1=0$")
        self.play(GrowFromCenter(euler), run_time=1.5)
        self.wait()
        self.play(Unwrite(euler))

        imo_problem = Tex(r"Let $n \geqslant 1$ be an odd integer. "
            r"Determine all functions $f$ from the set of integers "
            r"to itself such that for all integers $x$ and $y$ the "
            r"difference $f(x)-f(y)$ divides $x^{n}-y^{n}$.",
            font_size=32)
        self.play(FadeIn(imo_problem))
        self.wait(3)

class LaTexAlignment(Scene):
    def construct(self):
        from manim.utils.tex import TexTemplate
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage{ragged2e}")  # даёт justify

        # perelman = Tex(r"\begin{justify}"
        # r"Recall that every smooth vector field "
        # r"$X^{\alpha}=X^{\alpha}(x)$ on a manifold $(M, g)$ "
        # r"generates an infinitesimal diffeomorphism "
        # r"$x^{\alpha} \mapsto x^{\alpha}+\varepsilon "
        # r"X^{\alpha}+0\left(\varepsilon^{2}\right)$. "
        # r"Pulling back the metric $g_{\alpha \beta}$ by this "
        # r"diffeomorphism creates a infinitesimally deformed "
        # r"metric $g_{\alpha \beta} \mapsto g_{\alpha \beta}+$ "
        # r"$\varepsilon \pi_{\alpha \beta}"
        # r"0\left(\varepsilon^{2}\right)$."
        # r"\end{justify}", font_size=32)

        perelman = Tex(
            r"Recall that every smooth vector field $X^{\alpha}=X^{\alpha}(x)$ "
            r"on a manifold $(M, g)$ generates an infinitesimal diffeomorphism "
            r"$x^{\alpha}\mapsto x^{\alpha}+\varepsilon X^{\alpha}+0(\varepsilon^{2})$. "
            r"Pulling back the metric $g_{\alpha\beta}$ by this diffeomorphism "
            r"creates an infinitesimally deformed metric "
            r"$g_{\alpha\beta}\mapsto g_{\alpha\beta}+\varepsilon \pi_{\alpha\beta}"
            r"+0(\varepsilon^{2})$.",
            tex_template=template,
            tex_environment="justify"  # полная ширина, выравнивание по обеим
        )
        perelman.scale(0.7)
        self.play(Write(perelman), run_time=7)
        self.wait(3)

class TextExample(Scene):
    def construct(self):
        hello = Text(
            "Этот текст генерируется моментально",
            font='Times New Roman',
            color=LIGHT_GREY,
            font_size=32
        )
        self.play(Write(hello), run_time=2)
        self.wait()

        message = Text("LaTeX не требуется, кириллица поддерживается",
            font="Arial", font_size=32)
        self.play(FadeOut(hello, shift=DOWN),
            FadeIn(message, shift=DOWN))
        self.wait(3)

class LaTexFake(Scene):
    def construct(self):
        fake_latex = Text("CMU Serif для цифр:"
        " 0, 1, 2, 3, 4, 5, 6, 7, 8, 9", font="CMU Serif",
        color=WHITE, font_size=32)
        self.play(Write(fake_latex), run_time=3)
        self.wait()

        message = Text("Для перехода к новой строке "
        "используйте \\n. \nПри необходимости форматировать "
        "большие\nфрагменты текста присмотритесь к классу\n"
        "Paragraph.", font_size=32, font="CMU Serif")
        self.play(FadeOut(fake_latex), FadeIn(message))
        self.wait(3)

class SumSquare(Scene):
    def construct(self):
        sum = MathTex(r"1 + 3 + 5 + 7 + 9 = 5^2")
        self.play(Write(sum), run_time=3)
        self.wait()

class Sum2(Scene):
    def construct(self):
        sum = MathTex(r"1+5+10+10+5+1=2^5")
        self.play(GrowFromCenter(sum), run_time=1.5)
        self.wait()

class Squares(Scene):
    def construct(self):
        square = MathTex(r"(a^2 + b^2)(c^2 + d^2) = (ac + bd)^2 + (ad - bc)^2")
        self.play(FadeIn(square, shift=DOWN))
        self.wait()
    
class IneqChain(Scene):
    def construct(self):
        ineq = MathTex(r"x_1 < x_2 < x_3 < \dots < x_n ")
        self.play(Write(ineq))
        self.wait()
        self.play(Unwrite(ineq))
        self.wait()

class SumProduct(Scene):
    def construct(self):
        sp = MathTex(r"1+2+3=1 \times 2 \times 3")
        self.play(GrowFromCenter(sp))
        self.wait()
        self.play(FadeOut(sp))
        self.wait()

class Sin2Angle(Scene):
    def construct(self):
        sin = MathTex(r"\sin 2 \alpha = 2 \sin \alpha \cos \alpha")
        self.play(FadeIn(sin, shift=DOWN))
        self.wait()
        self.play(FadeOut(sin, shift=DOWN))
        self.wait()

class Log(Scene):
    def construct(self):
        log = MathTex(r"a^{\log_a b}=b")
        self.play(Write(log),run_time=3)
        self.wait()
        self.play(Unwrite(log))
        self.wait()

class Yellow(Scene):
    def construct(self):
        eul = MathTex(r"\frac{1}{1^2} + \frac{1}{2^2} " +
            r" + \frac{1}{3^2} + \dots = \frac{\pi^2}{6}",
            color=YELLOW)
        self.play(GrowFromCenter(eul), run_time=1.5)
        self.wait()
        self.play(FadeOut(eul))
        self.wait()

class Sets(Scene):
    def construct(self):
        sets = MathTex(r"A \cap (B \cup C) = (A \cap B)"
        r"\cup (A \cap C) ")
        self.play(FadeIn(sets, shift=DOWN))
        self.wait()
        self.play(FadeOut(sets, shift=DOWN))
        self.wait()
    
class Triangles(Scene):
    def construct(self):
        triangle = MathTex(r"\bigtriangleup ABC = "
        r"\bigtriangleup A_1 B_1 C_1"
        r"\Rightarrow \angle A = \angle A_1 ")
        self.play(Write(triangle), run_time=1.5)
        self.wait()
        self.play(Unwrite(triangle))
        self.wait()

class Brackers(Scene):
    def construct(self):
        bracket = MathTex(r"D(x)=\begin{cases} 1, \quad x \in \mathbb{Q}; \\" 
        r"0, \quad x \in  \mathbb{R} \setminus \mathbb{Q}. \end{cases}")
        self.play(GrowFromCenter(bracket), run_time=1.5)
        self.wait()
        self.play(FadeOut(bracket))
        self.wait()

class SquareBrackets(Scene):
    def construct(self):
        br = MathTex(
            r"\left[ \begin{aligned}"
            r"& x > \pi, \\"
            r"& x = \operatorname{arctg}\sqrt{5}."
            r"\end{aligned} \right."
        )
        self.play(GrowFromCenter(br))
        self.wait()
        self.play(FadeOut(br,shift=DOWN))
        self.wait()

class Cos(Scene):
    def construct(self):
        # text = Tex(r"Формула косинуса угла между прямыми."
        # r"Если $\vec{a}(x_1, y_1, z_1)$ и $\vec{b}(x_2, y_2, z_2)$"
        # r"направляющие векторы прямых $a$ и $b$, то")
        # cos = MathTex(r"\cos(a,b) = \frac{|\vec{a} \cdot \vec{b}|}{|\vec{a}|\cdot|\vec{b}|}"
        # r"\frac{|x_1 \cdot x_2 + y_1 \cdot y2 + z_1 \cdot z_2|}{\sqrt{x_1^2 + y_1^2 + z_1^2} \cdot \sqrt{x_2^2 + y_2^2 + z_2^2}}")

        text = Tex(r"Формула косинуса угла между прямыми. "
        r"Если $\vec{a}(x_1, y_1, z_1)$ и $\vec{b}(x_2, y_2, z_2)$ "
        r"направляющие векторы прямых $a$ и $b$, то"
        r"$$\cos(a,b) = \frac{|\vec{a} \cdot \vec{b}|}{|\vec{a}|\cdot|\vec{b}|}"
        r"\frac{|x_1 \cdot x_2 + y_1 \cdot y2 + z_1 \cdot z_2|}{\sqrt{x_1^2 + y_1^2 + z_1^2} \cdot \sqrt{x_2^2 + y_2^2 + z_2^2}}$$",
        font_size=32)
        #group = VGroup(text, cos)
        self.play(GrowFromCenter(text))
        self.wait()

class Equivalence(Scene):
    def construct(self):
        rplus = MathTex(r"(\mathbb{R}, +) ")
        simeq = MathTex(r"\simeq")
        rdot = MathTex(r"(\mathbb{R}^{+}, \cdot)")

        VGroup(rplus, simeq, rdot).arrange(RIGHT, buff=0.2).move_to(ORIGIN)

        self.play(FadeIn(rplus, shift=UP),
                GrowFromCenter(simeq),
                FadeIn(rdot, shift=DOWN))
        self.wait()

