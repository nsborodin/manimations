from manim import *
from networkx import depth_first_search
import numpy as np

class Diffraction(ThreeDScene):
    def construct(self):
        #self.set_camera_orientation(phi=80 * DEGREES, theta=-120* DEGREES)

        BEAM_COLOR = TEAL
        SOURCE_COLOR = GREY
        SLIT_COLOR = DARK_GREY

        CUBE_ANGLE = -3 * PI/16
        SLIT_ANGLE = 4 * PI/16
        CUBE_POSITION = np.array([-5, 0, 2])
        SLIT_POSITION = np.array([3, 0, -10])
        SPIRAL_POSITION = np.array([0, 0, -10])
        # 3D Cube

        source = Cube(side_length=1.5, fill_opacity=0.8, fill_color=SOURCE_COLOR)
        source.set_stroke(WHITE, 1)
        source.move_to(CUBE_POSITION)
        source.rotate(angle=CUBE_ANGLE, axis=DOWN)

        outer_shape = Rectangle(height=2, width=2)
        inner_hole = Triangle().scale(0.8)

        face = Cutout(outer_shape, inner_hole, fill_opacity=1, fill_color=SOURCE_COLOR)
        face.set_stroke(BLUE_E, 2)
        face.rotate(angle=PI/4, axis=DOWN)

        #slit = Prism(dimensions=[2,3,1], fill_color=SOURCE_COLOR)
        #slit.set_stroke(WHITE, 1)
        #slit.move_to(SLIT_POSITION)
        #slit.rotate(angle=SLIT_ANGLE, axis=DOWN)

        # Label — fixed orientation = always facing camera (flat), position still in 3D
        source_label = Tex(r"e$^{-}$/ion\\source", color=WHITE)
        source_label.next_to(source, 2*DOWN)
        #source_label.move_to(RIGHT)

        spiral = ParametricFunction(
                    lambda t: (
                        t,
                        np.cos(t),
                        np.sin(t)
                    ), color=RED, t_range = (-10, 10, 0.01)
                ).set_shade_in_3d(True)
        #spiral.rotate(angle=PI/2, axis=DOWN)
                
        #self.add(spiral)

        a=0.2
        R=1
        tube_r1 = 1
        tube_r2 = 0.1

        def helix_tube(u, v):
            r = np.array([a * u, u/40 * R * np.cos(u), u/40*R * np.sin(u)])
            L = np.sqrt(a**2 + R**2)
            T = np.array([a, -R * np.sin(u), R * np.cos(u)]) / L
            N = np.array([0, np.cos(u), np.sin(u)])
            B = np.cross(T, N)
            return r + tube_r1 * np.cos(v) * N + tube_r2 *np.sin(v) * B

        helix_surface = Surface(
            lambda u, v: helix_tube(u, v),
            u_range=[0, 40],
            v_range=[-TAU/2, TAU/2],
            resolution=(80, 24),
            fill_color=TEAL,
            fill_opacity=0.1,
            checkerboard_colors=False,
        )
        # Геометрический центр центральной линии r(u), не центр бокса — иначе ось не совпадает с визуальным центром
        u0, u1 = 0, 40
        centerline_center = np.array([
            a * (u0 + u1) / 2,
            (R / 40) * (u1 * np.sin(u1) + np.cos(u1) - u0 * np.sin(u0) - np.cos(u0)) / (u1 - u0),
            (R / 40) * (-u1 * np.cos(u1) + np.sin(u1) + u0 * np.cos(u0) - np.sin(u0)) / (u1 - u0),
        ])
        helix_surface.shift(SPIRAL_POSITION - centerline_center)

        # from scipy.special import jv  # J_{|ℓ|} — функция Бесселя первого рода

        # def bessel_beam(rho, phi, z, ell, p_perp, p_z, hbar=1.0):
        #     """ψ_ℓ^B(ρ, φ, z) = J_{|ℓ|}(p_⊥ ρ / ℏ) · exp(iℓφ) · exp(i p_z z / ℏ)."""
        #     x = p_perp * rho / hbar
        #     bessel_part = jv(abs(ell), x)
        #     phase_phi = np.exp(1j * ell * phi)
        #     phase_z = np.exp(1j * p_z * z / hbar)
        #     return bessel_part * phase_phi * phase_z

        # z0 = 0
        # ell, p_perp, p_z = 2, 1.0, 1.0

        # def intensity(rho, phi):
        #     psi = bessel_beam(rho, phi, z0, ell, p_perp, p_z)
            # return np.abs(psi) ** 2

        helix_surface.rotate(angle=-PI/4, axis=DOWN, about_point=SPIRAL_POSITION)
        # RIGHT, повёрнутый на PI/4 вокруг DOWN (формула Родрига)
        def rotated_vector(vec, axis, angle):
            a = np.asarray(axis) / np.linalg.norm(axis)
            return (
                np.asarray(vec) * np.cos(angle)
                + np.cross(a, vec) * np.sin(angle)
                + a * np.dot(a, vec) * (1 - np.cos(angle))
            )
        beam_axis = rotated_vector(RIGHT, DOWN, -PI / 4)

        # Ось вращения — через геометрический центр центральной линии (в SPIRAL_POSITION после сдвига и наклона)
        axis_length = 10.0
        rotation_axis_line = Line3D(
            start=SPIRAL_POSITION - axis_length * beam_axis,
            end=SPIRAL_POSITION + axis_length * beam_axis,
            color=YELLOW,
            thickness=0.06,
        )

        def create_prism_with_hole(width, height, depth, hole_scale):
            # Создаем детали БЕЗ цвета внутри функции, только геометрию
            outer_rect = Rectangle(width=width, height=height)
            inner_tri = Triangle().scale(hole_scale)

            # 1. Лицевые грани. Включаем shade_in_3d=True
            # Cutout наследует VMobject, так что параметр работает
            face_template = Cutout(outer_rect, inner_tri, shade_in_3d=True)
            front = face_template.copy().shift(OUT * depth/2)
            back = face_template.copy().shift(IN * depth/2)

            # 2. Внутренние стенки (щель)
            tri_verts = inner_tri.get_vertices()
            inner_walls = VGroup()
            for i in range(3):
                v1, v2 = tri_verts[i] + OUT*depth/2, tri_verts[(i+1)%3] + OUT*depth/2
                v3, v4 = v2 + IN*depth, v1 + IN*depth
                # Polygon тоже должен иметь shade_in_3d=True
                inner_walls.add(Polygon(v1, v2, v3, v4, shade_in_3d=True))
            
            # 3. Внешние боковые стенки
            rect_verts = outer_rect.get_vertices()
            outer_walls = VGroup()
            for i in range(4):
                v1, v2 = rect_verts[i] + OUT*depth/2, rect_verts[(i+1)%4] + OUT*depth/2
                v3, v4 = v2 + IN*depth, v1 + IN*depth
                outer_walls.add(Polygon(v1, v2, v3, v4, shade_in_3d=True))

            # Собираем всё в одну группу
            return VGroup(front, back, inner_walls, outer_walls)

        slit_prism = create_prism_with_hole(5, 5, 1, 1.75)
        slit_prism.set_fill(SOURCE_COLOR, opacity=0.3)
        slit_prism.set_stroke(LIGHT_GRAY, 1)

        slit_prism.rotate(angle=SLIT_ANGLE, axis=DOWN)
        slit_distance_from_spiral = 10
        slit_prism.move_to(SPIRAL_POSITION + beam_axis * slit_distance_from_spiral)

        self.add(source)
        self.add(rotation_axis_line)
        self.add(helix_surface)
        self.add(slit_prism)
        #self.add(face)
        self.add_fixed_orientation_mobjects(source_label)
        self.play(
            Rotate(helix_surface, angle=TAU, axis=-beam_axis, about_point=SPIRAL_POSITION),
            run_time=2,
            rate_func=linear,
        )
        self.wait(1)