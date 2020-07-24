// TODO: Change url
var prev_name = "";
var name = "";

function parse() {
    url = "http://127.0.0.1:8005/status.xsl";
    prev_name = name;
    var x = new XMLHttpRequest();
    x.open("GET", url, true);
    x.onreadystatechange = function () {
        if (x.readyState === 4 && x.status === 200) {
            var doc = x.responseXML;
            name = doc.getElementsByClassName("streamstats")[6].textContent;
            document.getElementById("song_name").innerHTML = name;
            // TODO: delete log
            //console.log("prev : " + prev_name);
            //console.log("name  : " + name);
            if (prev_name !== name) {
                $.ajax({
                    url: "post_ajax_req",
                    type: "POST",
                    data: {'get_name': name},
                    datatype: "json",
                    headers: {"X-CSRFToken": "{{ csrf_token }}"}, // for csrf token
                    success: function (res) {
                        // TODO: put in <img>
                        document.getElementById("cover").src = res.url;
                        console.log(res.url);
                    },

                });
            } else {
                prev_name = name;
            }
            return false;
        }
    };
    x.send(null);
    return 0;
}


setInterval(parse, 1000);