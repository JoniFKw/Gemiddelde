from manim import *

# Creating of the starting table with data points
class AveragePart1(Scene): 
    def construct(self):
        self.skip_animations = True
        # 
        row_labels = [Text(f"{i}") for i in range(1, 10)]

        data_0 = Table(
            [["120", "1.0"],
             ["130", "1.0"],
             ["140", "1.0"],
             ["140", "1.5"],
             ["150", "1.5"],
             ["160", "1.5"],
             ["160", "2.0"],
             ["170", "2.0"],
             ["180", "2.0"]],
             col_labels=[MathTex(r"Lengte (= Y_{i})"), MathTex(r"Leeftijd (= X_{i})")], row_labels=row_labels,
             top_left_entry= MathTex(r"Respondentnummer (= {i})"), include_outer_lines=True,
        ).scale(0.6)
        self.add(data_0)
        self.wait(1)

        data = Table(
            [["120", "1.0"],
             ["130", "1.0"],
             ["140", "1.0"],
             ["140", "1.5"],
             ["150", "1.5"],
             ["160", "1.5"],
             ["160", "2.0"],
             ["170", "2.0"],
             ["180", "2.0"]],
             col_labels=[MathTex(r"Y_{i}"), MathTex(r"X_{i}")], row_labels=row_labels,
             top_left_entry= MathTex(r"{i}"), include_outer_lines=True,
        ).scale(0.6)

        self.play(ReplacementTransform(data_0, data), rate_functions=smooth)
        self.wait(1)

        data_target = data.copy()
        data_target.move_to(1.1*UP + 5.5*LEFT).scale(0.75)
        self.play(Transform(data, data_target))
        self.wait(1) 

# Numberline with points of data
class AveragePart2(Scene):
    def construct(self):
        numberLine = NumberLine(x_range=(110, 190, 10), length=7, color=GREEN_E, include_numbers=True, label_direction=DOWN,
                font_size=30, stroke_width=2)
        numberLine.shift(UP + RIGHT*1.5)
        
        self.play(Create(numberLine))
        self.wait(1)

        points = [(120, 1), (130, 1), (140, 1), (150, 1), (160, 1), (170, 1), (180, 1)]
        doubles = [140, 160]
        dots = VGroup()

        for x, y in points:
            dot = Dot(numberLine.number_to_point(x), color=RED, radius=0.05).shift(0.5*UP)
            dots.add(dot)
            
            if x in doubles:
                dot = Dot(numberLine.number_to_point(x), color=RED, radius=0.05).shift(UP*1)
                dots.add(dot)
        
        self.play(Create(dots), run_time=2)
        self.wait(1)
# 1 +2 can be made into each other, after 2 fade out 1

# Rotation of numberline plus dots and movement to the left. Then made full so from 0-190
class AveragePart3(Scene):
    def construct(self):
        numberLine = NumberLine(x_range=(110, 190, 10), length=7, color=GREEN_E, include_numbers=True, label_direction=DOWN,
                font_size=30, stroke_width=2)
        numberLine.shift(UP + RIGHT*1.5)
        
        self.play(Create(numberLine))
        self.wait(1)

        points = [(120, 1), (130, 1), (140, 1), (150, 1), (160, 1), (170, 1), (180, 1)]
        doubles = [140, 160]
        dots = VGroup()

        for x, y in points:
            dot = Dot(numberLine.number_to_point(x), color=RED, radius=0.05).shift(0.5*UP)
            dots.add(dot)
            
            if x in doubles:
                dot = Dot(numberLine.number_to_point(x), color=RED, radius=0.05).shift(UP*1)
                dots.add(dot)
        
        self.play(Create(dots), run_time=2)
        self.wait(1)
        
        self.play(ApplyMethod(numberLine.shift, 0.5*DOWN), ApplyMethod(dots.shift, 0.5*DOWN))
        self.play(Rotate(numberLine, angle= PI/2, about_point=numberLine.get_center(),rate_func=smooth),
                Rotate(dots, angle= PI/2, about_point=numberLine.get_center(), rate_func=smooth))      
        self.wait(1)

        for label in numberLine.numbers:
            label.rotate(-PI / 2, about_point=label.get_center())
            label.shift(LEFT * 0.8)

        for i, dot in enumerate(dots):
            if i == 3 or i == 6:
                dot.shift(RIGHT * 1.8)
            else:
                dot.shift(RIGHT * 1)
        
        self.wait(1)
        self.play(ApplyMethod(numberLine.shift, 7*LEFT), ApplyMethod(dots.shift, 7*LEFT), 
                  run_time=2)
        self.wait(1)

        full_numberline = NumberLine(x_range=(0, 190, 10), length=16, color=GREEN_E, include_numbers=True, label_direction=LEFT,
        font_size=30, stroke_width=2)
        full_numberline.rotate(PI / 2)
        full_numberline.move_to(numberLine.get_center()).shift(
            UP * (numberLine.number_to_point(190)[1] - full_numberline.number_to_point(190)[1] -0.11) + RIGHT*0.3 )

        # Align the labels of full_numberline
        for label in full_numberline.numbers:
            label.rotate(-PI / 2, about_point=label.get_center())
            label.shift(LEFT * 0.4 + UP*0.5)

        # Transform numberLine into full_numberline
        # self.play(Transform(numberLine, full_numberline))
        self.play(FadeOut(numberLine), FadeIn(full_numberline))
        self.wait(1)

