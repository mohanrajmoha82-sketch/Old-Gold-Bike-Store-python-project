Old Gold Bike Store

Old Gold Bike Store is a Python-based vintage bike showroom management system developed using Object-Oriented Programming (OOP). The application allows users to register, log in, browse classic Indian bikes, purchase bikes, generate bills, and receive bills through WhatsApp. 

Users can:

• Sign up and log in with OTP verification
• Browse classic Indian bike brands
• View bike details, images, and music
• Purchase bikes
• Generate bills (Image + PDF)
• Make payments using UPI QR Code or Debit Card
• Receive bills through WhatsApp

User Authentication
• Sign Up
• Login
• OTP verification through WhatsApp
• Username validation
• Mobile number validation

Bike Showroom
Available bike companies:

•  Royal Enfield 
•  Ideal Jawa 
•  Yezdi 
•  Escorts Yamaha 
•  Hero Honda 
•  TVS Suzuki 
•  Bajaj Auto 
•  Rajdoot 
•  Kinetic Honda 
•  LML

Bike Information
Displays:

•  Model Name 
•  Color 
•  Price 
•  Launch Year 
•  Engine Details 
•  Top Speed 
•  Bike Description

Billing System
Generates:

•  Customer Bill 
•  Payment Details 
•  Remaining Amount 
•  Order Date

Payment Methods

1.UPI Payment

   •  QR Code Generation 
   •  Discount Calculation
2.Debit Card Payment

WhatsApp Integration
Uses pywhatkit to:

•  Send OTP 
•  Send Bike Bill 
•  Send Bill Image

Bill Generation
Creates:

•  PNG Bill Slip 
•  PDF Bill Slip

Technologies Used

•  Python 
•  OOP (Classes & Inheritance) 
•  Pygame 
•  Pillow (PIL) 
•  PyWhatKit 
•  PyAutoGUI 
•  QRCode 
•  ReportLab

Install required packages:

pip install qrcode
pip install pywhatkit
pip install pyautogui
pip install pillow
pip install pygame
pip install reportlab

Sample Workflow

1. Sign
2. Login

↓
OTP Verification

↓
Choose Bike Company

↓
Choose Bike Model

↓
View Bike Details

↓
Buy Bike

↓
Choose Payment Method

↓
Generate Bill

↓
Receive WhatsApp Bill




