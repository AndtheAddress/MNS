from manim import *
from numpy import random, sin

config.media_width = "100%"
config.verbosity = "WARNING"



%%manim -qp RLS_release

class RLS_release(ZoomedScene):
    def construct(self):
        case_ent = Title('Case')
        case_zhtext = ('病例')
        case_zht = MarkupText(case_zhtext, font='Alimama DaoLiTi').scale(0.9).move_to(case_ent[0])
        self.play(
            LaggedStart(
                Write(case_zht),
                Create(case_ent[1], rate_func=rate_functions.ease_in_expo),  
                lag_ratio=0.1, 
                run_time=1
            )
        )
        self.wait(3)
        case_text1 = (
            '这天，老刘在准备睡觉，躺在床上的时候，突然双腿一阵难受，\n'
            '很瘙痒，像有蚂蚁爬，还有烧灼感，他控制不住地想让腿活动。\n'
            '活动腿部或者进行了按摩后，老刘的症状明显地改善了。'
        )
        case_mtext1 = MarkupText(case_text1, font='FZCuYuanSongS-R-GB').scale(0.6).shift(1.5*UP) 
        case_text2 = (
            '后来老刘常常在睡觉前出现这种症状，因为腿部难受以及控制不住地\n'
            '想要活动腿部，搞得他睡眠质量变差了不少。老刘怀疑这是因为身体\n'
            '缺钙、抽筋、骨质疏松，是风湿，或者腿部血管堵塞。然而做了几次\n'
            '体检，还是没有发现准确的病因。'
        )
        case_mtext2 = MarkupText(case_text2, font='FZCuYuanSongS-R-GB').scale(0.6).align_to(case_mtext1, UP)
        case_text3 = (
            '那么这种情况到底是什么疾病呢？'
        )
        case_mtext3 = MarkupText(case_text3, font='FZCuYuanSongS-R-GB').scale(0.6).shift(1.5*UP)
        case_text4 = (
            '原来，老刘的腿不能安宁，是因为他得了不宁腿综合征。'
        )
        case_mtext4 = MarkupText(case_text4, font='FZCuYuanSongS-R-GB').scale(0.6).shift(1.5*UP)
        self.play(Write(case_mtext1), run_time=2)
        self.wait(5)
        case_path = Arc(radius=4, start_angle=15*DEGREES, angle=150*DEGREES).shift(6*DOWN)
        case_ant = ImageMobject("root\\s0\\ant_1f41c.png").scale(0.5)
        case_fire = ImageMobject("root\\s0\\fire_1f525.png").shift(2*DOWN)
        self.play(MoveAlongPath(case_ant, case_path), run_time=2)
        self.play(FadeIn(case_fire, shift=UP))
        self.play(FadeOut(case_ant, case_fire))
        self.wait(3)
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
        self.play(FadeOut(ease_muscle, ease_hand2), FadeOut(case_mtext1, shift=UP), FadeIn(case_mtext2, shift=UP))
        self.wait(21)
        self.play(FadeOut(case_mtext2, shift=UP), FadeIn(case_mtext3, shift=UP))
        self.wait(2)
        self.play(FadeOut(case_mtext3, shift=UP), FadeIn(case_mtext4, shift=UP))
        self.wait(2)
        self.play(Circumscribe(case_mtext4[18:], fade_out=True, buff=0.1, run_time=2))
        self.wait()
        
        
        def_zhtext = ('什么是不宁腿综合征？')
        def_zht = MarkupText(def_zhtext, font='Alimama DaoLiTi').scale(0.9).move_to(case_ent[0])
        self.play(FadeOut(case_mtext4), Transform(case_zht, def_zht))
        self.remove(case_zht)
        self.add(def_zht)
        self.wait(2)
        def_text1 = (
            '不宁腿综合征（RLS）是一种主要影响睡眠的运动障碍性疾病。\n'
            '其特征是强烈的双腿运动冲动，并且伴有难以描述的不适感，\n'
            '如蠕动、蚁行、瘙痒、烧灼、触电感等。'
        )
        def_mtext1 = MarkupText(def_text1, font='FZCuYuanSongS-R-GB').scale(0.6).shift(1.5*UP)
        self.play(Write(def_mtext1), run_time=2)
        def_leg = ImageMobject("root\\s2\\leg_1f9b5.png").scale(0.8).shift(6*DOWN)
        self.wait(10)
        self.add(def_leg)
        self.play(def_leg.animate.shift(UP*4.5))
        def_ache = ImageMobject("root\\s2\\high-voltage-sign_26a1.png").scale(0.6)
        def_fire = ImageMobject("root\\s2\\fire_1f525.png").scale(0.6)
        def_sting = ImageMobject("root\\s2\\collision_1f4a5.png").scale(0.6)
        def twinkle(mobg):
            stimulate_item = mobg[random.randint(0,3)].copy().move_to([random.uniform(-1,1),random.uniform(-3.4,0.3),0]).scale(random.uniform(0.8,1.2))
            return GrowFromCenter(stimulate_item, run_time=0.6)
        def_group = [def_ache, def_fire, def_sting]
        def_hg = AnimationGroup([twinkle(def_group) for _ in range(0,12)], lag_ratio=0.25)
        self.play(LaggedStart(def_hg))
        self.wait()
        self.play(FadeIn(Rectangle(width=10,height=5.4,color=BLACK, fill_opacity=1).move_to(2*DOWN)))
        self.clear()
        self.add(def_zht, case_ent[1])
        def_text2 = (
            '这些症状最主要是在安静状态下，如睡眠过程中出现。\n'
            '在活动后症状缓解是其显著特点。症状严重时不仅累\n'
            '及双腿，也可以出现胳膊，腹部，背部等感觉异常。'
        )
        def_mtext2 = MarkupText(def_text2, font='FZCuYuanSongS-R-GB').scale(0.6).shift(1.5*UP)
        def_man = ImageMobject("root\\s1\\exploding-head_1f92f.png").shift(2*DOWN)
        def_bub = ImageMobject("root\\s1\\cannot_sleep.png").scale(1.6).move_to(def_man).shift(2*UP+2*RIGHT)
        self.play(FadeOut(def_mtext1, shift=UP), FadeIn(def_mtext2, shift=UP))
        self.wait(2)
        self.play(FadeIn(def_man))
        self.play(GrowFromEdge(def_bub, DL))
        self.play(FadeOut(def_man, def_bub))
        
        def_run = ImageMobject("root\\s1\\person-running_1f3c3.png").shift(1.5*DOWN+2*LEFT)
        self.play(FadeIn(def_run, target_position=1.5*DOWN+2*RIGHT))
        self.wait(4)
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame
        frame.scale(2.2).scale([1.8, 0.5, 0]).move_to(1*DOWN+2.2*LEFT)
        zoomed_display.scale([1.8, 0.5, 0]).move_to(1*DOWN+3*RIGHT)
        self.play(Create(frame))
        self.activate_zooming()
        self.play(self.get_zoomed_display_pop_out_animation())
        self.play(
            frame.animate.scale([0.6/1.8,0.6/0.5,0]).move_to(1.3*DOWN+2.2*LEFT), 
            zoomed_display.animate.scale([0.6/1.8,0.6/0.5,0])
        )
        self.play(
            frame.animate.scale([0.5/0.6,1/0.6,0]).move_to(1.1*DOWN+1.8*LEFT), 
            zoomed_display.animate.scale([0.5/0.6,1/0.6,0])
        )
        self.play(self.get_zoomed_display_pop_out_animation(), rate_func=lambda t: smooth(1 - t))
        self.play(Uncreate(zoomed_display_frame), FadeOut(frame))
        self.play(FadeOut(def_run))
        self.wait()
        
        def_text3 = (
            '典型的不宁腿综合征就是睡眠中因难以忍受的腿部不适而控制\n'
            '不住地想活动腿部，故会明显影响睡眠。因此，也有很多患者\n'
            '因失眠就诊，最终医生问诊后发现是不宁腿综合征。'
        )
        def_mtext3 = MarkupText(def_text3, font='FZCuYuanSongS-R-GB').scale(0.6).shift(1.5*UP)
        def_sleep = ImageMobject("root\\s2\\person-in-bed_light-skin-tone_1f6cc-1f3fb_1f3fb.png").shift(DOWN)
        def_fbid = ImageMobject("root\\s2\\zzz_1f4a4.png").shift(DOWN+RIGHT)
        def_anger = ImageMobject("root\\s2\\person-in-bed_anger.png").shift(DOWN)
        #self.play(FadeOut(def_man, def_bub))
        self.play(FadeOut(def_mtext2, shift=UP), FadeIn(def_mtext3, shift=UP))
        self.wait(2)
        self.play(FadeIn(def_sleep))
        self.wait(3)
        self.remove(def_sleep).add(def_anger)
        self.play(FadeIn(def_fbid), def_anger.animate.shift(LEFT))
        self.wait(10)

        
        clas_zhtext = ('不宁腿综合征的分类')
        clas_zht = MarkupText(clas_zhtext, font='Alimama DaoLiTi').scale(0.9).move_to(case_ent[0])
        self.play(FadeOut(def_mtext3), FadeOut(def_anger, def_fbid), Transform(def_zht, clas_zht))
        self.remove(def_zht)
        self.add(clas_zht)
        clas_text = ('RLS可分为原发性和继发性两类。')
        clas_mtext = MarkupText(clas_text, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2.2*UP)
        clas_text1 = ('<span foreground="green">原发性：</span>\n原因不明，找不到确切病因，\n一部分患者有遗传家族史。')
        clas_mtext1 = MarkupText(clas_text1, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(UP+3.5*LEFT)
        clas_text2 = ('<span foreground="yellow">继发性：</span>\n其他疾病引起的上述症状，如：\n身体缺铁、怀孕、服用其他药\n物（如酒精，抗抑郁药，抗精\n神病药），以及神经系统疾病\n（如帕金森病，中风、脊髓病、\n多发性硬化等）。')
        clas_mtext2 = MarkupText(clas_text2, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).align_to(clas_mtext1, UP).shift(3.5*RIGHT)
        self.play(FadeIn(clas_mtext))
        self.wait(3)
        self.play(Write(clas_mtext1), run_time=2)
        clas_list = ImageMobject("root\\s3.5\\clipboard_1f4cb.png").scale(2).shift(DOWN+3.5*LEFT)
        clas_glass1 = ImageMobject("root\\s3.5\\magnifying-glass-tilted-left_1f50d.png").scale(0.5).move_to(clas_list).shift(RIGHT+0.3*UP)
        clas_glass2 = ImageMobject("root\\s3.5\\magnifying-glass-tilted-right_1f50e.png").scale(1.2).move_to(clas_list).shift(0.5*DOWN+0.7*LEFT)
        self.play(FadeIn(clas_list))
        self.play(LaggedStart(FadeIn(clas_glass1, shift=UL), FadeIn(clas_glass2, shift=UR), lag_ratio=0.25), run_time=1)
        self.play(FadeOut(clas_list, clas_glass1, clas_glass2))
        clas_old = ImageMobject("root\\s3.5\\old-man_1f474.png").scale(1.2).shift(DOWN+4.3*LEFT)
        clas_man = ImageMobject("root\\s3.5\\man_1f468.png").scale(1).shift(DOWN+3.5*LEFT)
        clas_baby = ImageMobject("root\\s3.5\\baby_1f476.png").scale(0.8).shift(DOWN+2.7*LEFT)
        self.play(
            LaggedStart(
                FadeIn(clas_old, shift=LEFT), 
                FadeIn(clas_man, shift=LEFT), 
                FadeIn(clas_baby, shift=LEFT), 
                lag_ratio=0.2
            ), 
            run_time=1.5
        )
        self.wait(0.5)
        self.play(FadeOut(clas_old, clas_man, clas_baby))
        clas_Fe = ImageMobject("root\\s3.5\\symbol-element-iron-Fe.png").scale(0.4).shift(2*DOWN+5.5*LEFT)
        clas_drug = ImageMobject("root\\s3.5\\drugs.png").scale(0.4).shift(2*DOWN+3.5*LEFT)
        clas_nerve = ImageMobject("root\\s3.5\\brain-stroke-100.png").scale(2.2).shift(2*DOWN+1.5*LEFT)
        self.play(Write(clas_mtext2), run_time=3)
        self.wait()
        self.play(FadeIn(clas_Fe))
        self.wait()
        self.play(FadeIn(clas_drug))
        self.wait(4)
        self.play(FadeIn(clas_nerve))      
        self.wait(5)
        
        
        epi_zhtext = ('相关统计资料')
        epi_zht = MarkupText(epi_zhtext, font='Alimama DaoLiTi').scale(0.9).move_to(case_ent[0])
        self.play(FadeOut(clas_mtext, clas_mtext1, clas_mtext2, clas_Fe, clas_drug, clas_nerve), Transform(clas_zht, epi_zht))
        self.remove(clas_zht)
        self.add(epi_zht)
        epi_bchart = BarChart(
            values=[0.027, 0.037, 0.035, 0.047, 0.072, 0.083, 0.087, 0.082], 
            bar_names=["15-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "over 80"], 
            y_range=[0,0.10,0.10], 
            bar_colors=["#84D9FC", "#B9E75D", "#F0847C"]
        )
        epi_xvar = Text("年龄范围", font="Microsoft YaHei", font_size=24).next_to(epi_bchart, DOWN)
        epi_yvar = Text("RLS\n的发\n病率", font="Microsoft YaHei", font_size=24).next_to(epi_bchart, LEFT, buff=0.1).shift(0.5*RIGHT)
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


        path_zhtext = ('发病的原因')
        path_zht = MarkupText(path_zhtext, font='Alimama DaoLiTi').scale(0.9).move_to(case_ent[0])
        self.play(
            FadeOut(epi_bchart, epi_xvar, epi_yvar, epi_labgroup, epi_dotgroup, epi_lchart), 
            Transform(epi_zht, path_zht)
        )
        self.remove(epi_zht)
        self.add(path_zht)
        self.wait(2)
        path_text = (
            '不宁腿综合征虽然主要是腿部不适，但是并不能算是腿部疾病，\n'
            '根本的发病原因是神经系统的紊乱，比如神经系统铁代谢紊乱、\n'
            '多巴胺功能紊乱（它和帕金森病高度相关）、神经环路异常等。 '
        )
        path_mtext = MarkupText(path_text, font='FZCuYuanSongS-R-GB').scale(0.6).shift(1.5*UP)
        self.play(Write(path_mtext), run_time=2)
        self.wait(13)
        
        
        cure_zhtext = ('如何诊治？')
        cure_zht = MarkupText(cure_zhtext, font='Alimama DaoLiTi').scale(0.9).move_to(case_ent[0])
        self.play(FadeOut(path_mtext), Transform(path_zht, cure_zht))
        self.remove(path_zht)
        self.add(cure_zht)
        self.wait(3)
        cure_text1 = (
            '首先，建议神经科就诊，医生会详细了解具体情况，完善\n'
            '必要检查，比如查找是不是继发性的不宁腿综合征，需要\n'
            '查血明确有无缺铁。如果是其他疾病引起的，积极治疗原\n'
            '发疾病，比如补铁。如果是用其他药物引起的，需要调整\n'
            '药物方案，比如酒精引起的发病，患者就需要戒酒。'
        )
        cure_mtext1 = MarkupText(cure_text1, font='FZCuYuanSongS-R-GB').scale(0.6).shift(1.5*UP)
        self.play(Write(cure_mtext1), run_time=3)
        cure_hosp = ImageMobject("root\\s4\\hospital_1f3e5.png").scale(3).to_edge(DOWN).shift(2.5*LEFT)
        cure_doc = ImageMobject("root\\s4\\woman-health-worker_1f469-200d-2695-fe0f.png").scale(1.6).to_edge(DOWN).shift(LEFT)
        cure_pat = ImageMobject("root\\s4\\hushed-face_1f62f.png").scale(1.1).move_to(cure_doc).shift(2.5*RIGHT)
        cure_syr = ImageMobject("root\\s4\\syringe_1f489.png").scale(0.8).move_to(cure_doc).shift(2.5*DOWN+0.8*RIGHT)
        self.play(LaggedStart(FadeIn(cure_hosp), FadeIn(cure_pat, target_position=cure_pat.get_center()+2*RIGHT), lag_ratio=0.3), run_time=1)
        self.wait()
        self.play(FadeIn(cure_doc, shift=RIGHT))
        self.wait(4)
        self.play(cure_syr.animate.shift(2*UP))
        self.wait(9)
        cure_pill = ImageMobject("root\\s4\\pill_1f48a.png").scale(0.4).to_edge(DOWN).shift(4*LEFT)
        cure_wine = ImageMobject("root\\s4\\wine-glass_1f377.png").scale(0.5).to_edge(DOWN).shift(4*RIGHT)
        self.play(FadeIn(cure_pill))
        self.play(FadeIn(cure_wine))
        self.wait(3)

        cure_text2 = ('确诊不宁腿综合征后，首先是生活方式的改善和物理治疗。')
        cure_mtext2 = MarkupText(cure_text2, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP)
        cure_text3 = ('对RLS有帮助的非药物措施包括伸展、按摩、散步、认知\n分心(如玩游戏或解谜)，或适度的温水浴或冷水浴。')
        cure_mtext3 = MarkupText(cure_text3, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP)
        self.play(FadeOut(cure_hosp, cure_doc, cure_pat, cure_syr, cure_pill, cure_wine), FadeOut(cure_mtext1, shift=DOWN), FadeIn(cure_mtext2, shift=DOWN))
        self.wait(5)
        self.play(FadeOut(cure_mtext2, shift=DOWN), FadeIn(cure_mtext3, shift=DOWN))
        self.wait(3)
        cure_massage = ImageMobject("root\\s4\\two_hands.png")
        cure_walk = ImageMobject("root\\s4\\person-walking_1f6b6.png").scale(0.5)
        cure_play = ImageMobject("root\\s4\\video-game_1f3ae.png")
        cure_puzzle = ImageMobject("root\\s4\\puzzle-piece_1f9e9.png")
        cure_shower = ImageMobject("root\\s4\\shower_1f6bf.png").scale(1.3)
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
        self.wait()   

        cure_text4 = ('在调节生活方式、物理治疗的基础上，依据症状给予药物治疗。')
        cure_mtext4 = MarkupText(cure_text4, font='FZCuYuanSongS-R-GB').scale(0.6).shift(1.5*UP)
        cure_text5 = (
            '最常使用的药物是多巴胺类药物或者多巴胺激动剂，\n'
            '如左旋多巴或普拉克索（是治疗帕金森病的药物）。'
        )
        cure_mtext5 = MarkupText(cure_text5, font='FZCuYuanSongS-R-GB').scale(0.6).shift(1.5*UP)
        self.play(FadeOut(*cure_group), FadeOut(cure_mtext3, shift=DOWN), FadeIn(cure_mtext4, shift=DOWN))
        self.wait(5)
        self.play(FadeOut(cure_mtext4, shift=DOWN), FadeIn(cure_mtext5, shift=DOWN))
        cure_lev = ImageMobject("root\\s4\\Levodopa.png").shift(1.5*DOWN+3*LEFT)
        cure_pra = ImageMobject("root\\s4\\Pramipexole.png").scale(1.2).shift(1.5*DOWN+3*RIGHT)
        self.wait(3)
        self.play(FadeIn(cure_lev, shift=RIGHT), FadeIn(cure_pra, shift=LEFT))
        self.wait(5)
        
        
        mis_zhtext = ('常见的误区')
        mis_zht = MarkupText(mis_zhtext, font='Alimama DaoLiTi').scale(0.9).move_to(case_ent[0])
        self.play(FadeOut(cure_mtext5, cure_lev, cure_pra), Transform(cure_zht, mis_zht))
        self.remove(cure_zht)
        self.add(mis_zht)
        self.wait(2)
        mis_text1 = ('“不宁腿综合征是一种腿部疾病”')
        mis_mtext1 = MarkupText(mis_text1, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP)
        self.play(Write(mis_mtext1), run_time=1)
        mis_leg = ImageMobject("root\\s5\\person-standing_1f9cd_leg.png").scale(1.5).move_to([-2,1,0])
        cor_body = ImageMobject("root\\s5\\person-standing_1f9cd.png", z_index=-1).scale(1.5).to_edge(DOWN, buff=0.5)
        mis_legr = Rectangle(width=4.5, height=1.2, stroke_width=2).move_to([0.8,0.35,0])
        self.play(FadeIn(mis_leg), Create(mis_legr))
        self.wait()
        cor_ent = Title('Correction')
        cor_ent[1].scale(0.5).next_to(case_ent[1], RIGHT, buff=-5.65)
        cor_ent[0].shift(3.5*RIGHT)
        cor_zhtext = ('订正')
        cor_zht = MarkupText(cor_zhtext, font='Alimama DaoLiTi').scale(0.9).move_to(cor_ent[0])
        cor_text1 = ('不宁腿的症状不只局限于腿\n脚，会向上肢及全身放射。')
        cor_mtext1 = MarkupText(cor_text1, justify=True, font='FZCuYuanSongS-R-GB').scale(0.6).shift(2*UP+3.5*RIGHT)
        self.play(
            case_ent[1].animate.scale(0.5).shift(3.5*LEFT), 
            mis_zht.animate.shift(3.5*LEFT), 
            mis_mtext1.animate.shift(3.5*LEFT)
        )
        #self.play(Write(cor_title), TransformFromCopy(mis_mtext1, cor_mtext1))
        self.play(
            LaggedStart(
                Write(cor_zht),
                Create(cor_ent[1], rate_func=rate_functions.ease_in_expo),  
                lag_ratio=0.1, 
                run_time=1
            ), 
            TransformFromCopy(mis_mtext1, cor_mtext1)
        )
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
        self.wait(4)
        mis_text2 = ('“必须对不宁腿综合征\n  施以药物、器械治疗”')
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
        self.wait(3)
        self.play(FadeIn(cor_man1))
        self.play(FadeIn(cor_thumb, shift=RIGHT), FadeIn(cor_board, cor_btext, shift=UP))
        self.wait(4)
        
        
        con_codeline = \
'''
if(is.RLS()) {
  Solution <- "Go to hospital for a check-up."
  # 如果您认为自己可能正患有RLS，请尽快前往医院检查！
}
'''
        con_code = Code(
            code=con_codeline, 
            tab_width=2, 
            background="window", 
            language="R", 
            style=Code.styles_list[14], 
            font="Monospace", 
            stroke_width=1, 
            background_stroke_width=2
        )
        self.play(GrowFromPoint(con_code, [3,-4,0]))
        self.wait(11)
