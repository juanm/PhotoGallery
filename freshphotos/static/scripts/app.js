// wait until the images load to run this code
$(window).load(function(){
    // set the container width to be the entire width of the browser
    var view_width = $(window).width();
    $('#carousel').css('width', view_width);
 
    // move the list of images to the right so that the first image stays centralized on the browser
    var img_width = $('#carousel ul li:first-child').outerWidth();
    var left_offset = (view_width - img_width) / 2;
 
    $('#carousel ul').attr('style', 'left: '+left_offset+'px;');
 
    // apply a special style to the first item of the list
    $('#carousel ul li:first-child').addClass('active');
 
    // Set up the list of images to be animated when any of its CSS properties change values
    $('#carousel ul').addClass('animate');
 
    // when the user click next run
    $('#carousel .next').click(function() {
 
        // find out the left offset need for the next image to be centralized (in relation to the wrapper)
        var next_img_width = $('#carousel li.active').next().outerWidth();
        var next_img_offset = (view_width - next_img_width) / 2;
 
        // find out the offset of the next image in relation to the list of images
        var next_img_position = $('#carousel li.active').next().position();
 
        // subtract the two and apply the result as the new offset of the list of images
        var list_left_offset = next_img_offset - next_img_position.left;
        $('#carousel ul').attr('style', '-webkit-transform: translate3d('+list_left_offset+'px, 0px, 0px);');
 
        // remove the special style from the image that was previously centralized and apply it to the newly centralized image
        $('#carousel ul li.active').removeClass('active').next().addClass('active');
    });
});


