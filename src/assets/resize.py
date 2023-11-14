from moviepy.editor import VideoFileClip

def resize_video(input_path, output_path, new_width, new_height):
    # Load video clip
    video_clip = VideoFileClip(input_path)

    # Resize the video
    resized_clip = video_clip.resize(width=new_width, height=new_height)

    # Write the resized video to the output file
    resized_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Close the clips
    video_clip.close()
    resized_clip.close()

# Example usage
input_video_path = "prueba.mp4"
output_video_path = "prueba_resize.mp4"
new_width = 640  # set your desired width
new_height = 480  # set your desired height

resize_video(input_video_path, output_video_path, new_width, new_height)