import json
import os
import unittest

from src.handlers import get_music_name, get_apple_music_url, get_spotify_music_url, get_default_message


class TestStringMethods(unittest.TestCase):

    def test_getMusicName_whenGetValidJson_expectValidNameString(self):
        # arrange
        expected_music_name = "Imagine Dragons - Warriors\nAlbum: Smoke + Mirrors (Deluxe)"
        with open(os.path.join("resources", "imagine_dragons.json"), 'r') as f:
            data = f.read()
        json_data = json.loads(data)

        # act
        actual_music_name = get_music_name(json_data)

        # assert
        self.assertEqual(actual_music_name, expected_music_name)

    def test_getAppleMusicUrl_whenGetValidJson_expectAppleMusicUrl(self):
        # arrange
        expected_music_url = "https://music.apple.com/us/album/warriors/1440831203?app=music&at=1000l33QU&i=1440831624&mt=1"
        with open(os.path.join("resources", "imagine_dragons.json"), 'r') as f:
            data = f.read()
        json_data = json.loads(data)

        # act
        actual_music_url = get_apple_music_url(json_data)

        # assert
        self.assertEqual(actual_music_url, expected_music_url)

    def test_getSpotifyMusicUrl_whenGetValidJson_expectSpotifyMusicUrl(self):
        # arrange
        expected_music_url = "https://open.spotify.com/track/1sWeSMifj6Z6kZyI6z3bRc"
        with open(os.path.join("resources", "imagine_dragons.json"), 'r') as f:
            data = f.read()
        json_data = json.loads(data)

        # act
        actual_music_url = get_spotify_music_url(json_data)

        # assert
        self.assertEqual(actual_music_url, expected_music_url)

    def test_getDefaultMessage_whenSpecificationSame_expectTechWriterMessage(self):
        # arrange
        expected_message = "Send me some audio, and I'll name the song for you"

        # act
        actual_message = get_default_message()

        # assert
        self.assertEqual(actual_message, expected_message)


if __name__ == '__main__':
    unittest.main()
