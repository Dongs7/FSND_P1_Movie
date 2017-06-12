import webbrowser
import os
import re

main_page_head ='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="master.css">
    <link href="https://fonts.googleapis.com/css?family=Oleo+Script" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="master.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
</head>
'''
main_page_body ='''
<body>
     <header class="nav navbar">
        <div class="container">
            <h3 class="center">Fresh Tomatoes Movie Trailers</h3>
        </div> 
     </header>
     
    <div class="main_wrapper">
        <div class="container">
            <div class="row">
                <button class="btn btn-primary select" id="ALL">SHOW ALL</button>
                <span class="space"></span>
                <button class="btn btn-success select" id="G">G</button>
                <button class="btn btn-warning select" id="PG">PG</button>
                <button class="btn btn-info select" id="PG-13">PG-13</button>
                <button class="btn btn-danger select" id="R">R</button>
            </div>      <!-- row -->
            {rand_tile}
        </div>      <!-- container -->      
    </div>      <!-- main_wrapper -->

    <!-- Modal Section -->  
    <div class="modal fade" id="detailModal" role="dialog" data-backdrop="static">
        <div class="modal-dialog">
            <div class="modal-content">
                <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
                    <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
                </a>
                <div class="modal-header">
                    <h4 class="modal-title center"></h4>
                </div>

                <div class="modal-body">

                    <div class="body_wrapper">
                        <div class="row">
                            <div class="preview"></div>
                        </div>

                        <div class="row">
                            <div class="poster_big col-md-6">
                                <img class="poster_detail" src="">
                            </div>

                            <div class="right col-md-6">
                                <div class="movie_info">
                                    <label for="_year"> Released Year : </label><br>
                                    <span id="_year" class="movie_year"></span><br>
                                    <hr class="spacer">
                                    <label for="_rating"> Movie Rating : </label><br>
                                    <span id="_rating" class="movie_rating"></span><br>
                                    <hr class="spacer">
                                    <label for="_story"> Movie Story : </label><br>
                                    <p id="_story" class="movie_story"></p><br>
                                </div>        <!-- movie_info -->
                            </div>        <!-- right -->
                        </div>        <!-- row -->
                    </div>        <!-- body_wrapper-->
                </div>        <!-- modal-body -->
            </div>        <!-- modal-content -->
        </div>        <!-- modal-dialog --> 
    </div>        <!---->
    <!-- Modal Section Ends -->
      
  </body> 
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-xs-12 col-sm-6 col-lg-4 element" data-rate="{rating}">
    <div class="info">
        <div class="info_box center">
            <p class="title">{title}</p>
            <span class="year">{year}</span>
            <hr style="width:50%">
            <p class="story">{story}</p>
            <input type="button" class="btn_expand" value="More Info" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#detailModal"/>
        </div> 
    </div>
    <img class="poster" src="{poster_url}"></img>
</div>
'''


def create_movie_tile(movies):
    # The HTML content for this section of the page
    content =''
    for movie in movies:
        # Extract youtube trailer ID
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            poster_url = movie.poster_url,
            rating = movie.rating,
            story = movie.story,
            title = movie.title,
            year = movie.year,
            trailer_youtube_id=trailer_youtube_id,
            )
    return content


def open_page(movies):
    # Create or overwrite the output file
    output_file = open('project1.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_body.format(
        rand_tile = create_movie_tile(movies))
    
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)


