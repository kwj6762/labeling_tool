
# coding: utf-8

# In[1]:



# coding: utf-8

# In[ ]:


import sys

from PIL import Image

from PyQt5 import QtCore, QtGui , QtWidgets
from PyQt5.QtWidgets import *
from lastUI5 import Ui_MainWindow
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
from PyQt5.QtCore import Qt
from lxml import etree
import os
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from popup import Ui_Form
from popup2 import Ui_Form2
from password import Ui_Form3
from xml.etree.ElementTree import parse
import csv
import shutil


# In[2]:


class Main(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self)
            
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

        self.point_1 = QtCore.QPoint(0,0)
        self.point_2 = QtCore.QPoint(0,0)
        self.point_3 = QtCore.QPoint(0,0)
        self.point_4 = QtCore.QPoint(0,0)

        self.setupUi(self)
        self.pixmap = QPixmap()
        self.viewType()
        self.flag = 0
        self.ctrl = False
        self.count = 0

        self.zoom_level = 0

    def viewType(self): 
        self.items=[]
        
        f = open('data.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        for line in rdr:
            self.items.append(line[0])
        f.close()    
        
        self.tableWidget.setRowCount(len(self.items))

        for i in range(0,len(self.items)):
            item = QTableWidgetItem(self.items[i])
            item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            self.tableWidget.setItem(i, 0, item)

    def browse(self):
        self.tableWidget_2.clear()
        try:
            folder = QFileDialog.getExistingDirectory (self)
            self.label_forder.setText(folder)
            file_list = os.listdir(folder)
            file_list.sort()
            file_list2 = []
            xml_list = []
            for i in range(0,len(file_list)):
                if('jpg' in file_list[i]):
                    file_list2.append(file_list[i])
                    
            for i in range(0,len(file_list)):
                if('xml' in file_list[i]):
                    xml_list.append(file_list[i])        
            
            self.tableWidget_2.setRowCount(len(file_list2))
            for i in range(0,len(file_list2)):
                    item = QTableWidgetItem(file_list2[i])
                    item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
                    self.tableWidget_2.setItem(i,0,item)
                    for j in range(0,len(xml_list)):
                        if(file_list2[i].split(".")[0] == xml_list[j].split(".")[0] ):
                            item = QTableWidgetItem("xml파일 존재")
                            item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
                            self.tableWidget_2.setItem(i,1,item)


            self.show()
        except:
            QMessageBox.about(self,"warning","폴더선택을 해주세요")
            
    def showfilelist(self):
        self.tableWidget_2.clear()
        try:
            folder = self.label_forder.text()
            file_list = os.listdir(folder)
            file_list.sort()
            file_list2 = []
            xml_list = []
            for i in range(0,len(file_list)):
                if('jpg' in file_list[i]):
                    file_list2.append(file_list[i])
                    
            for i in range(0,len(file_list)):
                if('xml' in file_list[i]):
                    xml_list.append(file_list[i])        
            
            self.tableWidget_2.setRowCount(len(file_list2))
            for i in range(0,len(file_list2)):
                    item = QTableWidgetItem(file_list2[i])
                    item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
                    self.tableWidget_2.setItem(i,0,item)
                    for j in range(0,len(xml_list)):
                        if(file_list2[i].split(".")[0] == xml_list[j].split(".")[0] ):
                            item = QTableWidgetItem("xml파일 존재")
                            item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
                            self.tableWidget_2.setItem(i,1,item)
            self.show()
        except:
            QMessageBox.about(self,"warning","폴더선택을 해주세요")
            
    def showXmlfile(self):
        path = str(self.label_forder.text())
        name = str(self.label_imname.text().split(".jpg")[0])
        try:
            tree = parse(path+"/"+name+".xml")
            note = tree.getroot()

            for child in note:
                if("입력값" in child.tag):
                    for c in child:
                        for i in range(0,self.tableWidget.rowCount()):
                            if(self.tableWidget.item(i,0).text() == c.tag):
                                item = QTableWidgetItem()
                                item.setText(c.text)
                                self.tableWidget.setItem(i,1,item)
        except:
            print("xml파일 없음")
        
    def previous_picture(self):
        try:
            folder = self.label_forder.text()
            file_list = os.listdir(folder)
            file_list.sort()
            file_list2 = []
            for i in file_list:
                if('jpg' in i):
                    file_list2.append(i)
                
            for index in range(0,len(file_list2)):
                if (file_list2[index] == self.label_imname.text()):
                    now = index
            try:
                self.tableWidget.clear()
                self.viewType()
                
                self.label_imname.setText(file_list2[now-1])
                self.tableWidget_2.selectRow(now-1)
                self.pixmap = QPixmap(folder+"/"+file_list2[now-1])
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                self.label_picture.resize(self.pixmap.width(),self.pixmap.height())
                self.label_picture.setPixmap(self.pixmap)
                self.zoom_level = 0

                self.show()
            except:
                self.label_imname.setText(file_list2[-1])
                self.tableWidget_2.selectRow(-1)
                self.pixmap = QPixmap(folder+"/"+file_list2[-1])
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                self.label_picture.resize(self.pixmap.width(),self.pixmap.height())
                self.label_picture.setPixmap(self.pixmap)
                self.zoom_level = 0

                self.show()
        except:
            QMessageBox.about(self,"warning","이미지선택을 해주세요")
        
        self.showXmlfile()
            
    def next_picture(self):
        try:
            folder = self.label_forder.text()
            file_list = os.listdir(folder)
            file_list.sort()
            file_list2 = []
            for i in file_list:
                if('jpg' in i):
                    file_list2.append(i)
                
            for index in range(0,len(file_list2)):
                if (file_list2[index] == self.label_imname.text()):
                    now = index
            try:
                self.tableWidget.clear()
                self.viewType()
                
                self.label_imname.setText(file_list2[now+1])
                self.tableWidget_2.selectRow(now+1)
                self.pixmap = QPixmap(folder+"/"+file_list2[now+1])
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                self.label_picture.resize(self.pixmap.width(),self.pixmap.height())
                self.label_picture.setPixmap(self.pixmap)
                self.zoom_level = 0

                self.show()
            except:
                self.label_imname.setText(file_list2[0])
                self.tableWidget_2.selectRow(0)
                self.pixmap = QPixmap(folder+"/"+file_list2[0])
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                self.label_picture.resize(self.pixmap.width(),self.pixmap.height())
                self.label_picture.setPixmap(self.pixmap)
                self.zoom_level = 0

                self.show()
                
        except:
            QMessageBox.about(self,"warning","이미지선택을 해주세요")
        
        self.showXmlfile()
            
    def savebtn(self):
        try:
            root = etree.Element("xml파일")
            row = self.tableWidget_2.currentItem().row()
            text = str(self.tableWidget_2.currentItem().text())
            try:
                itemsTextList =  []
                for i in range(self.tableWidget.rowCount()):
                    itemsTextList.append(str(self.tableWidget.item(i,0).text()))
                    
                xml_no1 = etree.Element("입력값")
                for t in range(0,len(itemsTextList)):
                    xml_type = etree.Element(str(itemsTextList[t]))
                    try:
                        xml_type.text = str(self.tableWidget.item(t,1).text())
                        xml_no1.append(xml_type)
                    except:
                        xml_type.text = "    "
                        xml_no1.append(xml_type)

                xml_no2 = etree.Element("파싱값")
                name = str(self.tableWidget_2.currentItem().text())
                parsing_name = []
                parsing_name = name.split("_")
                rgb = str(parsing_name[-1].split(".jpg")[0])+"/"+str(parsing_name[-2])
                parsing = ["날짜","id","차선","속도","레이더파워","화이트밸런스","RGB" ]
                
                for t in range(0,len(parsing)):
                    if(t==6):
                        xml_type = etree.Element(parsing[t])
                        xml_type.text = str(rgb)
                        xml_no2.append(xml_type)
                    else:
                        xml_type = etree.Element(parsing[t])
                        xml_type.text = str(parsing_name[t])
                        xml_no2.append(xml_type)
                root.append(xml_no2)
                root.append(xml_no1)
                
                        # Write to xml file
                name = self.label_imname.text()
                name = (name.split(".jpg"))[0]
                path = self.label_forder.text()
                x_output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
                x_header = '<?xml version="1.0" encoding="UTF-8"?>\n'
                ff=open(path +'/' + name + '.xml', 'w', encoding="utf-8")
                ff.write(x_header + x_output.decode('utf-8') )
            except:
                QMessageBox.about(self,"warning","값을 입력 해주세요")
        except:
            QMessageBox.about(self,"warning","이미지선택을 해주세요")
        
        self.next_picture()
        
    def xmlcreate(self):
        try:
            row = self.tableWidget_2.rowCount()
            for i in range(0,row):
                try:
                    xmlexist=self.tableWidget_2.item(i,1).text()
                except:
                    xmlexist="  "

                if(xmlexist=="xml파일 존재"):
                    print("이미존재")
                else:

                    root = etree.Element("xml파일")
                    xml_no2 = etree.Element("파싱값")
                    name = str(self.tableWidget_2.item(i,0).text())
                    parsing_name = []
                    try:
                        parsing_name = name.split("_")
                        rgb = str(parsing_name[-1].split(".jpg")[0])+"/"+str(parsing_name[-2])
                        parsing = ["날짜","id","차선","속도","레이더파워","화이트밸런스","RGB" ]
                    except:
                        parsing_name = []

                if(len(parsing_name)==8):
                    for t in range(0,len(parsing)):
                        if(t==6):
                            xml_type = etree.Element(parsing[t])
                            xml_type.text = str(rgb)
                            xml_no2.append(xml_type)
                        else:
                            xml_type = etree.Element(parsing[t])
                            xml_type.text = str(parsing_name[t])
                            xml_no2.append(xml_type)

                    root.append(xml_no2)

                    # Write to xml file
                    name = str(self.tableWidget_2.item(i,0).text())
                    name = (name.split(".jpg"))[0]
                    path = self.label_forder.text()
                    x_output = etree.tostring(root, pretty_print=True, encoding='UTF-8')
                    x_header = '<?xml version="1.0" encoding="UTF-8"?>\n'
                    ff=open(path +'/' + name + '.xml', 'w', encoding="utf-8")
                    ff.write(x_header + x_output.decode('utf-8') )

                    self.showfilelist()
        except:
            QMessageBox.about(self,"warning","폴더를 선택해주세요")
            
    def search(self):
        try:
            num=int(self.lineEdit.text())
            try:
                folder =self.label_forder.text()
                file_list = os.listdir(folder)
                file_list.sort()
                file_list2=[]
                for i in file_list:
                    if('jpg' in i):
                        file_list2.append(i)
                for index in range(0,len(file_list2)):
                    if(index+1 == num):
                        now=index

                self.tableWidget.clear()
                self.viewType()        
                        
                self.tableWidget_2.selectRow(now)
                self.label_imname.setText(file_list2[now])
                self.pixmap = QPixmap(folder + "/" +file_list2[now])
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                self.label_picture.resize(self.pixmap.width(),self.pixmap.height())
                self.label_picture.setPixmap(self.pixmap)
                self.zoom_level = 0
                

                self.show()
            except:
                QMessageBox.about(self,"warning","이미지파일경로를 선택해주세요")
        except:
            QMessageBox.about(self,"warning","숫자를 입력해주세요")
        
        self.showXmlfile()
            
    def showItem(self):
        
        filename = self.tableWidget_2.currentItem().text()
        
        self.tableWidget.clear()
        self.viewType()
        
        self.label_imname.setText(filename)
        folder = self.label_forder.text()
        self.pixmap = QPixmap(folder+"/"+filename)
        self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
        self.label_picture.resize(self.pixmap.width(),self.pixmap.height())
        self.label_picture.setPixmap(self.pixmap)
        self.zoom_level = 0 
        
        self.showXmlfile()
        
    def xyshowbutton(self):
        nowtext = self.pushButton_5.text()
        if(nowtext == "좌표 표시"):
            self.pushButton_5.setText("표시중....")
        else:
            self.pushButton_5.setText("좌표 표시")
            self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
            self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
            self.label_picture.setPixmap(self.pixmap)
            self.label_picture.resize(self.pixmap.width(),self.pixmap.height())
            
    def addxybutton(self):
                    
        one = self.label_4.text().split("첫번째좌표 : ")[1]
        two = self.label_5.text().split("두번째좌표 : ")[1]
        three = self.label_6.text().split("세번째좌표 : ")[1]
        four = self.label_7.text().split("네번째좌표 : ")[1]
        
                    
        point = [one,two,three,four]
        name = ["첫번째좌표" , "두번째좌표", "세번째좌표", "네번째좌표"]
        temp = []
        
        for i in range(0,len(name)):
            for j in range(0,self.tableWidget.rowCount()):
                if(self.tableWidget.item(j,0).text() == name[i]):
                    item = QTableWidgetItem(point[i])
                    self.tableWidget.setItem(j,1,item)
                    temp.append(name[i])
        
        for i in range(0,len(temp)):
            name.pop(name.index(temp[i]))

        for k in range(0,len(name)):
            
            rowcount = self.tableWidget.rowCount()+1
            self.tableWidget.setRowCount(rowcount)
            
            labeling_name = name[k]
            additems = [labeling_name]
            item = QTableWidgetItem(additems[0])
            item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
            self.tableWidget.setItem(rowcount-1, 0, item)
            itemsTextList =  []
            for i in range(self.tableWidget.rowCount()):
                itemsTextList.append(str(self.tableWidget.item(i,0).text()))

            f = open('data.csv', 'w', encoding='utf-8', newline='')
            wr = csv.writer(f)
            for i in range(0,len(itemsTextList)):
                temp=[]
                temp.append(itemsTextList[i])
                wr.writerow(temp)
            f.close()
            
            item = QTableWidgetItem(point[k])
            self.tableWidget.setItem(rowcount-1,1,item)

            self.show()
            
    def subtype(self):
        try:
            self.tableWidget.removeRow(self.tableWidget.currentItem().row())
            
            itemsTextList = []

            for i in range(self.tableWidget.rowCount()):
                itemsTextList.append(str(self.tableWidget.item(i,0).text()))

            f = open('data.csv', 'w', encoding='utf-8', newline='')
            wr = csv.writer(f)
            for i in range(0,len(itemsTextList)):
                temp=[]
                temp.append(itemsTextList[i])
                wr.writerow(temp)
            f.close()
            
        except:
            QMessageBox.about(self,"warning","행을 선택 해주세요")
            


    def paintEvent(self, event):
        nowtext = self.pushButton_5.text()

        temp_pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
        height = temp_pixmap.height()/450
        width = temp_pixmap.width()/730

        zoom = 1
        if self.zoom_level !=0:
            for i in range(self.zoom_level):
                zoom *=1.25

        v=self.scrollArea2.verticalScrollBar().value()
        h=self.scrollArea2.horizontalScrollBar().value()

        if(nowtext == "표시중...." and self.count != 4):
            painter = QtGui.QPainter(self.pixmap)
            pen = QPen(QtGui.QColor(255,0,0),5)
            painter.setPen(pen)

            if self.count == 1:
                painter.drawPoint(int((self.point_1.x()-24)+h),int((self.point_1.y()-141))+v)
                
            elif self.count == 2:
                painter.drawPoint(int((self.point_2.x()-24)+h),int((self.point_2.y()-141))+v)
                
            elif self.count == 3:
                painter.drawPoint(int((self.point_3.x()-24)+h),int((self.point_3.y()-141))+v)
                
            elif self.count == 3:
                painter.drawPoint(int((self.point_4.x()-24)+h),int((self.point_4.y()-141))+v)
 

            
            self.label_picture.setPixmap(self.pixmap)
            self.label_4.setText("첫번째좌표 : ("+str(int(((self.point_1.x()-24)+h)/zoom*width))+", "+str(int(((self.point_1.y()-141)+v)/zoom*height))+")")
            self.label_5.setText("두번째좌표 : ("+str(int(((self.point_2.x()-24)+h)/zoom*width))+", "+str(int(((self.point_2.y()-141)+v)/zoom*height))+")")
            self.label_6.setText("세번째좌표 : ("+str(int(((self.point_3.x()-24)+h)/zoom*width))+", "+str(int(((self.point_3.y()-141)+v)/zoom*height))+")")
            self.label_7.setText("네번째좌표 : ("+str(int(((self.point_4.x()-24)+h)/zoom*width))+", "+str(int(((self.point_4.y()-141)+v)/zoom*height))+")")

        elif(nowtext == "표시중...." and self.count == 4):
            painter = QtGui.QPainter(self.pixmap)
            pen = QPen(QtGui.QColor(255,0,0),5)
            painter.setPen(pen)

            x_list = [int(self.point_1.x()+h),int(self.point_2.x()+h),int(self.point_3.x()+h),int(self.point_4.x()+h)]
            y_list = [int(self.point_1.y()+v),int(self.point_2.y()+v),int(self.point_3.y()+v),int(self.point_4.y()+v)]
            
            painter.drawLine(x_list[0]-24,y_list[0]-141,x_list[1]-24,y_list[1]-141)
            painter.drawLine(x_list[1]-24,y_list[1]-141,x_list[2]-24,y_list[2]-141)
            painter.drawLine(x_list[2]-24,y_list[2]-141,x_list[3]-24,y_list[3]-141)
            painter.drawLine(x_list[3]-24,y_list[3]-141,x_list[0]-24,y_list[0]-141)
            
            self.label_picture.setPixmap(self.pixmap)

            self.label_4.setText("첫번째좌표 : ("+str(int((x_list[0]-24)/zoom*width))+", "+str(int((y_list[0]-141)/zoom*height))+")")
            self.label_5.setText("두번째좌표 : ("+str(int((x_list[1]-24)/zoom*width))+", "+str(int((y_list[1]-141)/zoom*height))+")")
            self.label_6.setText("세번째좌표 : ("+str(int((x_list[2]-24)/zoom*width))+", "+str(int((y_list[2]-141)/zoom*height))+")")
            self.label_7.setText("네번째좌표 : ("+str(int((x_list[3]-24)/zoom*width))+", "+str(int((y_list[3]-141)/zoom*height))+")")

            
    def mousePressEvent(self, event):
        nowtext = self.pushButton_5.text()
        if nowtext == "표시중....":
            if self.count == 0:
                self.point_1 = event.pos()
                self.update()
                print("press1"+str(event.pos()))
                self.count+=1

            elif self.count == 1:
                self.point_2 = event.pos()
                self.update()
                print("press2"+str(event.pos()))
                self.count+=1

            elif self.count == 2:
                self.point_3 = event.pos()
                self.update()
                print("press3"+str(event.pos()))
                self.count+=1

            elif self.count == 3:
                self.point_4 = event.pos()
                self.update()
                print("press4"+str(event.pos()))
                self.count+=1

            else :
                self.count = 0
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                self.label_picture.setPixmap(self.pixmap)
                self.zoom_level = 0

    def wheelEvent(self,event):
        delta = event.angleDelta()
        if delta.y() > 0 and self.ctrl == True and self.zoom_level < 12:
            self.zoomin()
        elif delta.y() < 0 and self.ctrl == True:
            self.zoomout()

    def keyPressEvent(self, e):
        def isPrintable(key): 
            printable = [ Qt.Key_Space, Qt.Key_Exclam, Qt.Key_QuoteDbl, Qt.Key_NumberSign, Qt.Key_Dollar, Qt.Key_Percent, Qt.Key_Ampersand, Qt.Key_Apostrophe, Qt.Key_ParenLeft, Qt.Key_ParenRight, Qt.Key_Asterisk, Qt.Key_Plus, Qt.Key_Comma, Qt.Key_Minus, Qt.Key_Period, Qt.Key_Slash, Qt.Key_0, Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7, Qt.Key_8, Qt.Key_9, Qt.Key_Colon, Qt.Key_Semicolon, Qt.Key_Less, Qt.Key_Equal, Qt.Key_Greater, Qt.Key_Question, Qt.Key_At, Qt.Key_A, Qt.Key_B, Qt.Key_C, Qt.Key_D, Qt.Key_E, Qt.Key_F, Qt.Key_G, Qt.Key_H, Qt.Key_I, Qt.Key_J, Qt.Key_K, Qt.Key_L, Qt.Key_M, Qt.Key_N, Qt.Key_O, Qt.Key_P, Qt.Key_Q, Qt.Key_R, Qt.Key_S, Qt.Key_T, Qt.Key_U, Qt.Key_V, Qt.Key_W, Qt.Key_X, Qt.Key_Y, Qt.Key_Z, Qt.Key_BracketLeft, Qt.Key_Backslash, Qt.Key_BracketRight, Qt.Key_AsciiCircum, Qt.Key_Underscore, Qt.Key_QuoteLeft, Qt.Key_BraceLeft, Qt.Key_Bar, Qt.Key_BraceRight, Qt.Key_AsciiTilde, ] 

            if key in printable: 
                return True 
            else: 
                return False 

        self.ctrl = False
        
        if e.modifiers() & Qt.ControlModifier: 
            self.ctrl = True
        elif e.key() in [Qt.Key_Return, Qt.Key_Enter]: 
            self.savebtn()
        if e.modifiers() & Qt.ShiftModifier: 
            print("수직:",self.scrollArea2.verticalScrollBar().value())
            print("수평:",self.scrollArea2.horizontalScrollBar().value())
            print("줌 레벨:",self.zoom_level)
        if e.key() == 50:
            if self.count == 1:
                self.point_1=QtCore.QPoint(self.point_1.x(),self.point_1.y()+5)
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)
                painter.drawPoint(self.point_1.x()-24,self.point_1.y()-141)
                self.label_4.setText("첫번째좌표 : ("+str(int(self.point_1.x()-24))+", "+str(int(self.point_1.y()-141))+")")
                self.label_picture.setPixmap(self.pixmap)

            elif self.count == 2:
                self.point_2=QtCore.QPoint(self.point_2.x(),self.point_2.y()+5)
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)
                painter.drawPoint(self.point_2.x()-24,self.point_2.y()-141)
                self.label_5.setText("두번째좌표 : ("+str(int(self.point_2.x()-24))+", "+str(int(self.point_2.y()-141))+")")
                self.label_picture.setPixmap(self.pixmap)

            elif self.count == 3:
                self.point_3=QtCore.QPoint(self.point_3.x(),self.point_3.y()+5)
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)
                painter.drawPoint(self.point_3.x()-24,self.point_3.y()-141)
                self.label_6.setText("세번째좌표 : ("+str(int(self.point_3.x()-24))+", "+str(int(self.point_3.y()-141))+")")
                self.label_picture.setPixmap(self.pixmap)

            elif self.count == 4:
                self.point_4=QtCore.QPoint(self.point_4.x(),self.point_4.y()+5)
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)

                x_list = [self.point_1.x(),self.point_2.x(),self.point_3.x(),self.point_4.x()]
                y_list = [self.point_1.y(),self.point_2.y(),self.point_3.y(),self.point_4.y()]
        
                painter.drawLine(x_list[0]-24,y_list[0]-141,x_list[1]-24,y_list[1]-141)
                painter.drawLine(x_list[1]-24,y_list[1]-141,x_list[2]-24,y_list[2]-141)
                painter.drawLine(x_list[2]-24,y_list[2]-141,x_list[3]-24,y_list[3]-141)
                painter.drawLine(x_list[3]-24,y_list[3]-141,x_list[0]-24,y_list[0]-141)
        
                self.label_picture.setPixmap(self.pixmap)
