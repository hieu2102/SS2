# encoding: utf-8

#import io
#import json
#source = open("C:\\Users\\DELL\\Desktop\\SS2\\NLP\\training_data\\News_Category_Dataset_v2.json")
#sport_file = open("sports.json", mode="w", encoding="utf-8")
#politics_file = open("politics.json", mode = "w", encoding="utf-8")
#food_file = open("food.json", mode = "w", encoding="utf-8")
#technology_file = open("tech.json", mode="w", encoding="utf-8")
#
#for line in source:
#    d=json.loads(line)
#    d.pop("authors")
#    d.pop("link")
#    d.pop("date")
#    if d["category"] == "POLITICS":
#        json.dump(d,politics_file)
#        politics_file.write("\n")
#    if d["category"] == "TECH":
#        json.dump(d,technology_file)
#        technology_file.write("\n")
#    if d["category"] == "FOOD & DRINK":
#        json.dump(d,food_file)
#        food_file.write("\n")
#    if d["category"] == "SPORTS":
#        json.dump(d,sport_file)
#        sport_file.write("\n")
#