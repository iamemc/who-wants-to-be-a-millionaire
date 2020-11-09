"""
Credits to:
    https://github.com/ilyankou
        For database structure and QAs

Q&A extracted from:
    https://gamefaqs.gamespot.com/gba/919785-who-wants-to-be-a-millionaire-2nd-edition/faqs/40044

"""
def getintro(n):
  return intro[n]
intro = [0 for i in range(10)]

def getstage(n):
  return stage[n]
stage = [0 for i in range(15)]

def getquestion(n):
  return a[n]
a = [0 for i in range(150)]

#Intros
intro[0] = ["Here is question nº"]
intro[1] = ["We're going to question nº"]
intro[2] = ["Question nº"]
intro[3] = ["This is the turn of question nº"]
intro[4] = ["Now is the turn of question nº"]
intro[5] = ["Let's see how you can cope with question nº"]
intro[6] = ["Let's see how much time it'll take you to answer question nº"]
intro[7] = ["Now onto question nº"]
intro[8] = ["Will you make it to the big levels? Here's question nº"]
intro[9] = ["Let's see how you'll do in question nº"]

#Stages
stage[0] = ["100€"]
stage[1] = ["200€"]
stage[2] = ["300€"]
stage[3] = ["500€"]
stage[4] = ["1.000€"]
stage[5] = ["2.000€"]
stage[6] = ["5.000€"]
stage[7] = ["10.000€"]
stage[8] = ["20.000€"]
stage[9] = ["50.000€"]
stage[10] = ["75.000€"]
stage[11] = ["150.000€"]
stage[12] = ["250.000€"]
stage[13] = ["500.000€"]
stage[14] = ["1.000.000€"]

#--------------------------------------List Syntax:--------------------------------------|
#                                                                                        |
#  a[i] = ["question", "option 1", "option 2", "option 3", "option 4", "correct answer"] |
#                                                                                        |
#--------------------------------------List Syntax:--------------------------------------|

