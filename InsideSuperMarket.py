from tkinter import *
from tkinter import messagebox
import webbrowser
import os,sys,random
from PIL import ImageTk, Image

# def welcome():
#     textarea1.delete('1.0', END)
#     textarea1.insert(END, "\t Super Market Developer Welcome You")
#     textarea1.insert(END, "\n======================================")
#     textarea1.insert(END, f"\n\t B.NUM  :{fatora.get()}")
#     textarea1.insert(END, f"\n\t NAME   :{namo.get()}")
#     textarea1.insert(END, f"\n\t PHONE  :{phono.get()}")
#     textarea1.insert(END, "\n======================================")
#     textarea1.insert(END, f"\nthe Price\t     the number\t        the Buy")
#     textarea1.insert(END, "\n=====================================")

# def removeAllEntry():
    #bqentr1.delete(0, 'end')
            #====================
    # cEntry = root.winfo_children()
    # for c in cEntry:
    #     childEnrty = c.winfo_class()
    #     if(childEnrty == "Entry"):
    #        pass

def ContentSuperMarket():
    ColorFrameOne = '#0B4C5F'
    root = Toplevel()
    root.geometry('1300x660+30+20')
    root.title("Super Market : سوبر ماركت")
    root.resizable(False, False)
    # To Create Icon In Form
    icon = ImageTk.PhotoImage(Image.open('super3.png'))
    root.wm_iconphoto(False, icon)
    title1 = Label(root, text="Manage SuperMarket", fg='white', bg='#0B2F3A', font=('tajawal', 16)).pack(fill=X)
    # ============= Variable ==========
    # The First Bicoliat [q1 => q18]
    q1 = IntVar()
    q2 = IntVar()
    q3 = IntVar()
    q4 = IntVar()
    q5 = IntVar()
    q6 = IntVar()
    q7 = IntVar()
    q8 = IntVar()
    q9 = IntVar()
    q10 = IntVar()
    q11 = IntVar()
    q12 = IntVar()
    q13 = IntVar()
    q14 = IntVar()
    q15 = IntVar()
    q16 = IntVar()
    # The Second Home [qq1 => qq18]
    qq1 = IntVar()
    qq2 = IntVar()
    qq3 = IntVar()
    qq4 = IntVar()
    qq5 = IntVar()
    qq6 = IntVar()
    qq7 = IntVar()
    qq8 = IntVar()
    qq9 = IntVar()
    qq10 = IntVar()
    qq11 = IntVar()
    qq12 = IntVar()
    qq13 = IntVar()
    qq14 = IntVar()
    qq15 = IntVar()
    qq16 = IntVar()
    # The Third Electrical [qqq1 => qqq18]
    qqq1 = IntVar()
    qqq2 = IntVar()
    qqq3 = IntVar()
    qqq4 = IntVar()
    qqq5 = IntVar()
    qqq6 = IntVar()
    qqq7 = IntVar()
    qqq8 = IntVar()
    qqq9 = IntVar()
    qqq10 = IntVar()
    qqq11 = IntVar()
    qqq12 = IntVar()
    qqq13 = IntVar()
    def total():
        # the price bicoliat
        resq1 = q1.get() * 6.2
        resq2 = q2.get() * 1.5
        resq3 = q3.get() * 1.1
        resq4 = q4.get() * 5.5
        resq5 = q5.get() * 1.5
        resq6 = q6.get() * 2.3
        resq7 = q7.get() * 6.1
        resq8 = q8.get() * 3.5
        resq9 = q9.get() * 2.5
        resq10 = q10.get() * 4
        resq11 = q11.get() * 2.3
        resq12 = q12.get() * 1.5
        resq13 = q13.get() * 1.5
        resq14 = q14.get() * 1.2
        resq15 = q15.get() * 5
        resq16 = q16.get() * 1.5
        totalBicoliat = (
                resq1 + resq2 + resq3 + resq4 + resq5 + resq6 + resq7 + resq8 + resq9
                + resq10 + resq11 + resq12 + resq13 + resq14 + resq15 + resq16)
        bicoliat.set(totalBicoliat)
        # the price to home
        resqq1 = qq1.get() * 6.2
        resqq2 = qq2.get() * 1.5
        resqq3 = qq3.get() * 1.1
        resqq4 = qq4.get() * 5.5
        resqq5 = qq5.get() * 1.5
        resqq6 = qq6.get() * 2.3
        resqq7 = qq7.get() * 6.1
        resqq8 = qq8.get() * 3.5
        resqq9 = qq9.get() * 2.5
        resqq10 = qq10.get() * 4
        resqq11 = qq11.get() * 2.3
        resqq12 = qq12.get() * 1.5
        resqq13 = qq13.get() * 1.5
        resqq14 = qq14.get() * 1.2
        resqq15 = qq15.get() * 5
        resqq16 = qq16.get() * 1.5
        totalAdoatHome = (
                resqq1 + resqq2 + resqq3 + resqq4 + resqq5 + resqq6 + resqq7 + resqq8 + resqq9
                + resqq10 + resqq11 + resqq12 + resqq13 + resqq14 + resqq15 + resqq16)
        adoat.set(totalAdoatHome)
        # the price to Kahraba
        resqqq1 = qqq1.get() * 6.2
        resqqq2 = qqq2.get() * 1.5
        resqqq3 = qqq3.get() * 1.1
        resqqq4 = qqq4.get() * 5.5
        resqqq5 = qqq5.get() * 1.5
        resqqq6 = qqq6.get() * 2.3
        resqqq7 = qqq7.get() * 6.1
        resqqq8 = qqq8.get() * 3.5
        resqqq9 = qqq9.get() * 2.5
        resqqq10 = qqq10.get() * 4
        resqqq11 = qqq11.get() * 2.3
        resqqq12 = qqq12.get() * 1.5
        resqqq13 = qqq13.get() * 1.5
        totalKahraba = (
                resqqq1 + resqqq2 + resqqq3 + resqqq4 + resqqq5 + resqqq6 + resqqq7
                + resqqq8 + resqqq9 + resqqq10 + resqqq11 + resqqq12 + resqqq13)
        kahraba.set(totalKahraba)

    def billFatora():
        numFatora = fatora.get()
        filename = "fatora"+str(numFatora)
        fFile = open("F:\\DataForMy\\CV Omar\\some Project using python(GUI)\\SuperMarketProject\\%s.txt" %(filename),"w")
        textInFile = "Super Market, Are You Welcome."+"\n======================================"\
                     +"\n\t B.NUM  :  "+fatora.get()+"\n\t NAME   :  "+namo.get()+"\n\t PHONE  :  "+phono.get()\
                     +"\n======================================"+"\nThe Total Of Bicoliat Is    :  %s" %(bicoliat.get())\
                     +"\nThe Total Of Adoat Is      :  %s" %(adoat.get())+"\nThe Total Of Kahraba Is     :  %s" %(kahraba.get())
        fFile.write(textInFile)
        fFile.close()
    # ============== Varaible Customer Data ==============
    namo = StringVar()
    phono = StringVar()
    fatora = StringVar()
    def changeNumPaypal():
        x = random.randint(1000, 9999)
        fatora.set(str(x))
    # ========== variable Price Calculate ===============
    bicoliat = StringVar()
    adoat = StringVar()
    kahraba = StringVar()
    # ========== Customer Data ==========
    fontFrameOne = ('tajawal', 10, 'bold')
    fgFrameOne = 'white'
    frameOne = Frame(root, bd=2, width=390, height=200, bg=ColorFrameOne).place(x=0, y=30)
    lbl1 = Label(root, text="Customer Data:", font=('tajawal', 14, 'bold'), bg=ColorFrameOne, fg="tomato").place(x=3,y=40)
    lbl2 = Label(root, text="Customer Name:", font=fontFrameOne, bg=ColorFrameOne, fg=fgFrameOne).place(x=3, y=80)
    lbl3 = Label(root, text="Customer Phone:", font=fontFrameOne, bg=ColorFrameOne, fg=fgFrameOne).place(x=3, y=120)
    lbl4 = Label(root, text="Customer Paypal:", font=fontFrameOne, bg=ColorFrameOne, fg=fgFrameOne).place(x=3, y=160)
    entr1 = Entry(root, textvariable=namo, justify='center').place(x=130, y=85)
    entr2 = Entry(root, textvariable=phono, justify='center').place(x=130, y=125)
    entr3 = Entry(root, textvariable=fatora, justify='center').place(x=130, y=165)
    btnSearch = Button(root, text="Change\nNumber\nPaypal", bg=ColorFrameOne, fg='white', font=('tajawl', 12, 'bold'),command=changeNumPaypal)\
        .place(x=280,y=85,width=100,height=100)
    # ============ Bill ===================
    titBill = Label(root, text="[Bill For Customer]", font=('tajawal', 14, 'bold'), bg=ColorFrameOne,fg="tomato").place(x=3, y=200)
    frameTow = Frame(root, bd=2, width=390, height=330, bg="white").place(x=0, y=230)
    textarea1 = Text(root, bg='white').place(x=0, y=230, width=390, height=310)
    # ========== Price Calculate ===============
    fontFrame3 = 'tajawal'
    bgAndfgFrame3 = 'gold'
    frameThree = Frame(root, bd=2, width=682, height=120, bg=ColorFrameOne).place(x=0, y=540)
    hesab = Button(root, text="The Price", font=fontFrame3, bg=bgAndfgFrame3,command=total).place(x=25, y=560,width=100,height=30)
    fator = Button(root, text="Export Bill", font=fontFrame3, bg=bgAndfgFrame3,command=billFatora).place(x=150,y=560,width=100,height=30)
    clear = Button(root, text="Clear Fields", font=fontFrame3, bg=bgAndfgFrame3).place(x=25,y=610,width=100,height=30)
    exit = Button(root, text="EXit", font=fontFrame3, bg=bgAndfgFrame3,command=root.destroy).place(x=150, y=610,width=100,height=30)

    lblo1 = Label(root, text="Total Count Of Legumes", font=fontFrameOne, fg=bgAndfgFrame3, bg=ColorFrameOne).place(x=300, y=560)
    lblo2 = Label(root, text="Electrical Tools Calculator", font=fontFrameOne, fg=bgAndfgFrame3, bg=ColorFrameOne).place(x=300, y=590)
    lblo3 = Label(root, text="Home Supplies Account", font=fontFrameOne, fg=bgAndfgFrame3,bg=ColorFrameOne).place(x=300, y=620)

    ent1 = Entry(root, textvariable=bicoliat, width=27).place(x=500, y=560)
    ent2 = Entry(root, textvariable=adoat, width=27).place(x=500, y=590)
    ent3 = Entry(root, textvariable=kahraba, width=27).place(x=500, y=620)
    # =========== ٍ Some Attrributes Is Fixed In Items ============
    itemsFont = ('tajawal', 11, 'bold')
    itemfg = 'white'
    # =========== Items One In supermarket ============
    frameItem1 = Frame(root, bd=2, width=300, height=627, bg=ColorFrameOne).place(x=998, y=31)
    item1Lbl = Label(root, text="البقوليات", font=('tajawal', 13, 'bold'), bg=ColorFrameOne, fg='gold').place(x=1108,y=37)
    bq1 = Label(root, text="أرز", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=90)
    bq2 = Label(root, text="برغل", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=125)
    bq3 = Label(root, text="مكرونه", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=155)
    bq4 = Label(root, text="فاصوليا", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=190)
    bq5 = Label(root, text="عدس", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=225)
    bq6 = Label(root, text="فريكه", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=265)
    bq7 = Label(root, text="حمص", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=300)
    bq8 = Label(root, text="سكر", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=335)
    bq9 = Label(root, text="فلفل اسود", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=370)
    bq10 = Label(root, text="كركم", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=405)
    bq11 = Label(root, text="لوبيه", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=440)
    bq12 = Label(root, text="عصير", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=475)
    bq13 = Label(root, text="الادمامي", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=505)
    bq14 = Label(root, text="قمح", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=545)
    bq15 = Label(root, text="شوفان", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=575)
    bq16 = Label(root, text="بلح", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=1005, y=610)

    bqentr1 = Entry(root, textvariable=q1, width=30).place(x=1080, y=90)
    bqentr2 = Entry(root, textvariable=q2, width=30).place(x=1080, y=125)
    bqentr3 = Entry(root, textvariable=q3, width=30).place(x=1080, y=160)
    bqentr4 = Entry(root, textvariable=q4, width=30).place(x=1080, y=195)
    bqentr5 = Entry(root, textvariable=q5, width=30).place(x=1080, y=230)
    bqentr6 = Entry(root, textvariable=q6, width=30).place(x=1080, y=265)
    bqentr7 = Entry(root, textvariable=q7, width=30).place(x=1080, y=300)
    bqentr8 = Entry(root, textvariable=q8, width=30).place(x=1080, y=335)
    bqentr9 = Entry(root, textvariable=q9, width=30).place(x=1080, y=370)
    bqentr10 = Entry(root, textvariable=q10, width=30).place(x=1080, y=405)
    bqentr11 = Entry(root, textvariable=q11, width=30).place(x=1080, y=440)
    bqentr12 = Entry(root, textvariable=q12, width=30).place(x=1080, y=475)
    bqentr13 = Entry(root, textvariable=q13, width=30).place(x=1080, y=510)
    bqentr14 = Entry(root, textvariable=q14, width=30).place(x=1080, y=545)
    bqentr15 = Entry(root, textvariable=q15, width=30).place(x=1080, y=580)
    bqentr16 = Entry(root, textvariable=q16, width=30).place(x=1080, y=615)
    # =========== Item tow in supermarket =============
    frameItem2 = Frame(root, bd=2, width=310, height=627, bg=ColorFrameOne).place(x=685, y=31)
    item2Lbl = Label(root, text="الادوات الكهربيه", font=('tajawal', 13, 'bold'), bg=ColorFrameOne, fg='gold').place(x=790, y=37)
    ho1 = Label(root, text="مكنسه", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=90)
    ho2 = Label(root, text="سجاد", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=125)
    ho3 = Label(root, text="Tv", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=155)
    ho4 = Label(root, text="غسالها", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=190)
    ho5 = Label(root, text="تلاجه", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=225)
    ho6 = Label(root, text="سرير", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=265)
    ho7 = Label(root, text="كنب", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=300)
    ho8 = Label(root, text="سخان", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=335)
    ho9 = Label(root, text="مكواه", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=370)
    ho10 = Label(root, text="مرتبات", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=405)
    ho11 = Label(root, text="مطبخ خشب", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=440)
    ho12 = Label(root, text="حلل", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=475)
    ho13 = Label(root, text="مكتبه", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=505)
    ho14 = Label(root, text="كرسي", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=545)
    ho15 = Label(root, text="ركنه", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=575)
    ho16 = Label(root, text="ساعات", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=695, y=610)

    hoentr1 = Entry(root, textvariable=qq1, width=30).place(x=770, y=90)
    hoentr2 = Entry(root, textvariable=qq2, width=30).place(x=770, y=125)
    hoentr3 = Entry(root, textvariable=qq3, width=30).place(x=770, y=160)
    hoentr4 = Entry(root, textvariable=qq4, width=30).place(x=770, y=195)
    hoentr5 = Entry(root, textvariable=qq5, width=30).place(x=770, y=230)
    hoentr6 = Entry(root, textvariable=qq6, width=30).place(x=770, y=265)
    hoentr7 = Entry(root, textvariable=qq7, width=30).place(x=770, y=300)
    hoentr8 = Entry(root, textvariable=qq8, width=30).place(x=770, y=335)
    hoentr9 = Entry(root, textvariable=qq9, width=30).place(x=770, y=370)
    hoentr10 = Entry(root, textvariable=qq10, width=30).place(x=770, y=405)
    hoentr11 = Entry(root, textvariable=qq11, width=30).place(x=770, y=440)
    hoentr12 = Entry(root, textvariable=qq12, width=30).place(x=770, y=475)
    hoentr13 = Entry(root, textvariable=qq13, width=30).place(x=770, y=510)
    hoentr14 = Entry(root, textvariable=qq14, width=30).place(x=770, y=545)
    hoentr15 = Entry(root, textvariable=qq15, width=30).place(x=770, y=580)
    hoentr16 = Entry(root, textvariable=qq16, width=30).place(x=770, y=615)
    # =========== Item Three in supermarket ===========
    frameItem3 = Frame(root, bd=2, width=290, height=507, bg=ColorFrameOne).place(x=393, y=31)
    item3Lbl = Label(root, text="اللاوازم المنزليه", font=('tajawal', 13, 'bold'), bg=ColorFrameOne, fg='gold').place(x=485, y=37)
    ele1 = Label(root, text="أرز", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=405, y=90)
    ele2 = Label(root, text="برغل", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=405, y=125)
    ele3 = Label(root, text="مكرونه", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=405, y=155)
    ele4 = Label(root, text="فاصوليا", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=405, y=190)
    ele5 = Label(root, text="عدس", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=405, y=225)
    ele6 = Label(root, text="فريكه", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=405, y=265)
    ele7 = Label(root, text="حمص", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=405, y=300)
    ele8 = Label(root, text="سكر", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=405, y=335)
    ele9 = Label(root, text="فلفل اسود", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=405, y=370)
    ele10 = Label(root, text="كركم", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=405, y=405)
    ele11 = Label(root, text="لوبيه", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=405, y=440)
    ele12 = Label(root, text="عصير", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=405, y=475)
    ele13 = Label(root, text="الادمامي", font=itemsFont, bg=ColorFrameOne, fg=itemfg).place(x=405, y=505)

    eleentr1 = Entry(root, textvariable=qqq1, width=30).place(x=475, y=90)
    eleentr2 = Entry(root, textvariable=qqq2, width=30).place(x=475, y=125)
    eleentr3 = Entry(root, textvariable=qqq3, width=30).place(x=475, y=160)
    eleentr4 = Entry(root, textvariable=qqq4, width=30).place(x=475, y=195)
    eleentr5 = Entry(root, textvariable=qqq5, width=30).place(x=475, y=230)
    eleentr6 = Entry(root, textvariable=qqq6, width=30).place(x=475, y=265)
    eleentr7 = Entry(root, textvariable=qqq7, width=30).place(x=475, y=300)
    eleentr8 = Entry(root, textvariable=qqq8, width=30).place(x=475, y=335)
    eleentr9 = Entry(root, textvariable=qqq9, width=30).place(x=475, y=370)
    eleentr10 = Entry(root, textvariable=qqq10, width=30).place(x=475, y=405)
    eleentr11 = Entry(root, textvariable=qqq11, width=30).place(x=475, y=440)
    eleentr12 = Entry(root, textvariable=qqq12, width=30).place(x=475, y=475)
    eleentr13 = Entry(root, textvariable=qqq13, width=30).place(x=475, y=510)

    root.grab_set()