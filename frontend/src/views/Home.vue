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
            </v-form>
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn color="primary" :loading="loading1" @click="loader = 'loading1'" :disabled="!valid" v-on:click="joinRoom(true)">New User</v-btn>
            <v-btn color="success" :loading="loading2" @click="loader = 'loading2'" :disabled="!valid" v-on:click="joinRoom(false)">View Room</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      <main class="l-main">
        <!--===== HOME =====-->
        <section class="home" id="home">
          <div class="home">
            <div class="home__container bd-grid">
              <div class="home__img">
                <img src="../images/landing1.png" data-speed="5" alt="" class="move">
                <img src="../images/landing2.png" data-speed="5" alt="" class="move">
                <img src="../images/landing3.png" data-speed="-2" alt="" class="move">
                <img src="../images/landing4.png" alt="" class="move">
                <img src="../images/landing5.png" alt="" class="move">
              </div>
              <div class="home__data">
                <div data-aos="zoom-in">
                  <h1 class="home__title">Commonette</h1>
                  <div data-aos="zoom-in" data-aos-delay="500">
                    <v-btn elevation="2" large class="ma-2 home__button" v-on:click="createRoomPopup = true"> Create Room</v-btn>
                    <v-btn elevation="2" large class="ma-2 home__button" v-on:click="joinRoomPopup = true">Join Room</v-btn>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>

      <!-- <v-img src="https://images.unsplash.com/photo-1487017159836-4e23ece2e4cf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1951&q=80">
        <v-theme-provider light>
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
      </v-img> -->
      <!-- 
      <section id="about">

        <div class="py-12"></div>
        <h2 class="display-2 font-weight-light mb-3">Optional Title Here?</h2>
        <v-responsive class="mx-auto mb-8" width="56">
          <v-divider class="mb-1"></v-divider>
          <v-divider></v-divider>
        </v-responsive>

        <v-container fluid class="my-5">
          <div v-for="(story, i) in stories" :key=i>
            <v-row>
              <v-col md=6 sm=12>
                picture here
                <v-parallax class="bottom-gradient" :src="story.src"></v-parallax>
              </v-col>
              <v-col md=6 sm=12>
                text here
              </v-col>
            </v-row>
          </div>

        </v-container>

        <v-divider class="mb-1"></v-divider>
        <v-divider></v-divider> -->

      <!-- <v-responsive v-for="(story, i) in stories" :key=i max-width="100%" height="500px">
          <div v-if="i % 2 == 0">
            <v-row height=500>
              <v-col cols='5' md='5'>
                <v-parallax class="bottom-gradient" height=700 :src="story.src"></v-parallax>
              </v-col>
              <v-col cols='7' md='7' class="py-6 px-12 fluid text-wrap" max-width="50%">
                <div class="py-10"></div>
                <h2 class="display-4 text-right mx-auto">{{ story.title }}</h2>
                <h2 class="display-2 text-right mx-auto my-4">{{ story.subtitle }}</h2>
                <p class="headline text-right mx-6">{{ story.message }}</p>
              </v-col>
            </v-row>
          </div>
          <div v-else>
            <v-row height=500>
            <v-col cols='7' md='7' class="py-6 px-12 fluid text-wrap" max-width="50%">
              <div class="py-10"></div>
              <h2 class="display-4 text-left mx-auto">{{ story.title }}</h2>
              <h2 class="display-2 text-left mx-auto my-4">{{ story.subtitle }}</h2>
              <p class="headline text-left mx-6">{{ story.message }}</p>
            </v-col>
            <v-col cols='5' md='5'>
              <v-parallax class="bottom-gradient align-left" height=500 :src="story.src"></v-parallax>
            </v-col>
          </v-row>
          </div>
        </v-responsive> -->

      <!-- align-center body text -->
      <!-- <v-responsive class="mx-auto title font-weight-light " max-width="720">
          <br><br>
        </v-responsive>

      </section> -->

      <section id="mediums" color="rgb(54, 54, 79)">
        <div class="py-12"></div>
        <v-container class="text-center">
          <h2 class="display-2 font-weight-bold mb-3" style="color:#ebebeb">What recommendations you can expect</h2>
          <v-responsive class="mx-auto mb-12" width="56">
            <v-divider class="mb-1" color="#ebebeb"></v-divider>
            <v-divider color="#ebebeb"></v-divider>
          </v-responsive>
          <v-row>
            <v-col v-for="({ icon, title, text }, i) in mediums" :key="i" cols="12" md="3">
              <div data-aos="flip-up" data-aos-delay="100">
                <v-card class="py-12 px-4 rounded-xl" color="#E3E9F2" flat>
                  <v-theme-provider dark>
                    <div>
                      <v-avatar color="primary" size="88">
                        <v-icon large v-text="icon"></v-icon>
                      </v-avatar>
                    </div>
                  </v-theme-provider>
                  <v-card-title class="justify-center font-weight-black text-uppercase" v-text="title" style="color:rgb(48, 48, 68);"></v-card-title>
                  <v-card-text class="subtitle-1" style="color:rgb(72, 72, 103)" v-text="text"> </v-card-text>
                </v-card>
              </div>
            </v-col>
          </v-row>
        </v-container>
        <div class="py-10"></div>
      </section>

      <v-theme-provider id="api" light>
        <!-- <v-parallax :height="$vuetify.breakpoint.smAndDown ? 700 : 1000" src="https://images.unsplash.com/photo-1416339442236-8ceb164046f8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1892&q=80"> -->
        <div>
          <v-container>
            <div class="py-6"></div>
            <h2 class="display-2 font-weight-bold mb-3" color="rgb(72, 72, 103)">APIs Used</h2>
            <v-responsive class="mx-auto mb-12" width="56">
              <v-divider class="mb-1"></v-divider>
              <v-divider></v-divider>
            </v-responsive>
            <v-row dense>
              <v-col v-for="(item, i) in items" :key="i" cols="12" lg='4' style="padding:10px">
                <div data-aos="fade-up">
                  <v-card color="#50587C" shaped>
                    <div class="d-flex flex-no-wrap justify-space-between">
                      <div>
                        <v-card-text class="headline" v-text="item.title" style="color: #ebebeb; text-align: left;"></v-card-text>

                        <v-card-subtitle v-text="item.description" style="color:#ebebeb; text-align: left"></v-card-subtitle>

                        <v-card-actions>
                          <!-- custom button here -->
                          <v-btn v-if="item.artist === 'Ellie Goulding'" class="ml-2 mt-3" fab icon height="40px" right width="40px">
                            <v-icon>mdi-play</v-icon>
                          </v-btn>

                          <v-btn v-else class="ml-2 mt-5 mb-3" color="#F1F4F9" rounded small :href="item.site" target="_blank">
                            ABOUT API
                          </v-btn>
                        </v-card-actions>
                      </div>

                      <v-avatar class="ma-4" size="105" tile>
                        <v-img :src="item.src" contain></v-img>
                      </v-avatar>
                    </div>
                  </v-card>
                </div>
              </v-col>
            </v-row>
          </v-container>
          <v-responsive class="mx-auto mb-12" width="56">
            <v-divider class="mb-1"></v-divider>
            <v-divider></v-divider>
          </v-responsive>
          <v-container>
            <h2 class="display-1 font-weight-bold mb-3" style="color:rgb(54, 54, 79)">
              What are you waiting for?
            </h2>
            <v-row class="mx-auto" justify="center">
              <v-btn elevation="2" large class="ma-2" v-on:click="createRoomPopup = true" color="#50587C" style="color:white">
                Create Room
              </v-btn>
              <v-btn elevation="2" large v-on:click="joinRoomPopup = true" class="ma-2" color="#50587C" style="color:white">
                Join Room
              </v-btn>
            </v-row>
          </v-container>
        </div>
        <!-- </v-parallax> -->
      </v-theme-provider>
    </v-main>
  </div>
