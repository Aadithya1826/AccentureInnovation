$(document).ready(function () {
    $('#crime-form').on('submit', function (event) {
        event.preventDefault();
        
        const crime_scene_data = $('#crime_scene_data').val();
        const chapter_title = $('#chapter_title').val();
        
        $.ajax({
            url: '/generate',
            method: 'POST',
            data: {
                crime_scene_data: crime_scene_data,
                chapter_title: chapter_title
            },
            success: function (response) {
                $('#scene-description').text(response.scene_description);
                $('#novel-chapter').text(response.novel_chapter);
            }
        });
    });
});
