<template>
  <v-main>

    <v-dialog v-model="showDetails" @keydown.esc="closeDetails" max-width="900px">
      <v-card>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-icon large color="black" v-on:click="showDetails=false">
            mdi-close-circle-outline
          </v-icon>
        </v-card-actions>
        <v-img v-if="details.img" max-height="300px" contain :src="details.img"></v-img>
        <iframe v-if="details.youtube" width="100%" height="400px" :src="details.youtube" allowfullscreen></iframe>
        <iframe v-if="details.spotify" width="100%" height="400px" :src="details.spotify" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
        <br><br>
        <v-card-text class="black--text">
          <h1>{{details.title}}</h1>
        </v-card-text>
        <v-card-text>
          <h2>{{details.subtitle}}</h2>
        </v-card-text>
        <v-card-text v-html="details.desc"></v-card-text>
        <v-card-text>
          <v-btn elevation="8" large rounded color="primary" :href="details.url">VIEW</v-btn>
        </v-card-text>
        <v-card-text>
          <b>Share</b>
          <v-btn icon :href="'https://t.me/share?url=' + details.url + '&text=Let%27s%20see%20this%20together!'" target="_blank">
            <v-icon color="blue">mdi-telegram</v-icon>
          </v-btn>
          <v-btn icon :href="'https://api.whatsapp.com/send?text=Let%27s%20see%20this%20together!%20' + details.url" target="_blank">
            <v-icon color="green">mdi-whatsapp</v-icon>
          </v-btn>
        </v-card-text>
      </v-card>
    </v-dialog>

    <section id="all" v-if="recommend">
      <span>
        <br>
        <h1>Recommendations for <b>{{roomName}}</b></h1>
        <h3>Invite your friends to join this room using the code <b>{{roomCode}}</b></h3>
        <br>
      </span>

      <v-sheet class="mx-auto" elevation="8" v-if="youtubeResults">
        <v-toolbar color="grey lighten-1" dense>
          <v-toolbar-title>
            <v-icon large color="red">
              mdi-youtube
            </v-icon>
            YouTube
          </v-toolbar-title>
        </v-toolbar>
        <v-slide-group class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="video in youtubeResults" :key="video.id">
            <v-container v-if="video.id" grid-list-md>
              <v-icon class="d-flex justify-end" color="black" v-on:click="video.id=false">mdi-minus-circle-outline</v-icon>
              <v-card class="mx-auto" max-width="300px" v-on:click="youtubeCard(video.snippet.title, video.snippet.channelTitle, video.snippet.description, video.id)">
                <v-img :src="video.snippet.thumbnails.medium.url" contain></v-img>
                <v-card-text>
                  <div class="subtitle-1 black--text text-truncate">
                    {{video.snippet.title}}
                  </div>
                  {{video.snippet.channelTitle}}
                </v-card-text>
              </v-card>
            </v-container>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>

      <v-sheet class="mx-auto" elevation="8" v-if="bookResults">
        <v-toolbar color="grey lighten-1" dense>
          <v-toolbar-title>
            <v-icon large color="blue">
              mdi-book
            </v-icon>
            Books
          </v-toolbar-title>
        </v-toolbar>
        <v-slide-group class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="book in bookResults" :key="book.id">
            <v-container v-if="book.id" grid-list-md>
              <v-icon class="d-flex justify-end" color="black" v-on:click="book.id=false">mdi-minus-circle-outline</v-icon>
              <v-card class="mx-auto" max-width="200px" v-on:click="bookCard(book.volumeInfo.title, book.volumeInfo.authors.toString(), book.volumeInfo.description, book.volumeInfo.previewLink, book.volumeInfo.imageLinks.thumbnail)">
                <v-img :src="book.volumeInfo.imageLinks.thumbnail" contain></v-img>
                <v-card-text>
                  <div class="subtitle-1 black--text">
                    {{book.volumeInfo.title}}
                  </div>
                  <div class="text-truncate">
                    {{book.volumeInfo.authors.toString()}}
                  </div>
                </v-card-text>
              </v-card>
            </v-container>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>

      <v-sheet class="mx-auto" elevation="8" v-if="movieResults">
        <v-toolbar color="grey lighten-1" dense>
          <v-toolbar-title>
            <v-icon large color="yellow">
              mdi-movie-open
            </v-icon>
            Movies & Shows
          </v-toolbar-title>
        </v-toolbar>
        <v-slide-group class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="movie in movieResults" :key="movie.id">
            <!-- Excluding movies with no thumbnails -->
            <v-container v-if="movie.imageurl[0]" grid-list-md>
              <v-icon class="d-flex justify-end" color="black" v-on:click="movie.imageurl=false">mdi-minus-circle-outline</v-icon>
              <v-card class="mx-auto" max-width="200px" v-on:click="movieCard(movie.title, movie.synopsis, movie.released, movie.imageurl[0], movie.imdbid)">
                <v-img :src="movie.imageurl[0]" contain></v-img>
                <v-card-text>
                  <div class="subtitle-1 black--text">
                    {{movie.title}}
                  </div>
                  {{movie.released}}
                </v-card-text>
              </v-card>
            </v-container>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>

      <v-sheet class="mx-auto" elevation="8" v-if="spotifyResults">
        <v-toolbar color="grey lighten-1" dense>
          <v-toolbar-title>
            <v-icon large color="green">
              mdi-spotify
            </v-icon>
            Spotify
          </v-toolbar-title>
        </v-toolbar>
        <v-slide-group class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="song in spotifyResults" :key="song.id">
            <v-container v-if="song.id" grid-list-md>
              <v-icon class="d-flex justify-end" color="black" v-on:click="song.id=false">mdi-minus-circle-outline</v-icon>
              <v-card class="mx-auto" max-width="150px" v-on:click="spotifyCard(song.name, song.album.name, song.album.release_date, song.artists, song.id)">
                <v-img :src="song.album.images[1].url" contain></v-img>
                <v-card-text>
                  <div class="subtitle-1 black--text text-truncate">
                    {{song.name}}
                  </div>
                  {{song.album.name}}
                </v-card-text>
              </v-card>
            </v-container>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>

    </section>
  </v-main>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    roomName: localStorage.getItem("roomName"),
    roomCode: localStorage.getItem("roomCode"),
    recommend: null,
    youtubeResults: null,
    bookResults: null,
    movieResults: null,
    spotifyResults: null,
    showDetails: false,
    details: {},
  }),
  created() {
    this.initialise();
  },
  methods: {
    navigateRoute(newpath) {
      this.$router.push(newpath);
    },
    initialise() {
      axios({
        url: "/recommend/" + this.roomCode,
        method: "GET",
      })
        .then((response) => {
          this.recommend = response.data;
          this.renderYoutube();
          this.renderBooks();
          this.renderMovies();
          this.renderSpotify();
        })
        .catch(() => {
          this.navigateRoute("/questionnaire");
        });
    },
    renderYoutube() {
      axios
        .get(
          "https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=50&regionCode=SG&videoCategoryId=" +
            this.recommend.youtube.videoCategory +
            "&key=AIzaSyA7Y61l8cbCs3iBaovaUT9iv8eczTikK9k"
        )
        .then((response) => {
          this.youtubeResults = response.data.items;
        })
        .catch((e) => {
          console.log(e.response.data);
        });
    },
    renderBooks() {
      axios
        .get(
          "https://www.googleapis.com/books/v1/volumes?q=subject:" +
            this.recommend.book.subject +
            "&langRestrict=en&maxResults=40"
        )
        .then((response) => {
          this.bookResults = response.data.items;
        })
        .catch((e) => {
          console.log(e.response.data);
        });
    },
    renderMovies() {
      this.recommend.movie.type = "movie";
      axios({
        method: "GET",
        url: "https://rapidapi.p.rapidapi.com/advancedsearch",
        params: this.recommend.movie,
        headers: {
          "x-rapidapi-host": "ott-details.p.rapidapi.com",
          "x-rapidapi-key":
            "9027419c0amshce93712d7412181p1dba86jsne0772b3fcfe5",
        },
      })
        .then((response) => {
          this.movieResults = response.data.results;
        })
        .catch((e) => {
          console.log(e.response.data);
        });
    },
    renderSpotify() {
      this.recommend.spotify.limit = 100;
      axios({
        url: "/spotify-token",
        method: "GET",
      }).then((auth) => {
        axios({
          method: "GET",
          url: "https://api.spotify.com/v1/recommendations",
          params: this.recommend.spotify,
          headers: auth.data,
        })
          .then((response) => {
            this.spotifyResults = response.data.tracks;
          })
          .catch((e) => {
            console.log(e.response.data);
          });
      });
    },
    youtubeCard(title, subtitle, desc, id) {
      this.details = {};
      this.details.title = title;
      this.details.subtitle = subtitle;
      this.details.desc = desc.replace(/(?:\r\n|\r|\n)/g, "<br/>");
      this.details.url = "https://www.youtube.com/watch?v=" + id;
      this.details.youtube = "https://www.youtube.com/embed/" + id;
      this.showDetails = true;
    },
    bookCard(title, subtitle, desc, url, img) {
      this.details = {};
      this.details.title = title;
      this.details.subtitle = subtitle;
      this.details.desc = desc;
      this.details.url = url;
      this.details.img = img;
      this.showDetails = true;
    },
    movieCard(title, desc, subtitle, img, id) {
      this.details = {};
      this.details.title = title;
      this.details.subtitle = subtitle;
      this.details.desc = desc;
      this.details.url = "https://www.imdb.com/title/" + id;
      this.details.img = img;
      this.showDetails = true;
    },
    spotifyCard(title, subtitle, release, artists, id) {
      this.details = {};
      this.details.title = title;
      this.details.subtitle = subtitle;
      let artistList = [];
      for (var i in artists) {
        artistList.push(artists[i].name);
      }
      artistList = artistList.toString();
      this.details.desc =
        "Release Date: " + release + "<br/>Artist(s): " + artistList;
      this.details.url = "https://open.spotify.com/track/" + id;
      this.details.spotify = "https://open.spotify.com/embed/track/" + id;
      this.showDetails = true;
    },
    closeDetails() {
      this.showDetails = !this.showDetails;
    },
    shuffle(arr) {
      var ctr = arr.length,
        temp,
        index;
      while (ctr > 0) {
        index = Math.floor(Math.random() * ctr);
        ctr--;
        temp = arr[ctr];
        arr[ctr] = arr[index];
        arr[index] = temp;
      }
      return arr;
    },
  },
};
</script>
