var audio = null;

function playSong(audioUrl) {
    if (audio) {
        audio.pause();
    }

    audio = new Audio(audioUrl);
    audio.play();
}

function stopSong() {
    if (audio) {
        audio.pause();
        audio.currentTime = 0;
    }
}Ф