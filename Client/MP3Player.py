import pygame
import os
 
class MP3Player(object):
    def __init__(self, file):
        self.file = file
        from mutagen.mp3 import MP3
        self.length = MP3(self.file).info.length
        self.begin = 0.0
        self.play_mp3(self.file)
 
    def get_pos(self):
        """
        获取当前播放进度
        :return:
        """
        game_pos = pygame.mixer.music.get_pos()
        if game_pos == -1:
            return -1
        return self.begin + game_pos / 1000
 
    def set_pos(self, value):
        """
        设置播放进度
        :param value: 秒
        :return:
        """
        if value >= self.length:
            dst = self.length
        else:
            dst = value
        self.play_mp3(self.file, dst)
 
    def play_mp3(self, mp3_file, pos=0.0):
        """
        播放mp3
        :param mp3_file:
        :param pos:
        :return:
        """
        if os.path.exists(mp3_file):
            pygame.mixer.init()
            pygame.mixer.music.load(mp3_file)
            pygame.mixer.music.play(start=pos)
            self.begin = pos
 
    @staticmethod
    def pause_mp3():
        """
        暂停播放
        :return:
        """
        pygame.mixer.music.pause()
 
    @staticmethod
    def unpause_mp3():
        """
        继续播放
        :return:
        """
        pygame.mixer.music.unpause()
 
    @staticmethod
    def stop_mp3():
        """
        停止播放  并 释放MP3文件
        :return:
        """
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()