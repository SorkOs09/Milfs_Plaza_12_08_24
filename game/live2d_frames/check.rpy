init 500 python:
    

    def check_live2d():
        
        try:
            _r = renpy.has_live2d()
        except:
            _r = False

        return _r


    live2d_loaded = check_live2d()


    