<template>
  <div id="app">
    <v-app>
      <v-app-bar app fixed dense dark clipped-left color="rgb(54, 54, 79)">
        <v-toolbar-title class="headline">
          <span>Commonette</span>
        </v-toolbar-title>
        <v-spacer></v-spacer>

        <v-menu offset-y v-if="roomName">
          <template v-slot:activator="{ on }">
            <v-btn text icon v-on="on">
              <v-icon>mdi-account-group</v-icon>
            </v-btn>
            {{ roomName }}
          </template>
          <v-list dense>
            <v-list-item>
              <v-list-item-title>
                <h3>In this room:</h3>
              </v-list-item-title>
            </v-list-item>
            <v-list-item v-for="item in roomUsers" :key="item">
              <v-list-item-title>
                <v-icon>mdi-account-outline</v-icon> {{item.name}}
              </v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-app-bar>

      <router-view></router-view>

      <v-footer class="justify-center" color="rgb(54, 54, 79)" height="150">
        <div class="title font-weight-light grey--text text--lighten-1 text-center">
          &copy; {{ (new Date()).getFullYear() }} — Commonette — IS216 G6T5<br>
          APIs Used:<br>
          <a href="https://rapidapi.com/gox-ai-gox-ai-default/api/ott-details/endpoints" target="_blank">
            <img src="./images/OTT.png" style="height:40px; width:40px; margin-left:10px; margin-right:10px">
          </a>
          <a href="https://developers.google.com/youtube/v3/docs/videos/list" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/1280px-YouTube_full-color_icon_%282017%29.svg.png" style="height:25px; width:40px; margin-left:10px; margin-right:10px">
          </a>
          <a href="https://developer.spotify.com/documentation/web-api/reference/browse/get-recommendations/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/1024px-Spotify_logo_without_text.svg.png" style="height:30px; width:30px; margin-left:10px; margin-right:10px">
          </a>
          <a href="https://developers.google.com/books" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/b/ba/Google_Books_logo_2015.svg" style="height:30px; width:60px; margin-left:10px; margin-right:10px">
          </a>
        </div>
      </v-footer>
    </v-app>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>

<script>
export default {
  data: () => ({
    roomName: null,
    roomUsers: null,
  }),
  created() {
    this.updateUsers();
    this.$bus.$on("updated", () => {
      this.updateUsers();
    });
  },
  methods: {
    navigateRoute(newpath) {
      this.$router.push(newpath);
    },
    updateUsers() {
      this.roomName = localStorage.getItem("roomName");
      this.roomUsers = JSON.parse(localStorage.getItem("roomUsers"));
    },
  },
};
</script>