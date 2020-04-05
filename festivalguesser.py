# -*- coding: utf-8 -*-
"""FestivalGuesser.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P73_0lh0x5Q37owUv1ZXlsIvjgzQ1P-Y
"""

#!pip install tensorflow==2.0.0
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
import numpy as np

stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

christmas = "A popular tradition in many churches is the Carol Service which is often lit only by candles. The carol service generally has lots of singing and Bible readings. There is a tradition in England which began in the Temple Church in London and has now spread to many other places for a service of Nine Lessons and Carols. The lessons are Bible readings. Some carols are sung by a choir and others by the choir and people (the congregation). Every year one of these services is recorded in a large English Church, often King's College Chapel, Cambridge, and is broadcast on radio and television to be enjoyed by people who love good music and carol singing, but particularly for people who cannot go to a Christmas service. Christmas (which means \"Feast day of Christ\") is a Christian holiday that refers to the birth of Jesus (whom Christians believe is the Son of God), and a cultural holiday for non-Christians. The day known as Christmas Day is celebrated on the 25th day of December. It is one of the most important days of the year for Christians, along with Easter when the death and resurrection of Jesus are celebrated. The season of preparing for Christmas is called Advent and begins on a Sunday about four weeks before Christmas. The Christmas Season (called Christmastide) ends 6 January or the Twelfth Day of Christmas, in which Epiphany is remembered. Christmas is celebrated all over the world, as a religious holiday or as a time of celebration by Christians and non-Christians alike. The traditions are different from country to country, but they nearly always include a feast, giving gifts or cards, and enjoying church or public festivities such as singing Christmas carols and songs. Santa Claus is a tradition in many countries of the world. Christmastide, as it is often called, is in the winter of the Northern Hemisphere, at a time when there were already ancient festivals. Some of the traditions that are used for Christmas are older than Christmas, or come from other non-Christian traditions such as Yule. Modern traditions of Christmas often focus on the giving of gifts. The season for retail stores to sell gifts, food, greeting cards, Christmas trees, and decorations begins the day about a month before Christmas Day. How many times have you thought as a child that tonight the Santa Claus will come and give gifts to you? Many times you may actually receive them although they are presents from your family. Such is the craze of Santa Claus and the gifts, Christmas trees associated with the festival of Christmas. It is a festival which attracts people of all faith towards it. Being one of those festivals which is widely celebrated all over the world, it is important for us to know about this festival we call Christmas. It does have a history to it along with some marked traditions which go along with it. In order to make students aware of all this, we have come up with long essays for students which shall enlighten them more about this festival. "+"Christmas is celebrated every year on 25th December. It is mainly the festival of Christians. But in today’s time, the festival of Christmas has surpassed the religious boundaries and become a symbol of the holistic culture. The winters in December carry a festive feeling. "+"Usually, the celebration begins much before the main day and continues for around 2 weeks after that. Men and women celebrate Christmas to honor the birth of Jesus Christ. Religious people go to church and light the candles to pray to their God, Jesus Christ. "+"A festival that is equally loved and cherished by adults and kids. People also bring a Christmas tree to their homes and decorate it with colorful balls, ribbons, and red socks. Market shops and showrooms display a theme of glittering red and white colors to set up the Christmas mood. "+"On Christmas night, folks enjoy a big feast and share gifts with each other. Homemade traditional plum cakes, cupcakes, and muffins are the special treats on Christmas. Kids are showered with lots of presents and new dresses. They also get to meet the ‘Santa Claus’, dressed in a fluffy red and white costume, who greets them with hugs and gifts. "+"Christmas is a festival of joy. It is about sharing and helping others. On this day, people remember Jesus Christ and his lessons of life. The festival definitely teaches us to practice kindness and love toward each other and help those who have less than us. "+"Christmas is a well-known Christian holiday set in December, celebrated the world over and famed for its decorations and Santa Clause. Christmas is celebrated on the 25th of December, on the occasion of the birth of Jesus Christ. One can write for ages about the many wonders that Christmas inspires in people. This holiday is also famous for the different customs that are associated with it and even though Christmas is celebrated in all Christian countries there are differences in the way each nation commemorates this date. "+"One of the more famous symbols of this holiday is the Christmas tree. Most people do not think about it and just maintain that this custom has been around for ages, while in fact, it is in use for the past 150 years. The idea originated in Germany and later on, it was spread to the rest of the western world by Queen Victoria and Prince Albert. This event was meant for the entire family to enjoy a day before the 25th of December. "+"The famous Santa Clause celebrated in many movies and made famous by Coca-Cola commercials is actually Saint Nicholas and he is traditionally celebrated on the 6th of December. The Santa goes around town and checks if all the children were good and if they were, he left them a present, but if a child misbehaved often the Krampus would come to punish them by leaving a whip for the parents. This myth was taken on by the movie industry and transformed into the white beard and red-coated child hero of today. "+"Traditionally Christmas is celebrated by a Church mass in the morning and then by a family meal later on in the day. That is if you are a religious person, otherwise, most people have some sort of Christmas dinner where they sing the appropriate songs and drink special drinks, somewhere its egg- nock and in other places its sweetened cooked red wine. Whatever the tradition the point of the holiday is to spend some quality time with your loved ones eating and resting. "+"Christmas is also famous as the time of the year when we give gifts to each other and appropriately this is also the time when companies try to sell everything they can. Marketing experts know how to use the traditional symbols of Christmas to make you want to buy something that you do not actually need. Not to mention that every gift that Santa brings has to be bought somewhere and every child wants a visit from their favorite imagined gift giver. The consumer society has transformed this holiday and made it part of its cosmology, the basic elements are still here but everything is set around decoration, gifts, and movies. "+"Whatever the backdrop of the holiday it still remains one of the coziest times of the year, at least form me. Spending time at home with the people we love, embraced, watching movies and surrounded by flickering lights is the image I have in my head when I think about Christmas. This is also an image that brings warmth to my heart. "
christmas = christmas.lower()
christmas = christmas.split(' ')
print(christmas)
christmas = [w for w in christmas if not w in stop_words]
christmas1 = ""
for i in christmas:
  christmas1+=i+" "
