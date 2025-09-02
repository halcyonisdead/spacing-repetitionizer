import customtkinter
from sqlite_memory import database_memory   
from datetime import date, timedelta

#MADE BY A CLOUD MAIN, FOR PEOPLE WHO CARE TOO MUCH. ~halcyon

#UI 
class app(customtkinter.CTk): 
    def __init__(ui):
        super().__init__()
        ui.db_manager = database_memory()
        ui.title("Spacing Repetitionizer")        
        ui.geometry("720x480")        
        ui.main_frame = customtkinter.CTkFrame(ui)
        ui.main_frame.pack(pady=20, padx=60, fill="both", expand=True)
        ui.label = customtkinter.CTkLabel(ui.main_frame, text="Enter Topic Studied! :3", font=("Roboto", 24))       
        ui.label.pack(pady=10)
        ui.entry = customtkinter.CTkEntry(ui.main_frame, placeholder_text="Topic Studied", width=300)
        ui.entry.pack(pady=10)
        ui.button = customtkinter.CTkButton(ui.main_frame, text="Studied!", command=ui.on_button_click)
        ui.button.pack(pady=20)
        ui.display = customtkinter.CTkTextbox(ui.main_frame, width=600, height=200)
        ui.display.configure(state="disabled")
        ui.display.pack(pady=10)
        ui.update_display()
    
        
    #BUTTON FUNCTION//REVIEW DATES CALCULATION METHOD

    def calculate_first_review_dates(ui, date_started):
        review_dates = []

        spaced_repetition_firstday = [2]
        
        for days in spaced_repetition_firstday:
            firstreview = date_started + timedelta(days=days)
            secondreview = firstreview + timedelta(days=7)
            thirdreview = secondreview + timedelta(days=21)
            finalreview = thirdreview + timedelta(days=60)
            review_dates.extend([firstreview, secondreview, thirdreview, finalreview])
        return review_dates
    
    def on_button_click(ui):
        topic_studied = ui.entry.get()
        if topic_studied:
            today = date.today()
            review_dates = ui.calculate_first_review_dates(today)
            ui.db_manager.add_topic(topic_studied, today, review_dates)
            print(f"Added {topic_studied} to topics studied on {today}.")
            print(f"Scheduled future review dates for {topic_studied}: {review_dates}")
            ui.entry.delete("end")
            ui.update_display()
            
    #DISPLAY OF DATABASE IN UI METHOD
    def update_display(ui):
        ui.display.configure(state="normal")
        ui.display.delete("1.0", "end")
        schedules = ui.db_manager.get_all_topics()
        for date in schedules:
            topic = date[1]
            date_started = date[2]
            review_dates = date[3:]
            display_review = f"TOPIC STUDIED: {topic}\nINITIAL READING: {date_started} \n - REVIEW DATES!!: {','.join(review_dates)}\n\n"
            ui.display.insert("end", display_review)
        ui.display.configure(state="disabled")
    

if __name__ == "__main__":
    app = app()
    app.mainloop()

















#I FUCKING NEED AN ACTUAL UI BENILDE STUDENT SAVE ME SAVE ME 
# #nothing is, but what is not?