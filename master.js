$(document).ready(function(){
    $('.select').on('click', function(){
        var rating = $(this).attr('id');

        //If ALL button pressed, show all movies
        //else show movies with the selected rating and hide others
        if(rating === 'ALL'){
          $('.element').show()
        }else{
            $('.element[data-rate='+rating+']').show();
            $('.element:not([data-rate='+rating+'])').hide();
        }
    });

    // Start playing the video whenever the trailer modal is opened
    $('.btn_expand').on('click', function(){

      //Get relevant information of the selected movie
      var title = $(this).siblings("p[class='title']").text();
      var year = $(this).siblings("span[class='year']").text();
      var story = $(this).siblings("p[class='story']").text();
      var poster_url = $(this).parents().siblings('.poster').attr('src');
      var rating = $(this).parents('div.element').data('rate');

      // Below code is taken from the provided file (fresh_tomatoes.py)
      var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
      var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
      $(".preview").empty().append($("<iframe></iframe>", {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
      }));
      //

      //Assign movie informtion to the modal fields
      $('#detailModal h4.modal-title').text(title);
      $('#detailModal img.poster_detail').attr('src',poster_url);
      $('#detailModal span.movie_rating').text(rating);
      $('#detailModal span.movie_year').text(year);
      $('#detailModal p.movie_story').text(story);
    });

    $('.hanging-close, .modal-backdrop').on('click',function (event) {
      // Remove the src so the player itself gets removed, as this is the only
      // reliable way to ensure the video stops playing in IE
      $(".preview").empty();
    });

    // Animate in the movies when the page loads
    $('.element').hide().first().show("fast", function showNext() {
      $(this).next("div").show("fast", showNext);
    });
});
