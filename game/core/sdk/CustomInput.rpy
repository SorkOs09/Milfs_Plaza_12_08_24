init -1000 python:
    class CustomInput(store.Input):
        highlight_start = -1
        highlight_end   = -1
        highlight_direction = 0
        def __init__(self,
        default="",
        length=None,
        style='input',
        allow=None,
        exclude='{}[]',
        prefix="",
        suffix="",
        changed=None,
        button=None,
        replaces=None,
        editable=True,
        pixel_width=None,
        value=None,
        copypaste=False,
        caret_blink=None,
        multiline=False,
        **properties):


            store.Input.__init__(
            self,
            default = default,
            length = length,
            style = style,
            allow = allow,
            exclude = exclude,
            prefix = prefix,
            suffix = suffix,
            changed = changed,
            button = button,
            replaces = replaces,
            editable = editable,
            pixel_width = pixel_width,
            value = value,
            copypaste = copypaste,
            caret_blink = caret_blink,
            multiline = multiline,
            **properties)

            self.highlight_start = -1
            self.highlight_end   = -1
            self.highlight_direction = 0
            self.hold_shift      = False


        def update_text(self, new_content, editable, check_size=False):

            edit = renpy.display.interface.text_editing

            old_content = self.content

            if new_content != self.content or editable != self.editable or edit:

                renpy.display.render.redraw(self, 0)

            self.editable = editable

            # Choose the caret.
            caret = self.style.caret

            if caret is None:
                caret = self.caret

            # Format text being edited by the IME.
            if edit:

                self.edit_text = edit.text

                edit_text_0 = edit.text[:edit.start]
                edit_text_1 = edit.text[edit.start:edit.start + edit.length]
                edit_text_2 = edit.text[edit.start + edit.length:]

                edit_text = ""

                if edit_text_0:
                    edit_text += "{u=1}" + edit_text_0.replace("{", "{{") + "{/u}"

                if edit_text_1:
                    edit_text += "{u=2}" + edit_text_1.replace("{", "{{") + "{/u}"

                if edit_text_2:
                    edit_text += "{u=1}" + edit_text_2.replace("{", "{{") + "{/u}"

            else:
                self.edit_text = ""
                edit_text = ""

            def set_content(content):

                if content == "":
                    content = u" "
                highlight = str("{color=#fff}" + content[self.highlight_start:self.highlight_end] + "{/color}")
                if editable:
                    l = len(content)
                    if self.highlight_direction == -1:
                        self.set_text(
                        [
                        self.prefix, 
                        content[0:self.highlight_start].replace("{", "{{"), 
                        edit_text, 
                        caret,
                        highlight, #str("{color=#4e5a65}" + content[self.highlight_start:self.highlight_end] + "{/color}"),#.replace("{", "{{"),
                        content[self.highlight_end:l].replace("{", "{{"), 
                        self.suffix]
                        )
                    elif self.highlight_direction == 1:
                        self.set_text(
                        [
                        self.prefix, 
                        content[0:self.highlight_start].replace("{", "{{"), 
                        edit_text, 
                        highlight, #str("{color=#4e5a65}" + content[self.highlight_start:self.highlight_end] + "{/color}"),#.replace("{", "{{"),
                        caret,
                        content[self.highlight_end:l].replace("{", "{{"), 
                        self.suffix]
                        )
                    else:
                        self.set_text(
                        [
                        self.prefix, 
                        content[0:self.caret_pos].replace("{", "{{"), 
                        edit_text, 
                        caret,
                        content[self.caret_pos:l].replace("{", "{{"), 
                        self.suffix]
                        )
                else:
                    self.set_text([self.prefix, content.replace("{", "{{"), self.suffix ])

                if isinstance(self.caret, renpy.display.behavior.CaretBlink):
                    self.caret.st_base = self.st
                    renpy.display.render.redraw(self.caret, 0)

            set_content(new_content)

            if check_size and self.pixel_width:
                w, _h = self.size()
                if w > self.pixel_width:
                    self.caret_pos = self.old_caret_pos
                    set_content(old_content)
                    return

            if new_content != old_content:
                self.content = new_content

                if self.changed:
                    self.changed(new_content)



        def event(self, ev, x, y, st):

            _highlight = False
            l          = len(self.content)

            if ev.type == pygame.KEYDOWN:
                if (ev.key == pygame.K_LSHIFT):
                    self.hold_shift = True
                
                elif ev.key == pygame.K_LEFT and self.hold_shift:


                    _highlight = True

                    if self.caret_pos > 0:
                        if self.highlight_direction == 0:
                            self.highlight_direction = -1
                            self.highlight_end = self.caret_pos

                        self.caret_pos -= 1

                        if self.highlight_direction == -1:
                            self.highlight_start = self.caret_pos
                        else:
                            self.highlight_end = self.caret_pos

                        if self.highlight_start == self.highlight_end:
                            self.highlight_start = -1
                            self.highlight_end   = -1
                            self.highlight_direction = 0
                        self.update_text(self.content, self.editable)

                    renpy.display.render.redraw(self, 0)
                    raise renpy.display.core.IgnoreEvent()

                elif ev.key == pygame.K_RIGHT and self.hold_shift:


                    _highlight = True
                    if self.caret_pos < l:
                        if self.highlight_direction == 0:
                            self.highlight_direction = 1
                            self.highlight_start = self.caret_pos

                        self.caret_pos += 1


                        if self.highlight_direction == 1:
                            self.highlight_end = self.caret_pos
                        else:
                            self.highlight_start = self.caret_pos




                        if self.highlight_start == self.highlight_end:
                            self.highlight_start = -1
                            self.highlight_end   = -1
                            self.highlight_direction = 0


                        self.update_text(self.content, self.editable)

                    renpy.display.render.redraw(self, 0)
                    raise renpy.display.core.IgnoreEvent()

            if ev.type == pygame.KEYUP:
                if (ev.key == pygame.K_LSHIFT):
                    self.hold_shift = False



            if not _highlight:
                if ev.type == pygame.KEYDOWN:
                    if self.highlight_direction:
                        if ev.key not in (
                            pygame.K_RCTRL,
                            pygame.K_LCTRL,
                            pygame.K_LSHIFT, 
                            pygame.K_RSHIFT, 
                            pygame.K_LALT,
                            pygame.K_RALT,
                            pygame.K_CAPSLOCK,
                            pygame.K_LEFT,
                            pygame.K_RIGHT,
                            pygame.K_DOWN,
                            pygame.K_UP,
                            
                            ):
                            
                            _content = self.content
                            
                            self.caret_pos = self.highlight_start

                            self.content = _content[0:self.highlight_start] + _content[self.highlight_end:l]
                            self.highlight_start = -1
                            self.highlight_end   = -1
                            self.highlight_direction = 0

                        if ev.key in (
                            pygame.K_LEFT,
                            pygame.K_RIGHT,
                            pygame.K_DOWN,
                            pygame.K_UP,
                            ):

                            self.highlight_start = -1
                            self.highlight_end   = -1
                            self.highlight_direction = 0
                        
                Input.event(self, ev, x, y, st)
