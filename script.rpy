﻿# Вы можете расположить сценарий своей игры в этом файле.

# Объявляйте изображения здесь, используя оператор image.
image bg img2 = "img2.jpeg"

# Определение персонажей игры.
define v1 = Character('Мужской голос', color="#c8ffc8")

define v2 = Character('Женский голос', color="#c8ffc8")

define v3 = Character('Голос из твоей головы', color="#c8ffc8")

define me = Character('Хиккару', color="#c8ffc8")

define sak = Character('Сакура', color="#c8ffc8")

define mis = Character('Мисато', color="#c8ffc8")

define meg = Character('Мэгуми', color="#c8ffc8")

define kao = Character('Каору', color="#c8ffc8")

define asu = Character('Асука', color="#c8ffc8")

define doc = Character('Врач-психиатр', color="#c8ffc8")

define nur = Character('Медсестра', color="#c8ffc8")

# Игра начинается здесь.
label start:
    
    with fade
    
    play music "gin.ogg"

    me "Я не знаю, кто я, и как я здесь оказался. Я не помню ничего, что могло бы прояснить мою память"
    
    me "Кто я? Где я? Что здесь происходит?"
    
    v1 "Сестра, дефибрилятор! Мы теряем его!"

    v2 "Дефибриляторы готовы"
    
    v1 "По моей команде: 3-2-1. Начали!"
    
    me "Мое тело поразил удар тока. Надеюсь, я очнусь, и эти люди ответят на мои вопросы"
    
    v3 "На самом деле он находится не в клинике. Точнее, чисто юридически, в клинике, но немного *другого* профиля" 
    
    v3 "Хочешь ли ты пройти по длинной и запутанной тропинке его истории или сразу же свернешь к финалу?" 
    
    menu:

        "... Да, веди меня за собой":

            jump yesido

        "... Нет уж, спасибо":

            jump noidont


label yesido:
    
    play music "alt.ogg"
    
    v3 "Ну вот и славно. Сейчас я расскажу тебе. Возможно, у тебя все еще есть возможность ему помочь"
    v3 "Все началось не так давно"
    v3 "Самый обыкновенный японский школьник оказался в своеобразном *доме отдыха*"
    v3 "Точнее, в психиатрической клинике"
    v3 "После аварии, в которую он попал вместе с родителями, его стало беспокоить ощущение, что таких реальностей, как эта, бесконечно много"
    v3 "И в каждой из них есть свой Хиккару"
    v3 "И с каждым из них он мечтает познакомиться"
    v3 "И мечтает остаться в той из реальностей, в которой его родители все еще живы"
    v3 "Как бы это не было цинично, но эти самые *реальности* - лишь плоды его воспаленного разума"
    v3 "Но не будем о грустном"
    v3 "Ха-ха, нае**л. Вся эта история насквозь пропитана грустью. А ты думал /-а/, что в графических романах есть только картиночки с лолями на пофапать?"
    v3 "Если да - смело жми Alt+f4/Cmd+Q или вводи в консоли xkill thisgame && purge thisgame && sudo -rm rf"
    v3 "О, я надеюсь, у тебя хватило ума не прописывать -rm rf из-под рута"
    v3 "Хотя, если бы ты это сделал, то уже не читал бы"
    v3 "И даже не пытайся сделать это сейчас" 
    
    me "Очередное серое и угрюмое утро застало меня спокойно сидящим на скамейке близ корпуса"
    me "Нужно возвращаться в палату. Если меня не застанут там при утреннем обходе, то ничем хорошим это не закончится"
    me "На самом деле надоело каждую ночь сбегать и бродить по округе"
    me "По этому парку, который я и днем вижу черезчур часто"
    me "По этому серпантину из прогулочных дорожек, каждая из которых успела осточертеть мне за столько лет"
    me "Ах да, сколько я здесь?"
    me "Я уже и не вспомню"
    
    sak "Хиккару-кун, Хиккару-кун"
    
    me "Да, Сакура, чем могу помочь?"
    
    sak "А помнишь, год назад, когда мы любили друг друга..."
    
    me "Не начинай снова, пожалуйста"
    me "Времена меняются"
    
    sak "Ну уж нет, давай поговорим об этом!"
    sak "Меня волнует твое безразличие ко всему происходящему"
    
    menu:

        "Да какое может быть различие во всем происходящем вокруг?":

            jump donttalksak

        "Хорошо, давай обсудим, хотя я очень не хочу к этому возвращаться":

            jump talksak

label talksak:
    
    sak "Расскажи, что ты чувствуешь?"
    
    return
    
label donttalksak:
    
    play music "gin.ogg"
    
    sak "Уходи, уходи и не попадайся мне на глаза!"
    
    v3 "Ему ничего не оставалось, кроме как уйти подальше от этой странной девочки, руки которой были обмотаны медицинскими бинтами"
    v3 "Даже здесь, в клинике, в которой, казалось бы, за пациентами ведется круглосуточное наблюдение, ей удавалось снова и снова пытаться вскрыть себе вены"
    v3 "Ему было жалко Сакуру"
    v3 "Но он не мог пересилить себя и заговорить с ней об их совместном прошлом"
    
    return
    
label noidont:
    
    
    
    v3 "История этого парнишки так и осталась неизвестной"
    v3 "Он скончался на том операционном столе"
    v3 "Ты мог спасти его"
    v3 "Но ты предпочел не вмешиваться"
    v3 "Я не виню тебя в его смерти"
    v3 "В конечном счете, это всего лишь игра"
    v3 "И, как и в любой другой игре, здесь есть начало и есть конец"
    v3 "Прощай"
    v3 "Game Over"

    return
