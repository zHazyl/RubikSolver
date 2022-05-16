from ursina import *
import tkinter as tk
from rubik.cube import Cube
import threading
import time
from rubik.optimize import dict_state_move, optimize_moves
from rubik.solve import Solver
import numpy as np
from rubik.IDA_star import Node, get_db, ida, ida1
from rubik.RubikProblem import xInitial
import sqlite3

def solve1(rubik):
    solver = Solver(Cube(rubik.rubik))
    solver.solve()
    opt_moves = optimize_moves(solver.moves)
    speed = 0.5
    dlay = 0.7
    
    ###stmove = dict_state_move(Cube(rubik.rubik), opt_moves)
    
    # rubik.rubik.file_state()
    # curr = Node()
    # curr.cube = np.array(xInitial)
    # handle = open('rubik/input.txt')
    # indexes = [0, 1, 2, 3, 6, 9, 12, 4, 7, 10, 13, 5, 8, 11, 14, 15, 16, 17]
    # index = 0
    # for line in handle:
    #     line = line.replace(' ', '')
    #     for row in line.split('['):
    #         if len(row) != 0:
    #             i = indexes[index]
    #             for j in range(3):
    #                 curr.cube[i, j] = row[j]
    #             index = index + 1
    # get_db()
    # opt_moves = ida(curr)[::-1]
    
    # speed = 0.5
    # dlay = 0.55
    
    ### opt_moves = ida1(curr,stmove)[::-1]
    
    rubik.moves.text = ' '.join(opt_moves)
    rubik.moves.appear()
    for move in opt_moves:
        if move == 'R':
            rubik.rotate_side('x3', 1, speed)
        elif move == 'Ri':
            rubik.rotate_side('x3', -1, speed)
        elif move == 'Li':
            rubik.rotate_side('x1', 1, speed)
        elif move == 'L':
            rubik.rotate_side('x1', -1, speed)
        elif move == 'U':
            rubik.rotate_side('y3', 1, speed)
        elif move == 'Ui':
            rubik.rotate_side('y3', -1, speed)
        elif move == 'Di':
            rubik.rotate_side('y1', 1, speed)
        elif move == 'D':
            rubik.rotate_side('y1', -1, speed)
        elif move == 'Bi':
            rubik.rotate_side('z3', 1, speed)
        elif move == 'B':
            rubik.rotate_side('z3', -1, speed)
        elif move == 'F':
            rubik.rotate_side('z1', 1, speed)
        elif move == 'Fi':
            rubik.rotate_side('z1', -1, speed)
        elif move == 'Mi':
            rubik.rotate_side('x2', 1, speed)
        elif move == 'M':
            rubik.rotate_side('x2', -1, speed)
        elif move == 'Ei':
            rubik.rotate_side('y2', 1, speed)
        elif move == 'E':
            rubik.rotate_side('y2', -1, speed)
        elif move == 'S':
            rubik.rotate_side('z2', 1, speed)
        elif move == 'Si':
            rubik.rotate_side('z2', -1, speed)
        elif move == 'Xi':
            rubik.rotate_side('x1', -1, speed)
            time.sleep(dlay)
            rubik.rotate_side('x2', -1, speed)
            time.sleep(dlay)
            rubik.rotate_side('x3', -1, speed)
        elif move == 'X':
            rubik.rotate_side('x1', 1, speed)
            time.sleep(dlay)
            rubik.rotate_side('x2', 1, speed)
            time.sleep(dlay)
            rubik.rotate_side('x3', 1, speed)
        elif move == 'Yi':
            rubik.rotate_side('y1', -1, speed)
            time.sleep(dlay)
            rubik.rotate_side('y2', -1, speed)
            time.sleep(dlay)
            rubik.rotate_side('y3', -1, speed)
        elif move == 'Y':
            rubik.rotate_side('y1', 1, speed)
            time.sleep(dlay)
            rubik.rotate_side('y2', 1, speed)
            time.sleep(dlay)
            rubik.rotate_side('y3', 1, speed)
        elif move == 'Zi':
            rubik.rotate_side('z1', -1, speed)
            time.sleep(dlay)
            rubik.rotate_side('z2', -1, speed)
            time.sleep(dlay)
            rubik.rotate_side('z3', -1, speed)
        elif move == 'Z':
            rubik.rotate_side('z1', 1, speed)
            time.sleep(dlay)
            rubik.rotate_side('z2', 1, speed)
            time.sleep(dlay)
            rubik.rotate_side('z3', 1, speed)
        time.sleep(dlay)
    # rubik.win_text_entity.text = 'SOLVED!!'

