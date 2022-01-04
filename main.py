import os
import discord

TOKEN = "*"

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(msg):
    textfile = str(msg.channel) + '.txt'
    
    if msg.content.startswith('!start') & msg.author.guild_permissions.administrator:
        chname = str(msg.channel).replace("-"," ").capitalize()
        url = "https://fr.classic.wowhead.com/item=" + str(msg.channel.topic.split("\n")[0])
        img = "https://wowclassic.judgehype.com/screenshots/database/images/icons/" + str(msg.channel.topic.split("\n")[1]) + ".png"
        prix = msg.channel.topic.split("\n")[2]
        embed=discord.Embed(title=chname, url=url, description="Le prix minimum de l'item est : %s <:gold:782769536822542388>\n" % prix, color=0xff0000)
        embed.set_thumbnail(url=img)
        message = await msg.channel.send(embed = embed)
        f = open(textfile,'w')
        f.write(str(message.id)+"\n")
        f.close()
        await msg.delete()

    
    if msg.content.startswith('!unbid') & msg.author.guild_permissions.administrator:
        #Création de l'embed
        chname = str(msg.channel).replace("-"," ").capitalize()
        auteur = msg.content.split(" ")[1];
        
        f = open(textfile,'r')
        msg_id = f.readline()
        f.seek(0)
        contenu = f.read().split('\n')
        f.close()

        #On délete le msg id du contenue
        del contenu[0]
        try :
            del contenu[0]
        except:
            print('ah')

        #On crée un tuple avec la liste des personnes
        personnes = {}
        for i in contenu:
            test = i.split(',')
            try:
                personnes[test[0]] = int(test[1])
            except:
                print('np')

        #On supprime le bid de l'auteur
        print(personnes)
        try:
            auteur = auteur.replace("!", "")
            del personnes[auteur]
            print("bid deleted")
        except:
            auteur = auteur[0:2] + "!" + auteur[2:]
            del personnes[auteur]
            print("bid deleted")

        print(personnes)
        #On réécrit le fichier
        f = open(textfile,'w')
        f.write(str(msg_id)+"\n")
        prix = msg.channel.topic.split("\n")[2]
        description = "Le prix minimum de l'item est : %s <:gold:782769536822542388>\n\n" % prix
        name = ""
        value = ""
        for i in personnes:
            name = i
            value = str(personnes[i]) + " <:gold:782769536822542388>\n"
            f.write(i + ',' + str(personnes[i]) + '\n')
            #On en profite pour mettre son embed a jour

            description += name + " | " + value + "\n"
            print(description)

        #On recupère le message de base et on l'édit
        url = "https://fr.classic.wowhead.com/item=" + msg.channel.topic.split("\n")[0]
        img = "https://wowclassic.judgehype.com/screenshots/database/images/icons/" + str(msg.channel.topic.split("\n")[1]) + ".png"
        embed=discord.Embed(title=chname, url=url, description=description, color=0xff0000)
        embed.set_thumbnail(url=img)
        await msg.delete()
        msg = await msg.channel.fetch_message(msg_id)
        await msg.edit(embed=embed)



    if msg.content.startswith('!bid'):
        #Création de l'embed
        chname = str(msg.channel).replace("-"," ").capitalize()
            
        f = open(textfile,'r')
        number = msg.content.split(" ")[1];
        auteur = msg.author.mention
        msg_id = f.readline()
        f.seek(0)
        contenu = f.read().split('\n')
        f.close()

        #On délete le msg id du contenue
        del contenu[0]
        try :
            del contenu[0]
        except:
            print('ah')

        #On crée un tuple avec la liste des personnes
        personnes = {}
        for i in contenu:
            test = i.split(',')
            try:
                personnes[test[0]] = int(test[1])
            except:
                print('np')

        newbid = bool(0)
        #On ajoute le bid ou le remplace si il en existe un plus petit
        number = int(number)
        if (auteur in personnes):
            if (int(personnes[auteur]) < number):
                if number>=int(msg.channel.topic.split("\n")[2]):
                    personnes[auteur] = number
                    newbid = bool(1)
                    
        elif number>=int(msg.channel.topic.split("\n")[2]):
            personnes[auteur] = number
            newbid = bool(1)

        #On retrie le tuple via les Golds
        personnes = sorted(personnes.items(), key=lambda kv:(kv[1], kv[0]), reverse=True)

        if newbid:
            user=await client.fetch_user("366986597159272448")
            await user.send('Un nouveau bid est disponible il est de : %s par %s sur %s' % (number, auteur, chname))
            user=await client.fetch_user("308349620218494978")
            await user.send('Un nouveau bid est disponible il est de : %s par %s sur %s' % (number, auteur, chname))
            for i in personnes:
                idname = i[0]
                idname = idname.replace("!", "")
                idname = idname.replace(">", "")
                idname = idname.replace("<", "")
                idname = idname.replace("@", "")
                user=await client.fetch_user(idname)
                await user.send('Un nouveau bid est disponible il est de : %s par %s sur %s' % (number, auteur, chname))

        #On réécrit le fichier
        f = open(textfile,'w')
        f.write(str(msg_id)+"\n")
        prix = msg.channel.topic.split("\n")[2]
        description = "Le prix minimum de l'item est : %s <:gold:782769536822542388>\n\n" % prix
        name = ""
        value = ""
        for i in personnes:
            f.write(i[0] + ',' + str(i[1]) + '\n')
            #On en profite pour mettre son embed a jour
            name = i[0]
            value = str(i[1]) + " <:gold:782769536822542388>\n"
            description += name + " | " + value + "\n"
        #On recupère le message de base et on l'édit
        url = "https://fr.classic.wowhead.com/item=" + msg.channel.topic.split("\n")[0]
        img = "https://wowclassic.judgehype.com/screenshots/database/images/icons/" + str(msg.channel.topic.split("\n")[1]) + ".png"
        await msg.delete()
        embed=discord.Embed(title=chname, url=url, description=description, color=0xff0000)
        embed.set_thumbnail(url=img)
        msg = await msg.channel.fetch_message(msg_id)
        await msg.edit(embed=embed)
            
client.run(TOKEN)
