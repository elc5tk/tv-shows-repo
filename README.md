This API was made to give information on TV shows, with information including: a summary of the show, the status of the show, episode summaries, and the cast. The information in the API is integrated from the tvmaze API (link: https://www.tvmaze.com/api#show-cast). 

Lightsail link: https://tv-shows.3btlos01i71ki.us-east-1.cs.amazonlightsail.com

There are five GET endpoints in the API.

    The first is just the '/' path which welcomes the user and gives them insturctions on how to use the API. 

    The second is the '/Summary/{show}' path which returns a summary of the show the user has entered. 

    The third is the '/ShowStatus/{show}' path which returns whether the show is 'Running' or if it had 'Ended'.

    The fourth is the '/EpisodeSummmary/{show}/{season}/{episode}' path which returns the episode summary of the specified episode.

    The fifth path is the 'Cast/{show}' path which returns the names of the main characters and the actors who portray them.

Important note: The show variable is meant to be a string that accepts both numbers and letters because show titles contain both. However, the API from which the information is sourced assigns a numerical ID to each tv show. Therefore, if a number is entered that is not a tv show (like 90210) the API will return the information for the show attached to the ID number entered.  

