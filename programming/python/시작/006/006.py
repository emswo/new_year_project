import os
def se(dire):
    try:
        fire = os.listdir(dire)
        for firef in fire:
            ffil = os.path.join(dire,firef)
            if os.path.isdir(ffil):
                se(ffil)
            else:
                ext = os.path.splitext(ffil)[-1]
                if ext == '.py':
                    print(ffil)
    except: pass
se("C:\\")