import telebot
import requests
# import os
from pytube import YouTube 
import youtube_dl

API_KEY = "Keep your Bot Token here!!!!"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start','hi','hello'])
def start(message):
    bot.reply_to(message, f"Hello! {message.from_user.first_name} {message.from_user.last_name}, how may I help you?, ")


@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, """commands you can use:
    /start => To start the bot
    /help => To know the commands that you can use
    /weather=>To get the weather of any City
    /quote => To get a random Quote everytime
    /joke => To get a random Joke everytime
    /insultmyfriend => To get an insult comment to use on your friend
    /advice => To get an Advice
    """)



@bot.message_handler(commands=['weather'])
def search(message):
    city = message.text
    city = city.replace('/weather ','')
    city.lower()
    res = requests.get(f'https://goweather.herokuapp.com/weather/{city}')
    reg=res.json()
    temp = reg['temperature']
    wind = reg["wind"]
    comment = reg["description"]
    forecast = reg["forecast"][0]
    # data_source": "https://www.google.com/search?lr=lang_en&q=weather+in+hyderabad
    print("Temperature:",temp, "wind:",wind,comment)
    output = f"Region: {city}  \nTemperature:{temp} celcius  \nWind: {wind} Km \nComment:{comment} \n FORECAST:{forecast}"
    bot.send_message(message.chat.id,output)
    


@bot.message_handler(commands=['quote'])
def quotes(message):
    res = requests.get('https://zenquotes.io/api/random')
    quote=res.json()
    quotetext = quote[0]["q"]
    author = quote[0]["a"]
    print("QUOTE:",quotetext,"AUTHOR:",author)
    det = f"Quote: {quotetext} \n Author: {author}"
    bot.send_message(message.chat.id,det)



# @bot.message_handler(commands=['dict'])
# def dictionary(message):
#     word = message.text
#     word = word.replace('/dict ','')
#     word.lower()
#     res = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
#     reg=res.json()
#     meaning = reg[0]["meanings"][2]['definitions'][0]['definition']
    # wind = reg["wind"]

    # print("meanings:",meaning)
    # # output = f"Region: {city}  \nTemperature:{temp} celcius  \nWind: {wind} Km \nComment:{comment}"
    # bot.send_message(message.chat.id,meaning)


@bot.message_handler(commands=['joke'])
def jokes(message):
    res = requests.get('https://icanhazdadjoke.com/slack')
    joke=res.json()
    joketext = joke["attachments"][0]["fallback"]
    print("JOKE:",joketext)
    jk = f"Joke: {joketext}"
    bot.send_message(message.chat.id,jk)

@bot.message_handler(commands=['insultmyfriend'])
def Insult(message):
    res = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    insults=res.json()
    insultext = insults["insult"]
    print("Insult:",insultext)
    inst = f"For Your Friend: {insultext}"
    bot.send_message(message.chat.id,inst)

# @bot.message_handler(commands=['codechef'])
# def CodeChef(message):
#     res = requests.get('https://kontests.net/api/v1/code_chef')
#     dts=res.json()
#     cctext = dts[-1]
#     nxtext=dts[-2]
#     print("Contest dts:",cctext)
#     ccdts = f"Contest Details: {cctext}"
#     nccdts=f"Next Contest Details: {nxtext}"
#     cc=f"{ccdts}\n{nccdts}"
#     bot.send_message(message.chat.id,cc)

@bot.message_handler(commands=['advice'])
def Advice(message):
    res = requests.get('https://api.adviceslip.com/advice')
    adv=res.json()
    advtext = adv["slip"]["advice"]
    print("Advice:",advtext)
    ins = f"Advice for You: {advtext}"
    bot.send_message(message.chat.id,ins)
'''for songs 
https://pagalworld.com.se/mehbooba-mp3-song-download.html
https://pagalworld.com.se/mahbooba-mp3-song-download.html
'''

# @bot.message_handler(commands=['ytd'])
# def ytvid(message):
#     link = message.text
#     link = link.replace('/ytd ','')
#     try:  
#         yt = YouTube(link) 
#     except: 
#         print("Connection Error")

#     print("Title: ",yt.title)
#     print("Views: ",yt.views)
#     print("Length(seconds): ",yt.length)
#     #print("Average Ratings: ",yt.rating)
#     path='./YOUTB folder'
#     # Path = os.getcwd()
#     # # Path += "/ytvd"
#     try: 
#         vid = yt.streams.get_highest_resolution()
#         # vid.download(path)
#         vid.download()
#         video (link)
#     except: 
#         status=("Some Error!") 
#         print("Some Error!")
#     print('Task Completed!') 

#     outputd = f"TITLE: {yt.title} \n VIEWS: {yt.views} \nLENGTH:{yt.length} seconds \nLOCATION: path \n {status} \nTask Completed!"
#     bot.send_message(message.chat.id,outputd)





# @bot.message_handler()
# def run(message):

#     message.text

#     if "https://www.youtube.com" not in message.text:
#         print("This is not YouTube link!")
#         return

#     bot.send_message(message.chat.id, "Please wait...")
    
#     video_info = youtube_dl.YoutubeDL().extract_info(url = message.text, download=False)
#     filename = f"{video_info['title']}.mp3"
#     options={
#       'format':'bestaudio/best',
#       'keepvideo':False,
#       'outtmpl':filename,
#     }

#     with youtube_dl.YoutubeDL(options) as ydl:
#         ydl.download([video_info['webpage_url']])

#     print("Download complete... {}".format(filename))
#     bot.send_audio(message.chat.id, audio=open(filename, 'rb'))



# from pytube import YouTube 


# # Change below path to the directory where you want to store the downloaded file.
# path = '/content/sample_data'

# link= text

# video = YouTube(link)
# video = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# video_saved_path = video.download(path)
# print(video_saved_path)

# import requests

# chat_id = "<your group id>"
# token = "<your telegram bot token>"


# base_url = "https://api.telegram.org/bot2007294251:AAHX3JS_k7YKoNqm05PYPYTn0Ehcpt-UgT4/sendVideo"


# my_file = open(video_saved_path, "rb")

# parameters = { "chat_id" : "-1001608236798" }

# files = { "video" : my_file }

# resp = requests.get(base_url, data = parameters, files=files)
# print(resp.text)
    



bot.polling()
