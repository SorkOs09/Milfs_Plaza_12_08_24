init 999 python:
    config.developer = False
    config.console   = False
    my_debug_mode    = False
    report_now       = None

    def load_bug_report(path, delete_after = False):
        #rv = preload_bug_report(path)
        #print()
        #custom_load(rv[1:])

        FilePage(1)()
        
        rd = os.path.join(renpy.config.gamedir, path)
        
        xs   = renpy.savelocation.FileLocation(rd)
        
        #if delete_after:
        #    persistent.delete_bug_report_save = True
            
        roots, log = cPickle.loads(xs.load(rd))
        log.unfreeze(roots, label="_after_load")
