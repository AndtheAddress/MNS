from manim import *
from numpy import random, sin

config.media_width = "100%"
config.verbosity = "WARNING"



%%manim -qm RLS_demo

class RLS_demo(Scene):
    def construct(self):
        def_title = Title('Definition')
        def_text1 = (
            '不宁腿综合征（RLS）系指强烈的、控制不住的想活动腿的欲望，大\n多发生在安静或休息时，尤其是夜间睡觉时容易出现，活动后可好转。'
        )
        def_mtext1 = MarkupText(def_text1, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP)
        self.play(FadeIn(def_title))
        self.play(Write(def_mtext1), run_time=2)
        def_man1 = ImageMobject("root\\smiling-face_263a-fe0f.png")
        def_man2 = ImageMobject("root\\fearful-face_1f628.png")
        def_man3 = ImageMobject("root\\face-exhaling_1f62e-200d-1f4a8.png")
        def_dizzy = ImageMobject("root\\dizzy-symbol_1f4ab.png").rotate(-15*DEGREES).scale(0.3)
        def dizzy_update(m):
            spin_an = (PI/6)*(0.4*sin(2*m.get_center()[0])+0.5)
            m.next_to(def_man1, RIGHT, buff=-1.1).shift(0.8*UP).rotate(spin_an)
        #def_dizzy.add_updater(lambda m: m.next_to(def_man1, RIGHT, buff=-1.1).shift(0.8*UP))
        def_dizzy.add_updater(dizzy_update)
        def_path1 = Line([4.5,0,0], [1.5,0,0])
        def_path2 = Line([1.5,0,0], [-1.5,0,0])
        def_path3 = Line([-1.5,0,0], [-3.9,0,0])
        def_path4 = Line([-3.9,0,0], [-4.5,0,0])
        self.play(FadeIn(def_man1, run_time=0.2), MoveAlongPath(def_man1, def_path1, rate_func=linear))
        self.play(FadeIn(def_dizzy, run_time=0.2), Transform(def_man1, def_man2.move_to([1.5,0,0]), run_time=0.2), MoveAlongPath(def_man1, def_path2, rate_func=linear))
        self.play(FadeOut(def_dizzy, run_time=0.2), Transform(def_man1, def_man3.move_to([-4.5,0,0]), run_time=0.2), MoveAlongPath(def_man1, def_path3, rate_func=linear, run_time=0.8))
        self.add(def_man3.move_to(def_man1))
        self.remove(def_man1)
        self.play(FadeOut(def_man3), MoveAlongPath(def_man3, def_path4, rate_func=linear), run_time=0.2)
        self.wait(0.5)
        def_text2 = (
            '                  RLS带来的最常见的问题是：\n很多人因为难以忍受的活动腿的欲望，睡眠很受影响。'
        )
        def_mtext2 = MarkupText(def_text2, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP)
        def_man4 = ImageMobject("root\\exploding-head_1f92f.png").shift(2*DOWN)
        def_bub = ImageMobject("root\\cannot_sleep.png").scale(2).move_to(def_man4).shift(2*UP+2*RIGHT)
        self.play(FadeOut(def_mtext1, shift=UP), FadeIn(def_mtext2, shift=UP))
        self.play(FadeIn(def_man4))
        self.play(GrowFromEdge(def_bub, DL))
        self.wait()
        
        
        sym_title = Title('Symptom')
        self.play(Transform(def_title, sym_title), FadeOut(def_mtext2, def_man4, def_bub))
        sym_text = ('产生下肢蠕动感，撕裂感，刺痛，烧灼感，疼痛。有强烈\n运动欲望，夜间卧床静息时出现。导致严重的睡眠剥夺。')
        sym_mtext = MarkupText(sym_text, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP)
        self.play(Write(sym_mtext), run_time=2)
        self.wait(0.5)
        sym_muscle = ImageMobject("root\\s2\\leg_1f9b5.png").scale(0.8).shift(6*DOWN)
        self.add(sym_muscle)
        self.play(sym_muscle.animate.shift(UP*4.5))
        sym_ache = ImageMobject("root\\s2\\high-voltage-sign_26a1.png").scale(0.6)
        sym_fire = ImageMobject("root\\s2\\fire_1f525.png").scale(0.6)
        sym_sting = ImageMobject("root\\s2\\collision_1f4a5.png").scale(0.6)
        def twinkle(mobg):
            stimulate_item = mobg[random.randint(0,3)].copy().move_to([random.uniform(-1,1),random.uniform(-3.4,0.6),0]).scale(random.uniform(0.8,1.2))
            return GrowFromCenter(stimulate_item, run_time=0.6)
        sym_group = [sym_ache, sym_fire, sym_sting]
        sym_hg = AnimationGroup([twinkle(sym_group) for _ in range(0,12)], lag_ratio=0.25)
        self.play(LaggedStart(sym_hg))
        self.wait()
        self.play(FadeIn(Rectangle(width=10,height=6,color=BLACK, fill_opacity=1).move_to(1.8*DOWN)))
        self.clear()
        self.add(sym_title, sym_mtext)
        sym_sleep = ImageMobject("root\\s2\\person-in-bed_light-skin-tone_1f6cc-1f3fb_1f3fb.png").shift(DOWN)
        sym_fbid = ImageMobject("root\\s2\\zzz_1f4a4.png").shift(DOWN+RIGHT)
        sym_anger = ImageMobject("root\\s2\\person-in-bed_anger.png").shift(DOWN)
        self.wait()
        self.play(FadeIn(sym_sleep))
        self.wait()
        self.remove(sym_sleep)
        self.add(sym_anger)
        self.play(FadeIn(sym_fbid), sym_anger.animate.shift(LEFT))
        self.wait()
        sym_text1 = ('哪些情况需要考虑RLS？')
        sym_mtext1 = MarkupText(sym_text1, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2.2*UP)
        sym_text_a = ('有迫切需要活动腿部的欲望，通常伴有腿部不适感，同时符合以下症状：')
        sym_mtext_a = MarkupText(sym_text_a, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6)
        sym_text_a1 = ('1、症状在休息或不活动时出现或加重，如躺着、坐着。')
        sym_mtext_a1 = MarkupText(sym_text_a1, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6)
        sym_text_a2 = ('2、活动可使症状部分或完全缓解，如行走、伸展腿部。')
        sym_mtext_a2 = MarkupText(sym_text_a2, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6)
        sym_text_a3 = ('3、症状全部或主要发生在傍晚或夜间。')
        sym_mtext_a3 = MarkupText(sym_text_a3, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6)
        sym_vg = VGroup(sym_mtext1, sym_mtext_a, sym_mtext_a1).arrange(DOWN, center=False)
        self.play(FadeOut(sym_mtext, sym_anger, sym_fbid))
        self.play(Write(sym_vg[0]))
        self.play(Write(sym_vg[1]), sym_vg[0].animate.set(color=YELLOW))
        self.play(FadeIn(sym_mtext_a1))
        sym_rest = ImageMobject("root\\s2\\chair_1fa91.png").shift(0.5*DOWN+3*LEFT).scale(0.5)
        sym_restman = ImageMobject("root\\s2\\anxious-face-with-sweat_1f630.png").shift(2*DOWN+3*LEFT)
        sym_sport = ImageMobject("root\\s2\\motorway_1f6e3-fe0f.png").scale(0.4).shift(0.5*DOWN)
        sym_sportman = ImageMobject("root\\s2\\hugging-face_1f917.png").shift(2*DOWN).scale(0.3)
        sym_night = ImageMobject("root\\s2\\night-with-stars_1f303.png").shift(0.5*DOWN+3*RIGHT).scale(0.4)
        sym_nightman = ImageMobject("root\\s2\\loudly-crying-face_1f62d.png").shift(2*DOWN+3*RIGHT)
        self.play(FadeIn(sym_rest, shift=RIGHT), FadeIn(sym_restman, shift=UR))
        self.wait()
        self.play(FadeOut(sym_mtext_a1), FadeIn(sym_mtext_a2.move_to(sym_mtext_a1)))
        self.play(FadeIn(sym_sport), FadeIn(sym_sportman, shift=UP))
        self.wait()
        self.play(FadeOut(sym_mtext_a2), FadeIn(sym_mtext_a3.move_to(sym_mtext_a1)))
        self.play(FadeIn(sym_night, shift=LEFT), FadeIn(sym_nightman, shift=UL))
        self.wait()
        sym_text_b1 = ('上述症状不能由其他疾病或行为问题解释。')
        sym_mtext_b1 = MarkupText(sym_text_b1, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6)
        sym_text_b2 = ('（如腿抽筋、姿势不适、肌痛、静脉曲张、关节炎、习惯性踮脚等）')
        sym_mtext_b2 = MarkupText(sym_text_b2, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6)
        sym_vg.remove(sym_mtext_a, sym_mtext_a1).add(sym_mtext_b1, sym_mtext_b2)
        sym_vg.arrange(DOWN, center=False)
        self.play(FadeOut(sym_rest, sym_restman, sym_sport, sym_sportman, sym_night, sym_nightman), FadeOut(sym_mtext_a, sym_mtext_a3))
        self.play(Write(sym_mtext_b1))
        self.play(FadeIn(sym_mtext_b2))
        sym_think = ImageMobject("root\\s2\\thinking-face_1f914.png").shift(DOWN)
        sym_why = ImageMobject("root\\s2\\question-mark_2753.png").next_to(sym_think, UR, buff=-0.25)
        self.play(LaggedStart(
            GrowFromCenter(sym_think),
            FadeIn(sym_why),
            lag_ratio=0.5
        ))
        self.play(Wiggle(sym_why))
        sym_text_c = ('症状导致患者忧虑苦恼、睡眠紊乱，或心理、躯\n体、社会、职业、行为及其他重要功能障碍。')
        sym_mtext_c = MarkupText(sym_text_c, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6)
        sym_annoy = ImageMobject("root\\s2\\confounded-face_1f616.png").shift(DOWN).scale(1.5)
        sym_vg.remove(sym_mtext_b1, sym_mtext_b2).add(sym_mtext_c)
        sym_vg.arrange(DOWN, center=False)
        self.play(FadeOut(sym_mtext_b1, sym_mtext_b2, sym_think, sym_why))
        self.play(Write(sym_mtext_c))
        self.play(SpinInFromNothing(sym_annoy, angle=4*PI))
        self.wait(3)
        
        
        ease_title = Title('Alleviation')
        self.play(Transform(sym_title, ease_title), FadeOut(sym_mtext1, sym_mtext_c, sym_annoy))
        ease_text = ('活动或揉捏后可缓解。')
        ease_mtext = MarkupText(ease_text, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP)
        self.play(Write(ease_mtext), run_time=1)
        self.wait(0.4)
        ease_muscle = ImageMobject("root\\s3\\leg_1f9b5.png").scale(0.8).shift(2*DOWN)
        self.play(FadeIn(ease_muscle, shift=UP))
        ease_hand1 = ImageMobject("root\\s3\\hand-with-fingers-splayed_1f590-fe0f.png").scale(0.6).shift(6*DOWN+RIGHT)
        self.play(ease_hand1.animate.next_to(ease_muscle, RIGHT, buff=0))
        ease_hand2 = ImageMobject("root\\s3\\waving-hand_1f44b.png").scale(0.6).next_to(ease_muscle, RIGHT, buff=0)
        self.remove(ease_hand1)
        self.add(ease_hand2)
        self.play(ease_hand2.animate.next_to(ease_muscle, LEFT, buff=0).shift(0.5*UP), run_time=0.3)
        self.play(ease_hand2.animate.next_to(ease_muscle, RIGHT, buff=0), run_time=0.3)
        self.play(ease_hand2.animate.next_to(ease_muscle, LEFT, buff=0).shift(0.5*UP), run_time=0.3)
        self.play(ease_hand2.animate.shift(0.25*DOWN+RIGHT), run_time=0.5)
        self.wait(3)
        
        
        path_title = Title("Pathogeny")
        path_text = ('RLS可分为原发性和继发性两类。')
        path_mtext = MarkupText(path_text, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2.2*UP)
        path_text1 = ('<span foreground="green">原发性：</span>\n原因不明，找不到确切病因，\n一部分患者有遗传家族史。')
        path_mtext1 = MarkupText(path_text1, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(UP+3.5*LEFT)
        path_text2 = ('<span foreground="yellow">继发性：</span>\n其他疾病引起的上述症状，如\n身体缺铁、其他药物影响、\n其他神经系统疾病。')
        path_mtext2 = MarkupText(path_text2, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).align_to(path_mtext1, UP).shift(3.5*RIGHT)
        self.play(Transform(sym_title, path_title), FadeOut(ease_mtext, ease_muscle, ease_hand2))
        self.play(FadeIn(path_mtext))
        self.play(Write(path_mtext1))
        path_list = ImageMobject("root\\s3.5\\clipboard_1f4cb.png").scale(2).shift(DOWN+3.5*LEFT)
        path_glass1 = ImageMobject("root\\s3.5\\magnifying-glass-tilted-left_1f50d.png").scale(0.5).move_to(path_list).shift(RIGHT+0.3*UP)
        path_glass2 = ImageMobject("root\\s3.5\\magnifying-glass-tilted-right_1f50e.png").scale(1.2).move_to(path_list).shift(0.5*DOWN+0.7*LEFT)
        self.play(FadeIn(path_list))
        self.play(LaggedStart(FadeIn(path_glass1, shift=UL), FadeIn(path_glass2, shift=UR), lag_ratio=0.25))
        self.play(FadeOut(path_list, path_glass1, path_glass2))
        path_old = ImageMobject("root\\s3.5\\old-man_1f474.png").scale(1.2).shift(DOWN+4.3*LEFT)
        path_man = ImageMobject("root\\s3.5\\man_1f468.png").scale(1.2).shift(DOWN+3.5*LEFT)
        path_baby = ImageMobject("root\\s3.5\\baby_1f476.png").scale(1.2).shift(DOWN+2.7*LEFT)
        self.play(
            LaggedStart(
                FadeIn(path_old, shift=LEFT), 
                FadeIn(path_man, shift=LEFT), 
                FadeIn(path_baby, shift=LEFT), 
                lag_ratio=0.2
            )
        )
        self.wait()
        self.play(FadeOut(path_old, path_man, path_baby))
        path_Fe = ImageMobject("root\\s3.5\\symbol-element-iron-Fe.png").scale(0.4).shift(1.5*DOWN+1.5*RIGHT)
        path_drug = ImageMobject("root\\s3.5\\drugs.png").scale(0.4).shift(1.5*DOWN+3.5*RIGHT)
        path_nerve = ImageMobject("root\\s3.5\\brain-stroke-100.png").scale(2.2).shift(1.5*DOWN+5.5*RIGHT)
        self.play(Write(path_mtext2))
        self.play(FadeIn(path_Fe))
        self.play(FadeIn(path_drug))
        self.play(FadeIn(path_nerve))
        self.wait()        
        self.play(FadeOut(path_Fe, path_drug, path_nerve))
        path_arrow1 = Arrow(3.5*LEFT, 2*DOWN+3.5*LEFT, buff=0)
        path_arrow2 = Arrow(0.5*DOWN+3.5*RIGHT, 1.8*DOWN+3.5*RIGHT, buff=0)
        self.play(GrowArrow(path_arrow1, point_color=GREEN), GrowArrow(path_arrow2, point_color=YELLOW))
        path_text3 = ('常使用治疗帕金森病的药物。')
        path_mtext3 = MarkupText(path_text3, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2.5*DOWN+3.5*LEFT)
        path_text4 = ('其他疾病引起的→治疗原发疾病\n使用药物引起的→调整药物方案')
        path_mtext4 = MarkupText(path_text4, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2.5*DOWN+3.5*RIGHT)
        self.play(Write(path_mtext3), Write(path_mtext4))
        self.wait(3)
        
        
        cure_title = Title('Treatment')        
        cure_text0 = ('建议首先去神经科就诊，完善必要检查，比如\n血液检查，明确是否缺铁。如果确诊不宁腿综\n合征，首先应改善生活方式、进行物理治疗。')
        cure_mtext0 = MarkupText(cure_text0, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(1.8*UP)
        self.play(Transform(sym_title, cure_title), FadeOut(path_mtext, path_mtext1, path_mtext2, path_mtext3, path_mtext4, path_arrow1, path_arrow2))
        self.play(Write(cure_mtext0))
        cure_hosp = ImageMobject("root\\s4\\hospital_1f3e5.png").scale(3).to_edge(DOWN).shift(2.5*LEFT)
        cure_doc = ImageMobject("root\\s4\\woman-health-worker_1f469-200d-2695-fe0f.png").scale(1.6).to_edge(DOWN).shift(LEFT)
        cure_pat = ImageMobject("root\\s4\\hushed-face_1f62f.png").scale(1.1).move_to(cure_doc).shift(2.5*RIGHT)
        cure_syr = ImageMobject("root\\s4\\syringe_1f489.png").scale(0.8).move_to(cure_doc).shift(2.5*DOWN+0.8*RIGHT)
        self.play(LaggedStart(FadeIn(cure_hosp), FadeIn(cure_doc, shift=RIGHT), lag_ratio=0.3))
        self.play(FadeIn(cure_pat, target_position=cure_pat.get_center()+2*RIGHT))
        self.play(cure_syr.animate.shift(2*UP))
        self.wait(3)
        
        cure_text1 = ('对RLS有帮助的非药物措施包括伸展、按摩、散步、认知分心(如玩\n游戏或解谜)，或适度的温水浴或冷水浴。')
        cure_mtext1 = MarkupText(cure_text1, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP)
        self.play(FadeOut(cure_hosp, cure_doc, cure_pat, cure_syr), FadeOut(cure_mtext0, shift=DOWN), FadeIn(cure_mtext1, shift=DOWN))
        self.wait()
        cure_massage = ImageMobject("root\\s4\\two_hands.png").scale(0.6)
        cure_walk = ImageMobject("root\\s4\\person-walking_1f6b6.png").scale(0.3)
        cure_play = ImageMobject("root\\s4\\video-game_1f3ae.png").scale(0.6)
        cure_puzzle = ImageMobject("root\\s4\\puzzle-piece_1f9e9.png").scale(0.6)
        cure_shower = ImageMobject("root\\s4\\shower_1f6bf.png").scale(0.8)
        cure_group = Group(cure_massage)
        self.play(FadeIn(cure_massage))
        self.wait(0.5)
        self.play(cure_group.animate.shift(1.3*LEFT), FadeIn(cure_walk.shift(RIGHT), shift=LEFT))
        cure_group.add(cure_walk)
        self.wait(0.5)
        self.play(cure_group.animate.shift(LEFT), FadeIn(cure_play.shift(2*RIGHT), shift=LEFT))
        cure_group.add(cure_play)
        self.wait(0.5)
        self.play(cure_group.animate.shift(LEFT), FadeIn(cure_puzzle.shift(3*RIGHT), shift=LEFT))
        cure_group.add(cure_puzzle)
        self.wait(0.5)
        self.play(cure_group.animate.shift(LEFT), FadeIn(cure_shower.shift(4*RIGHT), shift=LEFT))
        cure_group.add(cure_shower)
        self.wait(2)
        
        cure_text2 = ('非药物措施在间歇性与轻度RLS患者的治疗中为首选方法，对于其\n他RLS患者也可以作为药物治疗的补充治疗方法以减少药物使用量，\n但并不能根治RLS。') 
        cure_mtext2 = MarkupText(cure_text2, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(1.8*UP)
        self.play(FadeOut(*cure_group), FadeOut(cure_mtext1, shift=DOWN), FadeIn(cure_mtext2, shift=DOWN))
        self.wait()
        cure_r = Rectangle(width=8, height=0.6, color=BLUE, fill_opacity=0.5, z_index=3).shift(0.4*UP)
        cure_subtitle = Text("非药物治疗措施", font_size=24, font="Microsoft YaHei").move_to(cure_r).set_z_index(4)
        cure_r1 = Rectangle(width=4, height=3, fill_color=[GREEN, BLACK], fill_opacity=0.7, sheen_direction=RIGHT).move_to(cure_r.get_bottom()).set(stroke_color=[GREEN, BLACK]).shift(1.5*DOWN+2*LEFT)
        cure_r2 = Rectangle(width=4, height=3, fill_color=[YELLOW, BLACK], fill_opacity=0.7, sheen_direction=LEFT).move_to(cure_r.get_bottom()).set(stroke_color=[YELLOW, BLACK]).shift(1.5*DOWN+2*RIGHT)
        cure_labr1 = RoundedRectangle(corner_radius=0.1, width=2, height=1, color=GREEN, fill_opacity=0.6).next_to(cure_r1, LEFT).shift(0.8*UP)
        cure_labr2 = RoundedRectangle(corner_radius=0.1, width=2, height=1, color=GREEN, fill_opacity=0.6).next_to(cure_r1, LEFT).shift(0.6*DOWN)
        cure_labr3 = RoundedRectangle(corner_radius=0.1, width=2, height=1, color=YELLOW, fill_opacity=0.6).next_to(cure_r2, RIGHT).shift(0.3*UP)
        cure_lab1 = Text("间歇性", font_size=24, font="Microsoft YaHei").move_to(cure_labr1)
        cure_lab2 = Text("轻度", font_size=24, font="Microsoft YaHei").move_to(cure_labr2)
        cure_lab3 = Text("其他", font_size=24, font="Microsoft YaHei").move_to(cure_labr3)
        cure_good = ImageMobject("root\\s4\\thumbs-up_1f44d.png").scale(1.2).move_to(cure_r1).shift(0.2*LEFT)
        cure_ok = ImageMobject("root\\s4\\ok-hand_1f44c.png").scale(1.2).move_to(cure_r2).shift(0.2*RIGHT)
        self.play(FadeIn(cure_r, cure_subtitle))
        cure_agroup1 = AnimationGroup(Write(cure_r1), Write(cure_r2))
        cure_agroup2 = AnimationGroup(Create(cure_labr1), Create(cure_labr2), Create(cure_labr3), FadeIn(cure_lab1), FadeIn(cure_lab2), FadeIn(cure_lab3), FadeIn(cure_good), FadeIn(cure_ok), run_time=0.5)
        self.play(LaggedStart(cure_agroup1, cure_agroup2, lag_ratio=0.5))
        self.wait(2)
        
        cure_text3 = ('对于缺铁患者应优先使用补铁剂治疗，非缺铁患者应根据实际情况\n使用α-2-δ配体（Gabapentin enacarbil）或多巴胺激动剂治疗。')
        cure_mtext3 = MarkupText(cure_text3, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP)
        self.play(FadeOut(cure_r, cure_subtitle, cure_r1, cure_r2, cure_labr1, cure_labr2, cure_labr3, cure_lab1, cure_lab2, cure_lab3, cure_good, cure_ok), 
                  FadeOut(cure_mtext2, shift=DOWN), 
                  FadeIn(cure_mtext3, shift=DOWN)
                 )
        cure_med1 = ImageMobject("root\\s4\\900.png").scale(0.5).shift(8*LEFT+0.5*DOWN)
        cure_med2 = ImageMobject("root\\s4\\Gabapentin-Enacarbil_Conformer3D_large.png").scale(1.1).shift(10*RIGHT+0.5*DOWN)
        self.wait()
        self.add(cure_med1)
        self.play(cure_med1.animate.move_to(2*LEFT+0.5*DOWN))
        self.wait()
        self.add(cure_med2)
        self.play(cure_med2.animate.move_to(2*RIGHT+0.5*DOWN))
        self.wait(3)
        
        
        mis_title = Title('Misconception')
        self.play(Transform(sym_title, mis_title), FadeOut(cure_mtext3, cure_med1, cure_med2))
        self.remove(sym_title)
        self.add(mis_title)
        mis_text1 = ('“不宁腿综合征是一种腿部疾病”')
        mis_mtext1 = MarkupText(mis_text1, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP)
        self.play(Write(mis_mtext1), run_time=1)
        mis_leg = ImageMobject("root\\s5\\person-standing_1f9cd_leg.png").scale(1.5).move_to([-2,1,0])
        cor_body = ImageMobject("root\\s5\\person-standing_1f9cd.png", z_index=-1).scale(1.5).to_edge(DOWN, buff=0.5)
        mis_legr = Rectangle(width=4.5, height=1.2, stroke_width=2).move_to([0.8,0.35,0])
        self.play(FadeIn(mis_leg), Create(mis_legr))
        self.wait()
        cor_title = Title('Correction')
        cor_title[1].scale(0.5).next_to(mis_title[1], RIGHT, buff=-5.65)
        cor_title[0].shift(3.5*RIGHT)
        cor_text1 = ('不宁腿的症状不只局限于腿\n脚，会向上肢及全身放射。')
        cor_mtext1 = MarkupText(cor_text1, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP+3.5*RIGHT)
        self.play(mis_title[1].animate.scale(0.5).shift(3.5*LEFT), 
                  mis_title[0].animate.shift(3.5*LEFT), 
                  mis_mtext1.animate.shift(3.5*LEFT)
                 )
        self.play(Write(cor_title), TransformFromCopy(mis_mtext1, cor_mtext1))
        self.play(mis_leg.animate.move_to(cor_body), mis_legr.animate.move_to([2.8,-1.4,0]))
        cor_r1 = Rectangle(width=4.2, height=1.2, stroke_width=2).move_to([2.8,0,0])
        cor_r2 = Rectangle(width=4.5, height=1, stroke_width=3).rotate(10*DEGREES).move_to([0.2,0.7,0])
        cor_r3 = Rectangle(width=4.5, height=1, stroke_width=3).rotate(-5*DEGREES).move_to([0.2,-2.2,0])
        cor_r4 = Rectangle(width=3.5, height=3, stroke_width=4).move_to(cor_body).shift(3.5*LEFT)
        self.play(FadeIn(cor_body), run_time=0.6)
        self.add(cor_r1, cor_r2, cor_r3, cor_r4)
        self.wait(0.1)
        self.remove(cor_r1, cor_r2, cor_r3, cor_r4)
        self.wait(0.1)
        self.add(cor_r1, cor_r2, cor_r3, cor_r4)
        self.wait(0.05)
        self.remove(cor_r1, cor_r2, cor_r3, cor_r4)
        self.wait(0.05)
        self.add(cor_r1, cor_r2, cor_r3, cor_r4)
        self.wait(3)
        mis_text2 = ('“必须对不宁腿综合征\n施以药物、器械治疗”')
        mis_mtext2 = MarkupText(mis_text2, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP+3.5*LEFT)
        cor_text2 = ('保守治疗有效，不必强求\n药物治疗或器械治疗。')
        cor_mtext2 = MarkupText(cor_text2, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP+3.5*RIGHT)
        self.play(FadeOut(mis_legr, cor_r1, cor_r2, cor_r3, cor_r4, scale=1.1, run_time=0.6), 
                  FadeOut(mis_leg, cor_body), 
                  FadeOut(mis_mtext1, cor_mtext1, shift=DOWN), 
                  FadeIn(mis_mtext2, cor_mtext2, shift=DOWN)
                 )
        mis_man1 = ImageMobject("root\\s5\\face-with-steam-from-nose_1f624.png").shift(5.25*LEFT)
        cor_man1 = ImageMobject("root\\s5\\grinning-squinting-face_1f606.png").shift(1.75*RIGHT)
        mis_point = ImageMobject("root\\s5\\index-pointing-up_261d-fe0f.png").next_to(mis_man1, RIGHT)
        cor_thumb = ImageMobject("root\\s5\\thumbs-up_1f44d.png").scale(0.8).next_to(cor_man1, RIGHT)
        mis_pill = ImageMobject("root\\s5\\pill_1f48a.png").next_to(mis_point, RIGHT)
        mis_lancet = ImageMobject("root\\s5\\vector-medical-surgery-scalpel-tool.png").scale(0.4).next_to(mis_pill, RIGHT).shift(1.2*LEFT)
        cor_board = RoundedRectangle(corner_radius=0.1, width=1.5, height=1.5, color=GREY, fill_opacity=0.5).next_to(cor_thumb)
        cor_btext = Text("保  守\n\n治  疗", font="Microsoft YaHei", font_size=24).move_to(cor_board)
        self.play(FadeIn(mis_man1))
        self.play(
            FadeIn(mis_point, shift=RIGHT), 
            Wiggle(mis_man1), 
            LaggedStart(FadeIn(mis_pill, shift=UP), FadeIn(mis_lancet, shift=UP), lag_ratio=0.2)
        )
        self.play(FadeIn(cor_man1))
        self.play(FadeIn(cor_thumb, shift=RIGHT), FadeIn(cor_board, cor_btext, shift=UP))
        self.wait(3)
        
        
        epi_title = Title("Epidemiology")
        self.play(
            FadeOut(mis_mtext2, cor_mtext2, mis_man1, cor_man1, mis_point, cor_thumb, mis_pill, mis_lancet, cor_board, cor_btext), 
            FadeOut(mis_title, shift=LEFT), 
            Transform(cor_title, epi_title)
        )
        self.remove(cor_title)
        self.add(epi_title)
        self.add(epi_title)
        epi_bchart = BarChart(
            values=[0.027, 0.037, 0.035, 0.047, 0.072, 0.083, 0.087, 0.082], 
            bar_names=["15-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "over 80"], 
            y_range=[0,0.10,0.10], 
            bar_colors=["#84D9FC", "#B9E75D", "#F0847C"]
        )
        epi_xvar = Text("年龄范围", font="Microsoft YaHei", font_size=24).next_to(epi_bchart, DOWN)
        epi_yvar = Text("RLS的\n发病率", font="Microsoft YaHei", font_size=24).next_to(epi_bchart, LEFT, buff=0.1)
        epi_labgroup = VGroup()
        epi_dotgroup = VGroup()
        bar_values = ["2.7%", "3.7%", "3.5%", "4.7%", "7.2%", "8.3%", "8.7%", "8.2%"]
        for i in range(0,8):
            epi_dotgroup.add(Dot(point=epi_bchart[0][i].get_edge_center(UP), radius=0.1, fill_opacity=0.7))
            epi_labgroup.add(Text(bar_values[i], font_size=20, font="Times New Roman").move_to(epi_bchart[0][i].get_edge_center(UP)).shift(0.25*UP))
        self.play(LaggedStart(LaggedStart(Write(epi_bchart, run_time=4), Write(epi_labgroup), FadeIn(epi_xvar), lag_ratio=0.3), FadeIn(epi_yvar), lag_ratio=0.75))
        #self.play(FadeIn(epi_dotgroup))
        epi_dotx = []
        epi_doty = []
        epi_lchart = epi_bchart.plot_line_graph(
            x_values = [0.5+i for i in range(0,8)],
            y_values = [0.027, 0.037, 0.035, 0.047, 0.072, 0.083, 0.087, 0.082], 
            add_vertex_dots=False, 
            line_color=WHITE, 
        )
        self.play(LaggedStart( 
            Write(epi_dotgroup), 
            Create(epi_lchart), 
            lag_ratio=0.15
        ))
        self.wait(3)
        
        con_codeline = \
'''
if(is.RLS()) {
  Solution <- "Go to the hospital for a check-up."
  # 如果您认为自己可能正患有RLS，请尽快前往医院检查！
}
'''
        con_code = Code(code=con_codeline, 
                             tab_width=2, 
                             background="window", 
                             language="R", 
                             style=Code.styles_list[14], 
                             font="Monospace", 
                             stroke_width=1, 
                             background_stroke_width=2
                        )
        self.play(GrowFromPoint(con_code, [3,-4,0]))
        self.wait(8)
        
        
        self.play(FadeOut(epi_title, epi_bchart, epi_labgroup, epi_xvar, epi_yvar, epi_dotgroup, epi_lchart, con_code))
        self.wait()
