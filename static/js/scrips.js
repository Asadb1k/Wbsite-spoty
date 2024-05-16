  let currentAudio = null;

  function togglePlayPause(element, audioUrl) {
    if (currentAudio && currentAudio.src !== audioUrl) {
      currentAudio.pause();
      currentAudio = null;
    }

    if (!currentAudio) {
      currentAudio = new Audio(audioUrl);
      currentAudio.play();
      element.classList.remove('fa-play');
      element.classList.add('fa-pause');
    } else {
      if (currentAudio.paused) {
        currentAudio.play();
        element.classList.remove('fa-play');
        element.classList.add('fa-pause');
      } else {
        currentAudio.pause();
        element.classList.remove('fa-pause');
        element.classList.add('fa-play');
      }
    }
  }