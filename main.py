import ana_ekran,sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont,QFontDatabase,QColor,QPalette
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.pencere=ana_ekran.Ui_Form()
        self.pencere.setupUi(self)
        self.tahta_text=""
        self.pencere.label_7.setFont(program_font)
        self.gizle_birinci_grup()
        self.gizle_ikinci_grup()
        self.gizle_ucuncu_grup()
        self.gizle_dorduncu_grup()
        self.gizle_besinci_grup()
        self.pencere.pushButton_71.setText(" ")
        self.tahta_text="<html>"
        self.renk_kodu="#000000"
        self.pencere.pushButton_65.clicked.connect(self.cikis)
        self.pencere.pushButton.clicked.connect(self.goster_birinci_grup)
        self.pencere.pushButton_2.clicked.connect(self.goster_ikinci_grup)
        self.pencere.pushButton_3.clicked.connect(self.goster_ucuncu_grup)
        self.pencere.pushButton_4.clicked.connect(self.goster_dorduncu_grup)
        self.pencere.pushButton_5.clicked.connect(self.goster_besinci_grup)
        self.pencere.pushButton_6.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_7.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_8.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_9.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_10.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_11.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_12.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_13.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_14.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_15.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_16.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_17.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_18.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_19.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_20.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_21.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_22.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_23.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_24.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_25.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_26.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_27.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_28.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_29.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_30.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_31.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_32.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_33.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_34.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_35.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_36.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_37.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_38.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_39.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_40.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_41.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_42.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_43.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_44.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_45.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_46.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_47.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_48.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_49.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_50.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_51.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_52.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_53.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_54.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_55.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_56.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_57.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_58.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_59.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_60.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_61.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_62.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_63.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_64.clicked.connect(self.silgi)
        self.pencere.pushButton_67.clicked.connect(self.ColorSelect)
        self.pencere.pushButton_71.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_66.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_68.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_69.clicked.connect(self.buttonClicked)
        self.pencere.pushButton_70.clicked.connect(self.hakkinda)
        self.showFullScreen()###   Gösterimmmmm
    def gizle_birinci_grup(self):
        self.pencere.label_2.hide()
        self.pencere.pushButton_6.hide();self.pencere.pushButton_7.hide();self.pencere.pushButton_8.hide()
        self.pencere.pushButton_9.hide();self.pencere.pushButton_10.hide();self.pencere.pushButton_11.hide()
        self.pencere.pushButton_12.hide();self.pencere.pushButton_13.hide();self.pencere.pushButton_14.hide()
        self.pencere.pushButton_15.hide();self.pencere.pushButton_16.hide();self.pencere.pushButton_17.hide()
    def gizle_ikinci_grup(self):
        self.pencere.label_3.hide()
        self.pencere.pushButton_18.hide();self.pencere.pushButton_19.hide();self.pencere.pushButton_20.hide()
        self.pencere.pushButton_21.hide();self.pencere.pushButton_22.hide();self.pencere.pushButton_23.hide()
        self.pencere.pushButton_24.hide();self.pencere.pushButton_25.hide();self.pencere.pushButton_26.hide()
        self.pencere.pushButton_27.hide();self.pencere.pushButton_28.hide();self.pencere.pushButton_29.hide()
    def gizle_ucuncu_grup(self):
        self.pencere.label_4.hide()
        self.pencere.pushButton_30.hide();self.pencere.pushButton_31.hide();self.pencere.pushButton_32.hide()
        self.pencere.pushButton_33.hide();self.pencere.pushButton_34.hide();self.pencere.pushButton_35.hide()
        self.pencere.pushButton_36.hide();self.pencere.pushButton_37.hide();self.pencere.pushButton_38.hide()
        self.pencere.pushButton_39.hide();self.pencere.pushButton_40.hide();self.pencere.pushButton_41.hide()
    def gizle_dorduncu_grup(self):
        self.pencere.label_5.hide()
        self.pencere.pushButton_42.hide();self.pencere.pushButton_43.hide();self.pencere.pushButton_44.hide()
        self.pencere.pushButton_45.hide();self.pencere.pushButton_46.hide();self.pencere.pushButton_47.hide()
        self.pencere.pushButton_48.hide();self.pencere.pushButton_49.hide();self.pencere.pushButton_50.hide()
        self.pencere.pushButton_51.hide();self.pencere.pushButton_52.hide();self.pencere.pushButton_53.hide()
    def gizle_besinci_grup(self):
        self.pencere.label_6.hide()
        self.pencere.pushButton_54.hide();self.pencere.pushButton_55.hide();self.pencere.pushButton_56.hide()
        self.pencere.pushButton_57.hide();self.pencere.pushButton_58.hide();self.pencere.pushButton_59.hide()
        self.pencere.pushButton_60.hide();self.pencere.pushButton_61.hide();self.pencere.pushButton_62.hide()
        self.pencere.pushButton_63.hide()
    def goster_birinci_grup(self):
        self.pencere.label_2.show()
        self.pencere.pushButton_6.show();self.pencere.pushButton_7.show();self.pencere.pushButton_8.show()
        self.pencere.pushButton_9.show();self.pencere.pushButton_10.show();self.pencere.pushButton_11.show()
        self.pencere.pushButton_12.show();self.pencere.pushButton_13.show();self.pencere.pushButton_14.show()
        self.pencere.pushButton_15.show();self.pencere.pushButton_16.show();self.pencere.pushButton_17.show()
    def goster_ikinci_grup(self):
        self.pencere.label_3.show()
        self.pencere.pushButton_18.show();self.pencere.pushButton_19.show();self.pencere.pushButton_20.show()
        self.pencere.pushButton_21.show();self.pencere.pushButton_22.show();self.pencere.pushButton_23.show()
        self.pencere.pushButton_24.show();self.pencere.pushButton_25.show();self.pencere.pushButton_26.show()
        self.pencere.pushButton_27.show();self.pencere.pushButton_28.show();self.pencere.pushButton_29.show()
    def goster_ucuncu_grup(self):
        self.pencere.label_4.show()
        self.pencere.pushButton_30.show();self.pencere.pushButton_31.show();self.pencere.pushButton_32.show()
        self.pencere.pushButton_33.show();self.pencere.pushButton_34.show();self.pencere.pushButton_35.show()
        self.pencere.pushButton_36.show();self.pencere.pushButton_37.show();self.pencere.pushButton_38.show()
        self.pencere.pushButton_39.show();self.pencere.pushButton_40.show();self.pencere.pushButton_41.show()
    def goster_dorduncu_grup(self):
        self.pencere.label_5.show()
        self.pencere.pushButton_42.show();self.pencere.pushButton_43.show();self.pencere.pushButton_44.show()
        self.pencere.pushButton_45.show();self.pencere.pushButton_46.show();self.pencere.pushButton_47.show()
        self.pencere.pushButton_48.show();self.pencere.pushButton_49.show();self.pencere.pushButton_50.show()
        self.pencere.pushButton_51.show();self.pencere.pushButton_52.show();self.pencere.pushButton_53.show()
    def goster_besinci_grup(self):
        self.pencere.label_6.show()
        self.pencere.pushButton_54.show();self.pencere.pushButton_55.show();self.pencere.pushButton_56.show()
        self.pencere.pushButton_57.show();self.pencere.pushButton_58.show();self.pencere.pushButton_59.show()
        self.pencere.pushButton_60.show();self.pencere.pushButton_61.show();self.pencere.pushButton_62.show()
        self.pencere.pushButton_63.show()
    def buttonClicked(self):
        sender=self.sender()
        if sender:
            if sender==self.pencere.pushButton_66:
                self.tahta_text = self.tahta_text + "<font color='" + self.renk_kodu + "'>" + "?" + "</font>"

                self.pencere.label_7.setText(self.tahta_text)
            elif sender==self.pencere.pushButton_68:
                self.tahta_text = self.tahta_text + "<font color='" + self.renk_kodu + "'>" + "." + "</font>"

                self.pencere.label_7.setText(self.tahta_text)
            elif sender == self.pencere.pushButton_69:
                self.tahta_text = self.tahta_text + "<font color='" + self.renk_kodu + "'>" + "!" + "</font>"

                self.pencere.label_7.setText(self.tahta_text)
            else:
                self.tahta_text = self.tahta_text + "<font color='" + self.renk_kodu + "'>" + sender.text() + "</font>"

                self.pencere.label_7.setText(self.tahta_text)
    def silgi(self):

        self.tahta_text=self.pencere.label_7.text()[:-30]
        self.pencere.label_7.setText(self.tahta_text)
    def cikis(self):
        sys.exit()
    def ColorSelect(self):
        renk = QtWidgets.QColorDialog.getColor()
        if renk.isValid():
           self.renk_kodu=renk.name()

    def hakkinda(self):
        about_text = """
        PROGRAM EĞİTİMCİ ARKADAŞLAR İÇİN HAZIRLANMIŞ OLUP KULLANIMI TAMAMEN ÜCRETSİZDİR. 

        Programlama:Sedat DEMİR

        İstek,Öneri ve Fikirleriniz İçin:        
        İletişim:zeminkat.lab@gmail.com
        https://github.com/zeminkat  

        Not:Düzgün çalışabilmesi için ekran çözünürlüğü 1920*1080 olmalı ve program dosyalarında      değişiklik yapılmamalıdır.

        -------------------------------------------------------------------------------------------------------------------
        Programın kullanımından,dosyalarının değiştirilmesi,içeriğinin bozulması gibi durumlardan kullanıcı sorumludur.
        Açık kaynak kodlu hazırlanmış olup özgür yazılım felsefesi gereği programımızın kodları https://github.com/zeminkat adresinde yayımlanmıştır.
        -------------------------------------------------------------------------------------------------------------------
        
        """
        QMessageBox.information(self, "Hakkında", about_text)

app=QtWidgets.QApplication(sys.argv)


def font_ayarla():
    font_id = QFontDatabase.addApplicationFont("TTKBDikTemelAbece.ttf")
    font_ailesi = QFontDatabase.applicationFontFamilies(font_id)
    custom_font = QFont(font_ailesi[0], 105, QFont.Bold)

    return custom_font
program_font=font_ayarla()
pencere=Pencere()
sys.exit(app.exec_())
