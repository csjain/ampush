
function getURLParameter(name) {
  return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search) || [null, ''])[1].replace(/\+/g, '%20')) || null;
}

function track(page) {
var url = "/track?utm_id=" + getURLParameter("utm_id") + "&page=" + page
$.ajax({url: url, success: function(result){
        }});
}