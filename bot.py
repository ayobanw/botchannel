import telebot
from telebot import types
from telebot import apihelper

# --- FIX UNTUK PYTHONANYWHERE FREE ACCOUNT ---

# 1. MASUKKAN DATA KAU
TOKEN = '8951237964:AAH-p4DJvwsmRkt4fE1egnfkhwjCer6rS28'
CHANNEL_ID = -1003607814655
bot = telebot.TeleBot(TOKEN)

# --- DATABASE KOD KERETA (SEBARIS KE BAWAH) ---
KOD_KERETA_1 = """🏎️ **SENARAI KOD KERETA (1-90)**
1 BMW 135I
2 VW Scirocco
3 BMW M5 2015
4 G-Wagon LAMA
5 Chevy Camaro
6 Subaru BRZ
7 Lexus LFA
8 Infiniti G36
9 Subie Stinkeye
10 Ferrari F12
11 R34 Skyline
12 Evo 10
13 EK9
14 GTR R35
15 Audi RS4
17 Merc C63
18 Lambo Huracan
19 Merc AMG GTR
20 Audi TT
21 Jeep Wrangler
22 BMW M6
23 Hyundai Veloster
24 Porsche Panamera
25 Bugatti Veyron
28 Porsche Cayenne
29 Honda FN2
30 BMW M5 99's
31 BMW M5 05's
32 Koenigsegg Agera
35 Mustang Shelby GT500
37 Ford Transit
39 Dodge Charger 70's
40 Corvette C7
41 McLaren P1
42 Aventador
43 Lexus IS300
44 Lambo Veneno
45 BMW M5 97's
47 S2000
48 RX8
49 Supra MK4
51 Ferrari Lama
53 Hakosuka GTR
54 BMW M5 80's
55 Hummer H1
56 BMW M3 E93
57 Cadillac CTS-V
58 Ferrari 458
59 Smart Fortwo
60 Escalade
61 Mercedes Siri E
62 Dodge Charger
65 Gallardo
66 Chrysler 300C
70 Lori Scania
74 Peugeot 308
76 BMW Z4
77 Mini Cooper
81 Subaru Hawkeye
82 Evo 8
85 Ford Ranger
86 BMW X5
87 Mercedes Siri C
88 Ikonik BMW M3
89 Hudson Hornet
90 Porsche 911 Lama"""

KOD_KERETA_2 = """🏎️ **SENARAI KOD KERETA (99-180)**
99 LADA
100 Kereta Rusia
101 Treler Ford
102 Kereta Rusia
103 BMW M4 F82
104 BMW M5 F90
105 Dodge Challenger
106 Mercedes Siri E Lama
107 Audi R8 V10 Lama
108 Audi Quattro
109 Porsche 911 991
110 Range Rover SVR
111 NSX Baru
112 Mercedes Siri E/C
113 Golf R MK7
114 Mercedes Siri E/S
115 Audi R8 V10 Plus Baru
116 Mustang 5.0
117 Audi S7
118 BMW X6
119 Hummer Tentera
120 Toyota Camry
121 Toyota LC200
123 Mercedes GLE
124 Rolls Royce Wraith
125 Lambo Urus
126 GMC Sierra
127 BMW M2
128 Nissan S15
129 RX7
130 Ford GT
131 Nissan 240SX
132 Kereta Rusia
133 Myvi Perodua M600
134 Toyota Chaser
135 Audi RS6
136 Mercedes Siri
137 Honda FD2
138 BMW i8
139 Crown Victoria
140 Toyota AE86
141 Dodge Viper
142 Mercedes C63
143 Mercedes G63 Baru
145 Nissan 350Z
146 Kereta Rusia
147 Honda FK8
148 Fastback Mustang
149 Kereta Lama
150 Supra MK5
151 Toyota Velfire
152 Kereta Rusia
153 BMW M4 G82
154 Toyota Hilux
155 F1 Lama
156 R32 GTR
157 Golf R MK5/4
158 Mazda MX5
159 Lambo SVJ
160 Dodge Challenger Lama
161 Jeep Cherokee
162 McLaren 720S
163 Mercedes Convertible
164 Dune Buggy
165 F1 Baru
166 Corvette C8
167 Dodge Ram
168 Bentley Continental
169 Ford Explorer
170 Lori Peterbilt
171 Lori Scania
172 Rolls Royce Cullinan
173 Mercedes Siri
175 Mercedes Siri
176 Chevy Pickup
177 Nissan S13
178 Bugatti Chiron SS
179 Chevy
180 Chevy Pickup"""

KOD_KERETA_3 = """🏎️ **SENARAI KOD KERETA (181-259)**
181 Mustang Lama
182 Lori Drift Hoonicorn
183 Mustang Drift
184 Mitsubishi Eclipse
185 Chevy Impala
186 Van Astro
187 Mazda Miata
188 Porsche GT3RS
189 Ford Raptor
190 Peugeot
191 Bas 1
192 Ram TRX
193 M3 Touring
194 Mercedes SLR
195 Bas 2
196 Dodge Charger Lama
197 VW Microbus
198 Koenigsegg Jesko
199 Corvette C6
200 Dodge Durango
201 Mercedes CLK GTR
202 Pagani Zonda
204 Van Mercedes
205 Porsche RWB
206 Alfa Romeo Giulia
207 Porsche Le Mans
208 Ford Bronco
209 Lexus IS300 2009
210 Corvette C5
211 Audi RS7
212 6x6 Mercedes G63
213 Nissan R33
214 Toyota Chaser MK2
215 Chevy Tahoe
216 McLaren Senna
217 BMW X7
218 Toyota Crown
219 VW Passat
220 Fairlady Z
221 NSX Lama
222 Porsche 918
223 DMC Delorean
224 Subaru Raptor Eye
225 Honda DelSol
226 Van Fiat
227 AMG One
228 Audi RS2
229 Ferrari F40
230 Land Rover
231 Toyota LC250 Lama
232 Kia Stinger
233 BMW i7
234 Aston Martin Baru
235 Mustang Baru
236 RV
237 Lori Semi
238 BMW M5 Baru
239 Escalade Baru
240 Ford Focus
241 LaFerrari
242 Camaro Baru
243 Jeep Gladiator
244 Land Rover Baru
245 Toyota GR Yaris
248 Kereta Rusia Baru
249 Maybach Baru
250 Porsche Carrera GT
253 FORD TURCKS BARU
257 BMW M2 BARU
259 FORTUNER BARU"""