#Q&A
a[0] = ["The reputed last words of which famous composer were 'I shall hear in heaven'?","Wagner","Mozart","Albinoni","Beethoven","Beethoven"]
a[1] = ["What might an electrician lay?","Tables","Gables","Cables","Stables","Cables"];
a[2] = ["By what abbreviation is a compact disc commonly known?","CD","COD","CDIS","COMPD","CD"]
a[3] = ["Which colour is used as a term to describe an illegal market in rare goods?","Blue","Red","Black","White","Black"]
a[4] = ["Which of these would a film actor like to receive?","Oliver","Oscar","Oliphant","Osbert","Oscar"]
a[5] = ["In which country would you expect to be greeted with the word 'bonjour'?","Italy","France","Spain","Wales","France"]
a[6] = ["Which word follows 'North' and 'South' to give the names of two continents?","Africa","America","Asia","Australia","America"]
a[7] = ["Which country is not an island?","Madagascar","Cuba","Germany","Jamaica","Germany"]
a[8] = ["What would you normally do with a beret?","Eat it","Play it","Sit on it","Wear it","Wear it"]
a[9] = ["Which of these is a tool for shaping and smoothing wood?","Train","Plane","Car","Bike","Plane"]
a[10] = ["What would you expect to see at the London Aquarium?","Flowers","Trees","Steam rollers","Fish","Fish"]
a[11] = ["Which is not a type of antelope?","Gorilla","Gerenuk","Gemsbok","Gnu","Gorilla"]
a[12] = ["What is rioja a type of?","Bread","Vegetable","Wine","Nut","Wine"]
a[13] = ["Germania was the Roman name for which modern-day European country?","France","Austria","Germany","Spain","Germany"]
a[14] = ["What was the UK's top paying attraction of 2002?","London Nose","London Mouth","London Eye","London Ear","London Eye"]
a[15] = ["Which of these geographical features is a mountain?","Kilimanjaro","Danube","Amazon","Nile","Kilimanjaro"]
a[16] = ["Which of these is a popular form of music?","Country & Eastern","Kingdom & Northern","Land & Southern","Country & Western","Country & Western"]
a[17] = ["Which of these is a common term for a programme of physical exercises?","Stay able","Remain trim","Continue competent","Keep fit","Keep fit"]
a[18] = ["What is the name of the instrument panel in a car?","Chargeboard","Sprintboard","Dashboard","Jogboard","Dashboard"]
a[19] = ["What copy can be said to describe something identical?","Oxygen","Hydrogen","Nitrogen","Carbon","Carbon"]
a[20] = ["Which is a chain of international hotels?","Four Tops","Four Pennies","Four Seasons","Four Posters","Four Seasons"]
a[21] = ["Which of these is a spicy Indian dish?","Spaghetti","Biriani","Bellini","Crostini","Biriani"]
a[22] = ["Which country is not crossed by the Arctic Circle?","Norway","Finland","Greece","Sweeden","Greece"]
a[23] = ["In which film must a bus keep travelling at 50 miles per hour so that it does not explode?","Speed","Velocity","Tempo","Thrust","Speed"]
a[24] = ["An older person is sometimes described as 'long in the ...'?","Tooth","Eye","Hair","Nose","Tooth"]
a[25] = ["According to the saying, which of these is 'a dish best served cold'?","Revenge","Cottage pie","Custard","Stew","Revenge"]
a[26] = ["To know the rudiments of a subject is to 'know your ...'?","ABC","HIJ","KLM","QRS","ABC"]
a[27] = ["Which of these is a butter substitute made with vegetable oils?","Margaret","Margarine","Margarita","Margate","Margarine"]
a[28] = ["Complete the title of the 2003 Disney release, 'Pirates of the ...'?","Black Sea","Atlantic","English Channel","Caribbean","Caribbean"]
a[29] = ["Which of these countries did not host a Formula 1 Grand Prix race in 2003?","Monaco","France","Italy","Madagascar","Madagascar"]
a[30] = ["Which is not a recognized playing surface for tennis?","Grass","Linoleum","Clay","Cement","Linoleum"]
a[31] = ["Which of the following is a small sausage?","Maraschino","Chipolata","Risotto","Gazpacho","Chipolata"]
a[32] = ["What is the collective term for actors appearing in a film or play?","Cast","Band","Group","Clique","Cast"]
a[33] = ["What are you said to break, when you make friends with a stranger?","The ice","The snow","The hail","The frost","The ice"]
a[34] = ["Traditionally, people use their feet to extract juice from which fruit?","Pineapple","Cherry","Grape","Pricky pear","Grape"]
a[35] = ["With which activity is the phrase 'going, going, gone' most associated?","An auction","Gardening","Horse racing","Boxing","An auction"]
a[36] = ["Where are the headquarters of the US Department of Defense?","The Triangle","The Rectangle","The Pentagon","The Dodecahedron","The Pentagon"]
a[37] = ["Which of these is a theory about the creation of the universe?","Big Bong","Big Bang","Big Ben","Big Bertha","Big Bang"]
a[38] = ["Which of the following is most likely to run on caterpillar tracks?","Car","Train","Bulldozer","Bicycle","Buldozer"]
a[39] = ["Which of these is a satellite TV channel?","Trademark","Landmark","Hallmark","Dirtymark","Hallmark"]
a[40] = ["Which of these are located at the back of your throat?","Deltoids","Tabloids","Adenoids","Solenoids","Adenoids"]
a[41] = ["What type of steroids have a protein-building effect?","Carbolic","Shambolic","Anabolic","Diabolic","Anabolic"]
a[42] = ["What would be used to boost an electrical signal?","Ambrosia","Amphitheatre","Amphetamine","Amplifier","Amplifier"]
a[43] = ["How many lines are used for the 'equals' sign in mathematical notation?","One","Two","Three","Four","Two"]
a[44] = ["Which chemical element was named after a planet in our solar system?","Venusium","Jupiterium","Uranium","Saturnium","Uranium"]
a[45] = ["Which is not a classification of star?","Red giant","White dwarf","Red dwarf","Green goblin","Green goblin"]
a[46] = ["'Freak of Nature' is the title of a worldwide hit album by whom?","Anastacia","Caucasia","Dysphasia","Phoenicia","Anastacia"]
a[47] = ["Robbie Williams was once a member of which of these?","Ouch!","Take That","Wham!","Biff!","Take That"]
a[48] = ["Which of these is a three-stringed musical instrument?","Balaclava","Balakirev","Balalaika","Balanchine","Balalaika"]
a[49] = ["Which of these is a term for an actor?","Equestrian","Thespian","Pedestrian","Martian","Thespian"]
a[50] = ["Which of these might be sprinkled on a rice pudding?","Cinnabar","Cinnamon","Cincinnati","Cinerama","Cinnamon"]
a[51] = ["What is Double Gloucester?","Card game","Cheese","Very thick hedge","Thatched roof","Cheese"]
a[52] = ["Which of these first came on the market in 1937?","Posh Spice","Scary Spice","Baby Spice","Old Spice","Old Spice"]
a[53] = ["A person who slavishly buys the latest clothes is a 'fashion ...'?","Witness","Culprit","Suspect","Victim","Victim"]
a[54] = ["Who was not a Roman emperor?","Hadrian","Parallax","Claudius","Tiberius","Parallax"]
a[55] = ["Which island is known as Kriti in its own language?","Crete","Corsica","Corfu","Cuba","Crete"]
a[56] = ["What is the French for 'king'?","Kaiser","Duc","Herzog","Roi","Roi"]
a[57] = ["What term is used for the whole of the background of a flag?","Meadow","Lea","Pasture","Field","Field"]
a[58] = ["What term means a movie that is a box-office failure?","Grenade","Mine","Bomb","Shell","Bomb"]
a[59] = ["Which word is sometimes used to mean a dessert?","Befores","Whiles","Afters","Nevers","Afters"]
a[60] = ["Which creatures are traditionally kept in an aviary?","Birds","Fish","Reptiles","Insects","Birds"]
a[61] = ["The Latin phrase 'compos mentis' means 'of sound ...'?","Advice","Health","Mind","Garden","Mind"]
a[62] = ["Which is a material used in making roads?","Macaroni","Macabre","Macadam","Macdonald","Macadam"]
a[63] = ["From which of these do cats commonly suffer?","Fastballs","Hairballs","Meatballs","Curveballs","Hairballs"]
a[64] = ["Which is not an electrical SI unit of measurement?","Volt","Ampere","Ohm","Gallon","Gallon"]
a[65] = ["By what name is sodium carbonate commonly known?","Soda biscuit","Soda bread","Washing soda","Lime and soda","Washing soda"]
a[66] = ["According to the proverb, what does a watched pot never do?","Fill","Spill","Boil","Empty","Boil"]
a[67] = ["Which is a Mexican stuffed, fried pancake?","Waco","Saki","Taco","Pesto","Taco"]
a[68] = ["Who gave their name to a continent?","Europa Bellini","Amerigo Vespucci","Africo Tintorini","Asio Canelli","Amerigo Vespucci"]
a[69] = ["Which is the chief port of Athens?","Amadeus","Nicodemus","Piraeus","Celsius","Piraeus"]
a[70] = ["Which of these is not a European river?","Danube","Rhine","Seine","Missouri","Missouri"]
a[71] = ["Which is a South American capital city?","Paprika","Mustard","Cayenne","Saffron","Cayenne"]
a[72] = ["Which French word is used to mean a select group or class?","Elan","Eglise","Ecole","Elite","Elite"]
a[73] = ["Which is a tough durable synthetic material?","PVC","PTO","POW","PBX","PVC"]
a[74] = ["Which is a breed of dog formerly used as coach dogs?","Croatian","Dalmatian","Montenegran","Bosnian","Dalmatian"]
a[75] = ["The bird of paradise is native to which of these islands?","Anglesey","New Guinea","Iceland","Sicily","New Guinea"]
a[76] = ["Which of these is a 2003 Disney computer-animated film?","Locating Remo","Discovering Lemo","Unearthing Zemo","Finding Nemo","Finding Nemo"]
a[77] = ["Who released an album called 'Justified' in 2003?","Britney Spears","Justin Timberlake","Gareth Gates","Victoria Beckham","Justin Timberlake"]
a[78] = ["What is the subtitle of the 2003 film 'Legally Blonde 2'?","Blue Red & Blonde","Pink Blue & Blonde","Green Red & Blonde","Red White & Blonde","Red White & Blonde"]
a[79] = ["What would you normally do with a Liebfraumilch?","Drink it","Play a tune on it","Drive it","Sit on it","Drink it"]
a[80] = ["Which of these is not a type of paint used in decorating?","Gloss","Satin","Silk","Damask","Damask"]
a[81] = ["Which star's name is an anagram of a European country?","Demi Moore","Meg Ryan","Mira Sorvino","Minnie Driver","Meg Ryan"]
a[82] = ["Which is not an illegal punch in boxing?","Butt","Elbow","Jab","Palm","Jab"]
a[83] = ["Which of these words is used to identify an Internet server?","Realm","Province","Kingdom","Domain","Domain"]
a[84] = ["Which is an alternative name for a peanut?","Earthnut","Soilnut","Groundnut","Allnut","Groundnut"]
a[85] = ["Complete the name of the well-known rock group, Radio...?","Arm","Leg","Foot","Head","Head"]
a[86] = ["Complete the name of the British singer, Mica ... ?","Berlin","Madrid","Dublin","Paris","Paris"]
a[87] = ["What is the pop singer Beyonce's surname?","Cowles","Fowles","Knowles","Dowles","Knowles"]
a[88] = ["In the USA, for which organisation would a 'G-man' work?","FBI","NBA","NFL","MFI","FBI"]
a[89] = ["Originating in Italy, what type of food is mortadella?","Sausage","Pasta","Cheese","Pastry","Sausage"]
a[90] = ["Which of these place names means 'white house'?","Canberra","Canada","Casablanca","Canterbury","Casablanca"]
a[91] = ["Algeria has a coastline on which sea?","Adriatic","Caspian","Baltic","Mediterranean","Mediterranean"]
a[92] = ["What is the French word for England?","Angleterre","Etats-Unis","Inglaterra","Bretagne","Angleterre"]
a[93] = ["Which of these describes the rich and famous?","Glitterati","Hoi polloi","Establishment","Paparazzi","Glitterati"]
a[94] = ["Which Italian term is used to describe painting on wet plaster?","Frappe","Fresco","Fredo","Frisson","Fresco"]
a[95] = ["In which 2003 film is Jim Carrey granted divine powers by God?","Harry the Holy","Al Omnipotent","Gordon Plays God","Bruce Almighty","Bruce Almighty"]
a[96] = ["What name was given to South Africans of Dutch descent?","Moors","Boers","Creoles","Voortrekkers","Boers"]
a[97] = ["With what is the word 'QWERTY' associated?","Communism","Modern art","Computer keyboard","Wine","Computer keyboard"]
a[98] = ["What colour light indicates the port side of a ship?","Yellow","White","Blue","Red","Red"]
a[99] = ["Which US city is the setting for the TV sitcom 'Taxi'?","Boston","Dallas","Los Angeles","New York","New York"]
a[100] = ["A metric tonne consists of 1000 what?","Stones","Kilograms","Pounds","Grams","Kilograms"]
a[101] = ["Which element has the chemical symbol Co?","Carbon","Calcium","Chromium","Cobalt","Cobalt"]
a[102] = ["According to the Bible, which of these is not an archangel?","Michael","Raphael","Gabriel","Ishmael","Ishmael"]
a[103] = ["Which of these titles was bestowed upon Margaret Thatcher?","Marchioness","Duchess","Baroness","Countess","Baroness"]
a[104] = ["Which Jimmy, born in Jamaica in 1948, became a reggae star?","Edge","Mount","Cliff","Tor","Cliff"]
a[105] = ["Which of these authors was not sent to prison?","Oscar Wilde","John Bunyan","Agatha Christie","Brendan Behan","Agatha Christie"]
a[106] = ["What did the legendary Trojan horse contain?","Horses","Gold","Wheat","Soldiers","Soldiers"]
a[107] = ["Which was a battle in the American War of Independence?","Fairway Hill","Green Hill","Bunker Hill","Rough Hill","Bunker Hill"]
a[108] = ["Which present-day eastern European country was not part of the former USSR?","Hungary","Lithuania","Ukraine","Latvia","Hungary"]
a[109] = ["The Mount of Olives is just east of which city?","Jerusalem","Moscow","Hong Kong","Paris","Jerusalem"]
a[110] = ["In economics, what does the 'D' stand for in the abbreviation GDP?","Defence","Daily","Dual","Domestic","Domestic"]
a[111] = ["In painting, which of these is not a secondary colour?","Green","Orange","Purple","Red","Red"]
a[112] = ["Which dinosaur could fly?","Allosaurus","Diplodocus","Stegosaurus","Pterodactyl","Pterodactyl"]
a[113] = ["Which president was elected unopposed to a sixth term in March 2003?","George W Bush","Fidel Castro","Mary McAleese","Vladimir Putin","Fidel Castro"]
a[114] = ["What, in August 2003, was 'Sobig.F'?","New airline","Computer virus","Archaeological dig","Meteorite","Computer virus"]
a[115] = ["In October 2003, which became the third nation to put a man into space?","Japan","South Africa","Australia","China","China"]
a[116] = ["What would you normally do with a mai tai?","Eat it","Wear it","Drink it","Sing it","Drink it"]
a[117] = ["What was the name of the two NASA missions sent to Mars in 1975?","Viking","Visigoth","Saxon","Hun","Viking"]
a[118] = ["Which of these is an international motoring insurance?","Yellow card","Green card","Blue card","Red card","Green card"]
a[119] = ["What shape is an Australian Rules football pitch?","Rectangular","Circular","Diamond","Oval","Oval"]
a[120] = ["Which is not one of golf's 'Majors'?","USPGA","US Masters","US Open","US Pro-Am","US Pro-Am"]
a[121] = ["Of what is seismology the study?","Earthquakes","Tides","Clouds","Volcanoes","Earthquakes"]
a[122] = ["David Gates was the lead vocalist with which US band?","Yeast","Money","Dough","Bread","Bread"]
a[123] = ["Which of these is not a grain crop?","Wheat","Millet","Maize","Soya","Soya"]
a[124] = ["On a standard computer keyboard, what letter lies between 's' and 'f'?","c","d","e","r","d"]
a[125] = ["What type of fashion accessory is a 'pillbox'?","Scarf","Hat","Belt","Skirt","Hat"]
a[126] = ["In which year was the last successful invasion of Britain?","55 BC","1066","1812","1914","1066"]
a[127] = ["What name is given to the German air force?","Blitzkrieg","Luftwaffe","Panzer","Messerschmidt","Luftwaffe"]
a[128] = ["If you arrived at Split airport, which country would you be in?","Slovakia","Slovenia","Croatia","Hungary","Croatia"]
a[129] = ["Which of these oceans is the smallest?","Arctic","Pacific","Atlantic","Indian","Arctic"]
a[130] = ["The Dolomites are a range of mountains in the northeast of which country?","Poland","Turkey","Germany","Italy","Italy"]
a[131] = ["El Alamein is in which country?","Syria","Lebanon","Egypt","Saudi Arabia","Egypt"]
a[132] = ["Which of these deserts is in the USA?","Atacama Desert","Gobi Desert","Sahara Desert","Mojave Desert","Mojave Desert"]
a[133] = ["In which US state is the city of Tucson?","Arizona","Kansas","Texas","Colorado","Arizona"]
a[134] = ["Approximately 61% of the world's population live on which continent?","North America","Europe","Asia","Africa","Asia"]
a[135] = ["What is the English title of the Brazilian film 'Cidade de Deus'?","Church","City of God","Angels","Eternal City","City of God"]
a[136] = ["What nationality is the tennis player Alex Corretja?","Peruvian","Chilean","Brazilian","Spanish","Spanish"]
a[137] = ["Which sport is played by the Edmonton Oilers?","Basketball","Baseball","American football","Ice hockey","Ice hockey"]
a[138] = ["Which sport uses the Christmas Tree starting system?","Formula 1","Motocross","Drag racing","Car rallying","Drag racing"]
a[139] = ["Which Formula 1 racing team has won the most Constructor's titles?","Williams","Ferrari","Lotus","McLaren","Ferrari"]
a[140] = ["In which ocean are the Galapagos Islands?","Atlantic","Indian","Arctic","Pacific","Pacific"]
a[141] = ["In which country is the Atacama Desert?","Mexico","Morocco","Chile","Mongolia","Chile"]
a[142] = ["Of which country is Phnom Penh the capital?","Vietnam","Thailand","Cambodia","Malaysia","Cambodia"]
a[143] = ["Vesper is an archaic term for which time of day?","Morning","Evening","Noon","Night","Evening"]
a[144] = ["Which of these chemical elements is named after a Norse god?","Uranium","Neptunium","Osmium","Thorium","Thorium"]
a[145] = ["What name was given to the amicable separation of Slovakia and the Czech Republic?","Satin Split","Velvet Divorce","Silk Separation","Damask Parting","Velvet Divorce"]
a[146] = ["What is the UK equivalent of the CIA in the United States?","SAS","MI5","CND","MI6","MI6"]
a[147] = ["What lies at the centre of a heliocentric model of the solar system?","Earth","Sun","Moon","North star","Sun"]
a[148] = ["Who went on a 'Blonde Ambition' tour in 1990?","Blondie","Cher","Annie Lennox","Madonna","Madonna"]
a[149] = ["The Smurfs came from which country?","Sweden","Belgium","France","Denmark","Belgium"]