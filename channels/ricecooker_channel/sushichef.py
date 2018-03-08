#!/usr/bin/env python

from le_utils.constants import format_presets, licenses, exercises
from le_utils.constants.languages import getlang  # see also getlang_by_name, getlang_by_alpha2
from ricecooker.chefs import SushiChef
from ricecooker.classes.nodes import TopicNode

from ricecooker.classes.nodes import DocumentNode, AudioNode, VideoNode, HTML5AppNode
from ricecooker.classes.files import DocumentFile, AudioFile, VideoFile, HTMLZipFile

from ricecooker.classes.nodes import ExerciseNode
from ricecooker.classes.questions import SingleSelectQuestion, MultipleSelectQuestion, InputQuestion, PerseusQuestion

from ricecooker.classes.licenses import get_license
from ricecooker.exceptions import raise_for_invalid_channel





class SampleChef(SushiChef):
    """
    The chef class that takes care of uploading channel to Kolibri Studio.
    We'll call its `main()` method from the command line script.
    """

    channel_info = {
        'CHANNEL_SOURCE_DOMAIN': 'source.org',                  # content provider's domain
        'CHANNEL_SOURCE_ID': 'sample-ricecooker-channel',       # an alphanumeric channel ID
        'CHANNEL_TITLE': 'Sample Ricecooker Channel',           # a humand-readbale title
        'CHANNEL_LANGUAGE': getlang('en').id,                   # language code of channel
        'CHANNEL_THUMBNAIL': 'http://quantlabs.net/blog/wp-content/uploads/2015/11/pythonlogo.jpg', # (optional) local path or url to image file
        'CHANNEL_DESCRIPTION': 'This channel was created from the files in the '
                               'content/ dir and the metadata provided in Python'
    }


    def construct_channel(self, *args, **kwargs):
        """
        Create ChannelNode and build topic tree.
        """
        channel = self.get_channel(*args, **kwargs)   # create ChannelNode from data in self.channel_info
        self.create_content_nodes(channel)
        self.create_exercise_nodes(channel)
        raise_for_invalid_channel(channel)
        return channel


    def create_content_nodes(self, channel):
        """
        This function uses the methods `add_child` and `add_file` to build the
        hierarchy of topic nodes and content nodes. Every content node is associated
        with the underlying file node.
        """
        topic1 = TopicNode(
                source_id='121232ms',
                title='Content Nodes',
                description='Put folder description here',
                author=None,
                language=getlang('en').id,
                thumbnail=None,
        )
        channel.add_child(topic1)

        # AUDIO
        topic11 = TopicNode(
                source_id='138iuh23iu',
                title='Audio Files',
                description='Put folder description here',
                author=None,
                language=getlang('en').id,
                thumbnail=None,
        )
        topic1.add_child(topic11)

        content11a = AudioNode(
                source_id='940ac8ff',
                title='Whale sounds',
                author='First Last (author\'s name)',
                description='Put file description here',
                language=getlang('en').id,
                license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
                thumbnail=None,
                files=[],
        )
        topic11.add_child(content11a)
        audio_file = AudioFile(
                path='./content/ricecooker-channel-files/Whale_sounds.mp3',
                language=getlang('en').id
        )
        content11a.add_file(audio_file)


        # DOCUMENTS
        topic12 = TopicNode(
            source_id='asanlksnaklsn',
            title='Document Nodes',
            description='Put folder description here',
            author=None,
            language=getlang('en').id,
            thumbnail=None,
        )
        topic1.add_child(topic12)

        content12a = DocumentNode(
              source_id='80b7136f',
              title='The Supreme Court\u2019s Ruling in Brown vs. Board of Education',
              author='First Last (author\'s name)',
              description='Put file description here',
              language=getlang('en').id,
              license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
              thumbnail=None,
              files=[DocumentFile(
                            path='./content/ricecooker-channel-files/commonlit_the-supreme-court-s-ruling-in-brown-vs-board-of-education_student.pdf',
                            language=getlang('en').id
                    )]
        )
        topic12.add_child(content12a)


        # HTML5 APPS
        topic13 = TopicNode(
                source_id='asasa331',
                title='HTML5App Nodes',
                description='Put folder description here',
                author=None,
                language=getlang('en').id,
                thumbnail=None,
        )
        topic1.add_child(topic13)

        content13a = HTML5AppNode(
              source_id='302723b4',
              title='Sample React app',
              author='First Last (author\'s name)',
              description='Put file description here',
              language=getlang('en').id,
              license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
              thumbnail='./content/ricecooker-channel-files/html5_react.jpg',
              files=[HTMLZipFile(
                          path='./content/ricecooker-channel-files/html5_react.zip',
                          language=getlang('en').id
                     )]
        )
        topic13.add_child(content13a)

        content13b = HTML5AppNode(
              source_id='3f91184e',
              title='Sample Vue.js app',
              author='First Last (author\'s name)',
              description='Put file description here',
              language=getlang('en').id,
              license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
              thumbnail='./content/ricecooker-channel-files/html5_vuejs.jpg',
              files=[HTMLZipFile(
                          path='./content/ricecooker-channel-files/html5_vuejs.zip',
                          language=getlang('en').id
                     )]
        )
        topic13.add_child(content13b)

        content13c = HTML5AppNode(
              source_id='0aec4296',
              title='Sample wget-scraped web content',
              author='First Last (author\'s name)',
              description='Put file description here',
              language=getlang('en').id,
              license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
              thumbnail='./content/ricecooker-channel-files/html5_wget_scraped.jpg',
              files=[HTMLZipFile(
                          path='./content/ricecooker-channel-files/html5_wget_scraped.zip',
                          language=getlang('en').id
                     )]
        )
        topic13.add_child(content13c)


        # VIDEOS
        topic14 = TopicNode(
                source_id='121213m3m3',
                title='Video Nodes',
                description='Put folder description here',
                author=None,
                language=getlang('en').id,
                thumbnail=None,
        )
        topic1.add_child(topic14)
        content14a = VideoNode(
                source_id='9e355995',
                title='Wave particle duality explained in 2 mins',
                author='First Last (author\'s name)',
                description='Put file description here',
                language=getlang('en').id,
                license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
                derive_thumbnail=True,  # video-specicig flag
                thumbnail=None,
                files=[VideoFile(
                            path='./content/ricecooker-channel-files/Wave_particle_duality.mp4',
                            language=getlang('en').id
                       )]
        )
        topic14.add_child(content14a)



    def create_exercise_nodes(self, channel):
        """
        This function adds a few exercise nodes to the channel content tree.
        TODO: handle exercises with embedded image links + base64 encoded data.
        """

        # EXERCISES
        topic2 = TopicNode(
                source_id='mdmdmai3i13',
                title='Exercise Nodes',
                description='Put folder description here',
                author=None,
                language=getlang('en').id,
                thumbnail=None,
        )
        channel.add_child(topic2)

        exercise2a = ExerciseNode(
                source_id='asisis92',
                title='A literary question',
                author='LE content team',
                description='Showcase of the simple exercises supported by Ricecooker and Studio',
                language=getlang('en').id,
                license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
                thumbnail=None,
                exercise_data={
                    'mastery_model': exercises.M_OF_N,         # or exercises.DO_ALL
                    'randomize': True,
                    'm': 2,
                    'n': 3,
                },
                questions=[
                    # MultipleSelectQuestion(
                    #         id='ex2aQ1',
                    #         question = "Which numbers are even?",
                    #         correct_answers = ["2", "4",],
                    #         all_answers = ["1", "2", "3", "4", "5"],
                    #         # hints?
                    # ),
                    # SingleSelectQuestion(
                    #         id='ex2aQ2',
                    #         question = "What is 2 times 3?",
                    #         correct_answer = "6",
                    #         all_answers = ["2", "3", "5", "6"],
                    #         # hints?
                    # ),
                    # InputQuestion(
                    #         id='ex2aQ3',
                    #         question = "Name a factor of 10.",
                    #         answers = ["1", "2", "5", "10"],
                    #         # hints?
                    # ),
                    SingleSelectQuestion(
                            id='exampleMarkdownText2',
                            question = """
Dr. Martin Luther King, Jr. (1929-1968) was a Baptist minister and a leader of the African American Civil Rights Movement. This article shares key details about Dr. King’s life and accomplishments, including his belief in equality and non-violence.

Dr. Martin Luther King, Jr., was a great leader. He inspired many people. He brought about changes that are important to everyone in the United States. In fact, he is known around the world. He was the youngest person to win the Nobel Peace Prize. That is a prize given to a person who is important to the world. It is a peace prize. He wanted people to change things peacefully. He thought that violence only led to more problems.

Dr. King used a way of changing things called non-violent protest. He saw that people were not treated fairly. He protested for civil rights. When he led marches, people were angry. But he was determined. Even though people shouted at him, he kept marching.

People who had been afraid to protest before were encouraged. They joined him. He was able to give them confidence. Together they would overcome. Soon thousands of people were with him. He was changing America.

He organized boycotts. A boycott means that people do not buy something or shop at a store or use a service. The boycott he led was the Montgomery Bus Boycott. Before that boycott in 1955, African Americans could not ride in the front of buses. They had to sit or stand in the back even if there were seats in the front. Only whites could have those front seats. It took months, but they won. They got the right to sit anywhere in the bus.

Dr. King influenced many people. He reached them with his books and speeches. He gave a very inspiring speech in Washington, D.C. People call it his “I Have a Dream” speech. In it he told about what he had seen, the changes that had happened, and what would happen in the future.

Today the United States celebrates his life with a special holiday every year. On that day, people remember what he accomplished. They think about how he has made a difference to everyone in America.

*What made Dr. Martin Luther King, Jr. a unique leader in the Civil Rights Movement?*
""",
                            correct_answer = "He worked for change through non-violent, peaceful protests.",
                            all_answers = [
                                "He worked for change through non-violent, peaceful protests.",
                                "He called for equal rights among all people.",
                                "He was the first Civil Rights leader to win a Nobel Peace Prize.",
                                "He was very afraid to march with other protesters.",
                            ],
                            # hints?
                    ),
                ]
        )
        topic2.add_child(exercise2a)

        # LOAD JSON DATA (as string) FOR PERSEUS QUESTIONS
        SAMPLE_PERSEUS_4_JSON = open('./content/ricecooker-channel-files/sample_perseus04.json','r').read()
        exercise2b = ExerciseNode(
                source_id='baszzzs1',
                title='Perseus questions',
                author='LE content team',
                description='An example exercise with Persus questions',
                language=getlang('en').id,
                license=get_license(licenses.CC_BY, copyright_holder='Copyright holder name'),
                thumbnail=None,
                exercise_data={
                    'mastery_model': exercises.M_OF_N,         # or exercises.DO_ALL
                    'randomize': True,
                    'm': 2,
                    'n': 3,
                },
                questions=[
                    PerseusQuestion(
                            id='ex2bQ4',
                            raw_data=SAMPLE_PERSEUS_4_JSON,
                            source_url='https://github.com/learningequality/sample-channels/blob/master/contentnodes/exercise/sample_perseus04.json'
                    ),
                ]
        )
        topic2.add_child(exercise2b)



if __name__ == '__main__':
    """
    This code will run when the sushi chef scripy is called on the command line.
    """
    chef = SampleChef()
    chef.main()

