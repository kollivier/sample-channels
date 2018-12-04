#!/usr/bin/env python

from le_utils.constants import licenses, exercises
from le_utils.constants.languages import getlang  # see also getlang_by_name, getlang_by_alpha2
from ricecooker.chefs import SushiChef
from ricecooker.classes.nodes import TopicNode

from ricecooker.classes.nodes import DocumentNode, AudioNode, VideoNode, HTML5AppNode
from ricecooker.classes.files import DocumentFile, AudioFile, VideoFile, HTMLZipFile

from ricecooker.classes.nodes import ExerciseNode
from ricecooker.classes.questions import SingleSelectQuestion, MultipleSelectQuestion, InputQuestion, PerseusQuestion

from ricecooker.classes.licenses import get_license
from ricecooker.exceptions import raise_for_invalid_channel

from ricecooker.config import LOGGER
import logging
LOGGER.setLevel(logging.INFO)



class KamkalimaChef(SushiChef):
    """
    The chef class that takes care of uploading channel to Kolibri Studio.
    We'll call its `main()` method from the command line script.
    """

    channel_info = {
        'CHANNEL_SOURCE_DOMAIN': 'kamkalima.com',                  # content provider's domain
        'CHANNEL_SOURCE_ID': 'kds-example-test',       # an alphanumeric channel ID
        'CHANNEL_TITLE': 'Kamkalima  -- كم كلمة ',           # a humand-readbale title
        'CHANNEL_LANGUAGE': getlang('ar').id,                   # language code of channel
        'CHANNEL_THUMBNAIL': './content/kk-logo.png',
        'CHANNEL_DESCRIPTION': "Improve your school's Arabic learning experience with an engaging and beneficial platform, brought to you by teachers to teachers.",
    }


    def construct_channel(self, *args, **kwargs):
        """
        Create ChannelNode and build topic tree.
        """
        channel = self.get_channel(*args, **kwargs)   # create ChannelNode from data in self.channel_info
        self.create_content_nodes(channel)
        return channel


    def create_content_nodes(self, channel):
        """
        This function uses the methods `add_child` and `add_file` to build the
        hierarchy of topic nodes and content nodes. Every content node is associated
        with the underlying file node.
        """
        content_nodes_folder = TopicNode(
            source_id='121232ms',
            title='Content Nodes',
            description='Put folder description here',
            author=None,
            language=getlang('en').id,
            thumbnail=None,
        )
        channel.add_child(content_nodes_folder)



        # HTML5 APPS
        html5apps_folder = TopicNode(
            source_id='asasa331',
            title='HTML5App Nodes',
            description='Put folder description here',
            author=None,
            language=getlang('en').id,
            thumbnail=None,
        )
        content_nodes_folder.add_child(html5apps_folder)

        html5_node_a = HTML5AppNode(
            source_id='302723b4',
            title='الصَّديقانِ في الصَّحْراءِ',
            author='كم كلمة',
            description='الكاتب: كم كلمة   النّاشر: دار العلوم',
            language=getlang('ar').id,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
            thumbnail='./content/two_friends_in_desert/desert.jpg',
            files=[HTMLZipFile(
                      path='./content/two_friends_in_desert.zip',
                      language=getlang('ar').id
                 )]
        )
        html5apps_folder.add_child(html5_node_a)



        # AUDIO
        audio_nodes_folder = TopicNode(
            source_id='138iuh23iu',
            title='Audio Files Folder',
            description='Put folder description here',
            author=None,
            language=getlang('en').id,
            thumbnail=None,
        )
        content_nodes_folder.add_child(audio_nodes_folder)

        audio_node = AudioNode(
            source_id='940ac8ff',
            title='النّحلةُ',
            author='Kamkalima',
            description='الملخّص: يربط "أنشتاين" انقراض النّحل باقتراب نهاية العالم، لذا يشرح الكاتب خصائص هذه الحشرة وكيفيّة عملها وظاهرة "السّكر" الّتي تتميّز بها.',
            language=getlang('ar').id,
            license=get_license(licenses.CC_BY, copyright_holder='Kamkalima +  مجلّة دو- ري-مي (بتصرّف)'),
            thumbnail='./content/bees/bees.jpg',
            files=[],
        )
        audio_nodes_folder.add_child(audio_node)
        audio_file = AudioFile(
            path='./content/listening-file-1535521351.mp3',
            language=getlang('ar').id
        )
        audio_node.add_file(audio_file)



        exercise2a = ExerciseNode(
            source_id='asisis9',
            title='Bees exercise',
            author='Kamkalima',
            description='A simple multiple-choice exercise supported by Ricecooker and Studio',
            language=getlang('ar').id,
            license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
            thumbnail=None,
            exercise_data={
                'mastery_model': exercises.M_OF_N,         # or exercises.DO_ALL
                'randomize': False,
                'm': 1,
                'n': 1,
            },
            questions=[
                SingleSelectQuestion(
                        id='ex2aQ2',
                        question = 'إنَّ كلمةَ "انقراض" في الجملةِ: "عندَ اِنْقِراضِ النّحلِ تقتربُ نهايةُ العالمِ" تعني:',
                        correct_answer = "فناء",
                        all_answers = ["زراعة", "انتشار", "فناء", "الإصابة بالمرض"]
                        # hints?
                )
            ]
        )
        audio_nodes_folder.add_child(exercise2a)




if __name__ == '__main__':
    """
    This code will run when the sushi chef scripy is called on the command line.
    """
    chef = KamkalimaChef()
    chef.main()

