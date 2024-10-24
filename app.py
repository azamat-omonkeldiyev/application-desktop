from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout, QMessageBox, QCheckBox, QRadioButton, QComboBox

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.v_lbl_lay = QVBoxLayout()
        self.v_edit_lay = QVBoxLayout()
        self.h_edit_lbl = QHBoxLayout()
        
        self.ism_lbl = QLabel("Name:")        
        self.fam_lbl = QLabel("Surname:")
        self.yosh_lbl = QLabel("Age:")
        self.tel_lbl = QLabel("Tel raqam:")
        
        self.v_lbl_lay.addWidget(self.ism_lbl)
        self.v_lbl_lay.addWidget(self.fam_lbl)
        self.v_lbl_lay.addWidget(self.yosh_lbl)
        self.v_lbl_lay.addWidget(self.tel_lbl)
        
        self.ism_edit = QLineEdit()        
        self.fam_edit = QLineEdit()        
        self.yosh_edit = QLineEdit()
        self.tel_edit = QLineEdit()
        
        self.v_edit_lay.addWidget(self.ism_edit)
        self.v_edit_lay.addWidget(self.fam_edit)
        self.v_edit_lay.addWidget(self.yosh_edit)
        self.v_edit_lay.addWidget(self.tel_edit)
        
        self.h_edit_lbl.addLayout(self.v_lbl_lay)
        self.h_edit_lbl.addLayout(self.v_edit_lay)
        
        
        self.msg = QMessageBox()
        
        self.lbl = QLabel("Jinsni tanlang")
        self.lbl2 = QLabel("Qaysi viloyat")
        self.lbl3 = QLabel("Qiziqishlari")
        self.lbl4 = QLabel("Tuman")
        self.rd1 = QRadioButton("Erkak")
        self.rd2 = QRadioButton("Ayol")
        
        self.cmb_viloyat = QComboBox()
        self.cmb_tuman = QComboBox()
        self.cmb_viloyat.addItems(["Toshkent shahri","Jizzax","Buxoro"])
        self.cmb_viloyat.activated[str].connect(self.Tumanlar)
        
        self.q1 = QCheckBox("Sport")
        self.q2 = QCheckBox("Mutolaa")
        self.q3 = QCheckBox("Sanat")
        self.q4 = QCheckBox("Komputer o'yinlar")
        self.q5 = QCheckBox("Sayohat")
        self.lst = [self.q1,self.q2,self.q3,self.q4,self.q5]
        
        self.btn = QPushButton("Submit")
        self.btn.clicked.connect(self.yozish)
        
        self.v_main_lay.addLayout(self.h_edit_lbl)
        self.v_main_lay.addWidget(self.rd1)
        self.v_main_lay.addWidget(self.rd2)
        self.v_main_lay.addWidget(self.lbl2)
        self.v_main_lay.addWidget(self.cmb_viloyat)
        self.v_main_lay.addWidget(self.lbl4)
        self.v_main_lay.addWidget(self.cmb_tuman)
        self.v_main_lay.addWidget(self.lbl3)
        
        for i in self.lst:
            i.setStyleSheet("background:lightgreen")
            self.v_main_lay.addWidget(i)
            
        self.v_main_lay.addWidget(self.btn)
        
        self.setLayout(self.v_main_lay)
        
    def Tumanlar(self):
        if self.cmb_viloyat.currentText() == "Toshkent shahri":
            self.cmb_tuman.clear()
            self.cmb_tuman.addItems(["Yunusobod","Uchtepa","Chilonzor","Sergeli"])
            
        elif self.cmb_viloyat.currentText() == "Jizzax":
            self.cmb_tuman.clear()
            self.cmb_tuman.addItems(["Arnasoy","Paxtakor","Zafarodod","Forish"])
            
        elif self.cmb_viloyat.currentText() == "Buxoro":
            self.cmb_tuman.addItems(["Kogon","Jondor","Xatirchi"])

    def yozish(self):
        try:
            with open("Malumot.txt","+a") as file:
                
                if self.ism_edit.text().isalpha() and self.fam_edit.text().isalpha:
                    if self.tel_edit.text().startswith("+998"):
                        
                        file.write(f"{self.ism_edit.text()} {self.fam_edit.text()}")
                        file.write(f" {self.yosh_edit.text()} {self.tel_edit.text()}")
                        file.write(f" {self.rd1.text() if self.rd1.isChecked() else self.rd2.text()}")
                        file.write(f" {self.cmb_viloyat.currentText()}  {self.cmb_tuman.currentText()}")
                        for i in self.lst:
                            if i.isChecked():
                                file.write(f" {i.text()}")
                                
                    else:
                        self.msg.setText("Tel raqami +998 bilan boshlanmagan")
                        self.msg.setIcon(QMessageBox.Warning)
                        self.msg.exec_()
                        
                else:
                    self.msg.setText("Ism yoki Familiya xato kiritilgan")
                    self.msg.setIcon(QMessageBox.Warning)
                    self.msg.exec_()
                    
                
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")


app = QApplication([])
win = MyWindow()
win.show()
app.exec_()