# maybe fade out dots previously.

# Setting data on the according points then drawing lines. Scaling it and moving it to UL to then stack all the lines to create "total" with one line.
class AveragePart4(Scene):
    def construct(self):
        full_numberline = NumberLine(x_range=(0, 190, 10), length=16, color=GREEN_E, include_numbers=True, label_direction=LEFT,
        font_size=30, stroke_width=2)
        full_numberline.rotate(PI / 2)
        full_numberline.move_to(DOWN*4.5 +LEFT*6)

        for label in full_numberline.numbers:
            label.rotate(-PI / 2, about_point=label.get_center())
            label.shift(LEFT * 0.4 + UP*0.5)
        
        self.add(full_numberline)

        numberline_copy = full_numberline.copy()
        numberline_copy.move_to(6*LEFT).scale(0.46)

        self.play(Transform(full_numberline, numberline_copy))
        self.wait(1)

        points = [120, 130, 140, 140, 150, 160, 160, 170, 180]
        dots = VGroup()
        lines = VGroup()
        horizontal_shift = 1 * RIGHT

        for i, x in enumerate(points):
            dot = Dot(full_numberline.number_to_point(x), color=RED, radius=0.05).shift((i+1)*horizontal_shift)
            dots.add(dot)
            line = Line(start=dot.get_center(), end=full_numberline.number_to_point(0) + (i+1)*horizontal_shift, color=BLUE)
            lines.add(line)

        self.play(Create(dots), run_time=2)
        self.wait(1)
        self.play(Create(lines), run_time=2)
        self.play(FadeOut(dots))
        self.wait(1)

        group = VGroup(full_numberline, lines)
        self.play(group.animate.scale(0.15).to_edge(UL))
        self.wait(1)

        previous_line_end = UP * 3.8  # Start position for the first line at the top
        for i, line in enumerate(lines):
            line_target = line.copy().move_to(previous_line_end + DOWN * (line.get_length() / 2))
            self.play(Transform(line, line_target), run_time=0.5)
            previous_line_end = line_target.get_end()  # Update the end position for the next line
        self.wait(1)

# Stack the lines on top of each other
class AveragePart5(Scene):
    def construct(self):
        original_line = Line(start=[0, -3.8, 0], end=[0, 3.8, 0], color=BLUE)
        
        # Splitting into 9 equal parts
        lines = VGroup()
        for i in range(9):
            part = Line(
                start=original_line.point_from_proportion(i / 9),
                end=original_line.point_from_proportion((i + 1) / 9),
                color=BLUE
            )
            lines.add(part)
        
        # Arrange the parts vertically with no space in between
        lines.arrange(DOWN, buff=0)
        
        # Add the lines to the scene
        self.add(lines)

        movement = 0.5
        numbers = VGroup()

        # Moving the lines for clear visibility of 9 equal parts and writing their number underneath as well
        for i, line in enumerate(lines):
            self.play(line.animate.shift(RIGHT*(-5+movement)+ (line.get_start()[1] - 0) * DOWN), run_time=0.5)
            number = Text(f"{i + 1}", font_size=24, color=WHITE)
            number.next_to(line, DOWN)
            numbers.add(number)
            self.play(FadeIn(number), run_time=0.5)
            movement+=1

        self.wait(1)
        self.play(FadeOut(numbers))
        self.wait(1)

        self.play(FadeOut(lines[1:]))
        self.wait(1)