#########################################################################################아래##############################

        elif e.key() == 52:
            if self.count == 1:
                self.point_1=QtCore.QPoint(self.point_1.x()-5,self.point_1.y())
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)
                painter.drawPoint(self.point_1.x()-24,self.point_1.y()-141)
                self.label_4.setText("첫번째좌표 : ("+str(int(self.point_1.x()-24))+", "+str(int(self.point_1.y()-141))+")")
                self.label_picture.setPixmap(self.pixmap)

            elif self.count == 2:
                self.point_2=QtCore.QPoint(self.point_2.x()-5,self.point_2.y())
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)
                painter.drawPoint(self.point_2.x()-24,self.point_2.y()-141)
                self.label_5.setText("두번째좌표 : ("+str(int(self.point_2.x()-24))+", "+str(int(self.point_2.y()-141))+")")
                self.label_picture.setPixmap(self.pixmap)

            elif self.count == 3:
                self.point_3=QtCore.QPoint(self.point_3.x()-5,self.point_3.y())
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)
                painter.drawPoint(self.point_3.x()-24,self.point_3.y()-141)
                self.label_6.setText("세번째좌표 : ("+str(int(self.point_3.x()-24))+", "+str(int(self.point_3.y()-141))+")")
                self.label_picture.setPixmap(self.pixmap)

            elif self.count == 4:
                self.point_4=QtCore.QPoint(self.point_4.x()-5,self.point_4.y())
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)

                x_list = [self.point_1.x(),self.point_2.x(),self.point_3.x(),self.point_4.x()]
                y_list = [self.point_1.y(),self.point_2.y(),self.point_3.y(),self.point_4.y()]
        
                painter.drawLine(x_list[0]-24,y_list[0]-141,x_list[1]-24,y_list[1]-141)
                painter.drawLine(x_list[1]-24,y_list[1]-141,x_list[2]-24,y_list[2]-141)
                painter.drawLine(x_list[2]-24,y_list[2]-141,x_list[3]-24,y_list[3]-141)
                painter.drawLine(x_list[3]-24,y_list[3]-141,x_list[0]-24,y_list[0]-141)
        
                self.label_picture.setPixmap(self.pixmap)
