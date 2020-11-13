<template>
  <div class="home">
    <v-main>
      <v-dialog v-model="createRoomPopup" max-width="350">
        <v-card>
          <v-card-title class="headline justify-center" style="color:#494C97">Create New Room</v-card-title>
          <v-card-text>
            <v-form @submit.prevent v-model="valid" ref="form">
              <v-text-field label="Enter a room name" v-model="roomName" :rules="inputRequiredRule" autofocus v-on:keyup.enter="createRoom" @keyup.enter="loader = 'loading1'" color="#494C97"></v-text-field>
              <p v-if="errors" class="red--text">
                {{ errorMessage }}
              </p>
              <v-btn dark color="rgb(81, 81, 118)" :loading="loading1" @click="loader = 'loading1'" :disabled="!valid" v-on:click="createRoom">Enter</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-dialog>
      <v-dialog v-model="joinRoomPopup" max-width="350">
        <v-card>
          <v-card-title class="headline justify-center" style="color:#494C97">Join Existing Room</v-card-title>
          <v-card-text>
            <v-form @submit.prevent v-model="valid" ref="form">
              <v-text-field label="Enter the room code" v-model="roomCode" :rules="inputRequiredRule" autofocus v-on:keyup.enter="joinRoom" @keyup.enter="loader = 'loading1'" color="#494C97"></v-text-field>
              <p v-if="errors" class="red--text">
                {{ errorMessage }}
              </p>
            </v-form>
          </v-card-text>
          <v-card-actions class="justify-center">
            <v-btn dark color="rgb(81, 81, 118)" :loading="loading1" @click="loader = 'loading1'" :disabled="!valid" v-on:click="joinRoom(true)">New User</v-btn>
            <v-btn dark color="#7579BD" :loading="loading2" @click="loader = 'loading2'" :disabled="!valid" v-on:click="joinRoom(false)">View Room</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <section id="home">
        <div class="home__container bd-grid">
          <div class="home__img">
            <img src="../images/landing1.png" data-speed="5" alt="" class="move">
            <img src="../images/landing2.png" data-speed="5" alt="" class="move">
            <img src="../images/landing3.png" data-speed="-2" alt="" class="move">
            <img src="../images/landing4.png" alt="" class="move">
            <img src="../images/landing5.png" alt="" class="move">
          </div>
          <div class="home__data">

            <v-row class="ml-4">
              <div data-aos="zoom-in">
                <h1 class="mt-10 font-weight-bold text-lg-h1 text-md-h2 text-sm-h3 text-h4 text-center">Commonette</h1>
              </div>
            </v-row>

            <v-row class="ml-4">
              <div id="animated-description" class="my-4" data-aos="zoom-in" data-aos-delay="300">
                <span class="stationary-word mx-2 text-lg-h6 text-md-subtitle-1">We will recommend you</span>
                <span class="animate-word text-lg-h6 text-md-subtitle-1"> YouTube videos.</span>
                <span class="animate-word"> Movies.</span>
                <span class="animate-word"> Books.</span>
                <span class="animate-word"> Music.</span>
              </div>
            </v-row>

            <v-row align="center" class="white--text mx-auto" justify="center">
              <div data-aos="zoom-in" data-aos-delay="600">
                <v-btn elevation="2" large class="ma-2 home__button" v-on:click="createRoomPopup = true"> Create Room</v-btn>
              </div>
              <div data-aos="zoom-in" data-aos-delay="900">
                <v-btn elevation="2" large class="ma-2 home__button" v-on:click="joinRoomPopup = true">Join Room</v-btn>
              </div>
            </v-row>
            <div class="py-10">
              <!-- <div data-aos="zoom-in" data-aos-delay="600"> -->
              <v-theme-provider dark>
                <v-row align="center" class="white--text mx-auto" justify="center" data-aos="zoom-in" data-aos-delay="1200">
                  <v-btn class="align-self-end" fab outlined @click="$vuetify.goTo('#about')">
                    <v-icon>mdi-chevron-double-down</v-icon>
                  </v-btn>
                </v-row>
              </v-theme-provider>
            </div>
          </div>
        </div>
      </section>

      <section id="about">
        <div class="pt-10"></div>
        <v-responsive v-for="(story, i) in stories" :key=i>
          <div v-if="i % 2 == 0" data-aos="fade-right" data-aos-duration="2500">
            <v-row v-if="$vuetify.breakpoint.smAndDown">
              <v-col cols=12>
                <v-img height="300px" style="height:300px;width:600px;" :src="story.src"></v-img>
              </v-col>
              <v-col cols=12>
                <div class="px-5">
                  <h2 class="text-lg-h2 text-md-h2 text-sm-h3 text-h4 text-left mx-auto">{{ story.title }}</h2>
                  <h2 class="text-lg-h3 text-md-h4 text-sm-h5 text-h6 text-left mx-auto my-4">{{ story.subtitle }}</h2>
                  <p class="text-lg-h5 text-md-h6 text-body-1 text-left font-weight-regular">{{ story.message }}</p>
                </div>
              </v-col>
            </v-row>
            <v-row v-else>
              <v-col cols="1"></v-col>
              <v-col cols="4">
                <v-img height="350px" style="height:400px;width:700px;" :src="story.src"></v-img>
              </v-col>
              <v-col cols="6">
                <div class="pt-5 pr-5">
                  <h2 class="text-lg-h1 text-md-h2 text-sm-h3 text-h4 text-right mx-auto">{{ story.title }}</h2>
                  <h2 class="text-lg-h3 text-md-h4 text-sm-h5 text-h6 text-right mx-auto my-4">{{ story.subtitle }}</h2>
                  <p class="text-lg-h5 text-md-h6 text-body-1 text-right font-weight-light">{{ story.message }}</p>
                </div>
              </v-col>
              <v-col cols="1"></v-col>
            </v-row>
          </div>
          <div v-else data-aos="fade-left" data-aos-duration="2500">
            <v-row v-if="$vuetify.breakpoint.smAndDown">
              <v-col cols=12>
                <v-img height="300px" style="height:300px;width:600px;" :src="story.src"></v-img>
              </v-col>
              <v-col cols=12>
                <div class="px-5">
                  <h2 class="text-lg-h1 text-md-h2 text-sm-h3 text-h4 text-left mx-auto">{{ story.title }}</h2>
                  <h2 class="text-lg-h3 text-md-h4 text-sm-h5 text-h6 text-left mx-auto my-4">{{ story.subtitle }}</h2>
                  <p class="text-lg-h5 text-md-h6 text-body-1 text-left font-weight-regular">{{ story.message }}</p>
                </div>
              </v-col>
            </v-row>
            <v-row v-else>
              <v-col cols="1"></v-col>
              <v-col cols="6">
                <div class="pt-5 pl-5">
                  <h2 class="text-lg-h1 text-md-h2 text-sm-h3 text-h4 text-left mx-auto my-4">{{ story.title }}</h2>
                  <h2 class="text-lg-h3 text-md-h4 text-sm-h5 text-h6 text-left mx-auto my-4">{{ story.subtitle }}</h2>
                  <p class="text-lg-h5 text-md-h6 text-body-1 text-left font-weight-light">{{ story.message }}</p>
                </div>
              </v-col>
              <v-col cols="4">
                <v-img height="400px" style="height:400px;width:700px;" :src="story.src"></v-img>
              </v-col>
              <v-col cols="1"></v-col>
            </v-row>
          </div>
        </v-responsive>
        <div class="pb-10"></div>
      </section>

      <section id="mediums" color="rgb(54, 54, 79)">
        <div class="py-6"></div>
        <v-container class="text-center">
          <h2 class="text-lg-h3 text-md-h4 text-sm-h5 text-h6 text-left mx-auto mb-3 text-center" style="color:#ebebeb">Entertainment mediums</h2>
          <v-responsive class="mx-auto mb-12" width="56">
            <v-divider class="mb-1 white"></v-divider>
            <v-divider class="white"></v-divider>
          </v-responsive>
          <v-row>
            <v-col v-for="({ icon, title, text }, i) in mediums" :key="i" cols="12" sm="6" md='4' lg='3'>
              <div data-aos="flip-up" :data-aos-delay="200*i" data-aos-duration="500">
                <vue-flip active-hover width="280px" height="320px" class="mx-auto">
                  <template v-slot:front>
                    <v-card width="280px" height="320px" class="mx-auto py-12 px-4 rounded-xl" color="#E3E9F2" flat>
                      <v-theme-provider dark>
                        <div>
                          <v-avatar color="primary" size="88">
                            <v-icon large v-text="icon"></v-icon>
                          </v-avatar>
                        </div>
                      </v-theme-provider>
                      <v-card-title class="justify-center font-weight-black text-uppercase" v-text="title" style="color:rgb(48, 48, 68);"></v-card-title>
                      <p class="text--disabled card-text-hover" @mouseover="hoverText(true, 'Flipping!', i)" @mouseout="hoverText(false, '', i)">Touch me!</p>
                    </v-card>
                  </template>
                  <template v-slot:back>
                    <v-card width="280px" height="320px" class="mx-auto py-12 px-4 rounded-xl" color="#E3E9F2" flat>
                      <p v-if="title == 'Music'" class="subtitle-1 px-4 my-0 font-weight-bold text-left">How are Songs recommended?</p>
                      <p v-else class="subtitle-1 px-4 my-0 font-weight-bold text-left">How are {{title}} recommended?</p>
                      <v-card-text class="subtitle-1 text-left" style="color:rgb(72, 72, 103)" v-text="text"> </v-card-text>
                    </v-card>
                  </template>
                </vue-flip>
              </div>
            </v-col>
          </v-row>
        </v-container>
        <div class="py-10"></div>
      </section>

      <v-theme-provider id="bottom" class="white">
        <div>
          <v-container>
            <h2 class="text-lg-h4 text-md-h4 text-sm-h5 text-h6  my-3" style="color:rgb(54, 54, 79)">
              What are you waiting for?
            </h2>
            <v-row class="mx-auto mb-3 justify-center">
              <v-btn elevation="2" large class="ma-2" v-on:click="createRoomPopup = true" color="#50587C" style="color:white">
                Create Room
              </v-btn>
              <v-btn elevation="2" large v-on:click="joinRoomPopup = true" class="ma-2" color="#50587C" style="color:white">
                Join Room
              </v-btn>
            </v-row>
          </v-container>
        </div>
      </v-theme-provider>
    </v-main>
  </div>
