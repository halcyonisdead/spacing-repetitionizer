import customtkinter
from datetime import date, timedelta

#MADE BY A CLOUD MAIN, FOR PEOPLE WHO CARE TOO MUCH. ~halcyon

#UI CLASS
class app(customtkinter.CTk): 
    def __init__(ui):
        super().__init__()
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
    #BUTTON FUNCTION//REVIEW DATES CALCULATION METHOD
    def calculate_future_review_dates(ui, date_started):
        spaced_repetition_algo = [3, 7, 14, 30, 60, 120]
        review_dates = []
        for days in spaced_repetition_algo:
            next_review = date_started + timedelta(days=days)
            review_dates.append(next_review)
        return review_dates
    def on_button_click(ui):
        topic_studied = ui.entry.get()
        if topic_studied:
            today = date.today()
            review_dates = ui.calculate_future_review_dates(today)
            print(f"Added {topic_studied} to topics studied on {today}.")
            print(f"Scheduled future review dates for {topic_studied}: {review_dates}")
            ui.entry.delete("end")

if __name__ == "__main__":
    app = app()
    app.mainloop()


















 #nothing is, but what is not?
