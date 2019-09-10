#!usr/bin/python

import mysql.connector as mysql
from mysql.connector import Error
from mysql.connector import errorcode
import cv2
import random
import os
import time

'''
#for the connection from mariadb database

def insertPythonVaribleInTable():
    try:
        conn=mysql.connect(user='karan',password='q',host='localhost',database='attendance')
        sql_lang=conn.cursor()
        sql_insert_query = """ INSERT INTO `student`
                          (`name`, `email`,  `remark`) VALUES (%s,%s,%s)"""
        insert_tuple = ()
        result= sql_lang.execute(sql_insert_query, insert_tuple)
        conn.commit()
        print ("Record inserted successfully into python_users table")
    except mysql.Error as error :
        conn.rollback()
        print("Failed to insert into MySQL table {}".format(error))
    finally:
        #closing database connection.
        if(conn.is_connected()):
            sql_lang.close()
            conn.close()
            print("MySQL connection is closed")

insertPythonVaribleInTable()
'''
os.system("ssh ubuntu@35.154.49.223 -i /home/ankit/Downloads/cloud_ubuntu_mumbai.pem ")
time.sleep(5)
os.system("sudo -i")
os.system("cd /var/www/html/image/")
os.system("mkdir premwa")

"""
face_data=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

cap=cv2.VideoCapture(0)

while cap.isOpened() :
        status,frame=cap.read()
        graying=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_data.detectMultiScale(graying,1.15,5)
        for (x,y,w,h) in faces :
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,"face",(x,y),font,3,(0,0,0),cv2.LINE_AA)
            #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(frame,(x+w/2,y+h/2),90,(0,255,0),3)
            roi_gray=graying[y:y+h,x:x+w]
            roi_color=frame[y:y+h,x:x+w]
#showing current image
        cv2.imshow("current image",frame)

        if cv2.waitKey(30) & 0xFF == ord('q') :
            break
        elif cv2.waitKey(30) & 0xFF == ord('c') :
            num=str(random.random())[2:6]
            cv2.imwrite('image'+num+'.jpg',frame)
            os.system('mv image* /home/ankit/Desktop/captured')

cv2.destroyAllWindows()
cap.release()
"""