############################################################################################왼쪽#########################

        elif e.key() == 54:
            if self.count == 1:
                self.point_1=QtCore.QPoint(self.point_1.x()+5,self.point_1.y())
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)
                painter.drawPoint(self.point_1.x()-24,self.point_1.y()-141)
                self.label_4.setText("첫번째좌표 : ("+str(int(self.point_1.x()-24))+", "+str(int(self.point_1.y()-141))+")")
                self.label_picture.setPixmap(self.pixmap)

            elif self.count == 2:
                self.point_2=QtCore.QPoint(self.point_2.x()+5,self.point_2.y())
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)
                painter.drawPoint(self.point_2.x()-24,self.point_2.y()-141)
                self.label_5.setText("두번째좌표 : ("+str(int(self.point_2.x()-24))+", "+str(int(self.point_2.y()-141))+")")
                self.label_picture.setPixmap(self.pixmap)

            elif self.count == 3:
                self.point_3=QtCore.QPoint(self.point_3.x()+5,self.point_3.y())
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)
                painter.drawPoint(self.point_3.x()-24,self.point_3.y()-141)
                self.label_6.setText("세번째좌표 : ("+str(int(self.point_3.x()-24))+", "+str(int(self.point_3.y()-141))+")")
                self.label_picture.setPixmap(self.pixmap)

            elif self.count == 4:
                self.point_4=QtCore.QPoint(self.point_4.x()+5,self.point_4.y())
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)

                x_list = [self.point_1.x(),self.point_2.x(),self.point_3.x(),self.point_4.x()]
                y_list = [self.point_1.y(),self.point_2.y(),self.point_3.y(),self.point_4.y()]
        
                painter.drawLine(x_list[0]-24,y_list[0]-141,x_list[1]-24,y_list[1]-141)
                painter.drawLine(x_list[1]-24,y_list[1]-141,x_list[2]-24,y_list[2]-141)
                painter.drawLine(x_list[2]-24,y_list[2]-141,x_list[3]-24,y_list[3]-141)
                painter.drawLine(x_list[3]-24,y_list[3]-141,x_list[0]-24,y_list[0]-141)
        
                self.label_picture.setPixmap(self.pixmap)       
