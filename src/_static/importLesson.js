$(function() {

    $("#import-button").on("click", function(event) {
        var fromUrl = $("#from-url").val();
        var toUrl = $("#to-url").val();

        var postData = {
            fromUrl: fromUrl,
            toUrl: toUrl
        }
        postLessonData(postData);
    })

    function postLessonData(postData) {
        if (postData.fromUrl == "" && postData.toUrl == "") {
            return window.alert("The URL fields are required")
        } else {
            $.ajax({
                url: '/lesson',
                type: "POST",
                dataType: "json",
                data: postData,
                error: function(response, exception) {
                    if (response.status == '200') {
                        window.alert("Lesson imported successfully")
                    }
                }
            });
        }
    }
});