christmas = christmas1
print(christmas)

christmas=christmas.replace('?', '.')
christmas=christmas.split('.')
christmas_labels = [[1,0,0,0,0]]*len(christmas)
print(christmas)

diwali = "The festival of Diwali is associated with many historical as well as mythological tales. We will discuss a few of them here. Goddess Lakshmi’s Birth. According to the Puranas, Goddess Lakshmi took birth on the day of the new moon during Kartik month. In several Hindu-dominated areas, this day is celebrated in the form of Goddess Lakshmi’s birthday by performing different rituals. People worship her during the evening time. Since she is regarded as the ‘Goddess of Wealth’ as well, therefore, the Hindus hold high regard for her. Lord Rama’s Return to Ayodhya. It is the most widely accepted mythological tale regarding the celebration of Diwali. According to the Ramayana, Lord Rama returned to his kingdom of Ayodhya along with Mata Sita and brother Lakshman after spending 14 years in exile. To celebrate this occasion, the whole Ayodhya city was decorated with beautiful lights and colourful rangolis. People distributed sweets among themselves as well. This ritual is strictly followed even today. The Harvest Festival It is during the Diwali time when farmers start cultivating rice, especially in the South. Therefore, it is also regarded as the festival of harvest. Since India’s economy is mainly based on agriculture, therefore the day is a celebration time for the farmers and their families."+"What is the first thing that comes into your mind when you think about Diwali? Lights, fireworks, colourful paintings, sweets and what not. It is an occasion when all the members of our family come together to celebrate the Diwali night. "+"Diwali can rightly be called as one of the biggest festivals of Hindus which is celebrated with joy and harmony not only in India but across the globe. Especially the kids look forward to this festival since they get to burst their favourite crackers and eat whatever they wish. "+"The festival of Diwali takes place during the month of October or November every year. It is celebrated exactly 20 days after the festival of Vijayadashami. Spiritually, it is significant for us because it represents the victory of good over evil. While celebrating the festival, people try to follow all the rituals. Few of these are decorating the houses with candles and diyas and worshiping Lord Ganesha and Goddess Lakshmi. Diwali is a five day long festival. It starts with cleaning of houses and shops. Then people start decorating them. Whether it’s about washing the window curtains or cleaning the fans or painting the houses to discard those items which are old and unused - everything takes place during this time.  On the final day of Diwali, during the evening time, people start decorating their houses with colorful lanterns, diyas, candles, flowers and rangolis. They wear new dresses and worship Lord Ganesha and Goddess Lakshmi and distribute sweets and other eateries among friends and relatives. It is also an occasion for visiting friends and relatives & exchanging gifts with them. Nowadays, several residential societies organise Diwali parties where they invite every family irrespective of their religion, to celebrate. Although Diwali is a festival each one of us enjoys irrespective of religion, but while bursting crackers in huge numbers, we tend to forget this fact that it harms our environment on a large scale. This process results in air, noise and land pollution. In many Indian cities especially in Delhi, it has been observed that after Diwali celebrations the air quality degrades to a great extent. This is responsible for causing many harmful diseases such as breathing issues. Every year, the Government, health experts and environment experts issue an advisory stating that one should not burst crackers. Diwali minus crackers is a more beautiful festival where everyone can be seen enjoying it without any harm to the environment. Now that you know how hazardous it can be if you burst crackers during the celebration of Diwali, we all should stop doing the same next time onwards and find an alternate solution. What about switching to eco-friendly Diwali? Wouldn’t it contribute to the environment as well? As an adult, it is responsibility that we ask the young generation to stop using crackers. The government should also ban the same and check their sale. Those crackers which radiate hazardous gases should be immediately removed from the market. Diwali (also: Deepawali) is one of India's biggest festivals. The word Deepawali means rows of lighted lamps. It is a festival of lights and Hindus celebrate it with joy. During this festival, people light up their houses and shops with Diyas (small cup-shaped oil lamp made of baked clay). They worship the Lord Ganesha for welfare and prosperity and Goddess Lakshmi for wealth and wisdom. This festival is celebrated in the Hindu month of Kartikamasam which falls sometime during October or November. It is celebrated to mark the return of Lord Rama after 14 years of exile and his victory over the Demon Ravana. In many parts of India, Deepawali is celebrated for five consecutive days. Hindus regard it as a celebration of life and use the occasion to strengthen relationships. In some parts of India, it marks the beginning of a new year. People clean and decorate their house before the festival. Deepawali is celebrated and is a public holiday in countries such as Nepal, Sri Lanka, Singapore, Malaysia, Mauritius, Fiji, Suriname, Guyana, Trinidad and Tobago. It is also a school holiday in many states of the United States with a large Hindu population. President George W. Bush had the first celebration of the holiday in the White House. Hindus light up their homes and shops to welcome the Goddess Lakshmi and to give them good luck for the year ahead. A few days before Ravtegh, which is the day before Deepavali, houses, buildings, shops and temples are thoroughly cleaned, whitewashed and decorated with pictures, toys and flowers. On the day of Deepawali, people put on their best clothes and exchange greetings, gifts and sweets with their friends and family. At night, buildings are illuminated with earthen lamps, candle-sticks and electric bulbs. Sweets and toy shop are decorated to attract the passers-by. The bazaars and streets are overcrowded. People buy sweets for their own families and also send them as presents to their friends and relatives. The Goddess Lakshmi is also worshiped in the form of earthen images, silver rupee. Hindus believe that on this day, Lakshmi only enters houses which are neat and tidy. People offer prayers for their own health, wealth and prosperity. They leave the light on in buildings believing that Lakshmi will not have difficulty in finding her way in. "
diwali = diwali.lower()
diwali = diwali.split(' ')
print(diwali)
diwali = [w for w in diwali if not w in stop_words]
diwali1 = ""
for i in diwali:
  diwali1+=i+" "
