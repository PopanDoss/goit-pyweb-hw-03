from threading import Thread
import logging
from time import sleep
import os 
import shutil

class MyThread(Thread):
    def __init__(self, directory, final_directory):
        super().__init__()
        self.directory = directory
        self.final_directory = final_directory

    def copy_file(self):
        try:
            path, file_extension = os.path.splitext(self.directory)
            sub_directory = os.path.join(self.final_directory,"dist" ,file_extension)
            os.makedirs(sub_directory, exist_ok=True)
            shutil.copy2(self.directory, sub_directory)
        except Exception as e:
            logging.info(f"Виникла помилка при копіюванні: {e}")

    def run(self):
        sleep(2)
        
        logging.info(f"Початок копіювання файлу")
        self.copy_file()
        logging.info(f"Копіювання файлу закінчено ")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')
    directory = "C:\\Users\\PC\\Desktop\\g"
    final_directory = "D:\\Test"
    threads = []
    count = 0

    for path, _, files in os.walk(directory):

        for file in files:
            file_path = os.path.join(path, file)
            thread = MyThread(file_path, final_directory)
            thread.start()
            threads.append(thread)
            count +=1
            
    
    [el.join() for el in threads]

    logging.info(f"Зкопійовано файлі: {count} ")

    
    
    