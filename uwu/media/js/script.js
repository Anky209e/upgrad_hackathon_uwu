$(".navT").on("click", function () {
    $(this).toggleClass("active");
    $("#menu").toggleClass("open");
    $(".content").toggleClass("shift");


})
$(".social-media-box").tilt({
    glare: true,
    maxGlare: 0.5,
    reset: true,
    scale: 1.05,
    easing: "cubic-bezier(.03,.98,.52,.99)",
    perspective: 1000,
    maxTilt: 50
});

const audiotagDiv = document.getElementById('audiotag');
audiotagDiv.addEventListener('keypress',function(e){
    document.getElementById('jutsu').play();
})

function play() {
    var audio = document.getElementById("jutsu");
    audio.play();
}