</template>
        
<script>
import { gsap } from "gsap";
import axios from "axios";
import VueFlip from "vue-flip";
export default {
  components: {
    "vue-flip": VueFlip,
  },
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
          title: "",
          subtitle: "Surprise yourself and discover new content every day",
          message:
            "Can't find a good book to read? Sick of your usual playlists? Need a good YouTube rabbit hole to dive into? Use Commonette to discover content that you never knew you would love. ",
          src: require("../images/story1.png"),
        },
        {
          title: "",
          subtitle: "Countless recommendations catered to you and your friends",
          message:
            "Answer a questionnaire to find out what entertainment mediums you and your friends are likely to enjoy! Videos, movies, books or music — we've got you covered no matter the occasion.",
          src: require("../images/story2.png"),
        },
        {
          title: "",
          subtitle:
            "The easiest and most convenient way to find common interests",
          message:
            "You could be watching the perfect movie with your date or jamming to your favourite music with your friends in just a few clicks. It can't get any easier than this!",
          src: require("../images/story3.png"),
        },
      ],
      mediums: [
        {
          icon: "mdi-youtube red",
          title: "YouTube Videos",
          text:
            "Choose your favourite YouTube categories, and we will fetch common categories to be enjoyed by your group.",
        },
        {
          icon: "mdi-book blue",
          title: "Books",
          text:
            "Rank your favourite genres of books, and we will scour the internet to look for books that match those genres.",
        },
        {
          icon: "mdi-movie-open pink",
          title: "Movies",
          text:
            "By selecting your favourite genres and setting your minimum IMDB value, look for movies within those genres with a higher IMDB score.",
        },
        {
          icon: "mdi-spotify green",
          title: "Music",
          text:
            "By telling us your favourite songs and artists, we will generate new songs that are similar to your group's favourite artists and genres.",
        },
      ],
    };
  },

  mounted() {
    this.$nextTick(() => {
      var words = document.getElementsByClassName("animate-word");
      var currentWordIndex = 0;

      words[currentWordIndex].style.opacity = 1;

      var defaultClassName = words[0].className;
      console.log(defaultClassName);

      setInterval(() => {
        var outgoingWord = words[currentWordIndex];
        var incomingWord =
          currentWordIndex == words.length - 1
            ? words[0]
            : words[currentWordIndex + 1];

        // animate outgoing word out
        outgoingWord.className = defaultClassName + " out";

        // animate incoming word in
        incomingWord.className = defaultClassName + " behind";
        incomingWord.style.opacity = 1;
        setTimeout(() => {
          incomingWord.className = defaultClassName + " in";
        }, 400);
        // console.log(outgoingWord, incomingWord);

        // update word order
        currentWordIndex =
          currentWordIndex == words.length - 1 ? 0 : currentWordIndex + 1;
      }, 2500);

      // console.log(words);
    });
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
    hoverText(over, msg, i) {
      var text = document.getElementsByClassName("card-text-hover")[i];
      text.innerHTML = over ? msg : "Touch me!";
    },
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
                  gender: person.gender,
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

// HOME
gsap.config({
  nullTargetWarn: false,
});

gsap.from(".home__title", { opacity: 0, duration: 1, delay: 1.6, y: 30 });
gsap.from(".home__description", { opacity: 0, duration: 1, delay: 1.8, y: 30 });
gsap.from(".home__button", { opacity: 0, duration: 1, delay: 2.1, y: 30 });
gsap.from(".home__img", { opacity: 0, duration: 1, delay: 1.3, y: 30 });
</script>

<style lang="scss">
.animate-word {
  width: 100%;
  text-align: left;
  display: inline-block;
  position: absolute;
  transform: translateZ(50px);
  transform-origin: 50% 50% 25px;
  opacity: 0;
}

.animate-word.out {
  transform: rotateX(90deg);
  transition: transform 0.32s cubic-bezier(0.55, 0.055, 0.675, 0.19);
}

.animate-word.behind {
  transform: rotateX(-90deg);
}

.animate-word.in {
  transform: rotateX(0deg);
  transition: transform 0.38s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

/*===== GOOGLE FONTS =====*/
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap");
@import "~@/styles/colors";

/*===== VARIABLES CSS =====*/
:root {
  --header-height: 3rem;

  /*===== Font and typography =====*/
  --body-font: "Poppins", sans-serif;
  --big-font-size: 2.5rem;
  --normal-font-size: 0.938rem;
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
  background-color: $primary;
}

/*=== Show menu ===*/
.show {
  right: 0;
}

/*===== HOME =====*/
.home {
  background-color: $primary;
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
    color: $white;
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
    background-color: $primary-dark;
    color: var(--white-color);
    padding: 1.125rem 2rem;
    border-radius: 0.5rem;

    &:hover {
      background-color: $primary-darker;
    }
  }
}

.color-primary{
  color: $primary;
}

.white {
  color: $white;
}
.bg-white {
  background-color: $white;
}

#api,
#about {
  background-color: $white;
}

/* ===== MEDIA QUERIES=====*/
@media screen and(min-width: 768px) {
  body {
    margin: 0;
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
