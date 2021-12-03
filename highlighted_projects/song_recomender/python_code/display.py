from IPython.core.display import display
from IPython.display import IFrame

def recommend(track_id):
	display(IFrame(src=f"https://open.spotify.com/embed/track/{track_id}",
               width="320",
               height="80",
               frameborder="0",
               allowtransparency="true",
               allow="encrypted-media",
              ))