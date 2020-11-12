<template>
  <v-main class="color-bg-primary">

    <v-dialog v-model="showDetails" @keydown.esc="showDetails=false; details={};" max-width="800px" persistent>
      <v-card>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-icon large color="red" v-on:click="showDetails=false; details={};">
            mdi-close
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
          <v-btn elevation="8" large rounded color="#6A74A0" dark :href="details.url">VIEW</v-btn>
        </v-card-text>
        <v-card-text>
          <b>Share Here:</b><br>
          <v-btn icon :href="'https://t.me/share?url=' + details.url + '&text=Let%27s%20see%20this%20together!'" target="_blank">
            <v-icon color="blue">mdi-telegram</v-icon>
          </v-btn>
          <v-btn icon :href="'https://api.whatsapp.com/send?text=Let%27s%20see%20this%20together!%20' + details.url" target="_blank">
            <v-icon color="green">mdi-whatsapp</v-icon>
          </v-btn>
        </v-card-text>
      </v-card>
    </v-dialog>

    <section id="all" v-if="recommend && bookDisplay">
      <v-container fluid>
        <v-row>
          <v-col class="hidden-sm-and-down" md="4">
            <RotatingImage image="Nezuko" height="100"></RotatingImage>
          </v-col>
          <v-col class="hidden-md-and-up col-12">
            <v-row>
              <v-col class="col-3"></v-col>
              <v-col class="col-3">
                <RotatingImage image="Nezuko" height="100"></RotatingImage>
              </v-col>
              <v-col class="col-3">
                <RotatingImage image="Tanjiro" height="100"></RotatingImage>
              </v-col>
              <v-col class="col-3"></v-col>
            </v-row>
          </v-col>
          <v-col md="4" class="animate__animated animate__backInDown">
            <h1 class="color-white">Recommendations for <b class="color-highlight2">{{roomName}}</b></h1>
            <h3 class="color-white">Invite your friends to join this room using the code <b class="color-highlight1">{{roomCode}} </b>
              <v-btn v-clipboard="roomCode" icon color="#E3E9F2">
                <v-icon small>mdi-content-copy</v-icon>
              </v-btn>
            </h3>
            <h4 class="color-white animate__animated animate__flash animate__delay-5 animate__repeat-2">Make sure to <font class="color-highlight2">save the code</font> before exiting!</h4>
          </v-col>
          <v-col class="hidden-sm-and-down" md="4">
            <RotatingImage image="Tanjiro" height="100"></RotatingImage>
          </v-col>
        </v-row>
      </v-container>

      <v-sheet class="mx-auto" elevation="8" v-if="youtubeDisplay" color="rgb(81, 81, 118)" data-aos="fade-right" data-aos-duration="1000">
        <v-toolbar color="#E3E9F2" dense>
          <v-toolbar-title class="animate__animated animate__rubberBand">
            <v-icon large color="red" class="animate__animated animate__swing animate__infinite">
              mdi-youtube
            </v-icon>
            <font class="media-header"> YouTube</font>
          </v-toolbar-title>
        </v-toolbar>
        <v-slide-group class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="(video) in youtubeDisplay" :key="video.id">
            <v-container grid-list-md>
              <v-icon class="d-flex justify-content-end" color="red" v-on:click="remove('youtube', video.id)">mdi-close-circle</v-icon>
              <v-card class="mx-auto" width="250px" v-on:click="youtubeCard(video.snippet.title, video.snippet.channelTitle, video.snippet.description, video.id)">
                <v-img :src="video.snippet.thumbnails.medium.url" contain></v-img>
                <v-card-text>
                  <div class="subtitle-1 black--text text-truncate">
                    {{video.snippet.title}}
                  </div>
                  <div class="text-truncate">
                    {{video.snippet.channelTitle}}
                  </div>
                </v-card-text>
              </v-card>
            </v-container>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>

      <v-sheet class="mx-auto dark-background" elevation="8" v-if="bookDisplay" color="rgb(81, 81, 118)" data-aos="fade-left" data-aos-duration="800">
        <v-toolbar color="#E3E9F2" dense>
          <v-toolbar-title class="animate__animated animate__rubberBand">
            <v-icon large color="blue" class="animate__animated animate__flip animate__infinite">
              mdi-book
            </v-icon>
            <font class="media-header"> Books</font>
          </v-toolbar-title>
        </v-toolbar>
        <v-slide-group class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="(book) in bookDisplay" :key="book.id">
            <v-container grid-list-md v-if="book.volumeInfo.authors && book.volumeInfo.imageLinks">
              <v-icon class="d-flex justify-end" color="red" v-on:click="remove('book', book.id)">mdi-close-circle</v-icon>
              <v-card class="mx-auto" width="200px" v-on:click="bookCard(book.volumeInfo.title, book.volumeInfo.authors.toString(), book.volumeInfo.description, book.volumeInfo.previewLink, book.volumeInfo.imageLinks.thumbnail)">
                <v-img :src="book.volumeInfo.imageLinks.thumbnail" height="300px" contain></v-img>
                <v-card-text>
                  <div class="subtitle-1 black--text text-truncate">
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

      <v-sheet class="mx-auto dark-background" elevation="8" v-if="movieDisplay" color="rgb(81, 81, 118)" data-aos="fade-right" data-aos-duration="800">
        <v-toolbar color="#E3E9F2" dense>
          <v-toolbar-title class="animate__animated animate__rubberBand">
            <v-icon large color="pink" class="animate__animated animate__jello animate__infinite">
              mdi-movie-open
            </v-icon>
            <font class="media-header"> Movies</font>
          </v-toolbar-title>
        </v-toolbar>
        <v-slide-group class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="(movie) in movieDisplay" :key="movie.imdbid">
            <v-container grid-list-md v-if="movie.imageurl[0]">
              <v-icon class="d-flex justify-end" color="red" v-on:click="remove('movie', movie.imdbid)">mdi-close-circle</v-icon>
              <v-card class="mx-auto" width="200px" v-on:click="movieCard(movie.title, movie.synopsis, movie.released, movie.imageurl[0], movie.imdbid)">
                <v-img :src="movie.imageurl[0]" height="300px" contain></v-img>
                <v-card-text>
                  <div class="subtitle-1 black--text text-truncate">
                    {{movie.title}}
                  </div>
                  <div class="text-truncate">
                    {{movie.released}}
                  </div>
                </v-card-text>
              </v-card>
            </v-container>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>

      <v-sheet class="mx-auto dark-background" elevation="8" v-if="spotifyDisplay" color="rgb(81, 81, 118)" data-aos="fade-left" data-aos-duration="800">
        <v-toolbar color="#E3E9F2" dense>
          <v-toolbar-title class="animate__animated animate__rubberBand">
            <v-icon large color="green" class="animate__animated animate__tada animate__infinite">
              mdi-spotify
            </v-icon>
            <font style="font-size:18px"> Spotify</font>
          </v-toolbar-title>
        </v-toolbar>
        <v-slide-group class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="(song) in spotifyDisplay" :key="song.id">
            <v-container grid-list-md>
              <v-icon class="d-flex justify-end" color="red" v-on:click="remove('spotify', song.id)">mdi-close-circle</v-icon>
              <v-card class="mx-auto" max-width="150px" v-on:click="spotifyCard(song.name, song.album.name, song.album.release_date, song.artists, song.id)">
                <v-img :src="song.album.images[1].url" contain></v-img>
                <v-card-text>
                  <div class="subtitle-1 black--text text-truncate">
                    {{song.name}}
                  </div>
                  <div class="text-truncate">
                    {{song.album.name}}
                  </div>
                </v-card-text>
              </v-card>
            </v-container>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>
    </section>

    <!-- Handle slowest API - Books -->
    <v-container fluid fill-height v-else>
      <v-layout justify-center align-center>
        <breeding-rhombus-spinner :animation-duration="500" :size="65" color="#ff1d5e" />
        <h1 class="color-white">Running magic algorithm...</h1>
      </v-layout>
    </v-container>

  </v-main>
