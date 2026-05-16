import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os


class CheckSumrGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CheckSumr - Hash Verification & Generation")
        self.root.geometry("700x550")
        self.root.resizable(False, False)
        
        self.file_path = None
        self.hashing_obj = None
        
        self.setup_ui()
    
    def setup_ui(self):
        # Title Label
        title_label = tk.Label(
            self.root, 
            text="CheckSumr", 
            font=("Arial", 24, "bold"),
            fg="#2c3e50"
        )
        title_label.pack(pady=15)
        
        # File Selection Frame
        file_frame = tk.LabelFrame(
            self.root, 
            text="File Selection", 
            font=("Arial", 12, "bold"),
            padx=10, 
            pady=10
        )
        file_frame.pack(padx=20, pady=10, fill="x")
        
        self.file_label = tk.Label(
            file_frame, 
            text="No file selected", 
            font=("Arial", 10),
            fg="#7f8c8d",
            wraplength=600
        )
        self.file_label.pack(side="left", padx=5)
        
        browse_btn = tk.Button(
            file_frame, 
            text="Browse", 
            command=self.browse_file,
            bg="#3498db",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=5,
            cursor="hand2"
        )
        browse_btn.pack(side="right", padx=5)
        
        # Hash Verification Frame
        verify_frame = tk.LabelFrame(
            self.root, 
            text="Hash Verification", 
            font=("Arial", 12, "bold"),
            padx=10, 
            pady=10
        )
        verify_frame.pack(padx=20, pady=10, fill="x")
        
        tk.Label(
            verify_frame, 
            text="Enter Hash to Verify:", 
            font=("Arial", 10)
        ).pack(anchor="w", pady=(0, 5))
        
        self.hash_input = tk.Entry(
            verify_frame, 
            font=("Arial", 10),
            width=70
        )
        self.hash_input.pack(pady=5)
        
        verify_btn = tk.Button(
            verify_frame, 
            text="Verify Hash", 
            command=self.verify_hash,
            bg="#27ae60",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5,
            cursor="hand2"
        )
        verify_btn.pack(pady=10)
        
        # Hash Generation Frame
        generate_frame = tk.LabelFrame(
            self.root, 
            text="Hash Generation", 
            font=("Arial", 12, "bold"),
            padx=10, 
            pady=10
        )
        generate_frame.pack(padx=20, pady=10, fill="both", expand=True)
        
        tk.Label(
            generate_frame, 
            text="Select Hash Algorithm:", 
            font=("Arial", 10)
        ).pack(anchor="w", pady=(0, 5))
        
        self.hash_algorithm = ttk.Combobox(
            generate_frame,
            values=["md5", "sha1", "sha224", "sha256", "sha3_256", 
                    "sha384", "sha3_384", "sha512", "sha3_512"],
            state="readonly",
            font=("Arial", 10),
            width=20
        )
        self.hash_algorithm.current(0)
        self.hash_algorithm.pack(pady=5)
        
        generate_btn = tk.Button(
            generate_frame, 
            text="Generate Hash", 
            command=self.generate_hash,
            bg="#e67e22",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=20,
            pady=5,
            cursor="hand2"
        )
        generate_btn.pack(pady=10)
        
        # Output Frame
        output_label = tk.Label(
            generate_frame, 
            text="Generated Hash:", 
            font=("Arial", 10)
        )
        output_label.pack(anchor="w", pady=(10, 5))
        
        self.output_text = tk.Text(
            generate_frame, 
            height=4, 
            font=("Courier", 9),
            wrap="char",
            bg="#ecf0f1"
        )
        self.output_text.pack(fill="both", expand=True, pady=5)
        
        copy_btn = tk.Button(
            generate_frame, 
            text="Copy to Clipboard", 
            command=self.copy_to_clipboard,
            bg="#95a5a6",
            fg="white",
            font=("Arial", 9, "bold"),
            padx=15,
            pady=3,
            cursor="hand2"
        )
        copy_btn.pack(pady=5)
    
    def browse_file(self):
        """Open file dialog to select a file"""
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("All Files", "*.*")]
        )
        if file_path:
            self.file_path = file_path
            self.file_label.config(
                text=f"Selected: {os.path.basename(file_path)}", 
                fg="#2c3e50"
            )
    
    def verify_hash(self):
        """Verify the hash of the selected file"""
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file first!")
            return
        
        hash_value = self.hash_input.get().strip()
        if not hash_value:
            messagebox.showerror("Error", "Please enter a hash value to verify!")
            return
        
        try:
            from Hashing import Hashing
            hashing_obj = Hashing(self.file_path, hash_value, auto_run=True)
            result = hashing_obj.result
            
            if result is True:
                messagebox.showinfo(
                    "Verification Success", 
                    "✓ Hash verification PASSED!\n\nThe file matches the provided hash."
                )
            elif result is False:
                messagebox.showwarning(
                    "Verification Failed", 
                    "✗ Hash verification FAILED!\n\nThe file does NOT match the provided hash."
                )
            else:
                messagebox.showerror("Error", f"Verification error: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
    
    def generate_hash(self):
        """Generate hash for the selected file"""
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file first!")
            return
        
        algorithm = self.hash_algorithm.get()
        
        try:
            from Hashing import Hashing
            hashing_obj = Hashing(self.file_path, '', auto_run=False)
            hash_result = hashing_obj.gen_hash(algorithm)
            
            # Debug: Print to console to see what we got
            print(f"Hash result type: {type(hash_result)}")
            print(f"Hash result value: {hash_result}")
            
            # Clear previous output and insert new hash
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", str(hash_result))
            
            # Force update the text widget
            self.output_text.update_idletasks()
            
            messagebox.showinfo(
                "Success", 
                f"{algorithm.upper()} hash generated successfully!\n\nHash: {hash_result[:32]}..."
            )
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}\n\nDetails:\n{error_details}")
    
    def copy_to_clipboard(self):
        """Copy the generated hash to clipboard"""
        hash_value = self.output_text.get(1.0, tk.END).strip()
        if hash_value:
            self.root.clipboard_clear()
            self.root.clipboard_append(hash_value)
            messagebox.showinfo("Copied", "Hash copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No hash to copy!")
    
    def run(self):
        """Start the GUI main loop"""
        self.root.mainloop()
