import os
from pygame import mixer
import pygame

#准备音乐播放器需要的参数
#音乐播放路径 当前播放的音乐序号 音量
music_source,current_music_no,volume = [],0,0.2

#返回的是文件名列表
music_names = os.listdir('music')
for name in music_names :
    path = 'music/' + name
    print(name)
    music_source.append(path)

#实现播放器
mixer.init()
while True :
    print(

    )
    command =
