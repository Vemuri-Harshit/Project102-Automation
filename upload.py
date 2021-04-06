import dropbox;
import time;
import cv2;
import random;

start_time = time.time();

def picture_from_webcam():
    cam = cv2.VideoCapture(0);
    result = True;
    random_num = random.randint(1, 100);

    while (result):
        ret, frame = cam.read();
        print(ret);
        random_name = 'img' + str(random_num) + '.png';
        cv2.imwrite(random_name, frame);
        start_time = time.time();
        result = False;    

    
    return random_name;
    print("PIC TAKEN")
    cam.release();
    cv2.destroyAllWindows();    

def upload_in_dropbox(random_name):
    access_Token = "2yY5ydOGtP8AAAAAAAAAATqcutPgSObOuQFeEQprcPuE4O_kltsLabCHkNEE_qzN";
    file = random_name;
    file_from = file;
    file2 = "/WhiteHatJunior_Uploads/User_Face_Picture/" + random_name;
    dbx = dropbox.Dropbox(access_Token);
    with open(file_from, 'rb') as file:
        dbx.files_upload(file.read(), file2, mode = dropbox.files.WriteMode.overwrite);
        
    print("FILE UPloaded ❓ ")

def main():
    while (True):
        if ((time.time() - start_time) >= 300):
            name = picture_from_webcam();
            upload_in_dropbox(name)

main();                                 