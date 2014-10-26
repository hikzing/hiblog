$(".flp label").each(function(){
    var sop = '<span class="ch">';
    var scl = '</span>';
    $(this).html(sop + $(this).html().split("").join(scl+sop) + scl);
    $(".ch:contains(' ')").html("&nbsp;");
})

var d;
$(".flp input").focus(function(){
    var tm = $(this).outerHeight()/2 *-1 + "px";
    $(this).next().addClass("focussed").children().stop(true).each(function(i){
        d = i*50;
        $(this).delay(d).animate({top: tm}, 200, 'easeOutBack');
    })
})

$(".flp input").blur(function(){
    if($(this).val() == "")
    {
        $(this).next().removeClass("focussed").children().stop(true).each(function(i){
            d = i*50;
            $(this).delay(d).animate({top: 0}, 500, 'easeInOutBack');
        })
    }
})

$("#submitForm").submit(function() {

    var url = "/admin/j/login";
    var email = $("input#email").val();
    var password = $("input#password").val();

    $.ajax({
           type: "POST",
           url: url,
           dataType:"json",
           data: JSON.stringify({
                    mail: email,
                    password: password
            }),
           cache: false,
           success: function(err_data)
           {
                if(err_data && err_data.err) {
                    var myhash = err_data.err;
                    for(var key in myhash) {
                        alert(myhash[key]);
                    }
                }
                else {
                    window.location.reload();  // 刷新界面使用 cookie实现登录
                }
           },
           error: function(data) {
                alert('500 error');
           }
         });

    return false;
});
