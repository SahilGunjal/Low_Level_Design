from abc import abstractmethod, ABC

"""
Interface Segregation: No client should be forced to depend on interfaces they don't use
"""


class MediaPlayer(ABC):
    @abstractmethod
    def playVideo(self):
        pass

    @abstractmethod
    def stopVideo(self):
        pass

    @abstractmethod
    def setVideoBrightness(self, brightness):
        pass

    @abstractmethod
    def startMusic(self):
        pass

    @abstractmethod
    def stopMusic(self):
        pass

    @abstractmethod
    def adjustMusicVolume(self, musicVolume):
        pass


# In this case, if we want to create a class called mp3Player (which has only audios) and we
# extend it with mediaPlayer then it has to implement all the unnecessary video methods, which
# violets the ISP.

# Solution -> create 2 separate interfaces AudioPlayer and VideoPlayer


class VideoPlayer(ABC):
    @abstractmethod
    def playVideo(self):
        pass

    @abstractmethod
    def stopVideo(self):
        pass

    @abstractmethod
    def setVideoBrightness(self, brightness):
        pass


class AudioPlayer(ABC):

    @abstractmethod
    def startMusic(self):
        pass

    @abstractmethod
    def stopMusic(self):
        pass

    @abstractmethod
    def adjustMusicVolume(self, musicVolume):
        pass


class mp3Player(AudioPlayer):
    def startMusic(self):
        print("Start the music")

    def stopMusic(self):
        print("Stop the music")

    def adjustMusicVolume(self, musicVolume):
        print("adjust the music")

# Same way we can create class AviVideoPlayer
