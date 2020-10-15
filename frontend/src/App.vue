<template>
  <div id="app">
    <v-app>
      <v-app-bar app fixed dark clipped-left color="primary" v-on:click="navigateRoute('/')">
        <v-img class="mr-3" src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png" max-height="30" max-width="30"></v-img>
        <v-toolbar-title class="headline">
          <span>Commonette</span>
        </v-toolbar-title>
        <v-spacer></v-spacer>

        <v-menu offset-y v-if="roomName">
          <template v-slot:activator="{ on }">
            <v-btn text icon color="white" v-on="on">
              <v-icon dark>mdi-account-group</v-icon>
            </v-btn>
            {{ roomName }}'s Room
          </template>
          <v-list dense>
            <v-list-item>
              <v-list-item-title>Hi, Person A</v-list-item-title>
            </v-list-item>
            <!-- To replace with v-for -->
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-account-outline</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Person B</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-icon>
                <v-icon>mdi-account-outline</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Person C</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-app-bar>

      <router-view></router-view>

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
  data: () => ({
    roomName: localStorage.getItem("roomName"),
    roomCode: localStorage.getItem("roomCode"),
  }),
  methods: {
    navigateRoute(newpath) {
      this.$router.push(newpath);
    },
  },
};
</script>