# Scaling back and putting in the center. The average line is scaled accordingly and put back such that a dashed line represents the average. 
class AveragePart6(Scene):
    def construct(self):
        # Constructing the original numberline and where it last what placed
        full_numberline = NumberLine(x_range=(0, 190, 10), length=16, color=GREEN_E, include_numbers=True, label_direction=LEFT,
        font_size=30, stroke_width=2)
        full_numberline.rotate(PI / 2)
        full_numberline.move_to(DOWN*4.5 +LEFT*6)

        for label in full_numberline.numbers:
            label.rotate(-PI / 2, about_point=label.get_center())
            label.shift(LEFT * 0.4 + UP*0.5)

        numberline_scaled = full_numberline.copy()
        numberline_scaled.move_to(6*LEFT).scale(0.46)
        self.add(numberline_scaled)
        self.play(numberline_scaled.animate.scale(0.15).to_edge(UL))

        # Aligning with the starting and end points of the previous found line
        average_line = Line(start=[-4.5, 0, 0], end=[-4.5, 0.844444, 0], color=BLUE) 
        self.add(average_line)
        self.wait(1)

        y_axis_zero = numberline_scaled.number_to_point(0)[1]
        self.play(average_line.animate.scale(1.02).shift(UP * (y_axis_zero - average_line.get_start()[1]) + LEFT*2))
        self.wait(1)

        group = VGroup(numberline_scaled, average_line)
        self.play(group.animate.scale(6.5).shift(3*DOWN + 5*RIGHT))
        self.wait(1)

        dashed_line = DashedLine(start=numberline_scaled.number_to_point(150), end=numberline_scaled.number_to_point(150) + RIGHT*20, dash_length=0.2, color=WHITE)
        self.play(Create(dashed_line))
        self.wait(1)