################################################################################################오른쪽###################

        elif e.key() == 56:
            if self.count == 1:
                self.point_1=QtCore.QPoint(self.point_1.x(),self.point_1.y()-5)
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)
                painter.drawPoint(self.point_1.x()-24,self.point_1.y()-141)
                self.label_4.setText("첫번째좌표 : ("+str(int(self.point_1.x()-24))+", "+str(int(self.point_1.y()-141))+")")
                self.label_picture.setPixmap(self.pixmap)

            elif self.count == 2:
                self.point_2=QtCore.QPoint(self.point_2.x(),self.point_2.y()-5)
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)
                painter.drawPoint(self.point_2.x()-24,self.point_2.y()-141)
                self.label_5.setText("두번째좌표 : ("+str(int(self.point_2.x()-24))+", "+str(int(self.point_2.y()-141))+")")
                self.label_picture.setPixmap(self.pixmap)

            elif self.count == 3:
                self.point_3=QtCore.QPoint(self.point_3.x(),self.point_3.y()-5)
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)
                painter.drawPoint(self.point_3.x()-24,self.point_3.y()-141)
                self.label_6.setText("세번째좌표 : ("+str(int(self.point_3.x()-24))+", "+str(int(self.point_3.y()-141))+")")
                self.label_picture.setPixmap(self.pixmap)

            elif self.count == 4:
                self.point_4=QtCore.QPoint(self.point_4.x(),self.point_4.y()-5)
                self.pixmap = QPixmap(self.label_forder.text()+"/"+self.label_imname.text())
                self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
                painter = QtGui.QPainter(self.pixmap)
                pen = QPen(QtGui.QColor(255,0,0),5)
                painter.setPen(pen)

                x_list = [self.point_1.x(),self.point_2.x(),self.point_3.x(),self.point_4.x()]
                y_list = [self.point_1.y(),self.point_2.y(),self.point_3.y(),self.point_4.y()]
        
                painter.drawLine(x_list[0]-24,y_list[0]-141,x_list[1]-24,y_list[1]-141)
                painter.drawLine(x_list[1]-24,y_list[1]-141,x_list[2]-24,y_list[2]-141)
                painter.drawLine(x_list[2]-24,y_list[2]-141,x_list[3]-24,y_list[3]-141)
                painter.drawLine(x_list[3]-24,y_list[3]-141,x_list[0]-24,y_list[0]-141)
        
                self.label_picture.setPixmap(self.pixmap)
