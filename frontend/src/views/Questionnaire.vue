<template>
  <v-container fluid justify-center>
    <v-form ref="form">

      <v-layout row wrap justify-center mb-8>
        <v-flex xs12 md6 lg4>
          <v-text-field label="Name" v-model="name" :rules="inputRequiredRule"></v-text-field>
        </v-flex>
      </v-layout>

      <h1 class="mb-4">Youtube</h1>
      <div> Select up to 5 of your favourite Youtube video categories</div>
      <div id="youtube1">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="First Choice" v-model="youtubeCategory1" :items="inputYoutube" :rules="inputRequiredRule"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="youtube1btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="youtubeShow2">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
        </div>
      </div>

      <div id="youtube2" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Second Choice" v-model="youtubeCategory2" :items="inputYoutube"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="youtube2btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="youtubeShow3">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="youtubeRemove2">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="youtube3" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Third Choice" v-model="youtubeCategory3" :items="inputYoutube"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="youtube3btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="youtubeShow4">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="youtubeRemove3">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="youtube4" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Fourth Choice" v-model="youtubeCategory4" :items="inputYoutube"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="youtube4btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="youtubeShow5">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="youtubeRemove4">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="youtube5" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Fifth Choice" v-model="youtubeCategory5" :items="inputYoutube"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="youtube5btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="youtubeRemove5">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>
      <div class="mb-12"></div>

      <h1 class="mb-4">Books</h1>
      <div>Select up to 5 of your favourite book subjects</div>

      <div id="book1">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="First Choice" v-model="bookCategory1" :items="inputBook"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="book1btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="bookShow2">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
        </div>
      </div>

      <div id="book2" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Second Choice" v-model="bookCategory2" :items="inputBook"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="book2btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="bookShow3">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="bookRemove2">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="book3" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Third Choice" v-model="bookCategory3" :items="inputBook"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="book3btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="bookShow4">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="bookRemove3">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="book4" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Fourth Choice" v-model="bookCategory4" :items="inputBook"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="book4btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="bookShow5">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="bookRemove4">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="book5" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Fifth Choice" v-model="bookCategory5" :items="inputBook"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="book5btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="bookRemove5">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div class="mb-12"></div>

      <h1 class="mb-4">Movies</h1>
      <div>Select up to 5 of your favourite movie genres</div>

      <div id="movie1">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="First Choice" v-model="movieGenre1" :items="inputMovieGenre" :rules="inputRequiredRule"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="movie1btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="movieShow2">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
        </div>
      </div>

      <div id="movie2" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Second Choice" v-model="movieGenre2" :items="inputMovieGenre"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="movie2btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="movieShow3">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="movieRemove2">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="movie3" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Third Choice" v-model="movieGenre3" :items="inputMovieGenre"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="movie3btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="movieShow4">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="movieRemove3">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="movie4" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Fourth Choice" v-model="movieGenre4" :items="inputMovieGenre"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="movie4btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="movieShow5">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="movieRemove4">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="movie5" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Fifth Choice" v-model="movieGenre5" :items="inputMovieGenre"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="movie5btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="movieRemove5">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div class="mb-12"></div>

      <v-layout row wrap justify-center mb-8>
        <v-flex xs12 md6 lg4>
          <div>List your preferred languages</div>
          <v-autocomplete v-model="movieLanguage" :items="inputMovieLang" label="Language" multiple chips deletable-chips :rules="inputRequiredRule"></v-autocomplete>
        </v-flex>
      </v-layout>

      <v-layout row wrap justify-center mb-8>
        <v-flex xs12 md6 lg4>
          <div>Pick a minimum IMDB value</div>
          <v-slider v-model="movieImdb" :max="10" :min="0" :step="0.1" :thumb-size="30" thumb-label mb-8></v-slider>
        </v-flex>
      </v-layout>

      <h1 class="mb-4">Spotify</h1>
      <div>Select up to 3 of your favourite artists</div>
      <div id="spotifyArtist1">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="First Choice" v-model="spotifyArtist1" :items="inputSpotifyArtist" :rules="inputRequiredRule"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="artist1btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="artistShow2">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
        </div>
      </div>

      <div id="spotifyArtist2" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Second Choice" v-model="spotifyArtist2" :items="inputSpotifyArtist"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="artist2btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="artistShow3">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="artistRemove2">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="spotifyArtist3" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Third Choice" v-model="spotifyArtist3" :items="inputSpotifyArtist"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="artist3btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="artistRemove3">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div class="mb-8"></div>
      <div>Select up to 3 of your favourite tracks</div>
      <div id="spotifyTrack1">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="First Choice" v-model="spotifyTrack1" :items="inputSpotifyTrack" :rules="inputRequiredRule"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="track1btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="trackShow2">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
        </div>
      </div>

      <div id="spotifyTrack2" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Second Choice" v-model="spotifyTrack2" :items="inputSpotifyTrack"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="track2btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="trackShow3">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="trackRemove2">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="spotifyTrack3" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Third Choice" v-model="spotifyTrack3" :items="inputSpotifyTrack"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="track3btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="trackRemove3">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div class="mb-8"></div>
      <div>Select up to 5 of your favourite genres</div>
      <div id="spotifyGenre1">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="First Choice" v-model="spotifyGenre1" :items="inputSpotifyGenre" :rules="inputRequiredRule"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="sGenre1btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="sGenreShow2">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
        </div>
      </div>

      <div id="spotifyGenre2" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Second Choice" v-model="spotifyGenre2" :items="inputSpotifyGenre"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="sGenre2btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="sGenreShow3">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="sGenreRemove2">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="spotifyGenre3" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Third Choice" v-model="spotifyGenre3" :items="inputSpotifyGenre"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="sGenre3btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="sGenreShow4">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="sGenreRemove3">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="spotifyGenre4" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Fourth Choice" v-model="spotifyGenre4" :items="inputSpotifyGenre"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="sGenre4btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small indigo tooltip" @click="sGenreShow5">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate mdi mdi-plus theme--dark"></i>
            </span>
            <span class="tooltiptext">Add Row</span>
          </button>
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="sGenreRemove4">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div id="spotifyGenre5" style="display:none">
        <v-layout row wrap justify-center>
          <v-flex xs12 md6 lg4>
            <v-autocomplete label="Fifth Choice" v-model="spotifyGenre5" :items="inputSpotifyGenre"></v-autocomplete>
          </v-flex>
        </v-layout>
        <div id="sGenre5btn">
          <button type="button" class="mx-2 v-btn v-btn--contained v-btn--fab v-btn--round theme--dark v-size--small red tooltip" @click="sGenreRemove5">
            <span class="v-btn__content">
              <i aria-hidden="true" class="v-icon notranslate theme--dark">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" role="img" aria-hidden="true" class="v-icon__svg">
                  <path d="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z"></path>
                </svg></i>
            </span>
            <span class="tooltiptext">Remove Row</span>
          </button>
        </div>
      </div>

      <div class="mb-12"></div>
      <v-btn text class="success mx-0 mt-3" @click="submit">Let's Go</v-btn>
    </v-form>
  </v-container>