</template>
        
<script>
import { gsap } from "gsap";
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

      stories: [
        {
          title: "Suprise yourself",
          subtitle: "and your friends",
          message:
            "Tired of being indecisive about what movie to watch? Not sure what kind of music to listen to when you're with a group of friends? Trying to find the perfect movie watch with your date without yawning? We have...",
          src:
            "https://images.pexels.com/photos/3768177/pexels-photo-3768177.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
          alt:
            "https://images.pexels.com/photos/2253849/pexels-photo-2253849.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        },
        {
          title: "Recommendations",
          subtitle: "catered to you and your friends",
          message: "We will ask you to fill a questionnaire where...",
          src:
            "https://images.pexels.com/photos/2719510/pexels-photo-2719510.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
          alt:
            "https://images.pexels.com/photos/2479312/pexels-photo-2479312.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        },
        {
          title: "Countless of recommendations",
          subtitle: "all at your fingertips",
          message: "The results are then aggregated and sent to...",
          src:
            "https://images.pexels.com/photos/4488194/pexels-photo-4488194.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
          alt:
            "https://images.pexels.com/photos/2479312/pexels-photo-2479312.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260",
        },
      ],

      items: [
        {
          color: "#fafafa",
          textcolor: "color: black",
          src:
            "https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/1280px-YouTube_full-color_icon_%282017%29.svg.png",
          title: "YouTube Data API",
          description:
            "The YouTube Data API lets you incorporate functions normally executed on the YouTube website into your own website or application. ",
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
          description:
            "The Books API is a way to search and access the world's book contents, as well as to create and view personalization around that content.",
          site: "https://developers.google.com/books",
        },
        {
          color: "#fafafa",
          textcolor: "color: black",
          src: require("../images/OTT.png"),
          title: "OTT details API",
          description:
            "Get Streaming details of Movie and TV Shows. We support 150+ Streaming platforms in US and India such as HBO, YouTube, Netflix , Primve Video, Hotstar, Hulu, etc . ",
          site:
            "https://rapidapi.com/gox-ai-gox-ai-default/api/ott-details/endpoints",
        },
      ],

      mediums: [
        {
          icon: "mdi-youtube red",
          title: "YouTube",
          text: "See recommended videos for you and your friends.",
        },
        {
          icon: "mdi-spotify green",
          title: "Spotify",
          text:
            "Generate Spotify recommendations from you and your friends' favourite songs.",
        },
        {
          icon: "mdi-book blue",
          title: "Books",
          text: "Find books ",
        },
        {
          icon: "mdi-movie-open pink",
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
            localStorage.clear();
            localStorage.setItem("roomCode", response.data.room_code);
            localStorage.setItem("roomName", response.data.room_name);
            this.$bus.$emit("updated", "created");
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
    joinRoom(flag) {
      if (this.$refs.form.validate()) {
        let roomCode = this.roomCode;
        axios({
          url: "/room/" + roomCode,
          method: "GET",
        })
          .then((response) => {
            localStorage.clear();
            localStorage.setItem("roomName", response.data.room_name);
            localStorage.setItem("roomCode", this.roomCode);
            if (response.data.questionnaire) {
              let roomUsers = [];
              for (var person of response.data.questionnaire) {
                roomUsers.push({
                  name: person.name,
                  age: person.age,
                });
              }
              localStorage.setItem("roomUsers", JSON.stringify(roomUsers));
            }
            this.$bus.$emit("updated", "joined");
            if (flag) {
              this.navigateRoute("/questionnaire");
            } else {
              this.navigateRoute("/dashboard/" + this.roomCode);
            }
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

// /*===== MENU SHOW Y HIDDEN =====*/
// const navMenu = document.getElementById('nav-menu'),
//     toggleMenu = document.getElementById('nav-toggle'),
//     closeMenu = document.getElementById('nav-close')

// // SHOW
// toggleMenu.addEventListener('click', ()=>{
//     navMenu.classList.toggle('show')
// })

// // HIDDEN
// closeMenu.addEventListener('click', ()=>{
//     navMenu.classList.remove('show')
// })

// /*===== MOUSEMOVE HOME IMG =====*/
document.addEventListener("mousemove", move);
function move(e) {
  this.querySelectorAll(".move").forEach((layer) => {
    const speed = layer.getAttribute("data-speed");

    const x = (window.innerWidth - e.pageX * speed) / 120;
    const y = (window.innerHeight - e.pageY * speed) / 120;

    layer.style.transform = `translateX(${x}px) translateY(${y}px)`;
  });
}

/*===== GSAP ANIMATION =====*/
// // NAV
// gsap.from('.nav__logo, .nav__toggle', {opacity: 0, duration: 1, delay:2, y: 10})
// gsap.from('.nav__item', {opacity: 0, duration: 1, delay: 2.1, y: 30, stagger: 0.2,})

// HOME
gsap.from(".home__title", { opacity: 0, duration: 1, delay: 1.6, y: 30 });
gsap.from(".home__description", { opacity: 0, duration: 1, delay: 1.8, y: 30 });
gsap.from(".home__button", { opacity: 0, duration: 1, delay: 2.1, y: 30 });
gsap.from(".home__img", { opacity: 0, duration: 1, delay: 1.3, y: 30 });
</script>

<style lang="scss">
/*===== GOOGLE FONTS =====*/
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap");

/*===== VARIABLES CSS =====*/
:root {
  --header-height: 3rem;

  /*===== Colors =====*/
  --first-color: rgb(81, 81, 118);
  --first-color-dark: rgb(72, 72, 103);
  --first-color-darken: rgb(48, 48, 68);
  --white-color: #ebebeb;
  // #FCF8F8

  /*===== Font and typography =====*/
  --body-font: "Poppins", sans-serif;
  --big-font-size: 2.5rem;
  --normal-font-size: 0.938rem;

  /*===== z index =====*/
  --z-fixed: 100;
}

@media screen and (min-width: 768px) {
  :root {
    --big-font-size: 5rem;
    --normal-font-size: 1rem;
  }
}

/*===== BASE =====*/
*,
::before,
::after {
  box-sizing: border-box;
}

body {
  margin: var(--header-height) 0 0 0;
  padding: 0;
  font-family: var(--body-font);
  font-size: var(--normal-font-size);
  font-weight: 500;
}

h1,
p,
ul {
  margin: 0;
}

ul {
  padding: 0;
  list-style: none;
}

a {
  text-decoration: none;
}

img {
  max-width: 100%;
  height: auto;
}

/*===== LAYOUT =====*/
.bd-grid {
  max-width: 1024px;
  display: grid;
  grid-template-columns: 100%;
  column-gap: 2rem;
  width: calc(100% - 2rem);
  margin-left: 1rem;
  margin-right: 1rem;
}
.l-header {
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: var(--z-fixed);
  background-color: var(--first-color);
}

/*=== Show menu ===*/
.show {
  right: 0;
}

/*===== HOME =====*/
.home {
  background-color: var(--first-color);
  overflow: hidden;

  &__container {
    height: calc(100vh - var(--header-height));
    grid-template-rows: repeat(2, max-content);
    row-gap: 1.5rem;
  }
  &__img {
    position: relative;
    padding-top: 1.5rem;
    justify-self: center;
    width: 302px;
    height: 233px;

    & img {
      position: absolute;
      top: 0;
      left: 0;
    }
  }
  &__data {
    color: var(--white-color);
  }
  &__title {
    font-size: var(--big-font-size);
    line-height: 1.3;
    margin-bottom: 1rem;
  }
  &__description {
    margin-bottom: 2.5rem;
  }

  &__button {
    display: inline-block;
    background-color: var(--first-color-dark);
    color: var(--white-color);
    padding: 1.125rem 2rem;
    border-radius: 0.5rem;

    &:hover {
      background-color: var(--first-color-darken);
    }
  }
}

#api,
#about {
  background-color: #e3e9f2;
}

/* ===== MEDIA QUERIES=====*/
@media screen and(min-width: 768px) {
  body {
    margin: 0;
  }

  .nav {
    height: calc(var(--header-height) + 1.5rem);

    &__toggle,
    &__close {
      display: none;
    }
    &__list {
      display: flex;
    }
    &__item {
      margin-left: 3rem;
      margin-bottom: 0;
    }
  }

  .home {
    &__container {
      height: 100vh;
      grid-template-columns: repeat(2, max-content);
      grid-template-rows: 1fr;
      row-gap: 0;
      align-items: center;
      justify-content: center;
    }
    &__data {
      text-align: left;
    }
    &__img {
      order: 1;
      width: 375px;
      height: 289px;

      & img {
        width: 375px;
      }
    }
  }
}

@media screen and(min-width: 1024px) {
  .bd-grid {
    margin-left: auto;
    margin-right: auto;
  }

  .home {
    &__container {
      justify-content: initial;
      column-gap: 4.5rem;
    }
    &__img {
      width: 604px;
      height: 466px;
      & img {
        width: 604px;
      }
    }
  }
}
</style>

<style>
/* for stories */
.bottom-gradient {
  background-image: linear-gradient(
    to top,
    rgba(0, 0, 0, 0.4) 0%,
    transparent 72px
  );
}
.v-parallax__image {
  /* transform: none !important; */
  /* width: 100% !important; */
}
</style>

