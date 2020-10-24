<template>
  <v-main>

  </v-main>
</template>

<script>
import axios from "axios";
export default {
  data: () => ({
    roomName: localStorage.getItem("roomName"),
    roomCode: localStorage.getItem("roomCode"),
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
      axios
        .get("/recommend/" + this.roomCode)
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
