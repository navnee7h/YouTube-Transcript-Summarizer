from youtube_transcript_api import YouTubeTranscriptApi

text = YouTubeTranscriptApi.get_transcript('Etfomx4QEnk')
textFile = open('transcript.txt', 'w')
for i in range(len(text)):
    s = text[i]['text']
    textFile.writelines(s)
textFile.close()