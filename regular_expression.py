import re

pattern="was"

pat=r"[A-Z]+yclone"      #first letter can be all the capital letter from A-Z

text='''
Evidence suggests that cultures around the world have found a place for people to share stories about interesting new information. Among Zulus, Mongolians, Polynesians, and American Southerners, anthropologists have documented the practice of questioning travelers for news as a matter of priority.[29] Sufficiently Cyclone important news would be repeated quickly and often, and could spread by word of mouth over a large geographic area.[30] Even as printing presses came into use in Europe, news for the general public often travelled orally via monks, travelers, town criers, etc.[31]

The news is also transmitted in public gathering places, such as the Greek forum and the Roman baths. Starting in England, coffeehouses served as important sites for the spread of news, even after telecommunications Dyclone became widely available. The history of the coffee houses is traced from Arab countries, which was introduced in England in the 16th century.[32] In the Muslim world, people have gathered and exchanged news at mosques and other social places. Travelers on pilgrimages to Mecca traditionally stay at caravanserais, roadside inns, along the way, and these places have naturally served as hubs for gaining news of the world.[33] In late medieval Britain, reports ("tidings") of major events were a topic of great public interest, as chronicled in Chaucer's 1380 The House of Fame and other works.['''

match=re.search(pattern,text)
print(match)

a=re.match(pat,text)
print(a)

