from stegano import lsb
import time

#HIDE MESSAGE
image_path = "/Image path you want to encode/"
secret = lsb.hide(image_path, message= "Encode Message here")
secret.save("/save into a new image path with .png preferrably/")
# print("Encoding.....")
# time.sleep(5)
# print("Done Encoding Image")

#REVEAL MESSAGE
reveal_msg = lsb.reveal("/saved image path/")
print(reveal_msg)

