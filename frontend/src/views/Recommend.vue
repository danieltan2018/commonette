<template>
  <v-main>
    <section id="all" v-if="recommend">
      <span>
        <br>
        <h1>Recommendations for {{roomName}}</h1>
        <br>
        <h3>Get your friends to join this room using the code <b>{{roomCode}}</b></h3>
        <br>
      </span>

      <v-sheet class="mx-auto" elevation="8" v-if="youtubeResults">
        <v-toolbar color="grey" dense>
          <v-toolbar-title>
            <v-icon large color="red">
              mdi-youtube
            </v-icon>
            YouTube
          </v-toolbar-title>
        </v-toolbar>
        <v-slide-group class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="video in youtubeResults" :key="video.id">
            <v-container grid-list-md>
              <v-card class="mx-auto" max-width="200px">
                <v-img :src="video.snippet.thumbnails.medium.url" contain></v-img>
                <v-card-title v-text="video.snippet.title" class="h3"></v-card-title>
                <v-card-subtitle>
                  {{video.snippet.channelTitle}}
                </v-card-subtitle>
              </v-card>
            </v-container>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>

      <v-sheet class="mx-auto" elevation="8" v-if="bookResults">
        <v-toolbar color="grey" dense>
          <v-toolbar-title>
            <v-icon large color="blue">
              mdi-book
            </v-icon>
            Books
          </v-toolbar-title>
        </v-toolbar>
        <v-slide-group class="pa-4" active-class="success" show-arrows>
          <v-slide-item v-for="book in bookResults" :key="book.id">
            <v-container grid-list-md>
              <v-card class="mx-auto" max-width="200px">
                <v-img :src="book.volumeInfo.imageLinks.thumbnail" contain></v-img>
                <v-card-title v-text="book.volumeInfo.title" class="h3"></v-card-title>
                <v-card-subtitle>
                  {{book.volumeInfo.authors.toString()}}
                </v-card-subtitle>
              </v-card>
            </v-container>
          </v-slide-item>
        </v-slide-group>
      </v-sheet>

      <v-sheet class="mx-auto" elevation="8" v-if="movieResults">
        <v-toolbar color="grey" dense>
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
            <v-container grid-list-md v-if="movie.imageurl[0]">
              <v-card class="mx-auto" max-width="200px">
                <v-img :src="movie.imageurl[0]" contain></v-img>
                <v-card-title v-text="movie.title" class="h3"></v-card-title>
                <v-card-subtitle>
                  {{movie.released}}
                </v-card-subtitle>
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
    recommend: false,
    youtubeResults: false,
    bookResults: false,
    movieResults: false,
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
        })
        .catch(() => {
          this.navigateRoute("/questionnaire");
        });
    },
    renderYoutube() {
      axios
        .get(
          "https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&maxResults=10&regionCode=SG&videoCategoryId=" +
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
            this.recommend.book.subject
        )
        .then((response) => {
          this.bookResults = response.data.items;
        })
        .catch((e) => {
          console.log(e.response.data);
        });
    },
    renderMovies() {
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
  },
};
</script>