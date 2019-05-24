# encoding: utf-8
# topics : 1 - foods, 2 - economics, 3- tech, 4- politics
# model 1-2
topics1_2 = [4, 4, 1, 3, 2, 1, 1, 2, 2, 3, 3, 4, 2, 1, 4, 1, 4, 2, 1, 2]
topics1_4 = [4, 3, 1, 2, 1, 3, 1, 4, 3, 2, 1, 1, 4, 4, 2, 2, 1, 2, 4, 2]
topics2_12 = [3, 2, 1, 1, 1, 3, 1, 3, 4, 4, 2, 3, 3, 4, 2, 3, 1, 4, 3, 2]
topics2_9 = [4, 4, 1, 1, 1, 3, 4, 2, 3, 3, 1, 2, 2, 4, 1, 3, 4, 4, 2, 1]

# print(topics1_4[11])
topicsName = ['food_cat', 'eco_cat', 'tech_cat', 'pol_cat']
# print(topicsName[topics1_4[11]-1])
def getModelIndex(model, index):
    if (model == '1_2'):
        return topics1_2[index]
    elif (model == '1_4'):
        return topics1_4[index]
    elif (model == '2_12'):
        return topics2_12[index]
    else:
        return topics2_9[index]


def getModel(model):
    if (model == '1_2'):
        return topics1_2
    elif (model == '1_4'):
        return topics1_4
    elif (model == '2_12'):
        return topics2_12
    else:
        return topics2_9