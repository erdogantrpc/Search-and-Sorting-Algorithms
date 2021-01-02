from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QDesktopWidget, QCheckBox, QMessageBox, QPlainTextEdit
from PyQt5.QtGui import QPixmap, QIcon, QCursor
from PyQt5 import Qt
from PyQt5 import QtCore

import sys
import math
import random
import time

class BinarySearch(QWidget):
    def __init__(self, minRange = 0, maxRange = 1000, bulunacakSayi = random.randint(0, 999), uret = 1000):
        super().__init__()
        self.minRange = int(minRange)
        self.maxRange = int(maxRange)
        self.BulunacakSayi = int(bulunacakSayi)
        self.uret = int(uret)
        self.setUI()
    
    def setUI(self):
        self.Sayilar = []
        self.sayiUret(self.uret)
        self.Sayilar.sort()
        global count
        self.count = 0

        self.algorithm = QLabel(self)
        self.algorithm.move(370,10)
        self.algorithm.setText("Kullanılan Algoritma: Binary Search")
        self.algorithm.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")

        self.aranilanSayi = QLabel(self)
        self.aranilanSayi.move(430,40)
        self.aranilanSayi.setText(f"Aranilan sayı: {self.BulunacakSayi}")
        self.aranilanSayi.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")

        self.label = QLabel(self)
        self.label.setText("Kullanılan Dizi: ")
        self.label.move(10,70)
        self.label.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")

        self.kullanilanDizi = QPlainTextEdit(self)
        self.kullanilanDizi.setGeometry(150,70,790,150)
        self.kullanilanDizi.insertPlainText(str(self.Sayilar))
        self.kullanilanDizi.setStyleSheet("background-color: #000066;border-style: outset;color: white;border-color: white;border-width: 2px;border-radius: 10px;font: bold 14px;")
        self.kullanilanDizi.setReadOnly(True)

        self.setWindowIcon(QIcon('img/logo.png'))
        self.setWindowTitle("Sonuclar")
        self.centerPoint = QDesktopWidget().availableGeometry().center()
        self.setGeometry(self.centerPoint.x() - 475, self.centerPoint.y() - 182,950,365)
        self.setMinimumSize(QSize(950,365))
        self.setMaximumSize(QSize(950,365))
        self.setStyleSheet("background-color: #000066")

        self.hesapla()
        
    def sayiUret(self, x):
        for a in range(x):
            EklenecekSayi = random.randint(self.minRange, self.maxRange)
            self.Sayilar.append(EklenecekSayi)

    def hesapla(self):
        self.BaslamaZamani = time.time()
        cevap = self.ikiliArama(self.Sayilar, 0, len(self.Sayilar) - 1, self.BulunacakSayi)
        self.BitisZamani = time.time()
        self.zaman = self.BitisZamani-self.BaslamaZamani
        if cevap:
            self.bulunanSayi = QLabel(self)
            self.bulunanSayi.move(390,240)
            self.bulunanSayi.setText(f"Eleman {cevap}.indexte bulundu")
            self.bulunanSayi.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")

            self.adimSayisi = QLabel(self)
            self.adimSayisi.move(340,260)
            self.adimSayisi.setText(f"Bu elemanı bulmak için {self.count} işlem yapıldı")
            self.adimSayisi.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")
            
            self.sure = QLabel(self)
            self.sure.move(315,280)
            self.sure.setText("Algoritmanın çalışma süresi: {:.8f} saniye".format(self.zaman))
            self.sure.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")
        else:
            self.bulunamadi = QLabel(self)
            self.bulunamadi.move(370,240)
            self.bulunamadi.setText("Aranan sayı dizi içerisinde bulunamadı!")
            self.bulunamadi.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")

            self.sure = QLabel(self)
            self.sure.move(340,260)
            self.sure.setText("Algoritmanın çalışma süresi: {:.8f} saniye".format(self.zaman))
            self.sure.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")

    def ikiliArama(self, Sayilar, altSinir, ustSinir, bulunacakSayi):
        if ustSinir >= altSinir:
            self.count += 1
            orta = (ustSinir + altSinir) // 2
            if Sayilar[orta] == bulunacakSayi:
                self.count += 1
                return orta
            elif Sayilar[orta] > bulunacakSayi:
                self.count += 1
                return self.ikiliArama(Sayilar, altSinir, ustSinir - 1, bulunacakSayi)
            else:
                self.count += 1
                return self.ikiliArama(Sayilar, orta + 1, ustSinir, bulunacakSayi)
        else:
            self.count += 1
            return False