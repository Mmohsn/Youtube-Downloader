from  PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import os
import pytube
from os import path
import urllib.request
import sys
import pafy
import youtube_dl
import humanize
import threading
import PyQt5.sip
from ui import Ui_MainWindow

class MainApp(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
     super(MainApp,self).__init__(parent)
     QMainWindow.__init__(self)
     self.setupUi(self)
     self.Handel_UI()
     self.Buttons12()
     self.buttons1()

    def Handel_UI(self):      #Self = QMainWindow
        self.setWindowTitle('MM Downloader')
        self.setFixedSize(841,611)

    # ------------------------------------------------------------------------------------#

    def Buttons12(self):
        self.pushButton_7.clicked.connect(self.get_video)
        self.pushButton_6.clicked.connect(self.video_download)
        self.pushButton_9.clicked.connect(self.browse)
        self.pushButton_5.clicked.connect(self.playlist_download)
        self.pushButton_11.clicked.connect(self.stop)
        self.pushButton_12.clicked.connect(self.stop1)
        self.pushButton_20.clicked.connect(self.browse2)
        self.pushButton_22.clicked.connect(self.audio_download)
        self.pushButton_19.clicked.connect(self.get_audio)
        self.pushButton_21.clicked.connect(self.stop2)


    # ------------------------------------------------------------------------------------#

    def browse(self):
        save2 = QFileDialog.getExistingDirectory(self , "Select Download Path")
        self.lineEdit_6.setText(save2)

    #------------------------------------------------------------------------------------#
    def browse1(self):
        save2 = QFileDialog.getExistingDirectory(self, "Select Download Path")
        self.lineEdit_8.setText(save2)
    # ------------------------------------------------------------------------------------#
    def browse2(self):
        save2 = QFileDialog.getExistingDirectory(self, "Select Download Path")
        self.lineEdit_14.setText(save2)
    # ------------------------------------------------------------------------------------#

    def buttons1(self):
        self.pushButton_10.clicked.connect(self.browse1)


    # ------------------------------------------------------------------------------------#

    def video_progressbar(self, total, recvd, ratio, rate, eta):
                self.progressBar_2.setValue(ratio * 100)
                QApplication.processEvents()
    # ------------------------------------------------------------------------------------#
    def video_progressbar1(self, total, recvd, ratio, rate, eta):
                self.progressBar.setValue(ratio * 100)
                QApplication.processEvents()

    # ------------------------------------------------------------------------------------#
    def audio_progressbar5(self, total, recvd, ratio, rate, eta):
                self.progressBar_5.setValue(ratio * 100)
                QApplication.processEvents()
    # ------------------------------------------------------------------------------------#


    def vv(self):
        if len(self.lineEdit_5.text()) == 0:
            QMessageBox.warning(self , "Enter URL")

    def get_video(self):
        video_link = self.lineEdit_5.text()
        v = pafy.new(video_link)
        st = v.videostreams
        for s in st:
             size = humanize.naturalsize(s.get_filesize())
             data ='{} {} {} {}'.format( s.mediatype , s.extension , s.quality , size)
             self.comboBox_3.addItem(data)
    def video_download(self):
            video_link = self.lineEdit_5.text()
            save_location = self.lineEdit_6.text()
            v  = pafy.new(video_link)
            st = v.getbest(preftype="mp4")
            quality = self.comboBox_3.currentIndex()
            download = st.download(filepath=save_location, callback=self.video_progressbar)
            QMessageBox.information(self, "Download Completed" , "The Video Download Finished")


    # ------------------------------------------------------------------------------------#

    def playlist_download(self):
        playlist_url = self.lineEdit_7.text()
        save_location = self.lineEdit_8.text()

        if playlist_url == str(""):
            QMessageBox.warning(self, "Error", "please enter url")
        playlist = pafy.get_playlist(playlist_url)
        videos = playlist['items']

        os.chdir(save_location)

        if os.path.exists(str(playlist['title'])):
           os.chdir(str(playlist['title']))
        else:
           os.mkdir(str(playlist['title']))
           os.chdir(str(playlist['title']))

        for video in videos:
            p = video ['pafy']
            best = p.getbest(preftype='mp4')
            best.download(callback=self.video_progressbar1)
            QMessageBox.information(self, "Download Completed" , "The Playlist Download Finished")

    def stop(self):
            self.playlist_download.pause = True
            QApplication.processEvents()

    def stop1(self):
            self.video_download.pause = True
            QApplication.processEvents()


    def stop2(self):
            self.audio_download.pause = True
            QApplication.processEvents()
#-----------------------------------------------------------------------------#
    def v(self):
        if len(self.lineEdit_13.text()) == 0:
            QMessageBox.warning(self , "Enter URL")

    def get_audio(self):
        audio_link = self.lineEdit_13.text()
        v = pafy.new(audio_link)
        st = v.audiostreams
        for s in st:
             size = humanize.naturalsize(s.get_filesize())
             data ='{} {} {}'.format( s.mediatype , s.extension , size)
             self.comboBox_5.addItem(data)
    def audio_download(self):
            audio_link = self.lineEdit_13.text()
            save_location = self.lineEdit_14.text()
            v  = pafy.new(audio_link)
            st = v.getbestaudio()
            quality = self.comboBox_5.currentIndex()
            download = st.download(filepath=save_location, callback=self.audio_progressbar5)
            QMessageBox.information(self, "Download Completed" , "The Video Download Finished")




def main():
        app=QApplication(sys.argv)
        window = MainApp()
        window.show()
        app.exec()
if __name__ == '__main__':
     main()
