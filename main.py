from manim import * 

class Introduction(Scene):
    def construct(self):
        circ = Circle()
        self.add(circ)
        self.wait(3)

class AddAndRemoveMethods(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.wait(4)
        self.remove(square)
        self.wait(2)

class BackgroundColor(Scene):
    def construct(self):

        self.camera.background_color = DARK_GREY

        config.background_color = DARK_GREY

        line_1 = Line()
        self.add(line_1)
        self.wait(3)

        line_2 = Line(DOWN, UP)
        self.add(line_2)
        self.wait(3)

        self.remove(line_1, line_2)
        self.wait(3)

class FadeAnimation(Scene):
    def construct(self):
        circ = Circle(radius=2)
        self.play(FadeIn(circ))
        self.wait()
        self.play(FadeOut(circ))

        square = Square(side_length=3)
        self.play(FadeIn(square))
        self.wait()
        self.play(FadeOut(square))

        line = Line(LEFT, RIGHT + UP)
        self.play(FadeIn(line))
        self.wait()
        self.play(FadeOut(line))
        self.wait(3)

class PolygonalShapes(Scene):
    def construct(self):
        rectangle = Rectangle(height=2, width=3)
        self.play(FadeIn(rectangle))
        self.wait()

        regular_polygon = RegularPolygon(n=8, radius=1.5)
        self.play(FadeIn(regular_polygon), FadeOut(rectangle))
        self.wait()

        triangle = Triangle(radius=2)
        self.play(FadeIn(triangle), FadeOut(regular_polygon))
        self.wait()

        polygon = Polygon(DOWN + 2 * LEFT, UP + LEFT, ORIGIN, UP + RIGHT, DOWN + 2 * RIGHT)
        self.play(FadeIn(polygon), FadeOut(triangle))
        self.wait(3)

class ArcShapes(Scene):
    def construct(self):
        arc = Arc(
            radius=2,
            start_angle=PI / 4,
            angle=PI / 3
        )
        self.play(FadeIn(arc))
        self.wait()

        dot = Dot(radius=0.05)
        self.play(FadeIn(dot))
        self.wait()

        ellipse = Ellipse(height=2, width=4)
        self.play(FadeIn(ellipse))
        self.wait()

        annulus = Annulus(
            outer_radius=1,
            inner_radius=0.8
        )
        self.play(FadeIn(annulus))
        self.wait()

        sector = Sector(
            radius=0.8,
            angle=PI / 6
        )
        self.play(FadeIn(sector))
        self.wait(3)

class ArrowShapes(Scene):
    def construct(self):
        arrow = Arrow(LEFT + 3*RIGHT, tip_length=0.2)
        self.play(FadeIn(arrow))
        self.wait()
        self.play(FadeOut(arrow))

        double_arrow = DoubleArrow(2 * LEFT, 2 * RIGHT, tip_length=0.4)
        self.play(FadeIn(double_arrow))
        self.wait()
        self.play(FadeOut(double_arrow))

        curved_arrow = CurvedArrow(3 * LEFT, 3 * RIGHT, radius=10)
        self.play(FadeIn(curved_arrow))
        self.wait()
        self.play(FadeOut(curved_arrow))

        curved_double_arrow = CurvedDoubleArrow(2 * DOWN, 2 * UP)
        self.play(FadeIn(curved_double_arrow))
        self.wait(3)

class DecorativeShapes(Scene):
    def construct(self):
        dashed_line_1 = DashedLine(ORIGIN, 3 * UP)
        self.play(FadeIn(dashed_line_1))
        self.wait()

        dashed_line_2 = DashedLine(2 * LEFT, 2 * RIGHT, dash_length=0.2)
        self.play(FadeIn(dashed_line_2))
        self.wait()

        right_angle = RightAngle(dashed_line_1, dashed_line_2)
        self.play(FadeIn(right_angle))
        self.wait()

        line = Line(ORIGIN, 2 * UP + 1.5 * RIGHT)
        self.play(FadeOut(dashed_line_1, right_angle),
            FadeIn(line))
        self.wait()

        angle = Angle(dashed_line_2, line, radius=0.7)
        self.play(FadeIn(angle))
        self.wait()

        rounded_rect = RoundedRectangle(corner_radius=0.12)
        self.play(FadeOut(angle, dashed_line_2, line),
            FadeIn(rounded_rect))
        self.wait()
        self.play(FadeOut(rounded_rect))

        star = Star(n=5)
        self.play(FadeIn(star))
        self.wait()

        circ = DashedVMobject(Circle(radius=2), num_dashes=50)
        self.play(FadeIn(circ))
        self.wait(3)

class BezierAndRounded(Scene):
    def construct(self):
        spline = CubicBezier(
            3 * LEFT,
            4 * UP,
            3 * RIGHT + 2 * DOWN,
            4 * RIGHT + 3 * UP
        )
        self.play(FadeIn(spline))
        self.wait()

        star = Star(n=7).round_corners(radius=0.1)
        self.play(FadeIn(star))
        self.wait()

        triangle = Triangle(radius=2)
        triangle.round_corners(radius=0.05)
        self.play(FadeIn(triangle))
        self.wait(3)

class AnimationAttributes(Scene):
    def construct(self):
        circ = Circle()
        line = Line()
        dot = Dot()

        self.play(FadeIn(dot), run_time=1)
        self.wait(1)
        self.play(FadeIn(circ, shift=UP), run_time=1.5)
        self.wait(0.5)
        self.play(FadeIn(line, shift=RIGHT), run_time=2)
        self.wait()
        self.play(
            FadeOut(line, run_time=1.2), 
            FadeOut(circ, run_time=2, shift=UP)
        )
        self.wait()
        self.play(FadeOut(line, circ, dot, shift=UP), run_time=1.5)
        self.wait(3)

class CreationUncreationGrow(Scene):
    def construct(self):
        arrow = Arrow()
        circ = Circle(1.5)
        square = Square(3)
        polygon = Polygon(2 * UP, ORIGIN, 2 * RIGHT)

        self.play(Create(arrow))
        self.wait()
        self.play(Uncreate(arrow))
        self.play(Create(circ), run_time=2)
        self.wait()
        self.play(Uncreate(circ), run_time=2)
        self.wait()
        self.play(GrowFromCenter(square))
        self.wait()
        self.play(GrowFromCenter(polygon))
        self.wait(3)

class GrowingCircles(Scene):
    def construct(self):
        dot = Circle(0.01)
        circ = Circle(1)
        circ2 = Circle(2)
        circ3 = Circle(3)

        self.play(FadeIn(dot))
        self.play(GrowFromCenter(circ), run_time=1.5)
        self.play(GrowFromCenter(circ2), run_time=1)
        self.play(GrowFromCenter(circ3), run_time=1)
        self.wait()
        
class PolyhedraSquare(Scene):
    def construct(self):
        UR = UP + RIGHT
        UL = UP + LEFT
        DR = DOWN + RIGHT
        DL = DOWN + LEFT

        diag = np.sqrt(2)
        UR = UR / diag
        UL = UL / diag
        DR = DR / diag
        DL = DL / diag

        vertices = [
            UP,
            UR,
            RIGHT,
            DR,
            DOWN,
            DL,
            LEFT,
            UL
        ]
        vertices = [2 * vertex for vertex in vertices]
        polygon = Polygon(*vertices, color=BLUE)
        sq = Square(side_length=2*np.sqrt(2), stroke_width=2)
        circ = Circle(np.sqrt(2))
        tr = Triangle(radius=np.sqrt(2))

        self.play(GrowFromCenter(polygon))
        self.play(FadeIn(sq))
        self.play(Create(circ))
        self.play(GrowFromCenter(tr))
        self.wait()

def rotate_point(point, angle):
    """Поворачивает точку на заданный угол вокруг начала координат"""
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)
    x, y = point[0], point[1]
    return np.array([
        x * cos_a - y * sin_a,
        x * sin_a + y * cos_a,
        0
    ])

