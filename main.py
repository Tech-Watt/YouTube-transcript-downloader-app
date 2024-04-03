import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi as yta


def download_transcript(link):
        id = link.split('/')
        vid_id = id[-1]
        data = yta.get_transcript(vid_id)
        final_data = ''
        for val in data:
            for key, value in val.items():
                if key == 'text':
                    final_data += value
        processed_data = final_data.splitlines()
        clean_data = ' '.join(processed_data)
        return clean_data


st.title('Youtube Transcript Downloader')
video_link = st.text_input(label='paste video url here')
if video_link is not None:
    if st.button('Send'):
        transcript = download_transcript(video_link)
        st.write(transcript)

     