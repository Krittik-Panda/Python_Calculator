🧮 Python Scientific Calculator

A simple and modular Scientific Calculator built in Python.
This project is divided into two main components:

functions.py – Contains all mathematical functions

calculator_simulator.py – The core logic that displays a calculator menu, takes user input, and calls the appropriate functions

This structure makes the project clean, organized, and easy to extend.

📁 Project Structure
Python_Calculator/
│
├── functions/
│   └── functions.py            # Contains all math operations
│
└── calculator_simulator.py     # Menu-driven calculator logic

✨ Features
🔢 Basic Math Operations

Addition

Subtraction

Multiplication

Division

Modulus

🔍 Number Checks

Even or Odd

Positive or Negative

🧠 Advanced Math

Factorial (recursive)

Fibonacci sequence

Nth Fibonacci number

📐 Trigonometry

Sine

Cosine

Tangent

🧮 Conversions

Radian → Degree

Degree → Radian

📊 Logarithmic Function

Natural logarithm (log(value))

🚀 How to Run
Step 1 — Clone the repository
git clone https://github.com/<your-username>/<your-repo-name>.git

Step 2 — Open project directory
cd Python_Calculator

Step 3 — Run the calculator
python calculator_simulator.py

🖥️ User Interface

The calculator displays a menu-driven interface where the user chooses an operation.

Example:

===== SCIENTIFIC CALCULATOR =====
1. Addition
2. Subtraction
3. Multiplication
4. Division
...
0. Exit


The screen clears after each operation using:

os.system("cls" if os.name == "nt" else "clear")

🧩 Modularity

All functions are stored separately inside functions.py so that the main calculator code remains:

Clean

Readable

Easy to maintain

This also allows developers to extend functionality without modifying the main simulator.

🛠️ Technologies Used

Python 3.x

Standard Libraries (math, os)

🤝 Contributing

Feel free to fork this project and submit pull requests.
You can also open issues if you find bugs or want improvements.

📄 License

This project is open-source under the MIT License.