def solve(rubik):
    # solver = Solver(Cube(rubik.rubik))
    # solver.solve()
    # opt_moves = optimize_moves(solver.moves)
    # speed = 0.28
    # dlay = 0.31
    
    ###stmove = dict_state_move(Cube(rubik.rubik), opt_moves)
    
    rubik.rubik.file_state()
    curr = Node()
    curr.cube = np.array(xInitial)
    handle = open('rubik/input.txt')
    indexes = [0, 1, 2, 3, 6, 9, 12, 4, 7, 10, 13, 5, 8, 11, 14, 15, 16, 17]
    index = 0
    for line in handle:
        line = line.replace(' ', '')
        for row in line.split('['):
            if len(row) != 0:
                i = indexes[index]
                for j in range(3):
                    curr.cube[i, j] = row[j]
                index = index + 1
    get_db()
    opt_moves = ida(curr)[::-1]
    
    speed = 0.5
    dlay = 0.7
    
    ### opt_moves = ida1(curr,stmove)[::-1]
    
    rubik.moves.text = ' '.join(opt_moves)
    rubik.moves.appear()
    for move in opt_moves:
        if move == 'R':
            rubik.rotate_side('x3', 1, speed)
        elif move == 'Ri':
            rubik.rotate_side('x3', -1, speed)
        elif move == 'Li':
            rubik.rotate_side('x1', 1, speed)
        elif move == 'L':
            rubik.rotate_side('x1', -1, speed)
        elif move == 'U':
            rubik.rotate_side('y3', 1, speed)
        elif move == 'Ui':
            rubik.rotate_side('y3', -1, speed)
        elif move == 'Di':
            rubik.rotate_side('y1', 1, speed)
        elif move == 'D':
            rubik.rotate_side('y1', -1, speed)
        elif move == 'Bi':
            rubik.rotate_side('z3', 1, speed)
        elif move == 'B':
            rubik.rotate_side('z3', -1, speed)
        elif move == 'F':
            rubik.rotate_side('z1', 1, speed)
        elif move == 'Fi':
            rubik.rotate_side('z1', -1, speed)
        elif move == 'Mi':
            rubik.rotate_side('x2', 1, speed)
        elif move == 'M':
            rubik.rotate_side('x2', -1, speed)
        elif move == 'Ei':
            rubik.rotate_side('y2', 1, speed)
        elif move == 'E':
            rubik.rotate_side('y2', -1, speed)
        elif move == 'S':
            rubik.rotate_side('z2', 1, speed)
        elif move == 'Si':
            rubik.rotate_side('z2', -1, speed)
        elif move == 'Xi':
            rubik.rotate_side('x1', -1, speed)
            time.sleep(dlay)
            rubik.rotate_side('x2', -1, speed)
            time.sleep(dlay)
            rubik.rotate_side('x3', -1, speed)
        elif move == 'X':
            rubik.rotate_side('x1', 1, speed)
            time.sleep(dlay)
            rubik.rotate_side('x2', 1, speed)
            time.sleep(dlay)
            rubik.rotate_side('x3', 1, speed)
        elif move == 'Yi':
            rubik.rotate_side('y1', -1, speed)
            time.sleep(dlay)
            rubik.rotate_side('y2', -1, speed)
            time.sleep(dlay)
            rubik.rotate_side('y3', -1, speed)
        elif move == 'Y':
            rubik.rotate_side('y1', 1, speed)
            time.sleep(dlay)
            rubik.rotate_side('y2', 1, speed)
            time.sleep(dlay)
            rubik.rotate_side('y3', 1, speed)
        elif move == 'Zi':
            rubik.rotate_side('z1', -1, speed)
            time.sleep(dlay)
            rubik.rotate_side('z2', -1, speed)
            time.sleep(dlay)
            rubik.rotate_side('z3', -1, speed)
        elif move == 'Z':
            rubik.rotate_side('z1', 1, speed)
            time.sleep(dlay)
            rubik.rotate_side('z2', 1, speed)
            time.sleep(dlay)
            rubik.rotate_side('z3', 1, speed)
        time.sleep(dlay)
    # rubik.win_text_entity.text = 'SOLVED!!'
    
    
        