################################################################################################위에###################

    def close_application(self):
        print("종료")
        sys.exit()    

    def admin(self):
        self.window = Password(self)
        self.window.show()
        
    def doit(self):
        self.window = ChildWindow(self)
        self.window.show()

    def doit2(self):
        self.window = ChildWindow2(self)
        self.window.show()

    def doit3(self):
        try:
            self.tableWidget.removeRow(self.tableWidget.currentItem().row())
            
            itemsTextList = []

            for i in range(self.tableWidget.rowCount()):
                itemsTextList.append(str(self.tableWidget.item(i,0).text()))

            f = open('data.csv', 'w', encoding='utf-8', newline='')
            wr = csv.writer(f)
            for i in range(0,len(itemsTextList)):
                temp=[]
                temp.append(itemsTextList[i])
                wr.writerow(temp)
            f.close()
            
        except:
            QMessageBox.about(self,"warning","행을 선택 해주세요")

    def zoomin(self):
        self.pixmap = self.pixmap.scaled(1.25*self.pixmap.width(),1.25*self.pixmap.height())
        self.label_picture.setPixmap(self.pixmap)
        self.zoom_level = self.zoom_level + 1 

    def zoomout(self):
        if(0.8*self.pixmap.width() > 800):
            self.pixmap = self.pixmap.scaled(0.8*self.pixmap.width(), 0.8*self.pixmap.height())
            self.label_picture.setPixmap(self.pixmap)
            self.zoom_level = self.zoom_level - 1
        else:
            self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
            self.label_picture.setPixmap(self.pixmap)
            self.zoom_level = 0

    def original_picture(self):
        folder = self.label_forder.text()
        name = self.label_imname.text()
        self.pixmap = QPixmap(folder+"/"+name)
        self.pixmap = self.pixmap.scaled(800, 450, QtCore.Qt.KeepAspectRatio)
        self.label_picture.resize(self.pixmap.width(),self.pixmap.height())
        self.label_picture.setPixmap(self.pixmap)
        self.zoom_level = 0

