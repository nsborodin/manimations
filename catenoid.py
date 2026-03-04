from manim import GREY
from manim import *
import numpy as np

class Catenoid(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()
        labels = axes.get_axis_labels(
            x_label="x", 
            y_label="y", 
            z_label="z"
        )

        SOURCE_COLOR = WHITE

        N = 200

        B = ValueTracker(N)

        angle_tracker = ValueTracker(0)

        def get_t():
            current_B = B.get_value()
            k = 2 * PI * current_B / N + 0.01
            return PI * (np.cos(k - np.sin(2 * k) / 2) + 1) / 4

        n = 1

        def figure(u, v, t_param):
            

            nu = n * u

            f = np.cos(t_param) * np.sinh(v) * np.sin(nu) + np.sin(t_param) * np.cosh(v) * np.cos(nu)
            g = -np.cos(t_param) * np.sinh(v) * np.cos(nu) + np.sin(t_param) * np.cosh(v) * np.sin(nu)
            h = nu * np.cos(t_param) + v * np.sin(t_param)

            theta = angle_tracker.get_value()

            f_rot = f * np.cos(theta) - g * np.sin(theta)
            g_rot = f * np.sin(theta) + g * np.cos(theta)
            h_rot = h

            #z_offset = 2 * PI - abs(theta - 2 * PI)
            z_offset = 3 * np.sin(theta/4)

            return np.array([f_rot, g_rot, h_rot]) #+ np.array([0, 0, z_offset])

        a = PI/2
        b = PI

        catenoid = always_redraw(lambda: Surface(
            lambda u, v: figure(u, v, get_t()),
            u_range=[-b, b],
            v_range=[-a, a],
            resolution=(n*32, 16),
            checkerboard_colors=False,
            shade_in_3d=False, 
        ).set_fill("#000000", opacity=1)
         .set_stroke(WHITE, width=3, opacity=1)
         .set_reflectance(0) 
        )
        
        # Полностью выключаем все источники света в сцене
        self.camera.light_source.set_color(BLACK) 
        #self.camera.set_ambient_light(color=BLACK) # Выключаем фоновый свет
        #self.camera.frame.move_to([2, 1, 0])

        self.set_camera_orientation(phi=0*DEGREES, theta=-0*DEGREES, zoom=1)

        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        
        def get_k_val():
            return 2 * PI * B.get_value() / N + 0.01
        def get_s_val():
            return (PI / 2 - get_t()) / 2

        # phi.add_updater(lambda m: m.set_value(
        #     PI/2 - ( get_s_val()/4)
        # ))

        # theta.add_updater(lambda m: m.set_value(
        #     get_k_val() - PI/2
        # ))

        # gamma.add_updater(lambda m: m.set_value(
        #     get_k_val() 
        # ))


        self.add(catenoid)
        #self.add(gamma)
        #self.add(axes, labels,gamma)
        
        #self.play(gamma.animate.set_value(1))
        #self.play(distance_to_origin.animate.set_value(2))
        #self.play(focal_distance.animate.set_value(1.5))
        # self.play(phi.animate.set_value(45*DEGREES))
        # self.play(theta.animate.set_value(135*DEGREES))
        # self.play(
        #     focal_distance.animate.set_value(1.5),
        #     B.animate.set_value(1),
        #     angle_tracker.animate.set_value(4*PI),
        #     lag_ratio=0,
        #     run_time=5,
        #     rate_func=linear
        # )

        self.play(
            focal_distance.animate.set_value(1.5),
            B.animate.set_value(1),
            angle_tracker.animate.set_value(4*PI),
            run_time=5,
            rate_func=linear
        )
        # self.play(phi.animate.set_value(0*DEGREES))
        # self.play(theta.animate.set_value(0*DEGREES))

        # B = ValueTracker(N)

        # self.play(
        #     B.animate.set_value(1),
        #     angle_tracker.animate.set_value(4*PI),
        #     run_time=5,
        #     rate_func=linear
        # )
        

        self.wait()
        #self.interactive_embed()