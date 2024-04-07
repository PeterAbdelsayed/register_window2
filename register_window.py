import tkinter as tk
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class register_window(tk.Tk):

    def send_confirmation_email(self, email):
        # Email configuration
        sender_email = "TechWizardsCSUN@outlook.com"
        sender_password = "Comp380CSUN"
        smtp_server = "smtp-mail.outlook.com"
        smtp_port = 587 

        # Message configuration
        subject = "Account Creation Confirmation"
        message = "Hello User, \n\nYour account has been successfully created! \n\nThank you for choosing TechWizards! "

        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject

        # Attach message to container
        msg.attach(MIMEText(message, 'plain'))

        # Start SMTP session
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, msg.as_string())
        
        print("Confirmation email sent to", email)

    def check(self, controller, email_entry):
        #Logic for checking if info exist
        self.send_confirmation_email(email_entry.get())  # Send confirmation email
        controller.run_login()

    def page(self, controller):
        self.geometry("500x600")
        self.config(bg="#4a464d")
        self.minsize(500, 600)
        self.maxsize(500, 600)

        loginTitle = tk.Label(self, text="Register", fg="white", bg="#4a464d")
        loginTitle.pack(pady=10)
        loginTitle.config(font=("Courier", 12))

        entryFrame = tk.Frame(self, borderwidth=10,bg="#4a464d")
        entryFrame.pack(anchor="w")

        nameLbl = tk.Label(entryFrame, text="Username", bg="#4a464d",fg="white", font=("Courier", 12))
        nameLbl.grid(row=1,  column=0,padx=5, pady=10)

        emailLbl = tk.Label(entryFrame, text="Email", bg="#4a464d",fg="white", font=("Courier", 12))
        emailLbl.grid(row=2,  column=0,padx=5, pady=10)

        passwordLbl = tk.Label(entryFrame, text="Password", bg="#4a464d",fg="white", font=("Courier", 12))
        passwordLbl.grid(row=3,  column=0,padx=5, pady=10)

        nameEn = tk.Entry(entryFrame)
        nameEn.grid(row=1,  column=1)

        self.email_entry = tk.Entry(entryFrame)  # Define email_entry
        self.email_entry.grid(row=2, column=1)

        passwordEn = tk.Entry(entryFrame)
        passwordEn.grid(row=3,  column=1)

        backBtn = tk.Button(entryFrame, text="Back", bg="#888a86", activebackground="#a8aba6", command = lambda: [controller.run_login(), self.withdraw()])
        backBtn.grid(row=0,  column=0)

        submitBtn = tk.Button(entryFrame, text="Create an Account", bg="#888a86", activebackground="#a8aba6", command = lambda: [self.check(controller, self.email_entry), self.withdraw()])
        submitBtn.grid(row=4,  column=1,padx=5, pady=10)

    
if __name__ == "__main__":
    root = register_window()
    root.page(root)
    root.mainloop()
