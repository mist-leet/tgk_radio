function f() {
    var song_name = document.getElementById("song_name").textContent;
    document.getElementById("path").innerHTML = song_name;
}
setInterval(f, 1000);
