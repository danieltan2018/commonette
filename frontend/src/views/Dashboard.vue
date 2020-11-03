<template>
  <v-main class="home">

    <span>
      <br>
      <h3 style="color:#E3E9F2">Invite your friends to join this room using the code <b style="color:#5DC0BF">{{roomCode}}</b></h3>
      <br>
      <v-btn large v-on:click="navigateRoute('/recommend')">View Recommendations</v-btn>
      <br>
      <br>
    </span>

    <div class="row">
      <div class="col-3"></div>
      <div class="col-6" style="color:white">
        <h1>Here are some statistics!</h1><br>
        <h2>Total No. Of Users In Room: <b style="color:#F6CA83">{{userCount}}</b></h2>
      </div>
      <div class="col-3"></div>
    </div>

    <v-row>
      <v-col cols="2"></v-col>
      <v-col cols="12">
        <v-badge v-for="user in roomUsers" :key="user.name" :content="user.name" color='deep-purple accent-4' bottom left overlap>
          <v-img v-if='user.gender == "M"' src='../images/Tanjiro.png' style='height:200px; width:165px'></v-img>
          <v-img v-else src='../images/Nezuko.png' style='height:200px; width:200px'></v-img>
        </v-badge>
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>
    <!-- <div class="row">
      <div class="col-1"></div>
      <div class="col-10" id="display">
        <v-badge color="deep-purple accent-4" content="Tanjiro" bottom left overlap>
          <img src="../images/Tanjiro.png" style="height:200px; width:165px" alt="">
        </v-badge>
        <v-badge color="deep-purple accent-4" content="Nezuko" bottom left overlap>
          <img src="../images/Nezuko.png" style="height:200px; width:200px" alt="">
        </v-badge>
      </div>
      <div class="col-1"></div>
    </div> -->

    <div class="row">
      <div class="col-3"></div>
      <div class="col-2">
        <v-simple-table dark dense>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-center">Rank</th>
                <th class="text-center">Weight</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in rankings" :key="item.weight">
                <td>{{ item.rank }}</td>
                <td>{{ item.weight }}</td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </div>
      <div class="col-4" style="color:white">
        <br><br>Categories or Genres ranked were assigned weights!
        <br><br>Total Weights were calculated to display the <b style="color:#5DC0BF">TOP</b> Categories/Genres below!
      </div>
      <div class="col-3"></div>
    </div>
    <div class="row">
      <div class="col-1"></div>
      <div class="col-5" data-aos="fade-down-right" data-aos-duration="1000" v-if="youtubeReady">
        <v-card type="chart" dark>
          <v-card-title>
            <v-icon color="red" large>mdi-youtube</v-icon>
            Youtube
          </v-card-title>
          <div class="chart-area">
            <bar-chart style="height: 100%" chart-id="youtubeStats" :chart-data="youtubeBarChart.chartData" :gradient-stops="youtubeBarChart.gradientStops" :extra-options="youtubeBarChart.extraOptions">
            </bar-chart>
          </div>
        </v-card>
      </div>
      <div class="col-5" data-aos="fade-down-left" data-aos-duration="1000" data-aos-delay="500" v-if="bookReady">
        <v-card type="chart" dark>
          <v-card-title>
            <v-icon color="blue" large>mdi-book</v-icon>Book
          </v-card-title>
          <div class="chart-area">
            <bar-chart style="height: 100%" chart-id="bookStats" :chart-data="bookBarChart.chartData" :gradient-stops="bookBarChart.gradientStops" :extra-options="bookBarChart.extraOptions">
            </bar-chart>
          </div>
        </v-card>
      </div>
      <div class="col-1"></div>
    </div>
    <div class="row">
      <div class="col-1"></div>
      <div class="col-5" data-aos="fade-up-right" data-aos-duration="1000" data-aos-delay="600" v-if="movieReady">
        <v-card type="chart" dark>
          <v-card-title>
            <v-icon color="rgb(255, 0, 128)" large>mdi-movie-open</v-icon>Movie
          </v-card-title>
          <div class="chart-area">
            <bar-chart style="height: 100%" chart-id="movieStats" :chart-data="movieBarChart.chartData" :gradient-stops="movieBarChart.gradientStops" :extra-options="movieBarChart.extraOptions">
            </bar-chart>
          </div>
        </v-card>
      </div>
      <div class="col-5" data-aos="fade-up-left" data-aos-duration="1000" data-aos-delay="1000" v-if="spotifyReady">
        <v-card type="chart" dark>
          <v-card-title>
            <v-icon color="green" large>mdi-spotify</v-icon>Spotify
          </v-card-title>
          <div class="chart-area">
            <bar-chart style="height: 100%" chart-id="spotifyStats" :chart-data="spotifyBarChart.chartData" :gradient-stops="spotifyBarChart.gradientStops" :extra-options="spotifyBarChart.extraOptions">
            </bar-chart>
          </div>
        </v-card>
      </div>
      <div class="col-1"></div>
    </div>
  </v-main>
