<template>
  <div class="home">
    <v-main>
      <v-dialog v-model="createRoomPopup" max-width="350">
        <v-card>
          <v-card-title class="headline justify-center">Create New Room</v-card-title>
          <v-card-text>
            <v-form @submit.prevent v-model="valid" ref="form">
              <v-text-field label="Enter a room name" v-model="roomName" :rules="inputRequiredRule" autofocus v-on:keyup.enter="createRoom"></v-text-field>
              <p v-if="errors" class="red--text">
                {{ errorMessage }}
              </p>
              <v-btn color="primary" :loading="loading1" @click="loader = 'loading1'" :disabled="!valid" v-on:click="createRoom">Enter</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-dialog>
      <v-dialog v-model="joinRoomPopup" max-width="350">
        <v-card>
          <v-card-title class="headline justify-center">Join Existing Room</v-card-title>
          <v-card-text>
            <v-form @submit.prevent v-model="valid" ref="form">
              <v-text-field label="Enter the room code" v-model="roomCode" :rules="inputRequiredRule" autofocus v-on:keyup.enter="joinRoom"></v-text-field>
              <p v-if="errors" class="red--text">
                {{ errorMessage }}
              </p>
              <v-btn color="primary" :loading="loading2" @click="loader = 'loading2'" :disabled="!valid" v-on:click="joinRoom">Enter</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-dialog>

      <v-img src="https://images.unsplash.com/photo-1487017159836-4e23ece2e4cf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1951&q=80">
        <v-theme-provider dark>
          <v-container fill-height>
            <v-row align="center" class="white--text mx-auto" justify="center">
              <v-col class="white--text text-center" cols="12" tag="h1">
                <span :class="[
                    $vuetify.breakpoint.smAndDown ? 'display-1' : 'display-2',
                  ]" class="font-weight-light">
                  WELCOME TO
                </span>
                <br />
                <span :class="[
                    $vuetify.breakpoint.smAndDown ? 'display-3' : 'display-4',
                  ]" class="font-weight-black">
                  COMMONETTE
                </span>
              </v-col>
              <v-row justify="center">
                <v-btn elevation="2" large class="ma-2" color="primary" v-on:click="createRoomPopup = true">
                  Create Room
                </v-btn>
                <v-btn elevation="2" large class="ma-2" color="secondary" @click="$vuetify.goTo('#about')">
                  About
                </v-btn>
                <v-btn elevation="2" large class="ma-2" color="primary" v-on:click="joinRoomPopup = true">
                  Join Room
                </v-btn>
              </v-row>
            </v-row>
          </v-container>
        </v-theme-provider>
      </v-img>

      <section id="about">
        <div class="py-12"></div>
        <v-container class="text-center">
          <h2 class="display-2 font-weight-bold mb-3">What is commonette?</h2>
          <v-responsive class="mx-auto mb-8" width="56">
            <v-divider class="mb-1"></v-divider>
            <v-divider></v-divider>
          </v-responsive>
          <v-responsive class="mx-auto title font-weight-light mb-8" max-width="720">
            info about commonette here
          </v-responsive>
          <v-btn color="grey" v-on:click="navigateRoute('/questionnaire')" outlined large>
            <span class="grey--text text--darken-1 font-weight-bold">
              Questionnaire Page (Temporary)
            </span>
          </v-btn>
          <v-btn color="grey" v-on:click="navigateRoute('/recommend')" outlined large>
            <span class="grey--text text--darken-1 font-weight-bold">
              Recommendation Page (Temporary)
            </span>
          </v-btn>
        </v-container>
        <div class="py-12"></div>
      </section>

      <section id="mediums" class="grey lighten-3">
        <div class="py-12"></div>
        <v-container class="text-center">
          <h2 class="display-2 font-weight-bold mb-3">Mediums</h2>
          <v-responsive class="mx-auto mb-12" width="56">
            <v-divider class="mb-1"></v-divider>
            <v-divider></v-divider>
          </v-responsive>
          <v-row>
            <v-col v-for="({ icon, title, text }, i) in mediums" :key="i" cols="12" md="3">
              <v-card class="py-12 px-4" color="grey lighten-5" flat>
                <v-theme-provider dark>
                  <div>
                    <v-avatar color="primary" size="88">
                      <v-icon large v-text="icon"></v-icon>
                    </v-avatar>
                  </div>
                </v-theme-provider>
                <v-card-title class="justify-center font-weight-black text-uppercase" v-text="title"></v-card-title>
                <v-card-text class="subtitle-1" v-text="text"> </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
        <div class="py-12"></div>
      </section>

      <v-theme-provider dark>
        <v-parallax :height="$vuetify.breakpoint.smAndDown ? 700 : 1000" src="https://images.unsplash.com/photo-1416339442236-8ceb164046f8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1892&q=80">
          <v-container>
            <div class="py-12"></div>
            <h2 class="display-2 font-weight-bold mb-3">APIs Used</h2>
            <v-responsive class="mx-auto mb-12" width="56">
              <v-divider class="mb-1"></v-divider>
              <v-divider></v-divider>
            </v-responsive>
            <v-row dense>
              <v-col v-for="(item, i) in items" :key="i" cols="4">
                <v-card :color="item.color" dark>
                  <div class="d-flex flex-no-wrap justify-space-between">
                    <div>
                      <v-card-title class="headline" v-text="item.title" :style="item.textcolor"></v-card-title>

                      <v-card-subtitle v-text="item.description" :style="item.textcolor" style="text-align: left"></v-card-subtitle>

                      <v-card-actions>
                        <!-- custom button here -->
                        <v-btn v-if="item.artist === 'Ellie Goulding'" class="ml-2 mt-3" fab icon height="40px" right width="40px">
                          <v-icon>mdi-play</v-icon>
                        </v-btn>

                        <v-btn v-else class="ml-2 mt-5" color="secondary" rounded small :href="item.site" target="_blank">
                          ABOUT API
                        </v-btn>
                      </v-card-actions>
                    </div>

                    <v-avatar class="ma-3" size="125" tile>
                      <v-img :src="item.src" contain></v-img>
                    </v-avatar>
                  </div>
                </v-card>
              </v-col>
            </v-row>
          </v-container>
          <v-responsive class="mx-auto mb-12" width="56">
            <v-divider class="mb-1"></v-divider>
            <v-divider></v-divider>
          </v-responsive>
          <v-container>
            <h2 class="display-1 font-weight-bold mb-3 black--text">
              What are you waiting for?
            </h2>
            <v-row class="mx-auto" justify="center">
              <v-btn elevation="2" large class="ma-2" v-on:click="createRoomPopup = true">
                Create Room
              </v-btn>
              <v-btn elevation="2" large v-on:click="joinRoomPopup = true" class="ma-2">
                Join Room
              </v-btn>
            </v-row>
          </v-container>
        </v-parallax>
      </v-theme-provider>
    </v-main>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      createRoomPopup: false,
      joinRoomPopup: false,
      valid: false,
      roomCode: "",
      roomName: "",
      errors: false,
      errorMessage: "",
      inputRequiredRule: [(v) => v.length > 0 || "Required"],

      loader: null,
      loading1: false,
      loading2: false,
      loading3: false,

      items: [
        {
          color: "#fafafa",
          textcolor: "color: black",
          src:
            "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/1280px-YouTube_full-color_icon_%282017%29.svg.png",
          title: "YouTube Data API",
          description: "YouTube info here",
          site: "https://developers.google.com/youtube/v3/docs/videos/list",
        },
        {
          color: "#191414",
          textcolor: "color: #FFFFFF",
          src:
            "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/1024px-Spotify_logo_without_text.svg.png",
          title: "Spotify Search API",
          description:
            "Get Spotify Catalog information about albums, artists, playlists, tracks, shows or episodes that match a keyword string.",
          site:
            "https://developer.spotify.com/documentation/web-api/reference/search/search/",
        },
        {
          color: "#191414",
          textcolor: "color: #FFFFFF",
          src:
            "https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/1024px-Spotify_logo_without_text.svg.png",
          title: "Spotify Recommendations API",
          description:
            "Create a playlist-style listening experience based on seed artists, tracks and genres.",
          site:
            "https://developer.spotify.com/documentation/web-api/reference/browse/get-recommendations/",
        },
        {
          color: "#fafafa",
          textcolor: "color: black",
          src:
            "https://upload.wikimedia.org/wikipedia/commons/b/ba/Google_Books_logo_2015.svg",
          title: "Google Books API",
          description: "Info about google books here",
          site: "https://developers.google.com/books",
        },
        {
          color: "#fafafa",
          textcolor: "color: black",
          src:
            "https://s3.amazonaws.com/mashape-production-logos/apis/5c35064ce4b0ddd96d1a3a36_medium",
          title: "Entertainment Data Hub API",
          description: "Info about Data Hub API here",
          site:
            "https://rapidapi.com/IVALLC/api/entertainment-data-hub/details",
        },
        {
          color: "#fafafa",
          textcolor: "color: black",
          src:
            "https://rapidapi-prod-apis.s3.amazonaws.com/64ed0ed2-6103-4f9b-ab95-f8cc98c7e40c.png",
          title: "OTT details API",
          description:
            "Get Streaming details of Movie and TV Shows. We support 150+ Streaming platforms in US and India such as HBO, YouTube, Netflix , Primve Video, Hotstar, Hulu, etc . ",
          site:
            "https://rapidapi.com/gox-ai-gox-ai-default/api/ott-details/endpoints",
        },
      ],

      mediums: [
        {
          icon: "mdi-youtube",
          title: "YouTube",
          text: "See recommended videos for you and your friends.",
        },
        {
          icon: "mdi-spotify",
          title: "Spotify",
          text:
            "Generate Spotify recommendations from you and your friends' favourite songs.",
        },
        {
          icon: "mdi-book",
          title: "Books",
          text: "Find books ",
        },
        {
          icon: "mdi-filmstrip",
          title: "Movies",
          text: "I don't know what I'm doing",
        },
      ],
    };
  },

  watch: {
    loader() {
      const l = this.loader;
      this[l] = !this[l];

      setTimeout(() => (this[l] = false), 1500);

      this.loader = null;
    },
  },

  methods: {
    navigateRoute(newpath) {
      this.$router.push(newpath);
    },
    createRoom() {
      if (this.$refs.form.validate()) {
        let roomName = this.roomName;
        axios({
          url: "/create-room/" + roomName,
          method: "GET",
        })
          .then((response) => {
            localStorage.setItem("roomCode", response.data.room_code);
            localStorage.setItem("roomName", response.data.room_name);
            this.navigateRoute("/questionnaire");
          })
          .catch((error) => {
            this.errors = true;
            this.errorMessage = "API Connection Error";
            if (error.response) {
              this.errorMessage = error.response.data;
            }
          });
      }
    },
    joinRoom() {
      if (this.$refs.form.validate()) {
        let roomCode = this.roomCode;
        axios({
          url: "/room/" + roomCode,
          method: "GET",
        })
          .then((response) => {
            localStorage.setItem("roomName", response.data.room_name);
            localStorage.setItem("roomCode", this.roomCode);
            this.navigateRoute("/questionnaire");
          })
          .catch((error) => {
            this.errors = true;
            this.errorMessage = "API Connection Error";
            if (error.response) {
              this.errorMessage = error.response.data;
            }
          });
      }
    },
  },
};
</script>
