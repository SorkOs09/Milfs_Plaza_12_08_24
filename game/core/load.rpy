
init 20 python:
    import threading, zipfile, shutil, cPickle

    def get_custom_save_files(fl = 'nnnnnnnnnnnnnnnn'):
        rtrn = []
        for i in list_files:
            if '.save' in i.lower():
                if fl.lower() in i.lower():
                    return i
                rtrn.append(i)
        return rtrn

    disk_lock = threading.RLock()
    persistent.from_gallery = None
    def custom_preload(version):
        global android_load
        
        
        
        file =  os.path.join(renpy.config.gamedir, 'test_saves', version +'.save')
        
        with disk_lock:
            
            zf = zipfile.ZipFile(file, "r")
            rv = zf.read("log")
            
            
            zf.close()
            
            return rv

    def create_dump_line(version):
        dm = custom_preload(version)
        #os.path.join(renpy.config.gamedir, 'test_saves', version +'.save')
        
        f = open(os.path.join(renpy.config.gamedir, 'test.txt'), 'wb')
        cPickle.dump(dm, f)
        
        f.close()
    def custom_load(log_string):
        
        
        
        
        
        
        roots, log = cPickle.loads(log_string.encode('latin-1'))
        log.unfreeze(roots, label="_after_load")


    def custom_load_from_file(version, gallery = True, trig_custom_load = False):
        global wardrobe
        global store
        global persistent
        
        
        if gallery:
            persistent.from_gallery = True
        if trig_custom_load:
            persistent.custom_load  = True
        
        FilePage(1)()
        
        path = os.path.join(renpy.config.gamedir, 'test_saves', version)
        
        xs   = renpy.savelocation.FileLocation(path)
        
        roots, log = cPickle.loads(xs.load(path))
        log.unfreeze(roots, label="_after_load")
