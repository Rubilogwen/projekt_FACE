import telebot
import requests
import pickle
import cv2

with open('known_faces.dat', 'rb') as face_data_file:
    known_face_encodings, known_face_metadata = pickle.load(face_data_file)

face_number_dat = str(len(known_face_metadata))



bot = telebot.TeleBot('1888888:AAhh9S2qAPt9-CSyA0maGcNofhhhU3xo')

img = open('image-1.PNG', 'rb')
URL ='https://api.telegram.org/bot'
TOKEN= '888888:AAE9S2qAPt9-CSyA0maGcNofKhhqyWU3xo'
my_id = "8888888"
chat_id= "8888888"
def send_message(chat_id, text):
    requests.get(f'{URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={text}')

def send_photo_file(chat_id, img):
    files = {'photo': open(img, 'rb')}
    requests.post(f'{URL}{TOKEN}/sendPhoto?chat_id={chat_id}', files=files)



# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Лиц в базе " + face_number_dat)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id,  message.text)
    frame= known_face_metadata[int(message.text)]['face_image']
    cv2.imwrite('C:\\Users\Logwen\\PycharmProjects\\pythonProject3\\1022.png', frame)
    send_photo_file(my_id, 'C:\\Users\\Logwen\\PycharmProjects\\pythonProject3\\1022.png')
# Запускаем бота
bot.polling(none_stop=True, interval=0)



