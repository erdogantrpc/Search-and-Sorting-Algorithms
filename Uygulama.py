"""
@author: Erdogan Turpcu
"""
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QDesktopWidget, QCheckBox, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QCursor
from PyQt5 import Qt
from PyQt5 import QtCore


from Algorithms.LinearSearch import LinearSearch
from Algorithms.BinarySearch import BinarySearch
from Algorithms.InsertionSort import InsertionSort
from Algorithms.BucketSort import BucketSort
from Algorithms.CountingSort import CountingSort
from Algorithms.HeapSort import HeapSort
from Algorithms.MergeSort import MergeSort
from Algorithms.QuickSort import QuickSort
from Algorithms.RadixSort import RadixSort

import sys
import math
import random
import time

class Pencere(QWidget):
    global durum

    def __init__(self):
        super().__init__()
        self.durum = False
        self.setUI()
    
    def setUI(self):
        logo = QLabel(self)
        pixmap = QPixmap('img/logo-400.png')
        logo.setPixmap(pixmap)
        
        self.algorithm = QLabel(self)
        self.algorithm.move(520,30)
        self.algorithm.setText("Lütfen aşağıdan kullanmak istediğiniz algoritmayı seçiniz")
        self.algorithm.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")

        self.combo = QComboBox(self)
        self.combo.addItem("Algoritma Seçiniz...")
        self.combo.addItem("Linear Search")
        self.combo.addItem("Binary Search")
        self.combo.addItem("Insertion Sort")
        self.combo.addItem("Merge Sort")
        self.combo.addItem("Heap Sort")
        self.combo.addItem("Quick Sort")
        self.combo.addItem("Bucket Sort")
        self.combo.addItem("Counting Sort")
        self.combo.addItem("Radix Sort")
        self.combo.move(650, 70)
        self.combo.setStyleSheet("background-color: #000066;border-style: outset; color: white; border-color: white; border-width: 2px;border-radius: 10px;font: bold 14px;min-width: 10em;padding: 6px;")
        self.combo.activated[str].connect(self.onChanged)

        self.check = QCheckBox(self)
        self.check.setText("Rastgele üretilecek sayı adedini ve aralığını kendim belirlemek istiyorum.")
        self.chekInfo = QLabel(self)
        self.chekInfo.setText("(İşaretelemediğiniz takdirde 0-10000 arasından rastgele 1000 sayı üretilecektir)")
        self.chekInfo.move(420,150)
        self.chekInfo.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")
        self.check.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")
        self.check.stateChanged.connect(self.clickBox)
        self.check.move(435,120)

        self.button = QPushButton(self)
        self.button.move(660,300)
        self.button.setText("Algoritmayı Başlat")
        self.button.setStyleSheet("background-color: #000066;border-style: outset;color: white;border-width: 2px;border-radius: 10px;font: bold 14px;min-width: 10em;padding: 6px;")
        self.button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.button.clicked.connect(self.calculate)
        
        self.setWindowIcon(QIcon('img/logo.png'))
        self.setWindowTitle("Algoritmalar")
        self.centerPoint = QDesktopWidget().availableGeometry().center()
        self.setGeometry(self.centerPoint.x() - 550, self.centerPoint.y() - 182,1100,365)
        self.setMinimumSize(QSize(1100,365))
        self.setMaximumSize(QSize(1100,365))
        self.setStyleSheet("background-color: #000066")
        self.show()

    def clickBox(self, state):
        if state == QtCore.Qt.Checked:
            self.durum = True
            self.randomNumber = QLabel(self)
            self.randomNumber.move(480,180)
            self.randomNumber.setText("Üretmek istediğiniz sayı miktarını giriniz : ")
            self.randomNumber.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px;")
            self.randomNumber.show()
            self.randomNumberInput = QLineEdit(self)
            self.randomNumberInput.move(840,180)
            self.randomNumberInput.resize(100,20)
            self.randomNumberInput.setStyleSheet("width: 100%;border: 0;border-bottom: 2px solid gray;outline: 0;color: white;background: transparent")
            self.randomNumberInput.show()

            self.NumberRange = QLabel(self)
            self.NumberRange.move(510,210)
            self.NumberRange.setText("Sayıların aralığını belirleyiniz.")
            self.NumberRange.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px; text-align: center;") 
            self.NumberRange.show()

            self.NumberRangeInput_1 = QLineEdit(self)
            self.NumberRangeInput_1.move(770,210)
            self.NumberRangeInput_1.resize(50,20)
            self.NumberRangeInput_1.setStyleSheet("width: 100%;border: 0;border-bottom: 2px solid gray;outline: 0;color: white;background: transparent")
            self.NumberRangeInput_1.show()

            self.dash = QLabel(self)
            self.dash.setText("-")
            self.dash.move(840,200)
            self.dash.setStyleSheet("color: white; font-family: Arial Black; font-size: 25px;")
            self.dash.show()

            self.NumberRangeInput_2 = QLineEdit(self)
            self.NumberRangeInput_2.move(870,210)
            self.NumberRangeInput_2.resize(50,20)
            self.NumberRangeInput_2.setStyleSheet("width: 100%;border: 0;border-bottom: 2px solid gray;outline: 0;color: white;background: transparent") 
            self.NumberRangeInput_2.show()

        else:
            self.durum = False
            self.kontrol = QPushButton(self)
            self.kontrol.setStyleSheet("background-color: #000066; border-radius : 15px; border : 1px #000066")
            self.kontrol.setGeometry(430,180,640,50)
            self.kontrol.show()

    def onChanged(self, text):
        if text == "Linear Search":
                self.findNumber = QLabel(self)
                self.findNumber.move(540,240)
                self.findNumber.setText("Bulunmasını istediğiniz sayıyı giriniz: ")
                self.findNumber.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px; text-align: center;") 
                self.findNumber.show()
                self.findNumberInput = QLineEdit(self)
                self.findNumberInput.move(860,240)
                self.findNumberInput.resize(50,20)
                self.findNumberInput.setStyleSheet("width: 100%;border: 0;border-bottom: 2px solid gray;outline: 0;color: white;background: transparent") 
                self.findNumberInput.show()

                self.findNumberInfo = QLabel(self)
                self.findNumberInfo.move(440,265)
                self.findNumberInfo.setText("(Boş bıraktığınız takdirde 0-1000 arasından rastgele bir sayı aranacaktır.)")
                self.findNumberInfo.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px; text-align: center;") 
                self.findNumberInfo.show()
        elif text == "Binary Search":
                self.findNumber = QLabel(self)
                self.findNumber.move(540,240)
                self.findNumber.setText("Bulunmasını istediğiniz sayıyı giriniz: ")
                self.findNumber.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px; text-align: center;") 
                self.findNumber.show()
                self.findNumberInput = QLineEdit(self)
                self.findNumberInput.move(860,240)
                self.findNumberInput.resize(50,20)
                self.findNumberInput.setStyleSheet("width: 100%;border: 0;border-bottom: 2px solid gray;outline: 0;color: white;background: transparent") 
                self.findNumberInput.show()

                self.findNumberInfo = QLabel(self)
                self.findNumberInfo.move(440,265)
                self.findNumberInfo.setText("(Boş bıraktığınız takdirde 0-1000 arasından rastgele bir sayı aranacaktır.)")
                self.findNumberInfo.setStyleSheet("color: white; font-family: Arial Black; font-size: 15px; text-align: center;") 
                self.findNumberInfo.show()
        else:
            if not self.durum:
                self.kontrol = QPushButton(self)
                self.kontrol.setStyleSheet("background-color: #000066; border-radius : 15px; border : 1px #000066")
                self.kontrol.setGeometry(430,180,640,110)
                self.kontrol.show()
            else:
                self.kontrol = QPushButton(self)
                self.kontrol.setStyleSheet("background-color: #000066; border-radius : 15px; border : 1px #000066")
                self.kontrol.setGeometry(430,240,640,50)
                self.kontrol.show()
    
    def calculate(self):
        if self.combo.currentText() == "Linear Search":
            if self.durum and len(self.findNumberInput.text()) == 0:
                self.altSinir = self.NumberRangeInput_1.text()
                self.ustSinir = self.NumberRangeInput_2.text()
                self.rastgeleSayi = self.randomNumberInput.text()
                self.SW = LinearSearch(minRange = self.altSinir, maxRange = self.ustSinir, uret = self.rastgeleSayi)
                self.SW.show()
            elif self.durum and len(self.findNumberInput.text()) != 0:
                self.altSinir = self.NumberRangeInput_1.text()
                self.ustSinir = self.NumberRangeInput_2.text()
                self.bulunacakSayi = self.findNumberInput.text()
                self.rastgeleSayi = self.randomNumberInput.text()
                self.SW = LinearSearch(minRange = self.altSinir, maxRange = self.ustSinir, bulunacakSayi = self.bulunacakSayi, uret = self.rastgeleSayi)
                self.SW.show()
            elif len(self.findNumberInput.text()) != 0:
                self.bulunacakSayi = self.findNumberInput.text()
                self.SW = LinearSearch(bulunacakSayi = self.bulunacakSayi)
                self.SW.show()
            else:
                self.SW = LinearSearch()
                self.SW.show()
            self.findNumberInput.setText("")
        elif self.combo.currentText() == "Binary Search":
            if self.durum and len(self.findNumberInput.text()) == 0:
                self.altSinir = self.NumberRangeInput_1.text()
                self.ustSinir = self.NumberRangeInput_2.text()
                self.rastgeleSayi = self.randomNumberInput.text()
                self.SW = BinarySearch(minRange = self.altSinir, maxRange = self.ustSinir, uret = self.rastgeleSayi)
                self.SW.show()
            elif self.durum and len(self.findNumberInput.text()) != 0:
                self.altSinir = self.NumberRangeInput_1.text()
                self.ustSinir = self.NumberRangeInput_2.text()
                self.bulunacakSayi = self.findNumberInput.text()
                self.rastgeleSayi = self.randomNumberInput.text()
                self.SW = BinarySearch(minRange = self.altSinir, maxRange = self.ustSinir, bulunacakSayi = self.bulunacakSayi, uret = self.rastgeleSayi)
                self.SW.show()
            elif len(self.findNumberInput.text()) != 0:
                self.bulunacakSayi = self.findNumberInput.text()
                self.SW = BinarySearch(bulunacakSayi = self.bulunacakSayi)
                self.SW.show()
            else:
                self.SW = BinarySearch()
                self.SW.show()
            self.findNumberInput.setText("")
        elif self.combo.currentText() == "Insertion Sort":
            if self.durum:
                self.altSinir = self.NumberRangeInput_1.text()
                self.ustSinir = self.NumberRangeInput_2.text()
                self.rastgeleSayi = self.randomNumberInput.text()
                self.SW = InsertionSort(minRange = self.altSinir, maxRange = self.ustSinir, uret = self.rastgeleSayi)
                self.SW.show()
            else:
                self.SW = InsertionSort()
                self.SW.show()
        elif self.combo.currentText() == "Merge Sort":
            if self.durum:
                self.altSinir = self.NumberRangeInput_1.text()
                self.ustSinir = self.NumberRangeInput_2.text()
                self.rastgeleSayi = self.randomNumberInput.text()
                self.SW = MergeSort(minRange = self.altSinir, maxRange = self.ustSinir, uret = self.rastgeleSayi)
                self.SW.show()
            else:
                self.SW = MergeSort()
                self.SW.show()
        elif self.combo.currentText() == "Heap Sort":
            if self.durum:
                self.altSinir = self.NumberRangeInput_1.text()
                self.ustSinir = self.NumberRangeInput_2.text()
                self.rastgeleSayi = self.randomNumberInput.text()
                self.SW = HeapSort(minRange = self.altSinir, maxRange = self.ustSinir, uret = self.rastgeleSayi)
                self.SW.show()
            else:
                self.SW = HeapSort()
                self.SW.show()
        elif self.combo.currentText() == "Quick Sort":
            if self.durum:
                self.altSinir = self.NumberRangeInput_1.text()
                self.ustSinir = self.NumberRangeInput_2.text()
                self.rastgeleSayi = self.randomNumberInput.text()
                self.SW = QuickSort(minRange = self.altSinir, maxRange = self.ustSinir, uret = self.rastgeleSayi)
                self.SW.show()
            else:
                self.SW = QuickSort()
                self.SW.show()
        elif self.combo.currentText() == "Bucket Sort":
            if self.durum:
                self.altSinir = self.NumberRangeInput_1.text()
                self.ustSinir = self.NumberRangeInput_2.text()
                self.rastgeleSayi = self.randomNumberInput.text()
                self.SW = BucketSort(minRange = self.altSinir, maxRange = self.ustSinir, uret = self.rastgeleSayi)
                self.SW.show()
            else:
                self.SW = BucketSort()
                self.SW.show()
        elif self.combo.currentText() == "Counting Sort":
            if self.durum:
                self.altSinir = self.NumberRangeInput_1.text()
                self.ustSinir = self.NumberRangeInput_2.text()
                self.rastgeleSayi = self.randomNumberInput.text()
                self.SW = CountingSort(minRange = self.altSinir, maxRange = self.ustSinir, uret = self.rastgeleSayi)
                self.SW.show()
            else:
                self.SW = CountingSort()
                self.SW.show()
        elif self.combo.currentText() == "Radix Sort":
            if self.durum:
                self.altSinir = self.NumberRangeInput_1.text()
                self.ustSinir = self.NumberRangeInput_2.text()
                self.rastgeleSayi = self.randomNumberInput.text()
                self.SW = RadixSort(minRange = self.altSinir, maxRange = self.ustSinir, uret = self.rastgeleSayi)
                self.SW.show()
            else:
                self.SW = RadixSort()
                self.SW.show()
        else:
            mesajKutusu = QMessageBox()
            mesajKutusu.setWindowTitle("Hata!")
            mesajKutusu.setText("Lütfen Bir Algoritma Seçiniz")
            mesajKutusu.setIcon(QMessageBox.Warning)
            mesajKutusu.setStandardButtons(QMessageBox.Ok)
            mesajKutusu.setGeometry(self.centerPoint.x() - 75, self.centerPoint.y() - 75, 150,150)
            mesajKutusu.exec()
def window():
    app = QApplication(sys.argv)
    pencere = Pencere()
    sys.exit(app.exec())

if __name__ == "__main__":
    window()