class TriangleAngle(Scene):
    def construct(self):
        radius = 3
        start = ORIGIN - radius * UP
        tr = Polygon(
            start,
            radius * LEFT,
            radius * UP
        )
        tr.rotate(PI/4, about_point=ORIGIN)
        circ = Circle(radius)

        vertices = tr.get_vertices()

        side1 = Line(vertices[0], vertices[1])
        side2 = Line(vertices[1], vertices[2])
        side3 = Line(vertices[2], vertices[0])

        right_angle = RightAngle(
            side1,
            side2,
            length=0.4,
            quadrant=(-1,1),
            stroke_width=3
        )
        #angle = Angle()
        '''
        a,b = 3, 4
        r = max(a, b)
        tr = Polygon(
            ORIGIN - r * UP,
            r * RIGHT,
            (a/r) * RIGHT + (b/r) * UP
        )
        '''
        self.play(Create(circ))
        self.play(GrowFromCenter(tr))
        self.play(GrowFromCenter(right_angle))
        #self.play(tr.animate.rotate(PI/4, about_point=ORIGIN), run_time=2)

class TriangleMorph(Scene):
    def construct(self):
        radius = 3
        circ = Circle(radius)
        original_points = [
            ORIGIN - radius * UP,
            radius * LEFT,
            radius * UP
        ]

        rotated_points = [rotate_point(p, PI/4) for p in original_points]
        tr1 = Polygon(*original_points)
        tr2 = Polygon(*rotated_points)

        self.play(GrowFromCenter(tr1))
        self.play(Create(circ))
        self.wait()
        self.play(Transform(tr1, tr2), run_time=2)
        self.wait()

