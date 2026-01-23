import tkinter as tk
from tkinter import messagebox
from bernoulli_numbers_generator import *

class GUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Input GUI")
        self.root.geometry("500x600")
        
        # State variables
        self.radio_var = tk.StringVar(value="option1")
        self.switch_state = False
        self.number_var = tk.StringVar()
        
        # ===== Radio Button Section =====
        radio_frame = tk.LabelFrame(root, text="Which part of the Bernoulli numbers would you like?", padx=10, pady=10)
        radio_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Radiobutton(radio_frame, text="The whole number", variable=self.radio_var, 
                       value="option1_total").pack(anchor=tk.W)
        tk.Radiobutton(radio_frame, text="The numerator", variable=self.radio_var, 
                       value="option2_numerator").pack(anchor=tk.W)
        tk.Radiobutton(radio_frame, text="The denominator", variable=self.radio_var, 
                       value="option3_denominator").pack(anchor=tk.W)
        
        # ===== Switch/Toggle Button Section =====
        switch_frame = tk.Frame(root)
        switch_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(switch_frame, text="Output the list to a file?:").pack(side=tk.LEFT)
        self.switch_button = tk.Button(switch_frame, text="No", width=8, bg="lightcoral",
                                       command=self.toggle_switch)
        self.switch_button.pack(side=tk.LEFT, padx=5)
        
        # ===== Integer Input Section =====
        input_frame = tk.Frame(root)
        input_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(input_frame, text="I would like the first").pack(side=tk.LEFT)
        self.number_entry = tk.Entry(input_frame, width=10)
        self.number_entry.pack(side=tk.LEFT, padx=5)
        tk.Label(input_frame, text="Bernoulli numbers please and thank you...").pack(side=tk.LEFT)
        
        # ===== Run Button =====
        self.run_button = tk.Button(root, text="Run", command=self.run_code, 
                                    bg="lightgreen", font=("Arial", 12, "bold"))
        self.run_button.pack(pady=20)
        
        # ===== Output Display Area =====
        output_frame = tk.LabelFrame(root, text="Output", padx=10, pady=10)
        output_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.output_text = tk.Text(output_frame, height=8, width=40, 
                                   state=tk.DISABLED, bg="lightgray")
        self.output_text.pack(fill="both", expand=True)
    
    def toggle_switch(self):
        """Toggle the switch state and update button appearance"""
        self.switch_state = not self.switch_state
        if self.switch_state:
            self.switch_button.config(text="Yes", bg="lightgreen")
        else:
            self.switch_button.config(text="No", bg="lightcoral")
    
    def run_code(self):
        """Collect input data and execute code"""
        try:
            # Get the selected radio option
            selected_option = self.radio_var.get()
            
            # Get the switch state
            switch_state = self.switch_state
            
            # Get and validate the number input
            number_input = self.number_entry.get()
            if number_input and int(number_input)>0:
                user_number = int(number_input)
            else:
                messagebox.showwarning("Input Error", "Please enter a number positive integer greater than zero")
                return
            
            # ===== ADD YOUR CODE HERE =====
            # Use the following variables in your code:
            # - selected_option (str): the radio button selection
            # - switch_state (bool): True if ON, False if OFF
            # - user_number (int): the integer entered
            # Your code should assign the result to 'output_result'
            if selected_option == "option1_total":
                output_result = bernoulli_numbers_total(user_number, switch_state)
            elif selected_option == "option2_numerator":
                output_result = bernoulli_numbers_numerator(user_number, switch_state)
            elif selected_option == "option3_denominator":
                output_result = bernoulli_numbers_denominator(user_number, switch_state)
                        
            # Display output in the text widget
            self.display_output(output_result)
            #print(f"Option: {selected_option}, Switch: {switch_state}, Number: {user_number}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer")
    
    def display_output(self, result):
        """Display output in the text widget"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", str(result))
        self.output_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()
