# -*- coding: utf-8 -*-
from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'small',
    'version': '1.2',
    'name': 'big! small!',
    'author': [
        'DC_Provide'
    ],
    'link': 'Nope...[doge]'
}


def on_info(server, info):
    if info.content == '!!small':
        server.execute("execute as "+ info.player +" at @s run attribute @s minecraft:generic.scale base set 0.3")
        server.execute('tellraw '+info.player+' {"translate":"commands.attribute.base_value.set.success","with":[{"translate":"attribute.name.generic.scale"},"'+info.player+'","0.3"]}')
    if info.content == '!!ultrasmall':
        server.execute("execute as "+ info.player +" at @s run attribute @s minecraft:generic.scale base set 0.1")
        server.execute('tellraw '+info.player+' {"translate":"commands.attribute.base_value.set.success","with":[{"translate":"attribute.name.generic.scale"},"'+info.player+'","0.1"]}')
    if info.content == '!!normal':
        server.execute("execute as "+ info.player +" at @s run attribute @s minecraft:generic.scale base set 1") 
        server.execute('tellraw '+info.player+' {"translate":"commands.attribute.base_value.set.success","with":[{"translate":"attribute.name.generic.scale"},"'+info.player+'","1.0"]}')