diwali = diwali1
print(diwali)

diwali=diwali.replace('?', '.')
diwali=diwali.split('.')
diwali_labels =[[0,1,0,0,0]]*len(diwali)
print(len(diwali))
print(diwali_labels)

eid = "Eid or Eid-ul-Fitr is the greatest festival of the Muslims. The Muslims, all over the world, celebrate it with great pomp and show, zeal and gusto. This festival marks the end of Ramadan. Ramadan is a holy month of fasting. The Muslims observe fasts for a full month after sighting the moon of ‘Ramzan’. When the month of ‘Ramzan’, is over and the moon of Eid is sighted, they end their Roja (fasts). In this way, the Muslims break their month-long fast. The next day, the festival of Eid is celebrated. Every year it comes off on the first day of the month of Shawwal. It is a day of gaiety, festivity and feasting. It is a believed that fasting in the month of ‘Ramzan’ purifies the soul. The prayers after fasting save them from going to hell and open the doors of heaven. Thus, they lead a pure and holy life during the month of ‘Ramzan’. They observe fasts, offer regular prayers in the form of ‘Namaz’; read the holy Koran, feed the hungry and give alms to the poor. Charity is the greatest virtue to be practiced during the month of ‘Ramzan’. Fasting comes to an end when the new moon of Eid is sighted. The sight of the new moon of Eid is considered very pious and holy by the Muslims. It is a signal for the celebration of Eid the very next day. On the Eid day, Muslim people get up early in the morning. They take a bath and put on their best dresses. Houses are decorated. They thank Allah, visit mosques and offer prayers in the form of ‘Namaz’. They embrace one another and exchange Eid greetings. ‘Eid Mubarak’ is on the lips of each Muslim. Sweets are distributed, gifts are given and delicious dishes are prepared at home. Friends and relatives are invited to feasts. Sweet noodles are the most popular dish cooked on this day. At some places, Eid fairs are also held. Eid greetings are exchanged by one and all. Children buy toys and sweets. In India, all communities join the Muslims in celebrating Eid. Sweets are shared and greetings exchanged by all. The Hindus, Sikhs and Christians greet their Muslim brothers on this day. The celebration of Eid promotes national integration and the feeling of brotherhood. Joys are doubled when they are shared. Eid brings a message of brotherhood for all of us. It is a festival of love and goodwill. It gives us a message to love all and hate none. It teaches us to embrace all men as brothers. Separated lovers hope to meet on this day. It exhorts us to bid goodbye to hatred, jealousy and enmity and bring in an era of love, sympathy and brotherhood. ‘Eid-ul-Fitr’ or ‘Id’ is one of the biggest festivals of Muslims. This festival is one of the most important religious festivals of Muslims around the world. This festival is celebrated with great glamor throughout the world including India. The festival of Eid is celebrated after the holy month of Ramadan. Ramadan days are very important for Muslims. During this time, they keep a full fast throughout the day. Drinking water is also not allowed. In the evening, after eating prayers, they take food. On the last day of the month of Ramadan, when the moon appears in the sky, Eid is celebrated on the second day. Preparation to celebrate the festival of Eid is already started. Children, young and old, all appear enthusiastic — the crowd increases in markets. The rich and the poor get busy buying new clothes, footwear, gifts, etc. Indeed, the festival of Eid plays an important role in spreading happiness in the society, becoming a partner in the pleasures of neighbor’s, and spreading cordiality (describe a relationship that is friendly) among the people. In our country, when the festival of Eid comes, people from all other communities, except Muslims, are happily jumped. The month of Ramadan for Muslims is of particular religious significance. This is their month of self-restraint in their view. All Muslim people are fasting all day in this month. They do not even accept a drop of water throughout the day. People also pray ‘Namaz‘ on God days at five o’clock in the day and pray for self and purification of all the kin. All Muslim Muslims take food and water throughout the month of Ramadan. A large crowd can be seen in the shops of fruits and sweets around. There is a new loneliness in the atmosphere. The legend of the Eid scene is depicted by great novelist Munshi Premchand in his famous story ‘Idgah.’"
eid = eid.lower()
print(len(eid))
eid = eid.split(' ')
print(eid)
eid = [w for w in eid if not w in stop_words]
eid1 = ""
for i in eid:
  eid1+=i+" "
