## **Clicker da Bubs**

This a simple Python program that automates mouse clicks, allowing the user to click in a specific interval of time. This program was built using the Tkinter library for GUI, PyAutoGUI for automating mouse clicks, and the time library for time-related operations.

### **How it works**

When the user clicks on the "CLICAR" button, the program starts to automate mouse clicks. The interval between clicks is 60 seconds, and the program keeps track of the number of clicks made. A label shows the number of clicks made, and another label shows the remaining time for the next click. When the time is up, the program clicks the mouse and resets the timer.

The program also has a "STOP" button that stops the automation and resets the timer, clicks count, and other relevant variables.

### **Concepts used**

#### **Tkinter**

Tkinter is a Python library that allows programmers to create GUI applications. In this program, Tkinter was used to create the graphical interface, which consists of two buttons, three labels, and a frame.

#### **PyAutoGUI**

PyAutoGUI is a cross-platform GUI automation library that allows users to control the mouse and keyboard programmatically. In this program, PyAutoGUI was used to automate mouse clicks.

#### **Time**

The time library is a built-in Python library that provides various time-related functions. In this program, time was used to measure the time elapsed between clicks, keep track of the remaining time for the next click, and measure the time elapsed since the start of the program. 

### **How to run the program**

To run the program, you need to have Python 3 installed on your machine, along with the Tkinter and PyAutoGUI libraries. Then, you can simply run the "clicker.py" file from your terminal or Python IDLE.

```python
python clicker.py
```

### **Disclaimer**

This program is for educational purposes only. Please use it responsibly and do not misuse it to harm others. The author of this program is not responsible for any damage or harm caused by the use of this program.