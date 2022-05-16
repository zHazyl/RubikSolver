import sqlalchemy as db
from RubikProblem import RubikProblem

engine = db.create_engine('sqlite:///heuristic.db') 
connection = engine.connect()
metadata = db.MetaData()

heuristic = db.Table('heuristic', metadata,
              db.Column('state', db.String(200), primary_key=True),
              db.Column('rank', db.Integer())
              )

metadata.create_all(engine) #Creates the table


if __name__ == '__main__':
    level = 3
    state = {'F':[[9]*level, [9, 0, 9], [0]*level], 'R':[[9]*level, [9, 1, 9], [1]*level], 'B':[[9]*level, [9, 2, 9], [2]*level], 'L':[[9]*level, [9, 3, 9], [3]*level], 'D':[[9, 4, 9], [4, 4, 4], [9, 4, 9]], 'U':[[9]*level, [9, 5, 9], [9]*level]}
    rubik = RubikProblem(state, level)
    i = 1
    rbs = [rubik]
    count = 0
    query = db.insert(heuristic).values(state=rubik.string_state(), rank=0)
    connection.execute(query)
    l = len(rbs)
    rangelv = range(level)
    while i <= 5:
        rangel = range(l)
        for j in rangel:
            for dir in rangelv:
                for pos in [0, 2]:
                    for act in [-1, 1]:
                        r = RubikProblem(rbs[0].state,level).action(dir, act, pos)
                        try:
                            query = db.insert(heuristic).values(state=r.string_state(), rank=i)
                            connection.execute(query)
                        except:
                            continue
                        rbs.append(r)
                        count += 1
                        l += 1
                        print(count, l, i)
            rbs.pop(0)
            l -= 1
        i += 1