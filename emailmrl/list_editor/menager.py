def initialize(email_sender):
    from emailmrl.list_editor import List_Editor
    
    ems = List_Editor(email_sender)
    ems.enable_window()