KOD_SPOILER = """🛠️ **KOD SPOILER & BESI**
4 - Besi ampaian
5 - Bar depan
6 - Roofbox/Skybox
10 - Lampu roof
12 - Besi rack lata
13 - Host lata
14 - Roof RR
15 - Besi ford rangers
20 - Besi rack hakosuka
32 - Tire blakang jeep
33 - Besi atas jeep
34 - Besi blakang jeep
39 - Besi dalam dodge
45 - Besi atas hammer
46 - Besi blakang hilux
48 - Besi atas hilux
50 - Besi bar atas hilux
56 - Sportlight jeep
59 - Rack ford rangers
61 - Besi blakang hilux
63 - Besi blakang hilux papan
69 - Besi rack atas myvi
75 - Besi chavrolet

📍 **KOD SPOILER**
16 - Spoiler merc Amg
19 - Spoiler r35
41 - Spoiler 350z
49 - Spoiler brz
65 - Spoiler rx7
69 - Spoiler nsx
77 - Spoiler rx8
93 - Spoiler Itik
95 - Spoiler ducktail
96 - Spoiler wing
106 - Spoiler wing ek9
135 - Spoiler audi r8
148 - Spoiler ferrari
155 - Spoiler wing bmw
168 - Spoiler Evo
170 - Spoiler Lambo"""

@bot.message_handler(commands=['setup'])
def send_channel_menu(message):
    try:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("🌐 WEBSITE TOOL", url="https://anwstore.my.id")
        btn2 = types.InlineKeyboardButton("🎥 VIDEO ACC", url="https://t.me/+3xl0prkLlfI2ODll")
        btn3 = types.InlineKeyboardButton("🚗 KOD KERETA", url=f"https://t.me/{bot.get_me().username}?start=kod")
        btn4 = types.InlineKeyboardButton("🛠️ KOD SPOILER", url=f"https://t.me/{bot.get_me().username}?start=spoiler")
        # Link admin dah dibetulkan ke @ayobanw
        btn5 = types.InlineKeyboardButton("👨‍💻 CHAT ADMIN", url="https://t.me/ayobanw")

        markup.add(btn1, btn2, btn3, btn4, btn5)
        sent_msg = bot.send_message(CHANNEL_ID, "🏎️ **ANWSTORE DASHBOARD** 🏎️\nGunakan butang di bawah untuk info CPM:", reply_markup=markup, parse_mode="Markdown")
        bot.pin_chat_message(CHANNEL_ID, sent_msg.message_id)
        bot.reply_to(message, "✅ Menu kemas dah hantar ke channel!")
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {e}")

@bot.message_handler(commands=['start'])
def handle_start(message):
    if 'kod' in message.text:
        bot.send_message(message.chat.id, KOD_KERETA_1, parse_mode="Markdown")
        bot.send_message(message.chat.id, KOD_KERETA_2, parse_mode="Markdown")
        bot.send_message(message.chat.id, KOD_KERETA_3, parse_mode="Markdown")
    elif 'spoiler' in message.text:
        bot.send_message(message.chat.id, KOD_SPOILER, parse_mode="Markdown")
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add('🌐 Website Tool', '📺 Video Acc', '🚗 Kod Kereta', '🛠️ Kod Spoiler', '👨‍💻 Admin')
        bot.send_message(message.chat.id, "Sila pilih menu:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def menu_handler(message):
    if message.text == '🚗 Kod Kereta':
        bot.send_message(message.chat.id, KOD_KERETA_1, parse_mode="Markdown")
        bot.send_message(message.chat.id, KOD_KERETA_2, parse_mode="Markdown")
        bot.send_message(message.chat.id, KOD_KERETA_3, parse_mode="Markdown")
    elif message.text == '🛠️ Kod Spoiler':
        bot.send_message(message.chat.id, KOD_SPOILER, parse_mode="Markdown")
    elif message.text == '🌐 Website Tool':
        bot.send_message(message.chat.id, "🌐 **Website Tool:**\nhttps://anwstore.my.id")
    elif message.text == '📺 Video Acc':
        bot.send_message(message.chat.id, "🎥 **Video Acc:**\nhttps://t.me/+3xl0prkLlfI2ODll")
    elif message.text == '👨‍💻 Admin':
        bot.send_message(message.chat.id, "Admin: https://t.me/ayobanw")

print("Bot channel sedang berjalan...")
bot.infinity_polling()

# --- BAHAGIAN TAMBAHAN UNTUK RENDER (TAMPAL DI SINI) ---
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "ANW STORE IS ONLINE"

def run():
    app.run(host='0.0.0.0', port=8080)

t = Thread(target=run)
t.start()
# -----------------------------------------------------
bot = telebot.TeleBot("8951237964:AAH-p4DJvwsmRkt4fE1egnfkhwjCer6rS28")
# Tukar bot.polling() kepada macam ni supaya dia jalan serentak:
bot.infinity_polling(none_stop=True)