eid = eid1
print(eid)

eid=eid.replace('?', '.')
eid=eid.split('.')
eid_labels = [[0,0,1,0,0]]*len(eid)
print(len(eid))

holi = "Holi is one of the main festivals of Hindus. It is celebrated in South Asian countries, especially in India and Nepal. Holi is the festival of colours. The festival is celebrated for two to three days. People pour colored water on each other and cook many types of sweets and other food. Holi is celebrated in the spring season because it is welcomed spring. Hindus believe that spring is full of colours so they throw coloured water on each other. Holi is based on a legend about King Hiranyakaship. `Hiranyakashyap had a son, Prahlad. Prahlad was the greatest devotee of Lord Vishnu. Hiranyakashyap wanted to kill his son, so he called his sister, Holika. She had a magic robe. This robe had the power to save the wearer from burning in fire. Hiranyakashyap ordered his sister to sit on a burning fire along with Prahlad. He thought that his sister would not be harmed by the fire because of the magic robe and Prahlad would be burnt to death. But the result was the opposite to what the evil demon king planned. As is believed, no one can harm the person who has God as his saviour. Thus Prahlad came out of the burning fire safely and Holika was burnt to death. The other day is celebrated with joyful colours to mark the victory of virtue and goodness over evil. The festival is celebrated for five days. The 5th day, Rang Panchami, marks the closing day of the Holi festival. People are seen with different varieties of colours on Holi.They put colours on each other, sing, dance. They worship Lord Krishna and put colours on his idol. Families gather together and party whole day. They distribute sweets and enjoy to the fullest. The children wait for this event the entire year. This is because they get to play the entire day. Thus, Holi is considered to be a festival of joy. People eagerly wait for this every year. People celebrate Holi with utmost fervour and enthusiasm, especially in North India. One day before Holi, people conduct a ritual called ‘Holika Dahan’. In this ritual, people pile heaps of wood in public areas to burn. It symbolizes the burning of evil powers revising the story of Holika and King Hiranyakashyap. Furthermore, they gather around the Holika to seek blessings and offer their devotion to God. The next day is probably the most colourful day in India. People get up in the morning and offer pooja to God. Then, they dress up in white clothes and play with colours. They splash water on one another. Children run around splashing water colours using water guns. Similarly, even the adults become children on this day. They rub colour on each other’s faces and immerse themselves in water. In the evening, they bathe and dress up nicely to visit their friends and family. They dance throughout the day and drink a special drink called the ‘bhaang’. People of all ages relish holi’s special delicacy ‘gujiya’ ardently. In short, Holi spreads love and brotherhood. It brings harmony and happiness in the country. Holi symbolizes the triumph of good over evil. This colourful festival unites people and removes all sorts of negativity from life. The Hindu religion believes there was a devil king named Hiranyakashyap long ago. He had a son named Prahlad and a sister called Holika. It is believed that the devil king had blessings of Lord Brahma. This blessing meant no man, animal or weapon could kill him. This blessing turned into a curse for him as he became very arrogant. He ordered his kingdom to worship him instead of God, not sparing his own son. Following this, all the people began worshipping him except for his son, Prahlad. Prahlad refused to worship his father instead of God as he was a true believer of Lord Vishnu. Upon seeing his disobedience, the devil king planned with his sister to kill Prahlad. He made her sit in the fire with his son on the lap, where Holika got burned and Prahlad came out safe. This indicated he was protected by his Lord because of his devotion. Thus, people started celebrating Holi as the victory of good over evil. The popular legend of Holi is all about honoring Lord Vishnu who killed King Hiranyakashipu in his Narasimha avatar. Holika is the evil aunt of Prahlada, the ardent devotee of Lord Vishnu and the son of Hiranyakashipu who tried to kill Prahlada for worshipping Lord Vishnu and not accepting his father as a God. The festival of Holi lasts for two days. On the first night, people light the bonfires as part of the ceremony called the Burning of Holika. On the second day, people celebrate the Holi with colors smearing and spraying at each other, singing and dancing together and relishing the sweet delicacies. The celebration symbolizes the beginning of a new relationship with oneself and others, forgetting and forgiving past mistakes."
print(len(holi))
holi = holi.lower()
holi = holi.split(' ')
print(holi)
holi = [w for w in holi if not w in stop_words]
holi1 = ""
for i in holi:
  holi1+=i+" "