</template>

<script>
import BarChart from "../components/Charts/BarChart";
import * as chartConfigs from "../components/Charts/config";
import config from "../config";
import axios from "axios";
export default {
  components: {
    BarChart,
  },
  props: {
    roomCode: {
      type: String,
      default: "",
    },
  },
  data: () => ({
    roomUsers: [],
    userCount: 0,
    youtubeReady: false,
    bookReady: false,
    movieReady: false,
    spotifyReady: false,
    femaleSpeed: 3,
    maleSpeed: -3,
    usersDisplay: [],
    youtubeBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Weight",
            fill: true,
            borderColor: "red",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    bookBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Weight",
            fill: true,
            borderColor: config.colors.info,
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    movieBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Weight",
            fill: true,
            borderColor: "rgb(255, 0, 128)",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    spotifyBarChart: {
      extraOptions: chartConfigs.barChartOptions,
      chartData: {
        labels: [],
        datasets: [
          {
            label: "Weight",
            fill: true,
            borderColor: "green",
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            data: [],
          },
        ],
      },
      gradientColors: config.colors.primaryGradient,
      gradientStops: [1, 0.4, 0],
    },
    rankings: [
      { rank: '1', weight: 5 },
      { rank: '2', weight: 4 },
      { rank: '3', weight: 3 },
      { rank: '4', weight: 2 },
      { rank: '5', weight: 1 }
    ]
  }),
  created() {
    this.initialise();
  },
  mounted: function () {
    window.scrollTo(0, 0);
  },
  // watch: {
  //   roomUsers: {
  //     immediate: true,
  //     handler() {
  //       if (this.roomUsers != []) {
  //         // console.log(this.roomUsers);
  //         var users = this.roomUsers;
  //         var display = ""
  //         for (var user of users) {

  //           if (user.gender == "M") {
  //             display = " <v-badge color='deep-purple accent-4' content='" + user.name + "' bottom left overlap>\
  //                           <img src='../images/Tanjiro.png' style='height:200px; width:165px' alt=''>\
  //                         </v-badge>";
  //           }
  //           else {
  //             display = " <v-badge color='deep-purple accent-4' content='" + user.name + "' bottom left overlap>\
  //                           <img src='../images/Nezuko.png' style='height:200px; width:200px' alt=''>\
  //                         </v-badge>";
  //           }

  //           // document.getElementById("display").innerHTML += display;
  //         }
  //       }
  //     }
  //   }
  // },
  methods: {
    getImage(gender) {
      var image = "";
      if (gender == "F") {
        image = "../images/Nezuko.png";
      }
      else {
        image = "../images/Tanjiro.png";
      }

      return image;
    },
    navigateRoute(newpath) {
      this.$router.push(newpath);
    },
    initialise() {
      axios({
        url: "/room/" + this.roomCode,
        method: "GET",
      })
        .then((response) => {
          localStorage.clear();
          localStorage.setItem("roomName", response.data.room_name);
          localStorage.setItem("roomCode", this.roomCode);
          if (response.data.questionnaire) {
            for (var person of response.data.questionnaire) {
              this.roomUsers.push({
                name: person.name,
                gender: person.gender,
                image: this.getImage(person.gender)
              });
            }
            localStorage.setItem("roomUsers", JSON.stringify(this.roomUsers));
            this.userCount = this.roomUsers.length;
          } else {
            this.$bus.$emit("updated", "joined");
            this.navigateRoute("/questionnaire");
          }
          this.$bus.$emit("updated", "joined");
        })
        .catch(() => {
          this.navigateRoute("/");
        });
      axios.get("/dashboard/" + this.roomCode).then((response) => {
        for (const [key, value] of Object.entries(response.data.youtube)) {
          this.youtubeBarChart.chartData.labels.push(key);
          this.youtubeBarChart.chartData.datasets[0].data.push(value);
        }
        this.youtubeReady = true;
        for (const [key, value] of Object.entries(response.data.book)) {
          this.bookBarChart.chartData.labels.push(key);
          this.bookBarChart.chartData.datasets[0].data.push(value);
        }
        this.bookReady = true;
        for (const [key, value] of Object.entries(response.data.movie)) {
          this.movieBarChart.chartData.labels.push(key);
          this.movieBarChart.chartData.datasets[0].data.push(value);
        }
        this.movieReady = true;
        for (const [key, value] of Object.entries(response.data.spotify)) {
          this.spotifyBarChart.chartData.labels.push(key);
          this.spotifyBarChart.chartData.datasets[0].data.push(value);
        }
        this.spotifyReady = true;
      });
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

</script>
<style>
.home {
  background-color: rgb(81, 81, 118);
  justify-content: center;
}
</style>