import random as r
from traceback import print_tb
import qrcode
import pywhatkit as pk
import pyautogui as pg
import os
from statistics import quantiles
from PIL import Image,ImageDraw,ImageFont
import pygame as p
import time as t
from datetime import datetime
from reportlab.lib.pagesizes import A5
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.lib.utils import ImageReader
from soupsieve.css_types import SelectorList

LOGIN = "login_details.txt"
# Create file if not exists
if not os.path.exists(LOGIN):
    open(LOGIN, "w").close()

#================================ Bike Details ======================#
class Bike_details:
    model = None
    color = None
    price=None
    launch_year = None
    engine = None
    top_speed = None
    details = None

    def __init__(self, model, color,price,launch_year, engine, top_speed, details):
        self.model = model
        self.color = color
        self.price = price
        self.launch_year = launch_year
        self.engine = engine
        self.top_speed = top_speed
        self.details = details

    def Bike(self):
        print()
        print(" Bike details ".center(60, "="))
        print("㉦  Model: ", self.model)
        print(f"㉦ {self.model} Color: ", self.color)
        print(f"㉦ {self.model} price₹:", self.price)
        print(f"㉦ {self.model} Launch Year: ", self.launch_year)
        print(f"㉦ {self.model} Engine: ", self.engine)
        print(f"㉦ {self.model} Top Speed: ", self.top_speed)
        print(f"㉦ Details: ", self.details)
#=========================== Customer Details ========================#
class Customer:
    Name=None
    Mobile_3=None

    def __init__(self, Name, Mobile_3):
        self.Name = Name
        self.Mobile_3 = Mobile_3

    def customer_details(self):
        print("Customer Created".center(60, "="))
        print("Name :", self.Name)
        print("Mobile :", self.Mobile_3)
