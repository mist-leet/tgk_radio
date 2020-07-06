// TODO: Change url
function parse()
{
    url = "http://127.0.0.1:8005/status.xsl";
    var name = "0";
    var x = new XMLHttpRequest();
    x.open("GET", url, true);
    x.onreadystatechange = function ()
    {
    if (x.readyState === 4 && x.status === 200)
    {
        var doc = x.responseXML;
        console.log(doc.getElementsByClassName("streamstats")[6].textContent);
        //return doc.getElementsByClassName("streamstats")[6].textContent;
        document.getElementById("song_name").innerHTML = doc.getElementsByClassName("streamstats")[6].textContent;
    }
    };
    x.send(null);
    return 0;
}


setInterval(parse, 1000);