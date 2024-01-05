import tkinter as tk
from datetime import datetime, timedelta

class StopwatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Stopwatch App")

        self.is_running = False
        self.start_time = None

        # Stopwatch display
        self.display_var = tk.StringVar()
        self.display_var.set("00:00:00.000")
        self.display_label = tk.Label(master, textvariable=self.display_var, font=('Arial', 24))
        self.display_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Start/Pause button
        self.start_pause_button = tk.Button(master, text="Start", command=self.start_pause_stopwatch, font=('Arial', 12))
        self.start_pause_button.grid(row=1, column=0, padx=5)

        # Reset button
        self.reset_button = tk.Button(master, text="Reset", command=self.reset_stopwatch, font=('Arial', 12))
        self.reset_button.grid(row=1, column=1, padx=5)

        # Quit button
        self.quit_button = tk.Button(master, text="Quit", command=master.destroy, font=('Arial', 12))
        self.quit_button.grid(row=1, column=2, padx=5)

        # Update display every 50 milliseconds
        self.master.after(50, self.update_display)

    def start_pause_stopwatch(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = datetime.now() - timedelta(milliseconds=self.get_elapsed_time())
            self.start_pause_button["text"] = "Pause"
        else:
            self.is_running = False
            self.start_pause_button["text"] = "Resume"

    def reset_stopwatch(self):
        self.is_running = False
        self.start_time = None
        self.display_var.set("00:00:00.000")
        self.start_pause_button["text"] = "Start"

    def update_display(self):
        if self.is_running:
            elapsed_time = self.get_elapsed_time()
            self.display_var.set(self.format_time(elapsed_time))

        self.master.after(50, self.update_display)

    def get_elapsed_time(self):
        if self.start_time is not None:
            return (datetime.now() - self.start_time).total_seconds() * 1000
        return 0

    @staticmethod
    def format_time(milliseconds):
        minutes, milliseconds = divmod(int(milliseconds), 60000)
        seconds, milliseconds = divmod(milliseconds, 1000)
        return f"{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

if __name__ == "__main__":
    root = tk.Tk()
    stopwatch_app = StopwatchApp(root)
    root.mainloop()