holi = holi1
print(holi)

holi=holi.replace('?', '.')
holi=holi.split('.')
holi_labels = [[0,0,0,1,0]]*len(holi)
print(len(holi))

easter = "Easter is one of the most important Christian festivals which is observed in March 
or April. On this day the Christians celebrate the resurrection of Jesus after his death by crucifixion which is believed to have happened during this time around 30-33 A.D. Easter, also called Resurrection Day and Pascha, is a Christian holiday celebrating Jesus Christ returning from the dead. Christians believe that it is the holiest day in the year. Some people who are not Christians celebrate it as a cultural holiday.  Easter is not held on the same date every year. This is called a moveable feast. Currently all Christian churches agree on how the date is calculated. Easter is celebrated on the first Sunday following the first full moon which is on or after March 21st. This means it is celebrated in March or April. It can occur as early as March 22 and as late as April 25. Western churches, like the Roman Catholic Church, use the Gregorian calendar, while Eastern churches, like the Eastern Orthodox Church, use the Julian calendar. Because of this, the date of Easter celebrations is different for these two types of churches even though the way they calculate the date is similar. In 2015 Easter was celebrated on April 5 for both the Gregorian calendar and Julian calendar. In 2019 Easter will be celebrated on the 21st of April.  The word \"Easter\" is derived from Eastra, the name of the ancient German Goddess of Spring.[1] Her festival occurred at the vernal equinox. The French word for Easter, Pâcques, comes from the Greek word for Passover, which is the Jewish holiday celebrated at about the same time of the year. Jesus died roughly 2000 years ago in a city called Jerusalem (most of Jerusalem is in the modern country of Israel). The people who killed him did so because they believed that he was causing trouble for the government and because he was claiming to be the Messiah. When they crucified him (meaning they nailed him to a cross), they even hung a sign over his head, which said, \"King of the Jews.\"[2] The day he was crucified is known by Christians as Good Friday. The New Testament states that on the Sunday after Jesus was killed, his body was no longer in the tomb where he was laid.[4] Later, Jesus is said to have appeared to over 500 people and preached to them.[5] The New Testament teaches that the resurrection of Jesus is what Christianity is based on.[6] The resurrection made people believe that Jesus was the powerful Son of God.[6] It is also spoken of as proof that God will judge the world fairly.[7] Christians believe that God has given Christians \"a new birth into a living hope through the resurrection of Jesus Christ from the dead\".[8] Christians believe that through faith in God[9] they are spiritually made alive with Jesus so that they may lead a new life.[10] Easter is celebrated in several ways in northern Europe and the United States. Most of these celebrations have nothing to do with the Christian meaning of the holiday. These celebrations are related more to the pagan festivals of ancient Germany. Children are given baskets to fill with candy. Eggs are decorated and hidden for children to find that the Easter Bunny supposedly laid. People wear new clothes and go to church. Greeting cards are exchanged. An Easter Egg Roll is held on the lawn of the White House on the day after Easter. Small leafless trees or branches are carried indoors and decorated with colored eggs, paper trims, and lights. Some shopping malls offer children a chance to visit with an adult costumed as the Easter Bunny. Forced tulips, hyacinths and lilies are given as gifts. Week-long vacations are taken following Easter Day, giving families the chance to visit with distant relatives. In America, many families leave the cold of northern states to visit amusement parks or sunny beaches in the south. Spring break for American high school and college students usually occurs about Easter time. Easter is a Christian festival that celebrates the rebirth of Jesus Christ. Some people think that the term, “Easter”, originates from a Pagan goddess named Eostre. Records show that this festival was celebrated since the 2nd century. The season of Easter lasts for six weeks and begins sometime in March or April. Though the date of Easter is not fixed every year, it occurs on a Sunday. Sunday is symbolic, because it was the day that Jesus rose from the dead. Today, the meaning of Easter, for millions of Christians, is that of honouring and recognizing Jesus Christ's resurrection from the dead Christians around the globe hold this festival in high regard. People fast during this time and incorporate more spiritual habits into their daily routine. Many of the customary practices of Easter don’t, actually, have anything to do with the occasion itself. However, children participate in Easter egg hunts and are given tons of candy. Eggs are decorated using paint, pens and other adornments. Earlier, chicken eggs were dyed, for this festival. But modern traditions include eggs that are made of chocolate or plastic, which are filled with candies. The Easter bunny is a figure from folklore, which carries a basket of coloured eggs. On the night before Easter, the bunny is said to hide the basket in the homes of children, so that they may find it on the day of Easter. Ideally, the Easter bunny is a judge of character, as only those children, who have been nice, receive gifts on Easter. The celebration of Easter is different in all cultures. Some communities have elaborated celebrations such as processions, whereas others involve attending mass and singing songs. The day will also witness lavish feasts and a variety of tradition dishes being cooked and served. Easter truly encapsulates and celebrates the most important part of  Jesus Christ Life. It’s a reminder about the sufferings he underwent for the humanity, the prize he paid for it and his resurrection."
print(len(easter))
easter = easter.lower()
easter = easter.split(' ')
print(easter)
easter = [w for w in easter if not w in stop_words]
easter1 = ""
for i in easter:
  easter1+=i+" "