class TriangleRotate(Scene):
    def construct(self):
        radius = 3
        circ = Circle(radius)

        original_points = [
            ORIGIN - radius * UP,
            radius * LEFT,
            radius * UP
        ]

        rotated_points = [rotate_point(p, PI/4) for p in original_points]
        tr1 = Polygon(*original_points)
        tr2 = Polygon(*rotated_points)

        self.play(GrowFromCenter(tr1))
        self.play(Create(circ))
        self.wait()
        self.play(Transform(tr1, tr2), run_time=2)
        self.wait()

class TriangleSmooth(Scene):
    def construct(self):
        radius = 3
        circ = Circle(radius)
        
        num_steps = 20
        angles = np.linspace(0, 2*PI, num_steps)
        triangles = []

        for angle in angles:
            points = [
                rotate_point(ORIGIN - radius * UP, angle),
                rotate_point(radius * LEFT, angle),
                rotate_point(radius * UP, angle)
            ]
            triangles.append(Polygon(*points))

        self.add(circ)
        self.play(GrowFromCenter(triangles[0]))

        for i in range(len(triangles) - 1):
            self.play(Transform(triangles[i], triangles[i + 1]), run_time=0.1)
            #self.remove(triangles[i])

        self.wait()

class StarArcs(Scene):
    def construct(self):
        num=20
        star = Star(n=num)

        # if (num % 8) in [2, 6]:  # 6, 10, 14, 18, 22...
        #     shift = PI / num
        # else:  # 8, 12, 16, 20, 24...
        #     shift = 2 * PI / num

        shift = (PI/2) % (2 * PI / num)

        #angles = np.linspace(2*PI/num, 2 * PI + 2*PI/num, num_steps + 1)
        angles = [i * 2 * PI / num for i in range(0, num, 2)]
        arc_start_angles = [angle + shift for angle in angles]
        arcs = []

        for angle in arc_start_angles:
            arc = Arc(
                radius=1,
                start_angle=angle,
                angle=2 * PI / num
            )
            arcs.append(arc)

        self.play(GrowFromCenter(star))
        for i in range(len(arcs)-1):
            self.play(Create(arcs[i]))
            self.wait()

