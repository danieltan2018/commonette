<template>
  <v-main>

  </v-main>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    userCount: localStorage.getItem("roomUsers").length,
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
      axios({
        url: "/recommend/" + this.roomCode,
        method: "GET",
      })
        .then((response) => {
          this.youtubeTop = response.data.youtube.videoCategory.split(",");
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