##################################################################자식윈도우 class

class ChildWindow(QtWidgets.QMainWindow,Ui_Form):
    def __init__(self, parent):
        super(ChildWindow, self).__init__(parent)
        self.setupUi(self)
        
    def addLabeling(self):
        #try:
        rowcount = self.parent().tableWidget.rowCount()+1
        self.parent().tableWidget.setRowCount(rowcount)

        labeling_name = str(self.lineEdit.text())
        additems = [labeling_name]
        item = QTableWidgetItem(additems[0])
        item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        self.parent().tableWidget.setItem(rowcount-1, 0, item)
        itemsTextList =  []
        for i in range(self.parent().tableWidget.rowCount()):
            itemsTextList.append(str(self.parent().tableWidget.item(i,0).text()))

        f = open('data.csv', 'w', encoding='utf-8', newline='')
        wr = csv.writer(f)
        for i in range(0,len(itemsTextList)):
            temp=[]
            temp.append(itemsTextList[i])
            wr.writerow(temp)
        f.close()

        self.close()
        self.parent().show()
        #except:
            #QMessageBox.about(self,"warning","레이블이름을 적어주세요")
##################################################################자식윈도우 class2

class ChildWindow2(QtWidgets.QMainWindow,Ui_Form2):
    def __init__(self, parent):
        super(ChildWindow2, self).__init__(parent)
        self.setupUi(self)
        
        self.comboBox.addItems(["입력값", "파싱값"])
        
        self.comboBox.currentTextChanged.connect(self.change)

        self.radiobtn_state = 0
    
    def change(self):
        parsing = ["날짜","id","차선","속도","레이더파워","화이트밸런스"]
        if("파싱값" == self.comboBox.currentText()):
            self.comboBox_2.clear()
            self.comboBox_2.addItems(parsing)
        elif("입력값" == self.comboBox.currentText()):
            inputvalues = []
            self.comboBox_2.clear()
            for i in range(self.parent().tableWidget.rowCount()):
                inputvalues.append(str(self.parent().tableWidget.item(i,0).text()))
            self.comboBox_2.addItems(inputvalues)
    
    def adddivtype(self):
        typename = self.comboBox_2.currentText()
        typevalue = self.lineEdit.text()
        rowcount = self.tableWidget.rowCount()
        
        self.tableWidget.setRowCount(rowcount+1)
        
        item = QTableWidgetItem(typename)
        item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        self.tableWidget.setItem(rowcount, 0, item)
        
        item = QTableWidgetItem(typevalue)
        item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        self.tableWidget.setItem(rowcount, 1, item)

    def subdivtype(self):
        try:
            self.tableWidget.removeRow(self.tableWidget.currentItem().row())
        except:
            QMessageBox.about(self,"warning","행을 선택 해주세요")
            
    def creatediv(self):
        #폴더생성
        name =""
        for i in range(0,self.tableWidget.rowCount()):
            if(i==0):
                name = name+self.tableWidget.item(i,0).text()
            else:
                if(self.radiobtn_state == 1):
                    name = name+"and"+self.tableWidget.item(i,0).text()
                elif(self.radiobtn_state == 2):
                    name = name+"or"+self.tableWidget.item(i,0).text()

        newpath = self.parent().label_forder.text()+"/"+name 

        try:
            os.makedirs(newpath)
        except OSError:
            pass
        #xml파일리스트 추출
        try:
            folder = self.parent().label_forder.text()
            file_list = os.listdir(folder)
            file_list.sort()
            xml_list = []
                    
            for i in range(0,len(file_list)):
                if('xml' in file_list[i]):
                    xml_list.append(file_list[i])       
            
        except:
            pass
        
        path = self.parent().label_forder.text()
        
        for i in range(0,len(xml_list)):
            name = xml_list[i]
            tree = parse(path+"/"+name)
            note = tree.getroot()

            for child in note:
                for c in child:
                    for j in range(0,self.tableWidget.rowCount()):
                        if(c.tag == self.tableWidget.item(j,0).text()):
                            print(c.tag)
                            if(c.text == self.tableWidget.item(j,1).text()):
                                print(c.text)
                                xml_list.append(name)
        
        last = {}
        for xml in xml_list:
            try: 
                last[xml] +=1
            except:
                last[xml] = 1

        for i in range(0,len(last)):
            name_list = list(last.keys())
            count_list = list(last.values())
            if(self.radiobtn_state == 1):
                if(count_list[i]== self.tableWidget.rowCount()+1):
                    shutil.copyfile( path+"/"+name_list[i], newpath+"/"+name_list[i] )
                    shutil.copyfile( path+"/"+name_list[i].split(".xml")[0]+".jpg", newpath+"/"+name_list[i].split(".xml")[0]+".jpg" )
            elif(self.radiobtn_state == 2):
                if(count_list[i]== self.tableWidget.rowCount()):
                    shutil.copyfile( path+"/"+name_list[i], newpath+"/"+name_list[i] )
                    shutil.copyfile( path+"/"+name_list[i].split(".xml")[0]+".jpg", newpath+"/"+name_list[i].split(".xml")[0]+".jpg" )
        print(last)

    def btnstate(self):
        if self.radiobtn_1.isChecked() == True:
            self.radiobtn_state = 1
            print(self.radiobtn_1.text()+" is selected")
            
        if self.radiobtn_2.isChecked() == True:
            self.radiobtn_state = 2
            print(self.radiobtn_2.text()+" is selected")
            
#############################################################################################################

class Password(QtWidgets.QMainWindow,Ui_Form3):
    def __init__(self, parent):
        super(Password, self).__init__(parent)
        self.setupUi(self)
        
    def passwordcheck(self):

        if(self.lineEdit.text() == "1234"):
            if(self.parent().flag == 0):
                self.close()
                self.parent().action_0.setText("관리자 모드 설정")
                self.parent().action_1.setEnabled(True)
                self.parent().action_2.setEnabled(True)
                self.parent().action_4.setEnabled(True)
                self.parent().flag = 1
            elif(self.parent().flag == 1):
                self.close()
                self.parent().action_0.setText("관리자 모드 해제")
                self.parent().action_1.setEnabled(False)
                self.parent().action_2.setEnabled(False)
                self.parent().action_4.setEnabled(False)
                self.parent().flag = 0

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())