easter = easter1
print(easter)

easter=easter.replace('?', '.')
easter=easter.split('.')
easter_labels = [[0,0,0,0,1]]*len(easter)
print(len(easter))

data = christmas + diwali + eid + holi + easter
data_labels = christmas_labels + diwali_labels + eid_labels + holi_labels + easter_labels
random.seed(1)
random.shuffle(data)
random.seed(1)
random.shuffle(data_labels)

tokenizer = Tokenizer(num_words=1000, oov_token="unkown")
tokenizer.fit_on_texts(data)
word_index = tokenizer.word_index
print(word_index)

sequences = tokenizer.texts_to_sequences(data)
print(sequences)
#average length per sequence is 19 or 20, we will assume 20

padded = pad_sequences(sequences, padding='post')
for i in padded:
  print(i)
  print(len(i))
print(len(data_labels))

train_data = padded[:300]
train_labels = data_labels[:300]
test_data = padded[300:]
test_labels = data_labels[300:]

train_data = np.asarray(train_data)
test_data = np.asarray(test_data)
train_labels = np.asarray(train_labels)
test_labels = np.asarray(test_labels)
print(train_data)

vocab_size = 1000
embedding_dim = 16
max_length = 29
trunc_type='post'
oov_tok = "<OOV>"


model = tf.keras.Sequential([
                             tf.keras.layers.Embedding(vocab_size, embedding_dim, input_length=max_length),
                             #tf.keras.layers.Flatten(),
                             tf.keras.layers.Conv1D(128, 10, activation='relu'),
                             tf.keras.layers.GlobalMaxPooling1D(),
                             #tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
                             tf.keras.layers.Dense(128, activation='relu'),
                             tf.keras.layers.Dense(64, activation='relu'),
                             tf.keras.layers.Dense(5, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

model.fit(train_data,
          train_labels,
          epochs=50,
          validation_data=(test_data,test_labels))