</template>

<script>
export default {
  data: () => {
    return {
      name: "",
      youtubeCategory1: "",
      youtubeCategory2: "",
      youtubeCategory3: "",
      youtubeCategory4: "",
      youtubeCategory5: "",
      bookCategory1: "",
      bookCategory2: "",
      bookCategory3: "",
      bookCategory4: "",
      bookCategory5: "",
      movieGenre1: "",
      movieGenre2: "",
      movieGenre3: "",
      movieGenre4: "",
      movieGenre5: "",
      movieLanguage: [],
      movieImdb: 0,
      spotifyArtist1: "",
      spotifyArtist2: "",
      spotifyArtist3: "",
      spotifyTrack1: "",
      spotifyTrack2: "",
      spotifyTrack3: "",
      spotifyGenre1: "",
      spotifyGenre2: "",
      spotifyGenre3: "",
      spotifyGenre4: "",
      spotifyGenre5: "",
      inputRequiredRule: [(v) => v.length > 0 || "Required"],
      autocompleteMax3Rule: [
        (v) => v.length > 0 || "Required",
        (v) => v.length <= 3 || "Maximum 3 choices",
      ],
      autocompleteMax5Rule: [
        (v) => v.length > 0 || "Required",
        (v) => v.length <= 5 || "Maximum 5 choices",
      ],
      languages: ["English", "Mandarin", "Malay", "Tamil"],
      inputYoutube: ['Shorts', 'Entertainment', 'News & Politics', 'Howto & Style', 'Education', 'Gaming', 'Videoblogging', 'People & Blogs', 'Comedy', 'Trailers', 'Science & Technology', 'Shows', 'Sci-Fi/Fantasy', 'Thriller', 'Film & Animation', 'Autos & Vehicles', 'Music', 'Horror', 'Foreign', 'Pets & Animals', 'Sports', 'Travel & Events', 'Short Movies', 'Anime/Animation', 'Movies', 'Family', 'Drama', 'Documentary', 'Comedy', 'Classics', 'Action/Adventure'],
      youtubeCategories: {'Sci-Fi/Fantasy': '40', 'Entertainment': '24', 'Science & Technology': '28', 'Sports': '17', 'Pets & Animals': '15', 'Music': '10', 'Action/Adventure': '32', 'Comedy': '34', 'Shows': '43', 'Gaming': '20', 'Classics': '33', 'Shorts': '42', 'Anime/Animation': '31', 'Travel & Events': '19', 'Howto & Style': '26', 'Trailers': '44', 'Short Movies': '18', 'Thriller': '41', 'News & Politics': '25', 'Drama': '36', 'Movies': '30', 'Videoblogging': '21', 'Foreign': '38', 'Documentary': '35', 'Autos & Vehicles': '2', 'People & Blogs': '22', 'Family': '37', 'Education': '27', 'Horror': '39', 'Film & Animation': '1'},
      inputBook: ['Adult', 'Anthologies', 'Art', 'Audiobooks', 'Biographies', 'Body', 'Business', 'Children', 'Comics', 'Contemporary', 'Cooking', 'Crime', 'Engineering', 'Entertainment', 'Fantasy', 'Fiction', 'Food', 'Health', 'History', 'Horror', 'Investing', 'Literary', 'Literature', 'Manga', 'Media-help', 'Memoirs', 'Mind', 'Mystery', 'Nonfiction', 'Religion', 'Romance', 'Science', 'Self', 'Spirituality', 'Sports', 'Superheroes', 'Technology', 'Thrillers', 'Travel', 'Women', 'Young'],
      inputMovieGenre: ['Action', 'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Game-Show', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Talk-Show', 'Thriller', 'War', 'Western'],
      inputMovieLang: ['Abkhazian', 'Aboriginal', 'Acholi', 'Afar', 'Afrikaans', 'Akan', 'Albanian', 'Algonquin', 'American Sign Language', 'Amharic', 'Apache languages', 'Arabic', 'Aragonese', 'Aramaic', 'Armenian', 'Aromanian', 'Assamese', 'Assyrian Neo-Aramaic', 'Athapascan languages', 'Australian Sign Language', 'Awadhi', 'Aymara', 'Azerbaijani', 'Bable', 'Baka', 'Balinese', 'Bambara', 'Bashkir', 'Basque', 'Bassari', 'Belarusian', 'Bemba', 'Bengali', 'Berber languages', 'Bhojpuri', 'Bicolano', 'Bislama', 'Bodo', 'Bosnian', 'Brazilian Sign Language', 'Breton', 'British Sign Language', 'Bulgarian', 'Burmese', 'Cantonese', 'Catalan', 'Central American Indian languages', 'Chamorro', 'Chaozhou', 'Chechen', 'Cherokee', 'Cheyenne', 'Chhattisgarhi', 'Chinese', 'Cornish', 'Corsican', 'Cree', 'Creek', 'Crimean Tatar', 'Croatian', 'Crow', 'Czech', 'Danish', 'Dari', 'Dinka', 'Divehi', 'Dogri', 'Dutch', 'Dyula', 'Dzongkha', 'East-Greenlandic', 'Eastern Frisian', 'Egyptian (Ancient)', 'English', 'Esperanto', 'Estonian', 'Ewe', 'Faliasch', 'Faroese', 'Filipino', 'Finnish', 'Flemish', 'Fon', 'French', 'French Sign Language', 'Frisian', 'Fulah', 'Fur', 'Ga', 'Gaelic', 'Galician', 'Gallegan', 'Georgian', 'German', 'German Sign Language', 'Greek', 'Greek, Ancient (to 1453)', 'Greenlandic', 'Guarani', 'Gujarati', 'Gumatj', 'Haida', 'Haitian', 'Haitian; Haitian Creole', 'Hakka', 'Haryanvi', 'Hassanya', 'Hausa', 'Hawaiian', 'Hebrew', 'Herero', 'Himachali', 'Hindi', 'Hmong', 'Hokkien', 'Hopi', 'Hungarian', 'Ibo', 'Icelandic', 'Icelandic Sign Language', 'Igbo', 'Indian Sign Language', 'Indonesian', 'Interlingue', 'Inuktitut', 'Inupiaq', 'Irish', 'Irula', 'Italian', 'Japanese', 'Japanese Sign Language', 'Javanese', 'Jola-Fonyi', "Ju'hoan", 'Kabuverdianu', 'Kabyle', 'Kalaallisut', 'Kalmyk-Oirat', 'Kannada', 'Karen', 'Kashmiri', 'Kazakh', 'Khanty', 'Khasi', 'Khmer', 'Kikuyu', 'Kinyarwanda', 'Kirghiz', 'Kirundi', 'Klingon', 'Kodava', 'Konkani', 'Korean', 'Korean Sign Language', 'Kriolu', 'Kru', 'Kudmali', 'Kuna', 'Kurdish', 'Ladakhi', 'Ladino', 'Lao', 'Latin', 'Latvian', 'Letzeburgesch', 'Lingala', 'Lithuanian', 'Low German', 'Luxembourgish', 'Macedonian', 'Magahi', 'Maithili', 'Malagasy', 'Malay', 'Malayalam', 'Malinka', 'Maltese', 'Mandarin', 'Mandingo', 'Manipuri', 'Maori', 'Mapudungun', 'Marathi', 'Mari', 'Marshall', 'Marshallese', 'Masai', 'Maya', 'Mende', 'Micmac', 'Middle English', 'Min Nan', 'Minangkabau', 'Mirandese', 'Mixtec', 'Mizo', 'Mohawk', 'Moldavian', 'Mongolian', 'Montagnais', 'Morisyen', 'Nagpuri', 'Nahuatl', 'Nama', 'Navajo', 'Neapolitan', 'Nenets', 'Nepali', 'Norse, Old', 'North American Indian', 'North Ndebele', 'Northern Sami', 'Norwegian', 'Norwegian Nynorsk', 'Nushi', 'Nyanja', 'Occitan', 'Ojibwa', 'Ojihimba', 'Old English', 'Oriya', 'Papiamento', 'Parsee', 'Pawnee', 'Persian', 'Peul', 'Polish', 'Polynesian', 'Portuguese', 'Pular', 'Punjabi', 'Purepecha', 'Pushto', 'Quechua', 'Quenya', 'Raeto-Romance', 'Rajasthani', 'Rhaetian', 'Romanian', 'Romany', 'Russian', 'Russian Sign Language', 'Ryukyuan', 'Saami', 'Samoan', 'Sanskrit', 'Sardinian', 'Scanian', 'Scots', 'Scottish Gaelic', 'Serbian', 'Serbo-Croatian', 'Shanghainese', 'Shona', 'Shoshoni', 'Shuar', 'Sicilian', 'Sign Languages', 'Sindarin', 'Sindhi', 'Sinhalese', 'Sioux', 'Slovak', 'Slovenian', 'Somali', 'Songhay', 'Soninke', 'Sorbian languages', 'Southern Sotho', 'Spanish', 'Spanish Sign Language', 'Sranan', 'Sumerian', 'Swahili', 'Swati', 'Swedish', 'Swiss German', 'Syriac', 'Tagalog', 'Tahitian', 'Tajik', 'Tamashek', 'Tamil', 'Tarahumara', 'Tatar', 'Telugu', 'Teochew', 'Thai', 'Tibetan', 'Tigrigna', 'Tigrinya', 'Tlingit', 'Tok Pisin', 'Tonga', 'Tsonga', 'Tswana', 'Tulu', 'Tupi', 'Turkish', 'Turkmen', 'Tuvinian', 'Tzotzil', 'Uighur', 'Ukrainian', 'Ukrainian Sign Language', 'Ungwatsi', 'Urdu', 'Uzbek', 'Vietnamese', 'Vimeo - Official Chinese Language Version', 'Visayan', 'Washoe', 'Wayuu', 'Welsh', 'Wolof', 'Xhosa', 'Yakut', 'Yiddish', 'Yoruba', 'Zulu'],
      inputSpotifyArtist: [
        "name1",
        "name2",
        "name3",
        "name4",
        "name5",
        "name6",
        "name7",
        "name8",
        "name9",
        "name10",
        "name11",
      ],
      inputSpotifyTrack: [
        "track1",
        "track2",
        "track3",
        "track4",
        "track5",
        "track6",
        "track7",
        "track8",
        "track9",
        "track10",
        "track11",
      ],
      inputSpotifyGenre: ['acoustic', 'afrobeat', 'alt-rock', 'alternative', 'ambient', 'anime', 'black-metal', 'bluegrass', 'blues', 'bossanova', 'brazil', 'breakbeat', 'british', 'cantopop', 'chicago-house', 'children', 'chill', 'classical', 'club', 'comedy', 'country', 'dance', 'dancehall', 'death-metal', 'deep-house', 'detroit-techno', 'disco', 'disney', 'drum-and-bass', 'dub', 'dubstep', 'edm', 'electro', 'electronic', 'emo', 'folk', 'forro', 'french', 'funk', 'garage', 'german', 'gospel', 'goth', 'grindcore', 'groove', 'grunge', 'guitar', 'happy', 'hard-rock', 'hardcore', 'hardstyle', 'heavy-metal', 'hip-hop', 'holidays', 'honky-tonk', 'house', 'idm', 'indian', 'indie', 'indie-pop', 'industrial', 'iranian', 'j-dance', 'j-idol', 'j-pop', 'j-rock', 'jazz', 'k-pop', 'kids', 'latin', 'latino', 'malay', 'mandopop', 'metal', 'metal-misc', 'metalcore', 'minimal-techno', 'movies', 'mpb', 'new-age', 'new-release', 'opera', 'pagode', 'party', 'philippines-opm', 'piano', 'pop', 'pop-film', 'post-dubstep', 'power-pop', 'progressive-house', 'psych-rock', 'punk', 'punk-rock', 'r-n-b', 'rainy-day', 'reggae', 'reggaeton', 'road-trip', 'rock', 'rock-n-roll', 'rockabilly', 'romance', 'sad', 'salsa', 'samba', 'sertanejo', 'show-tunes', 'singer-songwriter', 'ska', 'sleep', 'songwriter', 'soul', 'soundtracks', 'spanish', 'study', 'summer', 'swedish', 'synth-pop', 'tango', 'techno', 'trance', 'trip-hop', 'turkish', 'work-out', 'world-music'],
    };
  },
  methods: {
    submit() {
      if (this.$refs.form.validate()) {
        console.log(this.name);
        // console.log(this.youtubeCategory);
        // console.log(this.spotifyArtists);
      }
    },
    bookShow2() {
      document.getElementById("book2").style.display = "inline";
      document.getElementById("book1btn").style.display = "none";
    },
    bookShow3() {
      document.getElementById("book3").style.display = "inline";
      document.getElementById("book2btn").style.display = "none";
    },
    bookShow4() {
      document.getElementById("book4").style.display = "inline";
      document.getElementById("book3btn").style.display = "none";
    },
    bookShow5() {
      document.getElementById("book5").style.display = "inline";
      document.getElementById("book4btn").style.display = "none";
    },
    bookRemove2() {
      this.bookCategory2 = "";
      document.getElementById("book2").style.display = "none";
      document.getElementById("book1btn").style.display = "inline";
    },
    bookRemove3() {
      this.bookCategory3 = "";
      document.getElementById("book3").style.display = "none";
      document.getElementById("book2btn").style.display = "inline";
    },
    bookRemove4() {
      this.bookCategory4 = "";
      document.getElementById("book4").style.display = "none";
      document.getElementById("book3btn").style.display = "inline";
    },
    bookRemove5() {
      this.bookCategory5 = "";
      document.getElementById("book5").style.display = "none";
      document.getElementById("book4btn").style.display = "inline";
    },
    movieShow2() {
      document.getElementById("movie2").style.display = "inline";
      document.getElementById("movie1btn").style.display = "none";
    },
    movieShow3() {
      document.getElementById("movie3").style.display = "inline";
      document.getElementById("movie2btn").style.display = "none";
    },
    movieShow4() {
      document.getElementById("movie4").style.display = "inline";
      document.getElementById("movie3btn").style.display = "none";
    },
    movieShow5() {
      document.getElementById("movie5").style.display = "inline";
      document.getElementById("movie4btn").style.display = "none";
    },
    movieRemove2() {
      this.movieGenre2 = "";
      document.getElementById("movie2").style.display = "none";
      document.getElementById("movie1btn").style.display = "inline";
    },
    movieRemove3() {
      this.movieGenre3 = "";
      document.getElementById("movie3").style.display = "none";
      document.getElementById("movie2btn").style.display = "inline";
    },
    movieRemove4() {
      this.movieGenre4 = "";
      document.getElementById("movie4").style.display = "none";
      document.getElementById("movie3btn").style.display = "inline";
    },
    movieRemove5() {
      this.movieGenre5 = "";
      document.getElementById("movie5").style.display = "none";
      document.getElementById("movie4btn").style.display = "inline";
    },
    youtubeShow2() {
      document.getElementById("youtube2").style.display = "inline";
      document.getElementById("youtube1btn").style.display = "none";
    },
    youtubeShow3() {
      document.getElementById("youtube3").style.display = "inline";
      document.getElementById("youtube2btn").style.display = "none";
    },
    youtubeShow4() {
      document.getElementById("youtube4").style.display = "inline";
      document.getElementById("youtube3btn").style.display = "none";
    },
    youtubeShow5() {
      document.getElementById("youtube5").style.display = "inline";
      document.getElementById("youtube4btn").style.display = "none";
    },
    youtubeRemove2() {
      this.youtubeCategory2 = "";
      document.getElementById("youtube2").style.display = "none";
      document.getElementById("youtube1btn").style.display = "inline";
    },
    youtubeRemove3() {
      this.youtubeCategory3 = "";
      document.getElementById("youtube3").style.display = "none";
      document.getElementById("youtube2btn").style.display = "inline";
    },
    youtubeRemove4() {
      this.youtubeCategory4 = "";
      document.getElementById("youtube4").style.display = "none";
      document.getElementById("youtube3btn").style.display = "inline";
    },
    youtubeRemove5() {
      this.youtubeCategory5 = "";
      document.getElementById("youtube5").style.display = "none";
      document.getElementById("youtube4btn").style.display = "inline";
    },
    artistShow2() {
      document.getElementById("spotifyArtist2").style.display = "inline";
      document.getElementById("artist1btn").style.display = "none";
    },
    artistShow3() {
      document.getElementById("spotifyArtist3").style.display = "inline";
      document.getElementById("artist2btn").style.display = "none";
    },
    artistRemove2() {
      this.spotifyArtist2 = "";
      document.getElementById("spotifyArtist2").style.display = "none";
      document.getElementById("artist1btn").style.display = "inline";
    },
    artistRemove3() {
      this.spotifyArtist3 = "";
      document.getElementById("spotifyArtist3").style.display = "none";
      document.getElementById("artist2btn").style.display = "inline";
    },
    trackShow2() {
      document.getElementById("spotifyTrack2").style.display = "inline";
      document.getElementById("track1btn").style.display = "none";
    },
    trackShow3() {
      document.getElementById("spotifyTrack3").style.display = "inline";
      document.getElementById("track2btn").style.display = "none";
    },
    trackRemove2() {
      this.spotifyTrack2 = "";
      document.getElementById("spotifyTrack2").style.display = "none";
      document.getElementById("track1btn").style.display = "inline";
    },
    trackRemove3() {
      this.spotifyTrack3 = "";
      document.getElementById("spotifyTrack3").style.display = "none";
      document.getElementById("track2btn").style.display = "inline";
    },
    sGenreShow2() {
      document.getElementById("spotifyGenre2").style.display = "inline";
      document.getElementById("sGenre1btn").style.display = "none";
    },
    sGenreShow3() {
      document.getElementById("spotifyGenre3").style.display = "inline";
      document.getElementById("sGenre2btn").style.display = "none";
    },
    sGenreShow4() {
      document.getElementById("spotifyGenre4").style.display = "inline";
      document.getElementById("sGenre3btn").style.display = "none";
    },
    sGenreShow5() {
      document.getElementById("spotifyGenre5").style.display = "inline";
      document.getElementById("sGenre4btn").style.display = "none";
    },
    sGenreRemove2() {
      this.spotifyGenre2 = "";
      document.getElementById("spotifyGenre2").style.display = "none";
      document.getElementById("sGenre1btn").style.display = "inline";
    },
    sGenreRemove3() {
      this.spotifyGenre3 = "";
      document.getElementById("spotifyGenre3").style.display = "none";
      document.getElementById("sGenre2btn").style.display = "inline";
    },
    sGenreRemove4() {
      this.spotifyGenre4 = "";
      document.getElementById("spotifyGenre4").style.display = "none";
      document.getElementById("sGenre3btn").style.display = "inline";
    },
    sGenreRemove5() {
      this.spotifyGenre5 = "";
      document.getElementById("spotifyGenre5").style.display = "none";
      document.getElementById("sGenre4btn").style.display = "inline";
    },
  },
};
</script>

<style>
/* Tooltip container */
.tooltip {
  position: relative;
  display: inline-block;
  border-bottom: 1px dotted black; /* If you want dots under the hoverable text */
}

/* Tooltip text */
.tooltip .tooltiptext {
  visibility: hidden;
  width: 120px;
  background-color: rgb(90, 90, 90);
  color: #fff;
  text-align: center;
  padding: 5px 0;
  border-radius: 6px;

  /* Position the tooltip text - see examples below! */
  position: absolute;
  z-index: 1;
  top: 100%;
  left: 50%;
  margin-left: -60px;
}

/* Show the tooltip text when you mouse over the tooltip container */
.tooltip:hover .tooltiptext {
  visibility: visible;
}

.tooltip .tooltiptext::after {
  content: " ";
  position: absolute;
  bottom: 100%; /* At the top of the tooltip */
  left: 50%;
  margin-left: -5px;
  border-width: 5px;
  border-style: solid;
  border-color: transparent transparent rgb(90, 90, 90) transparent;
}
</style>
