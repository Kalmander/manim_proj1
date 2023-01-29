from manim import *

class SquareToCircle(Scene):
    def construct(self):
        finite_sum = MathTex(r"1 + \frac{1}{4} + \frac{1}{9}")
        x_finite_sum = MathTex(r"x_1 + x_2 + x_3")
        sigma_finite_sum = MathTex(r"\Sigma_{n=1}^{3} x_n")

        self.play(Create(finite_sum))