class StarArcs2(Scene):
    def construct(self):
        num = 10
        star = Star(n=num)
        
        self.play(GrowFromCenter(star))
        
        # Создаем дуги напрямую
        for i in range(num // 2):
            arc = Arc(
                radius=1,
                start_angle=i * 2 * PI / num ,
                angle=2 * PI / num
            )
            self.play(Create(arc))
        
        self.wait()

class CircAxes(Scene):
    def construct(self):
        radius = 2
        circ = Circle(radius)

        self.play(Create(circ))
        arrowX = Arrow((radius + 1)*LEFT, (radius + 1)*RIGHT, tip_length=0.2)
        arrowY = Arrow((radius + 1)*DOWN, (radius + 1)*UP, tip_length=0.2)
        self.play(FadeIn(arrowX))
        self.wait()
        self.play(FadeIn(arrowY))
        self.wait()

        curved_arrow = Arc(
            radius=radius + 1, 
            start_angle=0,
            angle=PI/2)
        curved_arrow = CurvedArrow(
            start_point=(radius + 0.25) * RIGHT,
            end_point=(radius + 0.25) * UP,
            tip_length=0.15
        )
        self.play(FadeIn(curved_arrow))

class AnglesLines(Scene):
    def construct(self):
        #line1 = Line(LEFT-2, RIGHT+2)
        #line2 = Line(2*LEFT, 2*RIGHT)
        start1 = np.array([-3,-3,0])
        end1 = np.array([3,3,0])
        start2 = np.array([-2,0,0])
        end2 = np.array([2,0,0])

        line1 = Line(start1, end1)
        line2 = Line(start2, end2)
        self.play(Create(line1))
        self.play(Create(line2))

        angle = Angle(line2, line1, radius=0.7)
        self.play(Create(angle))

def create_polygon_from_normals(normal_angles, distances):
    vertices = []
    n = len(normal_angles)

    for i in range(n):
        angle1 = normal_angles[i]
        angle2 = normal_angles[(i + 1) % n]
        dist1 = distances[i]
        dist2 = distances[(i + 1) % n]

        a1, b1, c1 = np.cos(angle1), np.sin(angle1), dist1
        a2, b2, c2 = np.cos(angle2), np.sin(angle2), dist2

        det = a1 * b2 - a2 * b1
        if abs(det) > 1e-10:
            x = (c1 * b2 - c2 * b1) / det
            y = (a1 * c2 - a2 * c1) / det
            vertices.append(np.array([x, y, 0]))
    
    return vertices

class CircleInTriangle(Scene):
    def construct(self):
        radius = 1
        circ = Circle(radius=radius)
        dot = Dot(radius=0.04)

        normal_angles = [PI/4 + 0.1, PI, 3 * PI/2]
        distances = [radius, radius, radius]

        vertices = create_polygon_from_normals(normal_angles, distances)
        tr = Polygon(*vertices)

        self.play(Create(tr))
        self.play(GrowFromCenter(circ))
        self.play(GrowFromCenter(dot))

        side1 = Line(vertices[0], vertices[1])
        center = side1.get_center()
        direction = side1.get_unit_vector()
        perp = np.array([-direction[1], direction[0], 0]) * 0.1

        tick = Line(center - 0.05*direction - perp, center - 0.05*direction + perp)

        side2 = Line(vertices[1], vertices[2])
        center = side2.get_center()
        direction = side2.get_unit_vector()
        perp = np.array([-direction[1], direction[0], 0]) * 0.1

        #self.play(GrowFromPoint(tick, tick.get_center() + RIGHT))

        self.play(FadeIn(tick, run_time=2, shift=RIGHT))
        tick1 = Line(center - 0.05*direction - perp, center - 0.05*direction + perp)
        tick2 = Line(center + 0.05*direction - perp, center + 0.05*direction + perp)

        self.play(GrowFromPoint(tick1, tick1.get_center() + DOWN), GrowFromPoint(tick2, tick2.get_center() + DOWN))

class Hex(Scene):
    def construct(self):
        num_sides = 6
        radius = 2
        vertices = [
            radius * np.array([
                np.cos(2 * np.pi * i / num_sides),
                np.sin(2 * np.pi * i / num_sides),
                0
            ])
            for i in range(num_sides)
        ]
        hex = Polygon(*vertices)
        
        self.play(GrowFromCenter(hex))

        dotted = DashedVMobject(Line((radius + 1) * DOWN, (radius + 1) * UP),num_dashes=50)

        self.play(Create(dotted))

        curv = CurvedDoubleArrow( np.array([radius/2, radius, 0]), np.array([-radius/2, radius, 0]), tip_length = 0.15, radius = 2.5)

        self.play(FadeIn(curv, run_time=2, shift=DOWN))

class YtLogo(Scene):
    def construct(self):
        rounded_rect = DashedVMobject(RoundedRectangle(corner_radius=1, height=5, width=8), num_dashes=100)
        self.play(GrowFromCenter(rounded_rect))
        self.wait()
        tr = Polygon(RIGHT, DOWN + LEFT, UP + LEFT)
        tr.move_to(ORIGIN)
        tr.round_corners(radius=0.2)
        self.play(GrowFromCenter(tr))
        
class BezierVector(Scene):
    def construct(self):
        spline = CubicBezier(
            3 * LEFT + 3 * DOWN,
            5 * UP + LEFT,
            3 * RIGHT +5 * DOWN,
            4 * RIGHT + 3 * UP
        )
        self.play(Create(spline))

        vec = Arrow(3 * LEFT + 3 * DOWN, 4 * RIGHT + 3 * UP, tip_length=0.2)
        self.play(Create(vec))

class Smile(Scene):
    def construct(self):
        circ = Circle(2)

        self.play(Create(circ))

        mouth = Arc(
            radius=2-0.5,
            start_angle = PI + PI/6, 
            angle = PI - 2 * PI/6
        )
        #mouth.move_to(ORIGIN)
        self.play(Create(mouth))

        eye1 = Arc(
            radius = 1,
            start_angle = PI/2 - PI/6,
            angle = 2*PI/6
        )
        eye1.move_to(0.75*LEFT + 1.1*UP)
        eye1.rotate(PI/24)
        self.play(GrowFromCenter(eye1))

        eye2 = Arc(
            radius = 1,
            start_angle = PI/2 - PI/6,
            angle = 2*PI/6
        )
        eye2.move_to(0.75*RIGHT + 1.1*UP)
        eye2.rotate(-PI/24)
        self.play(GrowFromCenter(eye2))

        nose = Ellipse(height=0.3, width=0.4)
        self.play(Create(nose))