def initialize():
    from emailmrl.email_sender import Email_Sender
    
    ems = Email_Sender()
    ems.enable_window()