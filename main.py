###imports
import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QSizeGrip,QGraphicsDropShadowEffect, QTableWidgetItem
from PyQt5.QtCore import *
from PySide2 import QtCore, QtGui
from PySide2.QtCore import QRunnable, Slot, QThreadPool

###import GUI file
from interface import *

import psutil
import datetime
import platform
import shutil
from PySide2extn import *
from qt_material import *
from time import sleep

from multiprocessing import cpu_count


class WorkerSignals(QObject):
    finished = Signal()
    error =Signal(tuple)
    result = Signal(object)
    progress = Signal(int)
class Worker(QRunnable):
    def __init__(self, fn,*args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs["progress_callback"] = self.signals.progress

    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback, format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()    





class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.header_frame.installEventFilter(self)
     
        ###applying theme
        apply_stylesheet(app, theme='dark_cyan.xml')
        ###removing tittle bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        ###setting main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ###shadow effect style
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        ###set window tittle && icon
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/airplay.svg"))
        self.setWindowTitle("System Monitor By Reda")
        
        ###setting up custom tittle bar buttons
        self.ui.close_window_button.clicked.connect(lambda : self.close())
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        self.ui.restore_window_button.clicked.connect(lambda: self.restore())


        QSizeGrip(self.ui.size_grip)

        ### navigation
        self.ui.cpu_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cpu_and_memory))
        self.ui.activity_page_btn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.activity))
        self.ui.battery_apge_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.battery))
        self.ui.system_info_page_btn.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.system))
        self.ui.storage_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.storage))
        
        ### side menu animation
        self.ui.menuButton.clicked.connect(lambda:self.slideLeftMenu())

        ### apply style to side menu buttons when clickde
        for button in self.ui.menu_frame.findChildren(QPushButton):
            #add click event listener
            button.clicked.connect(self.applyButtonStyle)
            
        
        self.threadpool = QThreadPool()
        self.show()
        self.processes()
        #self.battery()
        self.system_info()
        #self.cpu_ram()
        self.storage()

        self.psutil_thread()
        


    def psutil_thread(self):
        worker = Worker(self.cpu_ram)

        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        self.threadpool.start(worker)

        battery_worker = Worker(self.battery)

        battery_worker.signals.result.connect(self.print_output)
        battery_worker.signals.finished.connect(self.thread_complete)
        battery_worker.signals.progress.connect(self.progress_fn)

        self.threadpool.start(battery_worker)

    def print_output(self, s):
        print(s)
    def thread_complete(self):
        print("THREAD COMPLETED")
    def progress_fn(self, n):
        print("%d%% DONE" % n)        


    def storage(self):
        storage_device = psutil.disk_partitions(all=False)
        z = 0
        for device in storage_device:
            rowPos = self.ui.storage_table.rowCount()
            self.ui.storage_table.insertRow(rowPos)
            self.create_table_widget(rowPos, 0, device.device, "storage_table")
            self.create_table_widget(rowPos, 1, device.mountpoint, "storage_table")
            disk_usage = shutil.disk_usage(device.mountpoint) 
            self.create_table_widget(rowPos, 2, str("{:.2f}".format(disk_usage.total/(1024*1024*1024))) + " GB", "storage_table")   
            self.create_table_widget(rowPos, 3, str("{:.2f}".format(disk_usage.used/(1024*1024*1024))) + " GB", "storage_table")   
            self.create_table_widget(rowPos, 4, str("{:.2f}".format(disk_usage.free/(1024*1024*1024))) + " GB", "storage_table")
            used_storage_percentage =   (disk_usage.used/disk_usage.total)*100
            used_storage_bar = QProgressBar()
            used_storage_bar.setObjectName(u"used_storage_progressBar")
            used_storage_bar.setMaximum(100)
            used_storage_bar.setValue(used_storage_percentage)
            self.ui.storage_table.setCellWidget(rowPos, 5, used_storage_bar)
             
            


    def create_table_widget(self, rowPos, columnPos, text,tableName):
        qtableWidgetItem = QTableWidgetItem()
        getattr(self.ui, tableName).setItem(rowPos, columnPos, qtableWidgetItem)
        qtableWidgetItem = getattr(self.ui, tableName).item(rowPos, columnPos)
        qtableWidgetItem.setText(text)

    def restore(self):
        ### if window is maximized(full screen) then show normal size window
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(":/icons/icons/square.svg"))
        ### else switch to full screen
        else:
            self.showMaximized() 
            self.ui.restore_window_button.setIcon(QtGui.QIcon(":/icons/icons/circle.svg"))


    def slideLeftMenu(self):
        width = self.ui.left_menu_cont_frame.width()
        if width == 40:
            newWidth = 200
        else:
            newWidth = 40
        self.animation = QPropertyAnimation(self.ui.left_menu_cont_frame, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()



    def applyButtonStyle(self):
        for button in self.ui.menu_frame.findChildren(QPushButton):
            # compare the actual iterated button with the clicked button
            if button.objectName != self.sender().objectName():
                # no style
                button.setStyleSheet("border-bottom : none;")

            self.sender().setStyleSheet("background-color:#838ea2 ;")   

    def battery(self, progress_callback):
        while True:
            batt = psutil.sensors_battery()  
            if not hasattr(psutil, 'sensors_battery'):
                self.ui.battery_status.setText("Platform not supported")
            if batt == None :
                self.ui.battery_status.setText("No battery installed")
            if batt.power_plugged :
                self.ui.battery_charge.setText(str(round(batt.percent,2))+"%")  
                if batt.percent<100:
                    self.ui.battery_status.setText("Charging")
                else:
                    self.ui.battery_status.setText("Fully Charged")
                self.ui.plugged_in.setText("Yes")
            else:
                self.ui.battery_charge.setText(str(round(batt.percent,2))+"%")
                self.ui.battery_status.setText("Discharging")
                self.ui.plugged_in.setText("No")
            #battery power indicator using round progress bar
            #set progress bar values
            self.ui.battery_usage.rpb_setMaximum(100) 
            self.ui.battery_usage.rpb_setValue(batt.percent)
            self.ui.battery_usage.rpb_setBarStyle("Hybrid2") 
            self.ui.battery_usage.rpb_setLineColor((255,30,99))  
            self.ui.battery_usage.rpb_setPieColor((45,74,83))
            self.ui.battery_usage.rpb_setTextColor((255,255,255))
            self.ui.battery_usage.rpb_setInitialPos("West")
            self.ui.battery_usage.rpb_setTextFormat("Percentage")
            self.ui.battery_usage.rpb_setLineWidth(15)
            self.ui.battery_usage.rpb_setPathWidth(15)
            self.ui.battery_usage.rpb_setLineCap("RoundCap")
            sleep(1)


    def cpu_ram(self, progress_callback):
        while True :
        
            totalRam = 1.0
            totalRam = psutil.virtual_memory()[0] * totalRam
            totalRam = totalRam / (1024 * 1024 * 1024)
            self.ui.total_ram.setText(str("{:.2f}".format(totalRam)) + " GB")

            availRam = 1.0
            availRam = psutil.virtual_memory()[1] * availRam
            availRam = availRam / (1024 * 1024 * 1024) 
            self.ui.available_ram.setText(str("{:.2f}".format(availRam)) + " GB")

            usedRam = 1.0
            usedRam = psutil.virtual_memory()[3] * usedRam
            usedRam = usedRam / (1024 * 1024 * 1024) 
            self.ui.used_ram.setText(str("{:.2f}".format(usedRam)) + " GB")


            freeRam = 1.0
            freeRam = psutil.virtual_memory()[4] * freeRam
            freeRam = freeRam / (1024 * 1024 * 1024) 
            self.ui.free_ram.setText(str("{:.2f}".format(freeRam)) + " GB")  

            core = cpu_count()
            self.ui.cpu_count.setText(str(core))
            cpuPer = psutil.cpu_percent()
            self.ui.cpu_usage_2.setText(str(cpuPer)+"%")
            cpuMainCore = psutil.cpu_count(logical = False)
            self.ui.main_cores.setText(str(cpuMainCore))



            self.ui.cpu_usage.rpb_setMaximum(100)
            self.ui.cpu_usage.rpb_setValue(cpuPer)
            self.ui.cpu_usage.rpb_setBarStyle("Hybrid2") 
            self.ui.cpu_usage.rpb_setLineColor((255,30,99))  
            self.ui.cpu_usage.rpb_setPieColor((45,74,83))
            self.ui.cpu_usage.rpb_setTextColor((255,255,255))
            self.ui.cpu_usage.rpb_setInitialPos("West")
            self.ui.cpu_usage.rpb_setTextFormat("Percentage")
            self.ui.cpu_usage.rpb_setLineWidth(15)
            self.ui.cpu_usage.rpb_setPathWidth(15)
            self.ui.cpu_usage.rpb_setLineCap("RoundCap")


            self.ui.ram_usage.spb_setMinimum((0,0,0))
            self.ui.ram_usage.spb_setMaximum((totalRam,totalRam,totalRam))
            self.ui.ram_usage.spb_setValue((availRam,usedRam,freeRam))
            self.ui.ram_usage.spb_lineColor(((6,233,38),(6,201,233),(233,6,201)))
            self.ui.ram_usage.spb_setInitialPos(("West","West","West"))
            self.ui.ram_usage.spb_setDirection(("Clockwise","Clockwise","Clockwise"))
            self.ui.ram_usage.spb_lineWidth(15)
            self.ui.ram_usage.spb_lineStyle(("SolidLine","SolidLine","SolidLine"))
            self.ui.ram_usage.spb_lineCap(("RoundCap","RoundCap","RoundCap"))
            self.ui.ram_usage.spb_setPathHidden(True)
            sleep(2)


    def system_info(self):
        time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.ui.system_time.setText(str(time))
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.ui.system_date.setText(str(date))
        self.ui.machine.setText(platform.machine())
        self.ui.op.setText(platform.system())
        self.ui.version.setText(platform.version())
        self.ui.processor.setText(platform.processor())
        self.ui.platform.setText(platform.platform())


    def processes(self):
        for x in psutil.pids():
            #create new row
            rowPos = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPos)
            try:
                process = psutil.Process(x)
                # x =column number
                self.create_table_widget(rowPos,0,str(process.pid),"tableWidget")
                self.create_table_widget(rowPos,1,process.name(),"tableWidget")
                self.create_table_widget(rowPos,2,process.status(),"tableWidget")
                self.create_table_widget(rowPos,3,str(datetime.datetime.utcfromtimestamp(process.create_time()).strftime("%Y-%m-%d %H:%M:%S")),"tableWidget")
                #create a cell widget
                #suspend button
                suspend_btn = QPushButton(self.ui.tableWidget)
                suspend_btn.setText("Suspend")
                suspend_btn.setStyleSheet("color : brown")
                self.ui.tableWidget.setCellWidget(rowPos, 4, suspend_btn)
                #resume button
                resume_btn = QPushButton(self.ui.tableWidget)
                resume_btn.setText("Resume")
                resume_btn.setStyleSheet("color : green")
                self.ui.tableWidget.setCellWidget(rowPos, 5, resume_btn)
                #terminate button
                terminate_btn = QPushButton(self.ui.tableWidget)
                terminate_btn.setText("Terminate")
                terminate_btn.setStyleSheet("color : orange")
                self.ui.tableWidget.setCellWidget(rowPos, 6, terminate_btn)
                #kill button
                kill_btn = QPushButton(self.ui.tableWidget)
                kill_btn.setText("Kill")
                kill_btn.setStyleSheet("color : red")
                self.ui.tableWidget.setCellWidget(rowPos, 7, kill_btn)
            except Exception as e:
                print(e)

            self.ui.activity_search.textChanged.connect(self.search_precesses)

    def search_precesses(self):
        name = self.ui.activity_search.text().lower()
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 1)
            self.ui.tableWidget.setRowHidden(row, name not in item.text().lower())

    ## drag main window
    def eventFilter(self, source, event):
        if source == self.ui.header_frame:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.offset = event.pos()
            elif event.type() == QtCore.QEvent.MouseMove and self.offset is not None:
                # no need for complex computations: just use the offset to compute
                # "delta" position, and add that to the current one
                self.move(self.pos() - self.offset + event.pos())
                # return True to tell Qt that the event has been accepted and
                # should not be processed any further
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.offset = None
        # let Qt process any other event
        return super().eventFilter(source, event)         

                
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())