#============================== Bike Bill Details =========================#
class Bill(Bike_details,Customer):
    def __init__(self, model, color, price,launch_year, engine, top_speed, details,Name, Mobile_3):
        Bike_details.__init__(self,model,color,price,launch_year,engine,top_speed,details)
        Customer.__init__(self,Name,Mobile_3)

    def Generate_bill(self):
        Quantiles = int(input("Enter the Quantity: "))
        Price = self.price * Quantiles
        print()
        print("BIKE SALES BILL".center(60,"="))
        self.customer_details()
        print("Bike Model:",self.model)
        print("Price:",self.color)
        print("Quantiles:",Quantiles)
        print("Total Amount:",Price)
        print("Payment Method".center(60,"="))
        print("1.UPI")
        print("2.Debit card")
        pay = input("Enter the choice: ")
        if pay == "1":
            upi_pay = int(float(Price) - (float(Price) * 70 / 100))
            upi_id = "yourname@bank"
            name = self.Name
            amount = upi_pay
            currency = "INR"
            pay_id = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(pay_id)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
            canvas = Image.new("RGB", (img.size[0], img.size[1] + 80), "white")
            canvas.paste(img, (0, 80))
            draw = ImageDraw.Draw(canvas)
            try:
                font = ImageFont.truetype("arial.ttf", 40)
            except:
                font = ImageFont.load_default()
            draw.text((canvas.size[0] // 2 - 80, 20), "PY-Pay", fill="green", font=font)
            canvas.save("py_pay_qr.png")
            p.init()
            p.display.set_caption("PY-Pay - SCAN TO PAY")
            ps1 = p.display.set_mode(canvas.size)
            ps1.blit(p.image.load("py_pay_qr.png"), (0, 0))
            p.display.update()
            t.sleep(10)
            p.quit()
            t.sleep(10)
            print("Payment Successful...✔")
        elif pay == "2":
            DEBIT_CARD = input("Enter the Debit Card No: ")
            print("₹",Price)
            PIN_number = input("Enter the PIN Number: ")
            t.sleep(3)
            print("Payment Successful...✔")
        else:
            print("Payment Method Not Define")
            b.Generate_bill()
        t.sleep(2)
        print("Your Order Confirmed")
        t.sleep(2)
        print("Standard delivery usually takes 5-7 days")
        t.sleep(1)
        print("Sending Bike Bill Copy to WhatsApp....")
        # t.sleep(10)
#============== Sending Messange in Whatsapp ==============#
        message="""
         ◉ ◉ ◉ ◉ ◉ ◉ OLD GOLD BIKS STORE ◉ ◉ ◉ ◉ ◉ ◉
        ◉ Name          : {}
        ◉ Moblie No     : {}
        ------------- BIKE SALES BILL --------------
         ◉ Bike Model      : {}
         ◉ Color           : {}
         ◉ Price           : ₹{}
         ◉ Quantiles       : {}
         ◉ Total Amount    : {}  
         -------------------------------------------
         Contact:+919876543210|oldgold@bike.com|@oldgoldbikesto
         Delivery
         ◉ Standard delivery usually takes 5-7 days  
        """
        bike_bill=message.format(self.Name,self.Mobile_3,self.model,self.color,self.price,Quantiles,Price)

        # --------------------SAMPLE VARIABLES---------------------------

        name = self.Name
        phone = self.Mobile_3
        bike_model = self.model
        bike_color = self.color
        bike_price = self.price
        bike_quantiles = Quantiles
        total_amount = Price
        date= datetime.now().date()
        remaining_amount= int(float(Price) - (float(Price) * 30 / 100))

        ASSETS_DIR = "assets"
        os.makedirs(ASSETS_DIR, exist_ok=True)
        db = {"appointments": []}

        # DATABASE SAVE FUNCTION
        def save_db(data):
            print("Database saved.")

        # PILLOW Bill IMAGE
        SW, SH = 720, 900
        slip = Image.new("RGB", (SW, SH), "white")
        d = ImageDraw.Draw(slip)
        try:
            f_title = ImageFont.truetype("arialbd.ttf", 34)
            f_h = ImageFont.truetype("arialbd.ttf", 22)
            f_t = ImageFont.truetype("arial.ttf", 20)
        except Exception:
            f_title = f_h = f_t = ImageFont.load_default()
        # Header
        d.rectangle([(0, 0), (SW, 90)], fill="#d6336c")
        d.text((150, 25),"OLD GOLD BIKE STORE",fill="white",font=f_title)
        y = 130
        fields = [

            ("Name", name),
            ("Mobile", phone),
            ("Bike Model", bike_model),
            ("Color", bike_color),
            ("price", bike_price),
            ("Quantiles",   bike_quantiles),
            ("Total Amount₹", str(total_amount)),
            ("Pay Amount₹", str(upi_pay)),
            ("Remaining Amount₹", str(remaining_amount)),
            ("Order Date", date)]
        for label, val in fields:
            d.text((40, y), f"{label:<15}: {val}", fill="#222222", font=f_t)
            y += 40
        # Footer
        d.rectangle([(0, SH - 90), (SW, SH)], fill="#12b886")
        d.text(
            (50, SH - 60),
            "Contact:+919876543210|oldgold@bike.com|@oldgoldbikesto",
            fill="white",
            font=f_h)
        # SAVE IMAGE
        slip_img_path = os.path.join(
            ASSETS_DIR,
            f"slip_{name}.png")
        slip.save(slip_img_path)
        print("Slip image saved at :", slip_img_path)
        # CREATE PDF
        slip_pdf_path = os.path.join(
            ASSETS_DIR,
            f"slip_{name}.pdf")
        c = pdf_canvas.Canvas(
            slip_pdf_path,
            pagesize=A5)
        c.drawImage(
            ImageReader(slip_img_path),20,20,width=A5[0] - 40,height=A5[1] - 40,preserveAspectRatio=True)
        c.showPage()
        c.save()
        print("Slip PDF saved at :", slip_pdf_path)
        # SAVE TO DATABASE
        db["appointments"].append({

            "name": name,
            "phone": phone,
            "model": bike_model,
            "color": bike_color,
            "quantiles": bike_quantiles,
            "price": bike_price,
            "total amount": total_amount,
            "Pay Amount₹":upi_pay,
            "Remaining Amount₹":remaining_amount,
            "order date": date,
            "created_at": datetime.now().isoformat()
        })
        save_db(db)
        try:
            # Send image
            pk.sendwhats_image(
                receiver=f"+91{phone}",
                img_path=slip_img_path,
                caption=bike_bill,
                wait_time=20,
                tab_close=True)
        except Exception as e:
            try:
                # Fallback text message
                pk.sendwhatmsg_instantly(f"+91{phone}",bike_bill, wait_time=20, tab_close=True)
                time.sleep(5)
                print("Bike Bill text message sent successfully!")
            except Exception as e2:
                print("Bike Bill text message failed!")

#================ pygame Image and Music ===========================#
def Image_and_music(model,img,mic):
    p.init()
    p.mixer.init()
    # set up display Name
    p.display.set_caption(model)
    # set up display
    ps1 = p.display.set_mode((636, 650))
    # load background Image
    ps = p.image.load(img)
    ps = p.transform.scale(ps, (636, 650))
    ps1.blit(ps, (0, 0))
    # update display
    p.display.update()
    # load background music
    p.mixer.music.load(mic)
    p.mixer.music.play(-1)
    # wait for image and music
    t.sleep(10)
    p.mixer.music.stop()
    p.quit()
    t.sleep(3)
#================= LML ===============#
def LML_Menu():
    class LML_NV():
        def model1(self):
            c = c = ["Red", "Black",""]
            color = r.choice(c)
            price = r.randrange(30000, 100000, 4999)
            Image_and_music("Kinetic Honda", r"images&music\LML NV (Vespa NV Series).jpg", r"images&music\LMI NV.mpeg")
            bike = Bike_details("LML NV (Vespa NV Series)",
                                f"{color}",
                                f"{price}",
                                "1986",
                                "100cc–150cc, 2-stroke",
                                "80 km/h",
                                """
            ◉ Vespa-style scooter licensed from Italy (Piaggio collaboration)
            ◉ Strong metal body design
            ◉ Very popular family scooter in India
            ◉ Manual gear twist system
                                """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                LML_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
#========================== LML Supremo ==========================#
    class LML_Supremo:
        def model2(self):
            c = c = ["Grwy", "Black","Blue"]
            color = r.choice(c)
            price = r.randrange(60000, 200000, 4999)
            Image_and_music("LMI", r"images&music\LML NV.jpg", r"images&music\LMI supermo.mpeg")
            bike = Bike_details("LML Supremo",
                                f"{color}",
                                f"{price}",
                                "1995",
                                "150cc, 2-stroke",
                                "85 km/h",
                                """
            ◉ Premium scooter inspired by Vespa Cosa
            ◉ Comfortable seat and strong build
            ◉ Used for family and business commuting
            ◉ Rare collector scooter today
                                """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                LML_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
    class LMI(LML_NV,LML_Supremo):
        def model(self):
            print(" LMI Model ".center(60,"="))
            l="""
    1.LML NV (Vespa NV Series)
    2.LML Supremo
    3.Back
            """
            print(l)
    lmi=LMI()
    lmi.model()
    choose_model=input("Enter your LMI choice: ")
    if choose_model == "1":
        lmi.model1()
    elif choose_model == "2":
        lmi.model2()
    elif choose_model == "3":
        LML_Menu()
    else:
        bike_company_name()


#====================== Kinetic Honda =================#
def Kinetic_Honda_Menu():
    class Kinetic_Honda:
        def model(self):
            print("Kinetic Honda Model".center(60,"="))
            c = c = ["Grwy","Black"]
            color = r.choice(c)
            price = r.randrange(25000, 70000, 4999)
            Image_and_music("Kinetic Honda", r"images&music\Kinetic Honda.jpg", r"images&music\Kinetic honda.mpeg")
            bike = Bike_details("Kinetic Honda EX",
                                f"{color}",
                                f"{price}",
                                "1984",
                                "98cc, 2-stroke",
                                "60–70 km/h",
                                """
            ◉ India’s first automatic (gearless) scooter
            ◉ Electric start (rare at that time)
            ◉ Very smooth riding in city traffic
            ◉ Strong nostalgic value in India 
                                """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                bike_company_name()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
    kinetic_honda = Kinetic_Honda()
    kinetic_honda.model()

#===================== Rajdoot Honda ==================#
def Rajdoot_Honda_Menu():
    class Rajdoot_Honda:
        def  model(self):
            print("Rajdoot Honda Model".center(60, "="))
            c=c = ["Blue", "Red", "Black"]
            color = r.choice(c)
            price = r.randrange(50000, 100000, 4999)
            Image_and_music("Rajdoot Honda", r"images&music\Rajdoot Rajdoot 175.jpg", r"images&music\Rajdoot.mpeg")
            bike = Bike_details("Rajdoot Rajdoot 175",
                                f"{color}",
                                f"{price}",
                                "1962",
                                 "173cc, 2-stroke single-cylinder",
                                "90 km/h",
                                """
            ◉ One of India’s most durable motorcycles
            ◉ Widely used in villages and small town
            ◉ Strong load-carrying capacity
            ◉ Simple engine and easy maintenance
                                """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                bike_company_name()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
    rajdoot_honda = Rajdoot_Honda()
    rajdoot_honda.model()

#===================== Bajaj Auto ========================#
def Bajaj_Auto_Menu():
#========================== Bajaj M80 ========================#
    class Bajaj_M80:
        def model1(self):
            c = ["Blue", "Red", "Green"]
            color = r.choice(c)
            price = r.randrange(20000, 60000, 999)
            Image_and_music("Bajaj Auto", r"images&music\Bajaj M80.jpg", r"images&music\Bajaj M80.mpeg")
            bike = Bike_details("Bajaj M80",
                                f"{color}",
                                f"{price}",
                                "1983",
                                "74cc, 2-strok",
                                "70 km/h",
                                """
            ◉ Combination of moped and motorcycle
            ◉ Lightweight utility vehicle
            ◉ Popular in rural India for carrying goods
            ◉ Fuel-efficient and easy to maintain
                                """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                Bajaj_Auto_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
#============================== Bajaj Auto ====================#
    class Bajaj_Sunny:
        def model2(self):
            c = ["Blue", "Red", "Black"]
            color = r.choice(c)
            price = r.randrange(10000, 50000, 999)
            Image_and_music("Bajaj Auto", r"images&music\Bajaj Sunny.jpg", r"images&music\Bajaj sunny.mpeg")
            bike = Bike_details("Bajaj Auto",
                                f"{color}",
                                f"{price}",
                                "1990",
                                "60cc, 2-stroke",
                                "50 km/h",
                                """
            ◉ Lightweight automatic scooter-bike
            ◉ Easy riding for students and women riders
            ◉ Good mileage and compact size
            ◉ Very popular in urban areas during the 1990s
                                """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                Bajaj_Auto_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
    class Bajaj_Auto(Bajaj_M80,Bajaj_Sunny):
        def model(self):
            print("Bajaj Auto Model".center(60,"="))
            l="""
    1.Bajaj M80
    2.Bajaj Sunny
    3,Back
            """
            print(l)
    bajaj=Bajaj_Auto()
    bajaj.model()
    choose_model=input("Enter your Bajaj Auto Model choice: ")
    if choose_model == "1":
        bajaj.model1()
    elif choose_model == "2":
        bajaj.model2()
    elif choose_model == "3":
        bike_company_name()
    else:
        Bajaj_Auto_Menu()

# ====================== TVS Suzuki =============================#
def TVS_Suzuki_Menu():
    class TVS_Suzuki:
        def model(self):
            print("TVS Suzuki Model".center(60, "="))
            c = ["Blue", "Red", "Black"]
            color = r.choice(c)
            price = r.randrange(50000, 100000, 4999)
            Image_and_music("TVS Suzuk", r"images&music\TVS Suzuki Model.jpg", r"images&music\Yezdi.mpeg")
            bike = Bike_details("TVS SUZUKI",
                                f"{color}",
                                f"{price}",
                                "1984",
                                "98cc, 2-stroke single-cylinder",
                                "85 km/h",
                                """
            ◉ One of the first successful TVS Suzuki motorcycles
            ◉ Lightweight and fuel efficient
            ◉ Easy maintenance and reliable engine
            ◉ Popular commuter bike in villages and cities
                              """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                bike_company_name()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
    tvs=TVS_Suzuki()
    tvs.model()
#=================== Escorts Yamaha ============#
def Escorts_Yamaha_Menu():
    class Rajdoot_Yamaha_RD350:
        def model1(self):
            c=["Blue", "Red", "Black"]
            color=r.choice(c)
            price=r.randrange(200000,500000,49999)
            Image_and_music("Yamaha", r"images&music\Rajdoot Yamaha RD350.jpg", r"images&music\Yamaha 350.mpeg")
            bike= Bike_details("Rajdoot Yamaha RD350",
                               f"{color}",
                               f"{price}",
                               "1983",
                               "9347cc, 2-stroke, parallel twin-cylinder8cc",
                               "150–160 km/h",
                               """
            ◉ India’s first performance motorcycle
            ◉ Manufactured by Escorts with Yamaha collaboration
            ◉ Famous for powerful acceleration and loud exhaust sound 
            ◉ High Torque (HT) version produced around 30.5 bhp
            ◉ Nicknamed “Rapid Death” because of its extreme speed and drum brakes
                               """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                Escorts_Yamaha_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
    class Yamaha_RX100:
        def model2(self):
            c = ["Blue", "Red", "Black"]
            color = r.choice(c)
            price = r.randrange(100000, 250000, 49999)
            Image_and_music("Yamaha", r"images&music\Yamaha RX100.jpg", r"images&music\Yamaha Rx100.mpeg")
            bike = Bike_details("Yamaha RX100",
                                f"{color}",
                                f"{price}",
                                "1985",
                                "98cc, 2-stroke single-cylinder",
                                "100 km/h",
                                """
            ◉ Legendary lightweight performance bike
            ◉ Excellent pickup and racing popularity
            ◉ Very popular among Indian youth
            ◉ Simple tuning and maintenance
                                """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                Escorts_Yamaha_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
    class Escorts_Yamaha(Rajdoot_Yamaha_RD350,Yamaha_RX100):
        def model (self):
            print("Escorts Yamaha Model".center(60,"="))
            l="""
    1.Rajdoot Yamaha RD350
    2.Yamaha RX100
    3,Back  
            """
            print(l)
    escorts_yamaha = Escorts_Yamaha()
    escorts_yamaha.model()
    choose_model=input("Enter your Escorts Yamaha Model choice: ")
    if choose_model == "1":
        escorts_yamaha.model1()
    elif choose_model == "2":
        escorts_yamaha.model2()
    elif choose_model == "3":
        bike_company_name()

#============== Hero Honda Menu ===============#
def Hero_Honda_Menu():
    class Hero_Honda_CD100:
        def model1(self):
            c=["Silver", "Red", "Black"]
            color=r.choice(c)
            price=r.randrange(100000,250000)
            Image_and_music("Hero Honda",r"images&music\Hero Honda CD100.jpg",r"images&music\Hero Honda.mpeg")
            bike=Bike_details("Hero Honda CD100 ",
                              f"{color}",
                              f"{price}",
                              "1989",
                              "97cc",
                              "85 km/h",
                              """
            ◉ Stylish commuter motorcycle
            ◉ Lightweight and easy handling
            ◉ Good mileage and reliability
            ◉ Designed for daily city riding
                              """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                Hero_Honda_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
    class Hero_Honda:
        def model2(self):
            c = ["Silver", "Red", "Black"]
            color = r.choice(c)
            price = r.randrange(30000, 60000,20000)
            Image_and_music("Yezdi", r"images&music\Hero Honda sleek.jpg", r"images&music\Hero Honda.mpeg")
            bike = Bike_details("Hero Honda Sleek",
                                f"{color}",
                                f"{price}",
                                "1990",
                                "97cc",
                                "80 km/h",
                                """
            ◉ Gearless motorcycle design
            ◉ Comfortable seating position
            ◉ Easy riding for city traffic
            ◉ Innovative commuter bike during its era
                                """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                Hero_Honda_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
#=========================== Hero Honda Model ====================#
    class Hero_Honda(Hero_Honda_CD100,Hero_Honda):
        def model(self):
            print("Hero Honda Sleek Model".center(60,"="))
            l="""
    1. Hero Honda CD100 
    2. Hero Honda Sleek
    3.Back
            """
            print(l)
    hero_honda=Hero_Honda()
    hero_honda.model()
    choose_model = input("Enter your choice: ")
    if choose_model == "1":
        hero_honda.model1()
    elif choose_model == "2":
        hero_honda.model2()
    elif choose_model == "3":
        bike_company_name()

#===================== Yezdi =========================#
def Yezdi_Menu():
    class Yezdi_Roadking_250:
        def model1(self):
            c = ["Silver", "Red", "Black"]
            color = r.choice(c)
            price = r.randrange(100000, 200000)
            Image_and_music("Yezdi",r"images&music\Yezdi Roadking 250.jpg",r"images&music\Yezdi.mpeg")
            bike=Bike_details("Yezdi Roadking 250",
                              f"{color}",
                              f"{price}",
                              " 1978",
                              "250cc, 2-stroke single-cylinder",
                              "120–130 km/h",
                              """
            ◉ One of the most famous Yezdi motorcycles
            ◉ Powerful pickup and loud exhaust sound
            ◉ Suitable for city and rough-road riding
            ◉ Popular among college students in the 1980s
                              """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                Yezdi_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
#==================== Yezdi Classic 250 ===========================#
    class Yezdi_Classic_250:
        def model2(self):
            c = ["Silver", "Red", "Black"]
            color = r.choice(c)
            price = r.randrange(100000, 200000)
            Image_and_music("Yezdi", r"images&music\Yezdi Classic 250.jpg", r"images&music\Yezdi.mpeg")
            bike=Bike_details("Yezdi Classic 250",
                              f"{color}",
                              f"{price}",
                              "1978",
                              "250cc, 2-stroke single-cylinder",
                              "120–130 km/h",
                              """
            ◉ One of the most famous Yezdi motorcycles
            ◉ Powerful pickup and loud exhaust sound
            ◉ Suitable for city and rough-road riding
            ◉ Popular among college students in the 1980s
                              """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                Yezdi_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
#================= Yezdi ==========================#
    class Yezdi(Yezdi_Roadking_250,Yezdi_Classic_250):
        def model(self):
            l="""
    1. Yezdi Roadking 250
    2. Yezdi Classic 250
            """
            print(l)
    yezdi = Yezdi()
    yezdi.model()
    choose_model = input("Choose the Yezdi Model: ")
    if choose_model == "1":
        yezdi.model1()
    elif choose_model == "2":
        yezdi.model2()
    elif choose_model == "3":
        bike_company_name()
#======================== Ideal Jawa ==========================#
def Ideal_Jawa_Menu():
    class Jawa_250_type_353:
        def model1(self):
            c=["Maroon", "Red", "Black"]
            color=r.choice(c)
            price=r.randrange(100000,250000)
            Image_and_music("Ideal Jawa",r"images&music\Jawa_250_type_353.jpg",r"images&music\Yezdi Roadking1.mpeg")
            bike = Bike_details("Jawa 250 Type 559",
                                f"{color}",
                                f"{price}",
                                "1971",
                                "248cc, 2-stroke",
                                "125 km/h",
                                """
            ◉ Improved suspension and fuel tank design
            ◉ Better comfort for long rides
            ◉ Reliable touring motorcycle
            ◉ Strong road grip and stability
                                """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                Ideal_Jawa_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
#================ Jawa 250 Type 559 ===========================#
    class Jawa_250_type_559:
        def model2(self):
            c = ["Maroon", "Red", "Black"]
            color = r.choice(c)
            price = r.randrange(100000, 250000)
            Image_and_music("Ideal Jawa",r"images&music\Jawa 250 Type 539.webp",r"images&music\Yezdi Roadking1.mpeg")
            bike=Bike_details("Jawa 250 Type 559",
                              f"{color}",
                                f"{price}",
                              "1971",
                              "248cc, 2-stroke",
                              "125 km/h",
                              """
            ◉ Improved suspension and fuel tank design
            ◉ Better comfort for long rides
            ◉ Reliable touring motorcycle
            ◉ Strong road grip and stability                
                              """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                Ideal_Jawa_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
#=============== Yezdi Roadking =======================#
    class Yezdi_Roadking:
        def model3(self):
            c = ["Silver", "Red", "Black"]
            color = r.choice(c)
            price = r.randrange(120000, 300000)
            Image_and_music("Ideal Jawa", r"images&music\Jawa 250 Type 539.webp", r"images&music\Yezdi Roadking1.mpeg")
            bike = Bike_details("Yezdi Roadking",
                                f"{color}",
                                f"{price}",
                                "1978",
                                "250cc, 2-stroke",
                                "120–130 km/h",
                                """
            ◉ Powerful off-road capable motorcycle
            ◉ Famous for loud exhaust sound
            ◉ Strong pickup and rugged design
            ◉ Very popular among college riders in the 1980s
                                """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                Ideal_Jawa_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
#================== Yezdi Classic 250 ==================#
    class Yezdi_Classic_250:
        def model4(self):
            c = ["Silver", "Red", "Black"]
            color = r.choice(c)
            price = r.randrange(100000, 250000)
            Image_and_music("Ideal Jawa", r"images&music\Yezdi Classic 250.webp", r"images&music\Yezdi Roadking1.mpeg")
            bike = Bike_details("Yezdi Classic 250",
                                f"{color}",
                                f"{price}",
                                "1980",
                                "250cc, 2-stroke",
                                "115 km/h",
                                """
            ◉ Comfortable everyday riding motorcycle
            ◉ Strong engine durability
            ◉ Easy spare-part maintenance during its era
            ◉ Popular in both cities and villages
                                """)
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            print("3.Home")
            choice = input("Enter your choice: ")
            if choice == "1":
                Ideal_Jawa_Menu()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
#================================= Ideal Jawa Model ==============================#
    class IJ(Jawa_250_type_353,Jawa_250_type_559,Yezdi_Roadking,Yezdi_Classic_250):
        def model(self):
            print(" Ideal Jawa ".center(60, "="))
            l="""
    1.Jawa 250 Type 353                  3.Yezdi Roadking
    2.Jawa 250 Type 559                  4,Yezdi Classic 250
                            5.Back
            """
            print(l)
    Ideal_Jawa=IJ()
    Ideal_Jawa.model()
    choose_model = input("Choose the Ideal Jawa Model: ")
    if choose_model == "1":
        Ideal_Jawa.model1()
    elif choose_model == "2":
        Ideal_Jawa.model2()
    elif choose_model == "3":
        Ideal_Jawa.model3()
    elif choose_model == "4":
        Ideal_Jawa.model4()
    elif choose_model == "5":
        bike_company_name()
    else:
        Ideal_Jawa()
#======================== Royal Enfield ======================#
def Royal_Enfield():
    class Bullet_350:
        def model1(self):
            p.init()
            p.mixer.init()
            # set up display Name
            p.display.set_caption("Royal Enfield")
            # set up display
            ps1 = p.display.set_mode((636, 636))
            # load background Image
            ps = p.image.load(r"images&music\Bullet 350 (Early Model).jpg")
            ps = p.transform.scale(ps, (636, 636))
            ps1.blit(ps, (0, 0))
            # update display
            p.display.update()
            # load background music
            p.mixer.music.load(r"images&music\r350cc.mp3")
            p.mixer.music.play(-1)
            # wait for image and music
            t.sleep(10)
            p.mixer.music.stop()
            p.quit()
            t.sleep(3)
            price=r.randrange(160000,230000)
            bike = Bike_details("Bullet 350 (Early Model)",
                                  "Black / Military Green",
                                    f"{price}",
                                  "1932 (India production 1955 onwards)",
                                  "346cc single-cylinder",
                                  "110 km/h",
                                """
            ◉ Most iconic Royal Enfield model
            ◉ Used by Indian Army & Police
            ◉ Known for strong metal body and “thump” sound"
            """)

            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            choice = input("Enter your choice: ")
            if choice == "1":
                Royal_Enfield()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model,bike.color,bike.price,bike.launch_year,bike.engine,bike.top_speed,bike.details,Name,Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
    class Bullet_500:
        def model2(self):
            p.init()
            p.mixer.init()
            # set up display Name
            p.display.set_caption("Royal Enfield")
            # set up display
            ps1 = p.display.set_mode((636, 636))
            # load background Image
            ps = p.image.load(r"images&music\ROYAL ENFIELD Bullet 500.jpg")
            ps = p.transform.scale(ps, (636, 636))
            ps1.blit(ps, (0, 0))
            # update display
            p.display.update()
            # load background music
            p.mixer.music.load(r"images&music\500cc.mpeg")
            p.mixer.music.play(-1)
            # wait for image and music
            t.sleep(10)
            p.mixer.music.stop()
            p.quit()
            t.sleep(3)
            price = r.randrange(150000, 250000)
            bike = Bike_details("Bullet 500",
                                  "Silver",
                                 f"{price}",
                                  "1986 (India upgrade era)",
                                  "499cc single-cylinder",
                                  "130 km/h",
                                  "\n◉ More powerful version of Bullet 350\n◉ Better highway performance\n◉ Popular among touring riders")
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            choice = input("Enter your choice: ")
            if choice == "1":
                Royal_Enfield()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
    class Royal_Enfield_Explorer:
        def model3(self):
            p.init()
            p.mixer.init()
            # set up display Name
            p.display.set_caption("Royal Enfield")
            # set up display
            ps1 = p.display.set_mode((636, 636))
            # load background Image
            ps = p.image.load(r"images&music\Royal Enfield Explorer.jpg")
            ps = p.transform.scale(ps, (636, 636))
            ps1.blit(ps, (0, 0))
            # update display
            p.display.update()
            # load background music
            p.mixer.music.load(r"images&music\350cc.mpeg")
            p.mixer.music.play(-1)
            # wait for image and music
            t.sleep(10)
            p.mixer.music.stop()
            p.quit()
            t.sleep(3)
            price = r.randrange(100000, 300000)
            bike=Bike_details("Royal Enfield Explore",
                                "Red / Black",
                                f"{price}",
                                "Early 1980s",
                                "200cc–250cc (varied prototypes)",
                                "90–100 km/h",
                                "\n◉ Lightweight experimental model\n◉ Designed for fuel efficiency\n◉ Limited production"
                                )
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            choice = input("Enter your choice: ")
            if choice == "1":
                Royal_Enfield()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_3 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
    class Royal_Enfield_Machismo_350:
        def model4(self):
            p.init()
            p.mixer.init()
            # set up display Name
            p.display.set_caption("Royal Enfield")
            # set up display
            ps1 = p.display.set_mode((636, 636))
            # load background Image
            ps = p.image.load(r"images&music\Royal Enfield Machismo 350.jpg")
            ps = p.transform.scale(ps, (636, 636))
            ps1.blit(ps, (0, 0))
            # update display
            p.display.update()
            # load background music
            p.mixer.music.load(r"images&music\4.mpeg")
            p.mixer.music.play(-1)
            # wait for image and music
            t.sleep(10)
            p.mixer.music.stop()
            p.quit()
            t.sleep(3)
            bike3 = Bike_details("Royal Enfield Machismo 350",
                                  "Black",
                                 "123456",
                                  "Eary 1989",
                                  "346cc single-cylinder",
                                  "110 km/h",
                                  "\n◉ Cruiser-style design\n◉ Comfortable long rides\n◉ Improved styling over Bullet")
            bike.Bike()
            t.sleep(1)
            print("1.Back")
            print("2.Buy Bike")
            choice = input("Enter your choice: ")
            if choice == "1":
                Royal_Enfield()
            elif choice == "2":
                change = input("Change the Name and Mobile Number? (1.yes/2.no): ")
                if change == "1":
                    Name = input("Enter the Name: ")
                    Mobile_2 = input("Enter the Mobile Number: ")
                    c = Customer(Name, Mobile_2)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_2)
                    b.Generate_bill()
                elif change == "2":
                    Name = Name2
                    Mobile_3 = Mobile_2
                    c = Customer(Name, Mobile_3)
                    c.customer_details()
                    b = Bill(bike.model, bike.color, bike.price, bike.launch_year, bike.engine, bike.top_speed,
                             bike.details, Name, Mobile_3)
                    b.Generate_bill()
            elif choice == "3":
                bike_company_name()
    class RE(Bullet_350,Bullet_500,Royal_Enfield_Explorer,Royal_Enfield_Machismo_350):
        def model(self):
            print(" Royal Enfield Models ".center(60,"="))
            l =""" 
    1.Bullet 350           3.Royal Enfield Explorer
    2.Bullet 500           4.Royal Enfield Machismo 350
                   5.Back
            """
            print(l)
    Royal_Enfield_Bike=RE()
    Royal_Enfield_Bike.model()
    print()
    choose_model = input("Choose Royal Enfield Model: ")
    if choose_model == "1":
        Royal_Enfield_Bike.model1()
    elif choose_model == "2":
        Royal_Enfield_Bike.model2()
    elif choose_model == "3":
        Royal_Enfield_Bike.model3()
    elif choose_model == "4":
        Royal_Enfield_Bike.model4()
    elif choose_model == "5":
        bike_company_name()
    else:
        Royal_Enfield()

#================ start the program ===============#
#======================= Bike Company ======================#
def bike_company_name():
    print()
    print(" Indian Bike Company ".center(60, "="))
    l = """
        1.Royal Enfield             6.TVS Suzuki
        2.Ideal Jawa                7.Bajaj Auto
        3.Yezdi                     8.Rajdoot
        4.Escorts Yamaha            9.Kinetic Honda
        5.Hero Honda                10.LML 
                        11.Back   
        """
    print(l)
    choose = input("Choose the Company: ")
    if choose == "1":
        Royal_Enfield()
    elif choose == "2":
        Ideal_Jawa_Menu()
    elif choose == "3":
        Yezdi_Menu()
    elif choose == "4":
        Escorts_Yamaha_Menu()
    elif choose == "5":
        Hero_Honda_Menu()
    elif choose == "6":
        TVS_Suzuki_Menu()
    elif choose == "7":
        Bajaj_Auto_Menu()
    elif choose == "8":
        Rajdoot_Honda_Menu()
    elif choose == "9":
        Kinetic_Honda_Menu()
    elif choose == "10":
        LML_Menu()
    else:
        Indian_Bike_Company()
# bike_company_name()

#=================== Login Page ===================#
#=============== Longin OTP Verification ===============#

def otp():
    print("Sending OTP to WhatsApp....")
    t.sleep(3)
    OTP_1 = r.randrange(1234, 5678)
    pk.sendwhatmsg_instantly(f"+91{Mobile_2}", f"Login OTP:{OTP_1}")
    pg.doubleClick()
    def Validation():
        Enter_OTP = int(input("Enter the OTP: "))
        if Enter_OTP == OTP_1:
            print("Login Successful...✔")
            t.sleep(2)
            print(f"Welcome {Name2}".center(60," "))
            bike_company_name()
        else:
            print("Wrong OTP Verify please try again...✖")
            Validation()
    Validation()
def login():
    global Mobile_2,Name2
    print()
    print("================== Login Page ================")
    t.sleep(1)
    username2 = input("Enter the Username: ")
    password2 = input("Enter the Password: ")
    found = False
    with open(LOGIN, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 4:
                continue
            username, password, mobile, name = parts
            if username2 == username and password2 == password:
                found = True
                Mobile_2 = mobile
                Name2 = name
                otp()
                break
    if not found:
        print("Wrong Username and Password Verify please try Again...❌")
        login()

#================== Sing Page ====================#
#save the Username and Password
def save():
    with open(LOGIN, "a") as file:
        file.write(f"{Username1},{Password1},{Mobile_1},{Name}\n")
        file.close()
        t.sleep(3)
    print("Signup Successful....✔")
    t.sleep(2)
    login()
def sign():
    global Name
    print()
    print("================== Sign Page ================")
    Name=input("Enter Your Name: ")
    Age=input("Enter Your Age: ")
    Gender=input("Enter Your Gender(Male/Female): ")
    #===============  Mobile Number Validation ================#
    def mobile():
        global Mobile_1
        Mobile_1=input("Enter your Mobile Number: ")
        if len(Mobile_1)==10 and Mobile_1.isdigit() and Mobile_1.startswith(("6","7","8","9")):
            return mobile
        else:
            print("Your Mobile Number Not Valid...✖")
            mobile()
    mobile()
    #================== Email Id Validation ==================#
    def email():
        global Email
        Email=input("Enter Your Email Id: ")
        if  "@" in Email and  ".com" in Email:
            return Email
        else:
            print("Your Email Address Not Valid...✖")
            email()
    email()
    #=================== Set the Username ===================#
    def username_1():
        global Username1
        Username1 = input("Create Your Username: ")
        found = False
        with open(LOGIN, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 4:
                    continue
                username, password, mobile, name = parts
                if Username1 == username:
                    found = True
                    break
        if found:
            print("Username Already Exists...✖")
            username_1()
    username_1()
    # ===================== Set the password ================#
    def password_1():
        global Password1
        Password1=input("Create Password (8 Characters): ")
        if len(Password1)==8:
            return password_1
        else:
            print("Password Must be 8 Characters... ✖")
            password_1()
    password_1()
    save()
#=================== Welcome page =====================#
Image_and_music("Ideal Jawa", r"images&music\welcome logo.jpeg", r"images&music\Welcome music.mpeg")
print("================== WELCOME to OLD GOLD BIKE STORE ===================")
l=["1.Sign","2.Login"]
for i in l:
    print(i)
choose=input("Please Choose Your Choice:")
if choose=="1":
    t.sleep(2)
    sign()
elif choose=="2":
    t.sleep(2)
    login()
else:
    print("Invalid Choice...")