</template>

<script>
import axios from "axios";
import RotatingImage from "../components/RotatingImage/RotatingImage.vue";
import "animate.css";
import { BreedingRhombusSpinner } from "epic-spinners";

export default {
  components: {
    RotatingImage,
    BreedingRhombusSpinner,
  },
  data: () => ({
    roomName: localStorage.getItem("roomName"),
    roomCode: localStorage.getItem("roomCode"),
    recommend: null,
    youtubeResults: null,
    bookResults: null,
    movieResults: null,
    spotifyResults: null,
    youtubeDisplay: null,
    bookDisplay: null,
    movieDisplay: null,
    spotifyDisplay: null,
    youtubeBlacklist: [],
    bookBlacklist: [],
    movieBlacklist: [],
    spotifyBlacklist: [],
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
        url: "/room/" + this.roomCode,
        method: "GET",
      }).then((response) => {
        if (typeof response.data.blacklist !== "undefined") {
          this.youtubeBlacklist = response.data.blacklist.youtube;
          this.bookBlacklist = response.data.blacklist.book;
          this.movieBlacklist = response.data.blacklist.movie;
          this.spotifyBlacklist = response.data.blacklist.spotify;
        }
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
          this.youtubeResults = this.shuffle(response.data.items);
          for (var item of this.youtubeBlacklist) {
            this.youtubeResults.splice(
              this.youtubeResults.findIndex((e) => e.id === item),
              1
            );
          }
          this.youtubeDisplay = this.youtubeResults.splice(0, 10);
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
          this.bookResults = this.shuffle(response.data.items);
          for (var item of this.bookBlacklist) {
            this.bookResults.splice(
              this.bookResults.findIndex((e) => e.id === item),
              1
            );
          }
          this.bookDisplay = this.bookResults.splice(0, 10);
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
          this.movieResults = this.shuffle(response.data.results);
          for (var item of this.movieBlacklist) {
            this.movieResults.splice(
              this.movieResults.findIndex((e) => e.imdbid === item),
              1
            );
          }
          this.movieDisplay = this.movieResults.splice(0, 10);
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
            this.spotifyResults = this.shuffle(response.data.tracks);
            for (var item of this.spotifyBlacklist) {
              this.spotifyResults.splice(
                this.spotifyResults.findIndex((e) => e.id === item),
                1
              );
            }
            this.spotifyDisplay = this.spotifyResults.splice(0, 10);
          })
          .catch((e) => {
            console.log(e.response.data);
          });
      });
    },
    youtubeCard(title, subtitle, desc, id) {
      this.details.title = title;
      this.details.subtitle = subtitle;
      this.details.desc = desc.replace(/(?:\r\n|\r|\n)/g, "<br/>");
      this.details.url = "https://www.youtube.com/watch?v=" + id;
      this.details.youtube = "https://www.youtube.com/embed/" + id;
      this.showDetails = true;
    },
    bookCard(title, subtitle, desc, url, img) {
      this.details.title = title;
      this.details.subtitle = subtitle;
      this.details.desc = desc;
      this.details.url = url;
      this.details.img = img;
      this.showDetails = true;
    },
    movieCard(title, desc, subtitle, img, id) {
      this.details.title = title;
      this.details.subtitle = subtitle;
      this.details.desc = desc;
      this.details.url = "https://www.imdb.com/title/" + id;
      this.details.img = img;
      this.showDetails = true;
    },
    spotifyCard(title, subtitle, release, artists, id) {
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
    remove(type, id) {
      axios({
        method: "post",
        url: "/dislike",
        data: {
          roomCode: this.roomCode,
          type: type,
          id: id,
        },
      }).then(() => {
        if (type == "youtube") {
          this.youtubeDisplay.splice(
            this.youtubeDisplay.findIndex((e) => e.id === id),
            1
          );
          if (this.youtubeResults.length > 0) {
            this.youtubeDisplay.push(this.youtubeResults.pop());
          }
        } else if (type == "book") {
          this.bookDisplay.splice(
            this.bookDisplay.findIndex((e) => e.id === id),
            1
          );
          if (this.bookResults.length > 0) {
            this.bookDisplay.push(this.bookResults.pop());
          }
        }
        if (type == "movie") {
          this.movieDisplay.splice(
            this.movieDisplay.findIndex((e) => e.imdbid === id),
            1
          );
          if (this.movieResults.length > 0) {
            this.movieDisplay.push(this.movieResults.pop());
          }
        }
        if (type == "spotify") {
          this.spotifyDisplay.splice(
            this.spotifyDisplay.findIndex((e) => e.id === id),
            1
          );
          if (this.spotifyResults.length > 0) {
            this.spotifyDisplay.push(this.spotifyResults.pop());
          }
        }
      });
    },
  },
};
</script>
<style>
:root {
  --animate-duration: 3s;
  --animate-delay: 0.9s;
}
</style>

<style lang="scss">
@import "~@/styles/colors";

.bg-primary{
  background-color: $primary;
}
.color{
  &-bg-primary{
    background-color: $primary;
  }
  &-white{
    color: $white;
  }
  &-highlight1{
    color: $highlight1;
  }
  &-highlight2{
    color: $highlight2;
  }
}
.media-header{
  font-size:18px;
}

</style>