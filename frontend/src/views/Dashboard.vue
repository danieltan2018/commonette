<template>
  <v-main>

  </v-main>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    userCount: JSON.parse(localStorage.getItem("roomUsers")).length,
    youtubeTop: [],
    bookTop: [],
    movieTop: [],
    spotifyTop: [],
  }),
  created() {
    this.initialise();
  },
  methods: {
    navigateRoute(newpath) {
      this.$router.push(newpath);
    },
    initialise() {
      axios
        .get("/recommend/" + localStorage.getItem("roomCode"))
        .then((response) => {
          this.youtubeTop = response.data.youtube.videoMore.split(",");
          this.bookTop = response.data.book.subject.split(",");
          this.movieTop = response.data.movie.genre.split(",");
          this.spotifyTop = response.data.spotify.seed_genres.split(",");
        })
        .catch(() => {
          this.navigateRoute("/questionnaire");
        });
    },
  },
};
</script>