class Rubik(Ursina):
    def __init__(self):
        super().__init__()
        self.ec = EditorCamera()
        self.level = 3
        camera.world_position = (0, 0, -15)
        self.model, self.texture = "models/custom_cube", "textures/rubik_texture"
        self.rotation_helper = Entity()
        self.win_text_entity = Text(y=.35, text='', color=color.green, origin=(0,0), scale=3)
        self.moves = Text(y=-.35, text='', color=color.green, origin=(0,0), scale=1)
        self.action_trigger = True
        self.load()
        self.solvethread = None
        self.solvethread1 = None
        
        # self.strcube = InputField()
        
        self.rubik = Cube('WWWWWWWWWGGGRRRBBBOOOGGGRRRBBBOOOGGGRRRBBBOOOYYYYYYYYY') 
        # self.rubik = Cube("DLURRDFFUBBLDDRBRBLDLRBFRUULFBDDUFBRBBRFUDFLUDLUULFLFR")
                    #Cube('OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR')
        
        
        
    def load(self):
        self.cubes = []
        lv = self.level
        for x in range(lv):
            for y in range(lv):
                for z in range(lv):
                    e = Entity(model=self.model, texture=self.texture, position=Vec3(x, y, z) - Vec3(lv, lv, lv)/lv, rotation_z=90)
                    self.cubes.append(e)
                    
        self.create_button()
        self.check_for_win()
        
    def randomize(self):
        self.moves.text = ''
        faces = ("x1","x3","y1","y3","z1","z3")
        for i in range(5):
            self.rotate_side(name=random.choice(faces), direction=random.choice((-1,1)), speed=0)
        self.check_for_win()
            
    def solve(self):
        self.moves.text = ''
        if self.solvethread:
            self.solvethread.join()
        self.solvethread = threading.Thread(target=solve, args=(self,))
        self.solvethread.start()
        
    def solve1(self):
        self.moves.text = ''
        if self.solvethread1:
            self.solvethread1.join()
        self.solvethread1 = threading.Thread(target=solve1, args=(self,))
        self.solvethread1.start()
        
    def set_level():
        pass
    
    def Submit(self, root, cube_str):
        self.rubik = Cube(cube_str.get("1.0", "end-1c"))
        
        root.destroy()
    
    def CubeStringWindow(self):
        root = tk.Tk()
        cubestr = tk.Text(root, height=1, width=54)
        cubestr.grid()
        tk.Button(root, text="Submit", bg="#488FB1", command=lambda : self.Submit(root, cubestr)).grid()
        root.grid()
        root.mainloop()
        
    def create_button(self):
        randomize_button = Button(text="Random", position=(-.7,-.4), on_click=self.randomize)
        randomize_button.fit_to_text()
        randomize_button = Button(text="Solve IDA*", position=(.7,-.4), on_click=self.solve)
        randomize_button.fit_to_text()
        randomize_button = Button(text="Solve Normal", position=(.4,-.4), on_click=self.solve1)
        randomize_button.fit_to_text()
        lv = self.level
        pre = "xyz"
        for i in range(3): 
                for j in range(lv):
                    if j == 1:
                        continue
                    name = pre[i]+str(j+1)
                    b = Button(text=name, position=(-.8+j/10,.4-i*2/10), on_click=Func(self.rotate_side, name, 1))
                    b.fit_to_text()
                    b = Button(text=name+"'", position=(-.8+j/10,.3-i*2/10), on_click=Func(self.rotate_side, name, -1))
                    b.fit_to_text()     
                
        Button(text="Reset view", position=(-.7,-.3), on_click=self.reset_view).fit_to_text()
        Button(text="Input Cube string", position=(-.7,-.2), on_click=self.CubeStringWindow).fit_to_text()
    
    def rotate_side(self, name, direction=1, speed=1):
        # self.moves.text = ''
        if not self.action_trigger:
            return
        if name == "x3":
            [setattr(e, 'world_parent', self.rotation_helper) for e in self.cubes if e.x > 0]
            self.rotation_helper.animate('rotation_x', 90 * direction, duration=.2*speed, curve=curve.linear)
            if direction == 1:
                self.rubik.R()
            else:
                self.rubik.Ri()
        elif   name == "x1":
            [setattr(e, 'world_parent', self.rotation_helper) for e in self.cubes if e.x < 0]
            self.rotation_helper.animate('rotation_x', 90 * direction, duration=.2*speed, curve=curve.linear)
            if direction == 1:
                self.rubik.Li()
            else:
                self.rubik.L()

        elif   name == "y3":
            [setattr(e, 'world_parent', self.rotation_helper) for e in self.cubes if e.y > 0]
            self.rotation_helper.animate('rotation_y', 90 * direction, duration=.2*speed, curve=curve.linear)
            if direction == 1:
                self.rubik.U()
            else:
                self.rubik.Ui()
        elif   name == "y1":
            [setattr(e, 'world_parent', self.rotation_helper) for e in self.cubes if e.y < 0]
            self.rotation_helper.animate('rotation_y', 90 * direction, duration=.2*speed, curve=curve.linear)
            if direction == 1:
                self.rubik.Di()
            else:
                self.rubik.D()

        elif   name == "z3":
            [setattr(e, 'world_parent', self.rotation_helper) for e in self.cubes if e.z > 0]
            self.rotation_helper.animate('rotation_z', 90 * direction, duration=.2*speed, curve=curve.linear)
            if direction == 1:
                self.rubik.Bi()
            else:
                self.rubik.B()
        elif   name == "z1":
            [setattr(e, 'world_parent', self.rotation_helper) for e in self.cubes if e.z < 0]
            self.rotation_helper.animate('rotation_z', 90 * direction, duration=.2*speed, curve=curve.linear)
            if direction == 1:
                self.rubik.F()
            else:
                self.rubik.Fi()
        elif   name == "x2":
            [setattr(e, 'world_parent', self.rotation_helper) for e in self.cubes if e.x == 0]
            self.rotation_helper.animate('rotation_x', 90 * direction, duration=.2*speed, curve=curve.linear)
            if direction == 1:
                self.rubik.Mi()
            else:
                self.rubik.M()
        elif   name == "y2":
            [setattr(e, 'world_parent', self.rotation_helper) for e in self.cubes if e.y == 0]
            self.rotation_helper.animate('rotation_y', 90 * direction, duration=.2*speed, curve=curve.linear)
            if direction == 1:
                self.rubik.Ei()
            else:
                self.rubik.E()
        elif   name == "z2":
            [setattr(e, 'world_parent', self.rotation_helper) for e in self.cubes if e.z == 0]
            self.rotation_helper.animate('rotation_z', 90 * direction, duration=.2*speed, curve=curve.linear)
            if direction == 1:
                self.rubik.S()
            else:
                self.rubik.Si()

        invoke(self.reset_rotation_helper, delay=.25*speed)

        if speed:
            self.action_trigger = False
            invoke(self.toggle_animation_trigger, delay=.25*speed)
            invoke(self.check_for_win, delay=.25*speed)

    def toggle_animation_trigger(self):
        '''prohibiting side rotation during rotation animation'''
        self.action_trigger = not self.action_trigger

    def reset_rotation_helper(self):
        [setattr(e, 'world_parent', scene) for e in self.cubes]
        self.rotation_helper.rotation = (0,0,0)
        
    def check_for_win(self):
        if {e.world_rotation for e in self.cubes} == {Vec3(0,0,90)}:
            self.win_text_entity.text = 'SOLVED!!'
            self.win_text_entity.appear()
        else:
            self.win_text_entity.text = ''
            
    def reset_view(self):
        self.ec.rotation = (0,0,0)
        