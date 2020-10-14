<template>
  <div id="app">
    <v-app>
      <v-app-bar app color="blue darken-2" height="70" v-on:click="navigateRoute('/')">
        <v-avatar class="mr-3" color="grey lighten-5" size="40">
          <v-img contain max-height="70%" src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"></v-img>
        </v-avatar>
        <v-toolbar-title class="font-weight-black headline">
          COMMONETTE
        </v-toolbar-title>
      </v-app-bar>

      <v-main>
        <v-container fluid>
          <router-view></router-view>
        </v-container>
      </v-main>

      <v-footer class="justify-center" color="#292929" height="100">
        <div class="title font-weight-light grey--text text--lighten-1 text-center">
          &copy; {{ (new Date()).getFullYear() }} — Commonette — IS216 G6T5
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
  methods: {
    navigateRoute(newpath) {
      this.$router.push(newpath);
    },
  },
};
</script>