class Average1(Scene):
    def construct(self):
        row_labels = [Text(f"{i}") for i in range(1, 10)]
        # Constructing of the oriiginal datapoints in a table
        data_0 = Table(
            [["120", "1.0"],
             ["130", "1.0"],
             ["140", "1.0"],
             ["140", "1.5"],
             ["150", "1.5"],
             ["160", "1.5"],
             ["160", "2.0"],
             ["170", "2.0"],
             ["180", "2.0"]],
             col_labels=[MathTex(r"Lengte (= Y_{i})"), MathTex(r"Leeftijd (= X_{i})")], row_labels=row_labels,
             top_left_entry= MathTex(r"Respondentnummer (= {i})"), include_outer_lines=True,
        ).scale(0.6)
        self.add(data_0)
        self.wait(1)

        # refining table by removing redundant information
        data = Table(
            [["120", "1.0"],
             ["130", "1.0"],
             ["140", "1.0"],
             ["140", "1.5"],
             ["150", "1.5"],
             ["160", "1.5"],
             ["160", "2.0"],
             ["170", "2.0"],
             ["180", "2.0"]],
             col_labels=[MathTex(r"Y_{i}"), MathTex(r"X_{i}")], row_labels=row_labels,
             top_left_entry= MathTex(r"{i}"), include_outer_lines=True,
        ).scale(0.6)

        self.play(ReplacementTransform(data_0, data), rate_functions=smooth)
        self.wait(1)

        # Scaling it in the UL
        data_target = data.copy()
        data_target.move_to(1.1*UP + 5.5*LEFT).scale(0.75)
        self.play(Transform(data, data_target))
        self.wait(1)             
        
        # Ask the question on how to calculate the average
        average_question = Text("Wat is het gemiddelde van deze datapunten?").scale(0.5)
        self.play(Create(average_question.to_edge(UR)))
        self.wait(2)
        
        # Give the formula for it
        average_calculation = MathTex(r"\overline{Y} = \frac{\sum_{i=1}^{n} Y_{i}}{n}").scale(0.6).next_to(average_question, DOWN)
        self.play(Create(average_calculation))
        self.wait(2)

        # Keep formula always visible for reference and to remember original goal
        self.play(FadeOut(average_question), average_calculation.animate.to_edge(DR))
        self.wait(1)

        numberLine = NumberLine(x_range=(110, 190, 10), length=7, color=GREEN_E, include_numbers=True, label_direction=DOWN,
                font_size=30, stroke_width=2)
        numberLine.shift(UP + RIGHT*1.5)
        
        self.play(Create(numberLine))
        self.wait(1)

        # creating dots on the numberline
        points = [(120, 1), (130, 1), (140, 1), (150, 1), (160, 1), (170, 1), (180, 1)]
        doubles = [140, 160]
        dots = VGroup()

        for x, y in points:
            dot = Dot(numberLine.number_to_point(x), color=RED, radius=0.05).shift(0.5*UP)
            dots.add(dot)
            
            if x in doubles:
                dot = Dot(numberLine.number_to_point(x), color=RED, radius=0.05).shift(UP*1)
                dots.add(dot)
        
        self.play(Create(dots), run_time=2)
        self.wait(1)  

        self.play(FadeOut(data))
        
        # Rotating the numberline, dots and labels and moving them as well
        self.play(ApplyMethod(numberLine.shift, 0.5*DOWN), ApplyMethod(dots.shift, 0.5*DOWN))
        self.play(Rotate(numberLine, angle= PI/2, about_point=numberLine.get_center(),rate_func=smooth),
                Rotate(dots, angle= PI/2, about_point=numberLine.get_center(), rate_func=smooth))      
        self.wait(1)

        for label in numberLine.numbers:
            label.rotate(-PI / 2, about_point=label.get_center())
            label.shift(LEFT * 0.8)

        for i, dot in enumerate(dots):
            if i == 3 or i == 6:
                dot.shift(RIGHT * 3)
            else:
                dot.shift(RIGHT * 1.5)
        
        self.wait(1)

        # Moving the numberline and dots to the left
        self.play(ApplyMethod(numberLine.shift, 7*LEFT), ApplyMethod(dots.shift, 7*LEFT), 
                  run_time=2)
        self.wait(1)

        # Making a new numberline such that is ranges from 0-190
        full_numberline = NumberLine(x_range=(0, 190, 10), length=16.625, color=GREEN_E, include_numbers=True, label_direction=LEFT,
        font_size=30, stroke_width=2)
        full_numberline.rotate(PI / 2)
        full_numberline.move_to(numberLine.get_center()).shift(
            UP * (numberLine.number_to_point(190)[1] - full_numberline.number_to_point(190)[1]) + RIGHT*0.25 )

        # Align the labels of full_numberline
        for label in full_numberline.numbers:
            label.rotate(-PI / 2, about_point=label.get_center())
            label.shift(LEFT * 0.4 + UP*0.5)

        # Transform numberLine into full_numberline
        self.play(FadeOut(numberLine), FadeIn(full_numberline))

        # moving the dots to the right and setting their i-th position for clearity above it
        ith_points = VGroup()
        for i, dot in enumerate(dots):
            if i == 3 or i == 6:
                self.play(dot.animate.shift(RIGHT * (i-1)), run_time=0.5)
                text = MathTex(f"i = {i + 1}", font_size=24, color=WHITE)
                text.next_to(dot, UP)
                ith_points.add(text)
                self.play(FadeIn(text), run_time=0.5)
            else:
                self.play(dot.animate.shift(RIGHT * i), run_time=0.5)
                text = MathTex(f"i = {i + 1}", font_size=24, color=WHITE)
                text.next_to(dot, UP)
                ith_points.add(text)
                self.play(FadeIn(text), run_time=0.5)

        lines = VGroup()

        # drawing the lines from the dots to the x-axis
        for i, dot in enumerate(dots):
            line = Line(start=dot.get_center(), end=[dot.get_center()[0], full_numberline.number_to_point(0)[1], 0], color=BLUE)
            lines.add(line)

        self.play(Create(lines), run_time=2)

        self.play(FadeOut(dots), FadeOut(ith_points))
        self.wait(1)

        # Scaling the numberline and lines and moving them to UL
        group = VGroup(full_numberline, lines)
        self.play(group.animate.scale(0.065).to_edge(UL))
        self.wait(1)

        # Formula for sigma Yi
        sigma_y = MathTex(r"\sum_{i=1}^{9} Y_{i} = Y_{1} + Y_{2} + Y_{3} + Y_{4} + Y_{5} + Y_{6} + Y_{7} + Y_{8} + Y_{9}").scale(0.4).to_edge(DL + UP)
        self.play(Create(sigma_y))
        self.wait(1)

        # Stacking all the lines from on top of each other 
        previous_line_end = UP * 3.9  
        for i, line in enumerate(lines):
            line_target = line.copy().move_to(previous_line_end + DOWN * (line.get_length() / 2))
            self.play(Transform(line, line_target), run_time=0.5)
            previous_line_end = line_target.get_end()  # Update the end position for the next line
        
        original_line = Line(start=[0, 3.9, 0], end=[0, -3.77812, 0], color=BLUE)
        self.play(ReplacementTransform(lines, original_line))

        # Filling in sigma Yi
        sigma_y_values = MathTex(r"\sum_{i=1}^{9} Y_{i} = 120 + 130 + 140 + 140 + 150 + 160 + 160 + 170 + 180 = 1350").scale(0.4).next_to(sigma_y, DOWN)
        sigma_y_values.shift(0.5*RIGHT)
        self.play(Create(sigma_y_values))
        self.wait(1) 

        total_value = MathTex(r"\sum_{i=1}^{9} Y_{i} = 1350").scale(0.4).next_to(lines, RIGHT)
        self.play(Create(total_value))
        self.wait(2)

        # Calculation for sigma Yi is now UR
        self.play(FadeOut(sigma_y), FadeOut(total_value), sigma_y_values.animate.to_edge(UR + 0.2*LEFT))
        
        # Pop the calculation for average to remind people
        self.play(Indicate(average_calculation, scale_factor=1.2, color=BLUE), run_time=1.5)
        self.wait(1)

        # Refering to the formula for the average that 1350/9
        filling_in = MathTex(r"\overline{Y} = \frac{\sum_{i=1}^{9} Y_{i}}{n} = \frac{1350}{9}").scale(0.4).next_to(sigma_y_values, DOWN)
        self.play(Create(filling_in))

        # Splitting into 9 equal parts
        lines = VGroup()
        for i in range(9):
            part = Line(
                start=original_line.point_from_proportion(i / 9),
                end=original_line.point_from_proportion((i + 1) / 9),
                color=BLUE
            )
            lines.add(part)
        
        # Arrange the parts vertically with no space in between
        lines.arrange(DOWN, buff=0)
        
        # Add the lines to the scene
        self.add(lines)
        self.play(FadeOut(original_line))

        movement = 0.5

        # Moving the lines for clear visibility of 9 equal parts and writing their number underneath as well
        for i, line in enumerate(lines):
            self.play(line.animate.shift(RIGHT*(-5+movement)+ (line.get_start()[1] - 0) * DOWN), run_time=0.5)
            movement+=1
        self.wait(1)

        final_calculation = MathTex(r"\overline{Y} = 150").scale(0.4).next_to(filling_in, DOWN)
        self.play(Create(final_calculation))
        self.play(FadeOut(lines[1:]))
        
        average_line = lines[0]

        self.play(final_calculation.animate.next_to(average_line, RIGHT), FadeOut(average_calculation, sigma_y_values, filling_in))
        self.wait(1)

        average = VGroup(average_line, final_calculation)

        self.play(average.animate.shift(UP * (full_numberline.number_to_point(0)[1] - average_line.get_end()[1]) + LEFT*2))
        self.wait(1)

        group = VGroup(full_numberline, average_line)
        self.play(group.animate.scale(6.5).shift(3.2*DOWN + 5*RIGHT), final_calculation.animate.scale(2).shift(3.2*DOWN + 6*RIGHT))
        self.wait(1)

        dashed_line = DashedLine(start=full_numberline.number_to_point(150), end=full_numberline.number_to_point(150) + RIGHT*20, dash_length=0.2, color=WHITE)
        self.play(Create(dashed_line))
        self.wait(1)
