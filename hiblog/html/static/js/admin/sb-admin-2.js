
$('#blogForm').submit(function() {

    var url = "/admin/j/blog/save";
    var author = $('input#author').val();
    var title = $('input#title').val();
    var content = $('textarea#content').val();
    var _id = $('input#blog_id').val();

    $.ajax({
        type: "POST",
        url: url,
        dataType: "json",
        data: JSON.stringify({
            author: author,
            title: title,
            content: content,
            _id: _id
        }),
        cache: false,
        success: function(err_data) {
            if(err_data && err_data.err) {
                var myhash = err_data.err;
                for(var key in myhash) {
                    var err_help = $('#' + key).next();
                    err_help.removeClass('hide');
                    err_help.text(myhash[key]);
                }
            }
            else {
                alert('保存成功');
            }
        },
        error: function() {
            '保存失败';
        }

    });

    return false;

})

function delBlog(id) {
    $.ajax({
        type: 'POST',
        url: '/admin/j/blog/rm/' + id,
        dataType: 'JSON',
        data: {},
        cache: false,
        success: function() {
            window.location.reload()
        },
        error: function() {
            alert('删除失败');
        }

    })
    return false;
}

$(function() {

    $('#side-menu').metisMenu();

});

//Loads the correct sidebar on window load,
//collapses the sidebar on window resize.
// Sets the min-height of #page-wrapper to window size
$(function() {
    $(window).bind("load resize", function() {
        topOffset = 50;
        width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            $('div.navbar-collapse').addClass('collapse')
            topOffset = 100; // 2-row-menu
        } else {
            $('div.navbar-collapse').removeClass('collapse')
        }

        height = (this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height;
        height = height - topOffset;
        if (height < 1) height = 1;
        if (height > topOffset) {
            $("#page-wrapper").css("min-height", (height) + "px");
        }
    })
})
