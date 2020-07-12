document.getElementById('jcp-volume').oninput=function setVolume (){
   var mediaClip = document.getElementById("playerStream");
   mediaClip.volume = document.getElementById("jcp-volume").value;
}
let bl=true;
   document.getElementById('btnId').onclick=function SupBtn(){
    if(bl){
      document.getElementById('playerStream').muted=false;
      bl=false;
      document.getElementById('imgPl').src="static/images/stopPng.png";
      document.getElementById('playerStream').play();
      document.getElementById('circle1').style.animationPlayState = 'running';
      document.getElementsByClassName('wave')[0].style.animationPlayState = 'running';
      document.getElementsByClassName('wave')[1].style.animationPlayState = 'running';
      document.getElementsByClassName('wave')[2].style.animationPlayState = 'running';
      document.getElementsByClassName('wave')[3].style.animationPlayState = 'running';
    }else
    {
      vl=document.getElementById('playerStream').volume;
      bl=true;
      document.getElementById('imgPl').src="static/images/Play.png";
      document.getElementById('playerStream').muted=true;
      document.getElementById('circle1').style.animationPlayState = 'paused';
      document.getElementsByClassName('wave')[0].style.animationPlayState = ' paused';
      document.getElementsByClassName('wave')[1].style.animationPlayState = ' paused';
      document.getElementsByClassName('wave')[2].style.animationPlayState = ' paused';
      document.getElementsByClassName('wave')[3].style.animationPlayState = ' paused';
    }
  }